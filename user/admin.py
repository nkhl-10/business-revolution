from django.contrib import admin
from .models import about_us, user_contact, register, idea_description, subscribe, user_upload_idea, Order
from innovator.models import register_innovator, sub_category_innovator, category_innovator, innovator_uploads


# Register your models here.


class category(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_editable = ["name"]
    list_filter = ["name"]


class innovatorupload(admin.ModelAdmin):
    list_display = ["id", "admin_photo", "idea_title", "publisher_name", "innovator_id", "date", "urls",
                    "idea_description"]
    list_editable = ["idea_title", "publisher_name", "idea_description"]
    readonly_fields = ['admin_photo', "date"]


admin.site.register(about_us)
admin.site.register(register)
admin.site.register(user_contact)
admin.site.register(register_innovator)
admin.site.register(idea_description)
admin.site.register(subscribe)
admin.site.register(user_upload_idea)
admin.site.register(sub_category_innovator)
admin.site.register(category_innovator, category)
admin.site.register(innovator_uploads, innovatorupload)
admin.site.register(Order)
