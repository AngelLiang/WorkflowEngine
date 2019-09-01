from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from workflowengine.models import *


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUserModel.CustomUser
	list_display = ["email", "username", "role", "is_staff"]
	fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('role',)}), )
	


class FlowAdmin(ImportExportModelAdmin):
	model=FlowModel.Flow
	list_display=['id','stage','flow_type', 'completed','created_at','updated_at', 'flow_name'] 

class FormFieldAdmin(ImportExportModelAdmin):
	model=FormFieldModel.FormField
	list_display=['id','form','field', 'stage','index', 'mandatory']

class UserFlowAdmin(ImportExportModelAdmin):
	model=UserFlowModel.UserFlow
	list_display=['user','flow','created_at','updated_at']

class FormDataAdmin(ImportExportModelAdmin):
	model=FormDataModel.FormData
	list_display=['id','user','formfield','flow','file','text', 'created_at', 'updated_at']

class ExpertAdmin(ImportExportModelAdmin):
	model=ExpertModel.Expert
	list_display=['id','user','expertise','index']

class WorkflowTypeAdmin(ImportExportModelAdmin):
	model=WorkflowTypeModel.WorkflowType
	list_display=['id','workflow_type','start_stage','primary']


admin.site.register(CustomUserModel.CustomUser, CustomUserAdmin)
admin.site.register(FieldModel.Field)
admin.site.register(FlowModel.Flow,FlowAdmin)
admin.site.register(FormModel.Form)
admin.site.register(FormFieldModel.FormField,FormFieldAdmin)
admin.site.register(RoleModel.Role)
admin.site.register(UserFlowModel.UserFlow,UserFlowAdmin)
admin.site.register(FormDataModel.FormData,FormDataAdmin)

admin.site.register(ExpertModel.Expert,ExpertAdmin)
admin.site.register(ExpertiseModel.Expertise)
admin.site.register(WorkflowTypeModel.WorkflowType,WorkflowTypeAdmin)


