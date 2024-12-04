from django.urls import path
from  .views import contact
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('course_details/', views.course_details, name='course-details'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('index/', views.index, name='index'),
    path('pricing/', views.pricing, name='pricing'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('trainers/', views.trainers, name='trainers'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    
]
