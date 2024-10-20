from django.contrib import admin
from.models import about_us,user_contact,register,ideas_discription,subscribe,user_upload,Order
from innovator.models import register_innovator,sub_category_innovator,category_innovator,innovator_uploads

# Register your models here.


class category(admin.ModelAdmin):
    list_display = ["id","name"]
    list_editable = ["name"]
    list_filter = ["name"]

class innovatorupload(admin.ModelAdmin):
    list_display = ["id","admin_photo","idea_title","publisher_name","innovator_id","date","urls"]
    list_editable = ["idea_title","publisher_name"]
    readonly_fields = ['admin_photo',"date"]




admin.site.register(about_us)
admin.site.register(register)
admin.site.register(user_contact)
admin.site.register(register_innovator)
admin.site.register(ideas_discription)
admin.site.register(subscribe)
admin.site.register(user_upload)
admin.site.register(sub_category_innovator)
admin.site.register(category_innovator, category)
admin.site.register(innovator_uploads,innovatorupload)
admin.site.register(Order)

