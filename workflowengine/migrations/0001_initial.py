# Generated by Django 2.2 on 2020-05-17 17:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profilePhoto', models.FileField(null=True, upload_to='')),
                ('dateOfBirth', models.DateField(null=True)),
                ('restriction_pin', models.CharField(blank=True, max_length=128, null=True, verbose_name='restriction_pin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expertise', models.CharField(default='', max_length=200)),
                ('description', models.CharField(blank=True, default='', max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=200)),
                ('question', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('label', models.CharField(default='', max_length=200)),
                ('field_type', models.CharField(choices=[('TEXT', 'TEXT'), ('LONG_TEXT', 'LONG_TEXT'), ('DATE', 'DATE'), ('DATETIME', 'DATETIME'), ('CHECK_BOX', 'CHECK_BOX'), ('MULTICHOICE', 'MULTICHOICE'), ('RADIO', 'RADIO'), ('FILE', 'FILE'), ('CHILD_FLOW_CREATION_BUTTON', 'CHILD_FLOW_CREATION_BUTTON'), ('MESSAGE_PROCESS', 'MESSAGE_PROCESS'), ('SECTION_SEPERATOR', 'SECTION_SEPERATOR'), ('HIDDEN', 'HIDDEN'), ('LOCATION', 'LOCATION'), ('SKIP_STEP_BUTTON', 'SKIP_STEP_BUTTON'), ('API_DATA_DROPDOWN', 'API_DATA_DROPDOWN'), ('TIME_DELTA', 'TIME_DELTA'), ('PRICE', 'PRICE'), ('EXPERT', 'EXPERT')], default='TEXT', max_length=40)),
                ('multichoice_options', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('restricted', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flow_name', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(default='', max_length=50)),
                ('visible', models.BooleanField(default=False)),
                ('index', models.IntegerField(default=0)),
                ('primary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_type', models.CharField(max_length=20)),
                ('primary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserFlow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creator', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Flow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('index', models.IntegerField(default=0)),
                ('mandatory', models.BooleanField(default=False)),
                ('expert_search_criteria', models.BooleanField(default=False)),
                ('include_in_summary', models.BooleanField(default=True)),
                ('field', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Field')),
                ('form', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Form')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('text', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('flow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='workflowengine.Flow')),
                ('formfield', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflowengine.FormField')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='flow',
            name='flow_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='workflowengine.WorkflowType'),
        ),
        migrations.AddField(
            model_name='flow',
            name='parent_flow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Flow'),
        ),
        migrations.AddField(
            model_name='field',
            name='flow_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='workflowengine.WorkflowType'),
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('index', models.IntegerField(default=0)),
                ('certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('reviewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expertise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Expertise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Role'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
