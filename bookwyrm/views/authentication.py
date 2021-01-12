''' class views for login/register/password management views '''
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils import timezone
from django.views import View

from bookwyrm import forms, models
from bookwyrm.settings import DOMAIN


# pylint: disable= no-self-use
class LoginView(View):
    ''' authenticate an existing user '''
    def get(self, request):
        ''' login page '''
        if request.user.is_authenticated:
            return redirect('/')
        # send user to the login page
        data = {
            'title': 'Login',
            'login_form': forms.LoginForm(),
            'register_form': forms.RegisterForm(),
        }
        return TemplateResponse(request, 'login.html', data)

    def post(self, request):
        ''' authentication action '''
        login_form = forms.LoginForm(request.POST)

        localname = login_form.data['localname']
        username = '%s@%s' % (localname, DOMAIN)
        password = login_form.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # successful login
            login(request, user)
            user.last_active_date = timezone.now()
            return redirect(request.GET.get('next', '/'))

        # login errors
        login_form.non_field_errors = 'Username or password are incorrect'
        register_form = forms.RegisterForm()
        data = {
            'login_form': login_form,
            'register_form': register_form
        }
        return TemplateResponse(request, 'login.html', data)


class RegisterView(View):
    ''' register a user '''
    def post(self, request):
        ''' join the server '''
        if not models.SiteSettings.get().allow_registration:
            invite_code = request.POST.get('invite_code')

            if not invite_code:
                raise PermissionDenied

            invite = get_object_or_404(models.SiteInvite, code=invite_code)
            if not invite.valid():
                raise PermissionDenied
        else:
            invite = None

        form = forms.RegisterForm(request.POST)
        errors = False
        if not form.is_valid():
            errors = True

        localname = form.data['localname'].strip()
        email = form.data['email']
        password = form.data['password']

        # check localname and email uniqueness
        if models.User.objects.filter(localname=localname).first():
            form.errors['localname'] = [
                'User with this username already exists']
            errors = True

        if errors:
            data = {
                'login_form': forms.LoginForm(),
                'register_form': form,
                'invite': invite,
                'valid': invite.valid() if invite else True,
            }
            if invite:
                return TemplateResponse(request, 'invite.html', data)
            return TemplateResponse(request, 'login.html', data)

        username = '%s@%s' % (localname, DOMAIN)
        user = models.User.objects.create_user(
            username, email, password, localname=localname, local=True)
        if invite:
            invite.times_used += 1
            invite.save()

        login(request, user)
        return redirect('/')
