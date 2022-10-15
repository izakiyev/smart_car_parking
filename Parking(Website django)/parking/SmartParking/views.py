from django.shortcuts import render
from .models import Room,Customer
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def index(request):
    rooms=Room.objects.all()
    content={"rooms":rooms}
    return render(request,"index.html",content)
def payment(request):
    
    if request.method == 'POST':
        message_name=request.POST['name']
        message_mail=request.POST['mail']
        message_phone=request.POST['phone']
        message_time=request.POST['time']
        b=''
        for i in message_mail:
            if i=='@':
                break
            else:
                b+=i
        # time=request.POST['time']
       
        user = Customer.objects.create(
        time = message_phone,
        email = message_mail,
    )
        user.save()
        send_mail(
            'Parking Time limit' ,
            """Hello,Your time finised please enter the site and increase you time.\n
                http://127.0.0.1:8000/payment
            
            """,
            settings.EMAIL_HOST_USER,
            [message_mail],
            fail_silently = False)
        return render(request,'paid_parking.html',{})
    else:
        return render(request,'paid_parking.html',{})