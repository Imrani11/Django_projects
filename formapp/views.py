from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import StudentForm
from . import forms

# Create your views here.
def get_details(request):
        form = forms.StudentForm()
        if request.method == 'POST':
                form = forms.StudentForm(request.POST)
                if form.is_valid():
                        print("Form validation success and printing the student information")
                        print("Student name:",form.cleaned_data['name'])
                        print("Student Email:",form.cleaned_data['email'])
                        return render(request,'formapp/thankyou.html',{'name':form.cleaned_data['name']})

        return render(request, 'formapp/index.html',{'form': form})
