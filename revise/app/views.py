from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def form(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.POST.get('images')

        try:
            user = formfill(namemodel=name,emailmodel=email,imagemodel=image)
            user.full_clean()
            user.save()
            return redirect('form')
        except Exception as e:
            return redirect('form')
    return render(request,"app/form.html")