from django.http import HttpResponse 
from django.shortcuts import render,redirect
from imageapp.models import *

def about(request):
    name='shivam datta'
    link='https://www.youtube.com/truthtimes'
    data={'name':name,'link':link}
    return render(request,"about.html",data)
def home(request):
    cats=Category.objects.all()
    images=Image.objects.all()
    data={'images':images,'cats':cats}
    
    return render(request,"index.html",data)
def category(request,cid):
    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.all()
    image=Image.objects.filter(cat=category)
    data={'image':image,'cat':category}
    return render(request,"index.html",data)
def home1(request):
    return redirect('/home')