# Generated by Django 2.2.4 on 2019-09-09 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0017_field_flow_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='expert_search_criteria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='formfield',
            name='include_in_summary',
            field=models.BooleanField(default=True),
        ),
    ]
