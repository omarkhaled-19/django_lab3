from django.shortcuts import render

# Create your views here.
def aboutuspage(request):
    return render(request,'about.html')