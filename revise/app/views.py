from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
from .models import formfill

# Create your views here.


###########READ##############
def home(request):
    user = formfill.objects.filter(isdelete=False)
    return render(request,"app/home.html",{'datauser': user})

########Create###############3
def form(request):
    if request.method=='POST' and request.FILES: ##file chahi halnai parxa ani matra if statement ma xirxa
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('images')
        video = request.FILES.get('videos')
        check = request.POST.get('checkname')=='on'

        try:
            user = formfill(namemodel=name,emailmodel=email,imagemodel=image,checkmodel=check,videomodel=video)
            user.full_clean()
            user.save()
            messages.success(request,'form submitted successfully')
            return redirect('form')
        except Exception as e:
            messages.error(request,f'{str(e)}')
            return redirect('form')

    return render(request,"app/form.html")

####UPDATE################
def edit(request,id):
    return render(request,'app/edit.html')

######delete##################
def delete(request,id):
    particular_Data = formfill.objects.get(id=id) #3
    particular_Data.isdelete=True
    particular_Data.isdelete2=False ##particular_Data ma aako data ko isdelete =True
    particular_Data.save()
    return redirect('home')

####recycle bin####################
def recycle(request):
        data = formfill.objects.filter(isdelete=True,isdelete2=False) ##same as and operation
        return render(request,'app/recycle.html',{'recyclebin':data})

def restore_all(request):
     data = formfill.objects.filter(isdelete=True).update(isdelete=False,isdelete2=False)
     return redirect('recycle')

def delete_all(request):
    formfill.objects.filter(isdelete=True).update(isdelete2=True)

    # Redirect to the recycle bin to see the changes
    return redirect('recycle')
    