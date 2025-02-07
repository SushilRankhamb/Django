from django.shortcuts import render,HttpResponse
from .models import product,cars
from .forms import productFrom
# Create your views here.
def home(request):
    if request.method =="POST":
        form=productFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        data = product.objects.all()   
    form = productFrom()     
    data = product.objects.all()
    data1 = cars.objects.all()
    return render(request,'electronics/home.html',{'data':data,'form':form,'data1':data1})