# Generated by Django 2.2.4 on 2019-08-17 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0001_initial'),
        ('workflowengine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Case')),
            ],
        ),
    ]
