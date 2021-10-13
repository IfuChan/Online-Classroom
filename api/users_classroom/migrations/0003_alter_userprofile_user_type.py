# Generated by Django 3.2.4 on 2021-06-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_classroom', '0002_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[(None, None), ('teacher', 'teacher'), ('student', 'student')], default=None, max_length=10),
        ),
    ]
