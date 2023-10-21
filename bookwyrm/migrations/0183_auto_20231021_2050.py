# Generated by Django 3.2.20 on 2023-10-21 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0182_merge_20230905_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='related_user_export',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookwyrm.bookwyrmexportjob'),
        ),
        migrations.AlterField(
            model_name='childjob',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('complete', 'Complete'), ('stopped', 'Stopped'), ('failed', 'Failed')], default='pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('FAVORITE', 'Favorite'), ('REPLY', 'Reply'), ('MENTION', 'Mention'), ('TAG', 'Tag'), ('FOLLOW', 'Follow'), ('FOLLOW_REQUEST', 'Follow Request'), ('BOOST', 'Boost'), ('IMPORT', 'Import'), ('USER_IMPORT', 'User Import'), ('USER_EXPORT', 'User Export'), ('ADD', 'Add'), ('REPORT', 'Report'), ('LINK_DOMAIN', 'Link Domain'), ('INVITE', 'Invite'), ('ACCEPT', 'Accept'), ('JOIN', 'Join'), ('LEAVE', 'Leave'), ('REMOVE', 'Remove'), ('GROUP_PRIVACY', 'Group Privacy'), ('GROUP_NAME', 'Group Name'), ('GROUP_DESCRIPTION', 'Group Description')], max_length=255),
        ),
        migrations.AlterField(
            model_name='parentjob',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('complete', 'Complete'), ('stopped', 'Stopped'), ('failed', 'Failed')], default='pending', max_length=50, null=True),
        ),
    ]
