from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
from innovator.models import innovator_uploads, category_innovator, sub_category_innovator


# Create your models here.

class register(models.Model):
    uname = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.uname


class user_contact(models.Model):
    user_id = models.ForeignKey(register, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_subject = models.CharField(max_length=30)
    user_message = models.CharField(max_length=300)

    def __str__(self):
        return self.user_name


class about_us(models.Model):
    img = models.ImageField(upload_to='image/')
    team_name = models.CharField(max_length=30)
    team_designation = models.CharField(max_length=300)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)

    def __str__(self):
        return self.team_name


class idea_description(models.Model):
    img = models.ImageField(upload_to='image/')
    business_name = models.CharField(max_length=30)
    business_detail = models.CharField(max_length=300)
    business_detail_link = models.URLField(max_length=200)


class subscribe(models.Model):
    email = models.EmailField()


# user upload ideas
class user_upload_idea(models.Model):
    user_id = models.ForeignKey(register, on_delete=models.CASCADE)
    publisher_name = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    idea_title = models.CharField(max_length=30)
    ideas_image = models.ImageField(upload_to='images/')
    idea_description = models.TextField()
    idea_document = models.FileField(upload_to='documents/')
    urls = models.URLField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.publisher_name


class category(models.Model):
    name = models.CharField(max_length=50)


class sub_category(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


# class leavecmnt(models.Model):
#     uid=models.ForeignKey(register,on_delete=models.CASCADE)
#     postid=models.ForeignKey(ideass,on_delete=models.CASCADE)
#     msg=models.CharField(max_length=350)


class order_Show(models.Model):
    uid = models.ForeignKey(register, on_delete=models.CASCADE)
    iu_id = models.ForeignKey(innovator_uploads, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
