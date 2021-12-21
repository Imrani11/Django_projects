from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from .models import Contact

# Create your views here.
def feedback(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        name = request.POST.get('name','')
        Number = request.POST.get('Number','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        if username and name and Number and email and password:
            contact = Contact(username=username,name=name,Number=Number,email=email,password=password)
            contact.save()
        else:
            return HttpResponse("Enter all the details")
    return render(request,'student_fbapp/index.html')