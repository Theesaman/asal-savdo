from django.urls import path
from .views import home_view,about_view,booking_view,contact_view,distination_view,package_view,service_view,team_view,testimonial_view

urlpatterns = [
    path('',home_view,name='index.html'),
    path('about.html/',about_view,name='about.html'),
    path('booking.html/',booking_view,name='booking.html'),
    path('contact.html',contact_view,name='contact.html'),
    path('destination.html',distination_view,name='distination.html'),
    path('package.html',package_view,name='package.html'),
    path('service.html',service_view,name='service.html'),
    path('team.html',team_view,name='team.html'),
    path('testimonial.html',testimonial_view,name='testimonial.html'),
    
      
]