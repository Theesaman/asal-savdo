from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request=request,template_name='index.html')

def about_view(request):
    return render(request=request,template_name='index.html')

def booking_view(request):
    return render(request=request,template_name='index.html')

def contact_view(request):
    return render(request=request,template_name='index.html')

def package_view(request):
    return render(request=request,template_name='index.html')

def d_view(request):
    return render(request=request,template_name='index.html')

def service_view(request):
    return render(request=request,template_name='index.html')

def team_view(request):
    return render(request=request,template_name='index.html')

def testimonial_view(request):
    return render(request=request,template_name='index.html')

def distination_view(request):
    return render(request=request,template_name='index.html')
