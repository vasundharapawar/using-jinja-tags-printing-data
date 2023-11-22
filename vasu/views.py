from django.shortcuts import render

# Create your views here.
def v(request):
    d={'name':'vasu','age':'22'}
    return render(request,'vasu.html',d)
