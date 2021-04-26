# Generated by Django 3.1.8 on 2021-04-23 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0069_auto_20210422_1604"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="usertag",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="usertag",
            name="book",
        ),
        migrations.RemoveField(
            model_name="usertag",
            name="tag",
        ),
        migrations.RemoveField(
            model_name="usertag",
            name="user",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.DeleteModel(
            name="UserTag",
        ),
    ]
