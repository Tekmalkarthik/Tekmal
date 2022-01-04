from django.shortcuts import render,HttpResponse

# Create your views here.
def Registration(request):
     return render(request,'Registration.html')
