from django.shortcuts import render

# Create your views here.
def m(request):
    d={'name':'maya','age':19}
    return render(request,'maya.html',context=d)