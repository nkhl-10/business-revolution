from django.shortcuts import render, redirect
from .models import register_innovator, category_innovator, innovator_uploads
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

# def index(request):
#     return render(request,"innovator/login.html")
#
# def loadfile(request):
#     if request.POST:
#         uname = request.POST['uname']
#         phonenumber = request.POST['phonenumber']
#         email = request.POST['email']
#         password = request.POST['password']
#         obj = register1(uname=uname, phonenumber=phonenumber, email=email, password=password)
#         obj.save()
#         request.session['email'] = email
#         request.session['phonenumber'] = phonenumber
#         request.session['uname'] = uname
#         request.session['password'] = password
#
#         subject = 'thank you for registration to BUSINESS REVOLUTION'
#         message = 'thank you for my website'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)
#         return redirect('/login')
#     return render(request, "innovator/login.html")

def load(request):
    if request.session.has_key('innovator_id'):
        return render(request, 'innovator/index.html')
    return render(request, 'innovator/login.html')


def signup(request):
    if request.POST:
        username = request.POST['username']
        phone_no = request.POST['phoneno']
        email = request.POST['email1']
        password = request.POST['password1']
        obj = register_innovator(username=username, phone_no=phone_no, email=email, password=password)
        obj.save()
        request.session['email1'] = email
        request.session['phoneno'] = phone_no
        request.session['username'] = username
        request.session['password1'] = password
        subject = 'thank you for registration to BUSINESS REVOLUTION'
        message = 'thank you for my website'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return redirect('innovator/login')
    return render(request, 'innovator/login.html')


def login(request):
    if request.POST:
        email = request.POST['email1']
        password = request.POST['password1']
        count = register_innovator.objects.filter(email=email, password=password).count()
        if count > 0:
            request.session['innovator_id'] = True
            request.session['innovator_id'] = \
                register_innovator.objects.values('id').filter(email=email, password=password)[0]['id']
            return redirect('/innovator/upload')
        else:
            if not register_innovator.objects.filter(email=email):
                messages.error(request, "Please must be enter a valid email!!!")
                return redirect('/innovator/login')
            if not register_innovator.objects.filter(password=password):
                messages.error(request, "Password must be enter a valid password!!! ")
                return redirect('/innovator/login')
    return render(request, "innovator/login.html")


def upload(request):
    category = category_innovator.objects.all()
    if request.POST:
        try:
            obj = innovator_uploads(
                publisher_name=request.POST['publisher_name'],
                idea_title=request.POST['idea_title'],
                idea_image=request.FILES['idea_image'],
                idea_description=request.POST['idea_description'],
                idea_document=request.FILES['idea_document'],
                urls=request.POST['urls'],
                price=request.POST['price'],
                category1_id=request.POST['category1'],
                subcategory1_id=request.POST['subcategory1'])
            obj.innovator_id_id = request.session.get('innovator_id')
            obj.save()
        except Exception as e:
            # Log the error and show an error message
            print(f"Error occurred: {e}")
        return redirect('innovator/upload')
    return render(request, "innovator/uploads.html", {"category": category})


def logout(request):
    try:
        if request.method == 'GET':
            del request.session['innovator_id']
            return redirect('/innovator/login')
    except KeyError:
        return redirect('/innovator/login')


# def loadfile(request):
#     return render(request, "innovator/index.html")
#
# def home(request):
#     return render(request, "innovator/index.html")


def profile(request):
    uid = request.session.get('user_id')
    if request.POST:
        username = request.POST['username']
        phoneno = request.POST['phoneno']
        email1 = request.POST['email1']
        password1 = request.POST['password1']
        obj = register_innovator(username=username, phoneno=phoneno, email1=email1, password1=password1, id=uid)
        obj.save()
        request.session['email1'] = email1
        request.session['phoneno'] = phoneno
        request.session['username'] = username
        request.session['password1'] = password1
        return redirect('/upload')
    return render(request, "innovator/myprofile.html")
