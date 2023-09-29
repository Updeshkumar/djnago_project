from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= (
        "mobile_number",
        "otp",
        "active",
        "created_at",
        "updated_at"
    )
admin.site.register(Account_Pending)

@admin.register(state)
class stateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id" ,
        "state_name" 
    )
@admin.register(district)
class districtAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        "id" ,
        "state_id" ,
        "district_name" 
    )
    search_fields = ('district_name',)
    list_filter = ('state_id' , )
@admin.register(tahseel)
class tahseelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'district_id',
        'tahseel_name',
    
        )
    search_fields = ('tahseel_name',)
    list_filter = ('district_id' , )


@admin.register(profileofall)
class profileofallAdmin(admin.ModelAdmin):
    list_display=('user', 'role')
    
    
    
@admin.register(requirement)
class requirementAdmin(admin.ModelAdmin):
 list_display=("title", 'description')

@admin.register(accepted_requirement)
class accepted_requirementAdmin(admin.ModelAdmin):
    list_display=(
        "user" ,
        "requirement",
        "status"
    )


