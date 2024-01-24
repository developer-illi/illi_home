from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
import socket

# Create your views here.
def main(request):
    content = {}
    return render(request, 'index.html', content)

def project(request):
    content = {}
    return render(request, 'temporary.html', content)

def temporary(request):
    content = {}
    return render(request, 'temporary.html', content)

def about(request):
    content = {}
    return render(request, 'about.html', content)

def contact(request):
    content = {}
    return render(request, 'contact.html', content)

def end(request):
    content = {}
    return render(request, 'reserend.html', content)

@csrf_exempt
def mails(request):
    name = request.POST['name_u']
    phone = request.POST['phone']
    email_u = request.POST['email']
    belong = request.POST['belong']
    message = request.POST['message']
    mail_title = "IFP Conference Reservation"
    mail_to = 'kylie@illi.kr'
    #mail_to = 'jin@illi.kr'
    sends = '이름 :' + name + '\n' + '핸드폰번호 :' + phone + '\n'+ '소속 :' + belong + '\n' + '이메일 :' + email_u + '\n' + '문의사항 :' + message
    email = EmailMessage(mail_title, sends, to=[mail_to])
    email.send()
    return redirect('end')

@csrf_exempt
def terms(request):
    if request.method == "POST":
        name = request.POST['name_u']
        phone = request.POST['phone']
        email_u = request.POST['email']
        belong = request.POST['belong']
        message = request.POST['message']
    content = {'name':name, 'phone':phone, 'email_u':email_u, 'message':message, 'belong':belong}
    return render(request, 'cheack.html', content)

class ProductListAPI(APIView):
    def get(self, request):
        queryset = Test_model.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)