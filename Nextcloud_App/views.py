from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact

# Create your views here.
# def index(request):
#     return render(request, 'Nextcloud_App/index.html')


def index(request):
    if request.method == "POST":
        name = request.POST['contname']
        email = request.POST['contemail']
        msg = request.POST['contmessage']
        # print(name, email, msg)
        if name == '':
            messages.error(request, 'Name Should not be blank')
        elif len(name) < 3:
            messages.error(
                request, 'Name Should be Contain Atlist 3 Caracters')
        elif email == '':
            messages.error(request, 'Email Should not be blank')
        elif len(email) < 7:
            messages.error(
                request, 'Email Should be Contain Atlist 7 Caracters')
        elif msg == '':
            messages.error(request, 'message Should not be blank')
        elif len(msg) < 20:
            messages.error(
                request, 'message Should be Contain Atlist 20 Caracters')
        else:
            Contact(contname=name, contemail=email, contmessage=msg).save()
            messages.success(request, 'Submit Your Form successfully')
    return render(request, 'Nextcloud_App/index.html')
