import datetime
# Create your views here.
import json

import razorpay
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *


def load(request):
    if request.POST:
        uname = request.POST['uname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        obj = register(uname=uname, phonenumber=phonenumber, email=email, password=password)
        obj.save()
        request.session['email'] = email
        request.session['phonenumber'] = phonenumber
        request.session['uname'] = uname
        request.session['password'] = password

        subject = 'thank you for registration to BUSINESS REVOLUTION'
        message = 'thank you for my website'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('/login')
    return render(request, 'user/login.html')


def login(request):
    if request.session.has_key('is_login'):
        return redirect('/home')
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = register.objects.filter(email=email, password=password).count()
        # if count is not None:
        #     login(request, count)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'The email or password you entered is incorrect. Please try again.')
        if count > 0:

            request.session['is_login'] = True
            request.session['user_id'] = register.objects.values('id').filter(email=email, password=password)[0]['id']
            return redirect('/home')
        else:
            if not register.objects.filter(email=email):
                messages.error(request, "Please must be enter a valid email!!!")
                return redirect('/login')
            if not register.objects.filter(password=password):
                messages.error(request, "Password must be enter a valid password!!! ")
                return redirect('/login')

            return redirect('/login')
    return render(request, "user/login.html")


def logout(request):
    try:
        if request.method == 'GET':
            del request.session['is_login']
            return redirect('/login')
    except KeyError:
        return redirect('/login')


def loadfile(request):
    about_data = about_us.objects.all()
    idea_data = innovator_uploads.objects.order_by('?')[:3]
    idea_count = innovator_uploads.objects.count()
    data2 = register.objects.all()
    data5 = order_Show.objects.all()
    data3 = data2.count()
    data6 = data5.count()
    return render(request, 'user/home.html',
                  {"about": about_data, "idea_data": idea_data, "idea_count":idea_count , "data2": data2, "data3": data3, "data5": data5,
                   "data6": data6})


def home(request):
    about_data = about_us.objects.all()
    idea_data = innovator_uploads.objects.order_by('?')[:3]
    idea_count = innovator_uploads.objects.count()
    data2 = register.objects.all()
    data5 = order_Show.objects.all()
    data3 = data2.count()
    data6 = data5.count()
    return render(request, 'user/home.html',
                  {"about": about_data, "idea_data": idea_data, "idea_count": idea_count, "data2": data2, "data3": data3, "data5": data5,
                   "data5": data6})


def about(request):
    about_data = about_us.objects.all()
    return render(request, 'user/about.html', {"about": about_data})


def service(request):
    return render(request, 'user/service.html')


def contact(request):
    if request.POST:
        uname = request.POST['user_name']
        email = request.POST['user_email']
        subject = request.POST['user_subject']
        message = request.POST['user_message']
        uid = request.session.get('user_id')
        obj = user_contact(user_name=uname, user_email=email, user_subject=subject, user_message=message)
        obj.user_id_id = uid
        obj.save()
        return redirect('/contact')
    return render(request, "user/contact.html")


def feature(request):
    return render(request, 'user/feature.html')


def team(request):
    about = about_us.objects.all()
    return render(request, 'user/team.html', {"about": about})


def testimonial(request):
    return render(request, 'user/testimonial.html')


def readmore(request, id):
    data = innovator_uploads.objects.get(id=id)
    category = category_innovator.objects.all()
    subcategory = sub_category_innovator.objects.all()
    data1 = innovator_uploads.objects.all().order_by('-id')[0:5]

    return render(request, "user/readmore.html",
                  {"data": data, "category": category, "subcategory": subcategory, "data1": data1})


def profile(request):
    if not request.session.get('is_login', False):
        return redirect('/login')
    uid = request.session.get('user_id')
    if request.POST:
        uname = request.POST['uname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        obj = register(uname=uname, phonenumber=phonenumber, email=email, password=password, id=uid)
        obj.save()
    re = register.objects.get(id=uid)
    return render(request, "user/profile.html", {"re": re})


def i_save(request):
    uid = request.session.get('user_id')

    if request.POST:
        iuid = request.POST['iuid']

    return redirect('/index')


def password(request):
    return render(request, "user/changepassword.html")


def anotherway(request):
    return render(request, "user/anotherway.html")




def subscribe2(request):
    if request.POST:
        email = request.POST['email']
        obj = subscribe(email=email)
        obj.save()
        subject = 'thank you for registration to BUSINESS REVOLUTION'
        message = 'thank you for my website'
        email_from = settings.EMAIL_HOST_USER
        resipient_list = [email]
        send_mail(subject, message, email_from, resipient_list)
        return redirect('/home')
    return render(request, "user/footer.html")


def idea(request):
    data = innovator_uploads.objects.all()
    category = category_innovator.objects.all()
    subcategory = sub_category_innovator.objects.all()
    data1 = innovator_uploads.objects.all().order_by('-id')[0:5]
    return render(request, 'user/idea1.html',
                  {"data": data, "category": category, "subcategory": subcategory, "data1": data1})


def search(request):
    query = request.GET['query']
    data = innovator_uploads.objects.filter(idea_title__icontains=query)
    context = {
        "data": data,
    }
    return render(request, "user/search.html", context)


def index(request):
    return render(request, "user/index.html")


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=("rzp_test_TY9w1JsSfTWi9i", "APEvVFj0VsmsRkLXh4AyMvDF"))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create( name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "user/payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/callback",
                "razorpay_key": "rzp_test_TY9w1JsSfTWi9i",
                "order": order,
            },
        )
    return render(request, "user/payment.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=("rzp_test_TY9w1JsSfTWi9i", "APEvVFj0VsmsRkLXh4AyMvDF"))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "user/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "user/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "user/callback.html", context={"status": order.status})


def cat(request, id):
    cats = sub_category_innovator.objects.get(id=id)
    idea = innovator_uploads.objects.filter(subcategory1=cats)
    context = {
        "cats": cats,
        "idea": idea,
    }
    return render(request, "user/category.html", context)


def view_order(request):
    if not request.session.get('is_login', False):
        return redirect('/login')
    uid = request.session.get('user_id')
    data = order_Show.objects.filter(uid=uid)
    return render(request, "user/order.html", {"data": data})


def buyorder(request):
    if not request.session.get('is_login', False):
        return redirect('/login')
    uid = request.session.get('user_id')
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.POST:
        ui_id = request.POST['id']
    data1 = order_Show(date=x)
    data1.uid_id = uid
    data1.iu_id_id = ui_id
    data1.save()
    data = innovator_uploads.objects.get(id=ui_id)
    return render(request, "user/buyorder.html", {"data": data})


def details1(request, id):
    data = order_Show.objects.get(id=id)
    return render(request, "user/details1.html", {"data": data})
