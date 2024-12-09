from django.urls import path
from . import views
from .views import success
urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('BookYourDemo/', views.bookDemo, name='bookDemo'),
    path('Find Us/', views.contactUs, name='contactUs'),
    path('success/', views.book_demo, name='success'),
    path('Profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('paymentcheckout/',views.paymentcheckout, name='paymentcheckout'),
    path('paymentdone/',views.paymentdone, name='paymentdone'),
    path('login/', views.login, name='login'),
    path('user_login/', views.user_login, name='user_login'),

]
