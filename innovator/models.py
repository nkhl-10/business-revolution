import datetime

from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class register_innovator(models.Model):
    username = models.CharField(max_length=30)
    phone_no = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class category_innovator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class sub_category_innovator(models.Model):
    category1 = models.ForeignKey(category_innovator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.category1.name + "--" + self.name


class innovator_uploads(models.Model):
    innovator_id = models.ForeignKey(register_innovator, on_delete=models.CASCADE)
    publisher_name = models.CharField(max_length=50)
    idea_title = models.CharField(max_length=50)
    idea_image = models.ImageField(upload_to='images/')
    idea_description = models.TextField()
    idea_document = models.FileField(upload_to='documents/')
    date = datetime.datetime.now()
    urls = models.URLField(max_length=300)
    # category = models.ForeignKey(category_innovator, on_delete=models.CASCADE, default=True)
    # subcategory = models.ForeignKey(sub_category_innovator, on_delete=models.CASCADE, default=True)

    category = models.IntegerField()
    subcategory = models.IntegerField()
    price = models.IntegerField()

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.idea_image.url))

    admin_photo.short_description = "idea_image"
    admin_photo.allow_tags = True

    def __str__(self):
        return self.publisher_name
