from django.shortcuts import render
from .models import Place,Person
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2 = Person.objects.all()
    return render(request,'index.html',{'result':obj,'resu':obj2})
