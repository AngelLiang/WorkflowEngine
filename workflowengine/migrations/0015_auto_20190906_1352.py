# Generated by Django 2.2.4 on 2019-09-06 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0014_role_primary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role',
            new_name='role_name',
        ),
    ]