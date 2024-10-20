from django.shortcuts import render

# Create your views here.

def loadfile(request):
    return render(request,'myadmins/index.html')

def forzerofor(request):
    return render(request,'myadmins/404.html')

# def loadfile(request):
#     data = ideass.objects.all
#     return render(request,'myadmins/approve.html',{"data":data})
#
# def forzerofor(request):
#     return render(request,'myadmins/404.html')

def user_data(request):
    # data=BR.objects.all
    return render(request,"myadmins/user_BR.html")

def invoice(request):
    return render(request,"myadmins/invoice.html")

def alert(request):
    return render(request,"myadmins/alert.html")

def analytics(request):
    return render(request,"myadmins/analytics.html")

def apex(request):
    return render(request,"myadmins/apex-charts.html")

def badge(request):
    return render(request,"myadmins/badge.html")

def chat(request):
    return render(request,"myadmins/chat.html")

def team(request):
    # data=members.objects.all
    return render(request,"myadmins/team.html")

def contacts(request):
    return render(request,"myadmins/contacts.html")

def uas(request):
    return render(request,"myadmins/user-account-settings.html")

def approve(request):
    # data=ideass.objects.all
    return render(request,"myadmins/approve.html")

def Readmore(request,id):
    # data=ideass.objects.get(id=id)
    return render(request, "myadmins/readmore.html")