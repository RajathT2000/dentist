from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        # send_mail(fname,
        # 'Noticed That You want an appointment',
        # 'rajathttt@gmail.com', 
        # [email])
        return render(request,'home.html',{'fname':fname})
    else:
        return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def news(request):
    return render(request,'news.html')

def patients(request):
    return render(request,'patients.html')

def services(request):
    return render(request,'services.html')

def base(request):
    return render(request, 'base.html')


