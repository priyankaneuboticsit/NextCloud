from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import profile
from .models import *
import uuid
# for send mail.
from django.conf import settings
from django.core.mail import send_mail
# for login.
from django.contrib.auth import authenticate
# becouse function name and import module name nao will be same.
from django.contrib.auth import login as auth_login
# for home.
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def home(request):
    return render(request, 'Form_App/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
      
        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'username already exist')
                return redirect('/register')
            if User.objects.filter(email=email).first():
                messages.success(request, 'email already exist')
                return redirect('/register')
            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            profile_obj = profile.objects.create(
                user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_email_after_register(email, auth_token)
            return redirect('/token_send')
        except Exception as e:
            print(e)

    return render(request, 'Form_App/register.html')


def login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username=username).first()
            if user_obj is None:
                messages.success(request, 'user not found')
                return redirect('/login')

            profile_obj = profile.objects.filter(user=user_obj).first()
            if not profile_obj.is_verified:
                messages.success(
                    request, 'Profile is not verify check your mail')
                return redirect('/login')

            user = authenticate(username=username, password=password)
            if user is None:
                messages.success(request, 'Wrong password')
                return redirect('/login')

            auth_login(request, user)
            return redirect('/home')

        return render(request, 'Form_App/login.html')


def success(request):
    return render(request, 'Form_App/success.html')


def token_send(request):
    return render(request, 'Form_App/token_send.html')


def send_email_after_register(email, token):
    subject = 'Your Account need to be verified'
    message = f'Hi paste thre link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request, auth_token):
    try:
        profile_obj = profile.objects.filter(auth_token=auth_token).first()

        if profile_obj.is_verified:
            messages.success(request, 'Your account is already verified')
            return redirect('/login')

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
           print(e)
           return redirect('/home')


def error(request):
    return render(request, 'Form_App/error.html')
