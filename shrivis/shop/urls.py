from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('reservation/', views.reservation, name="reservation"),
    path('search/', views.search, name="search"),
    path('history/', views.order_history, name="history"),
    path('handlerequest/', views.handlerequest, name="handlerequest")
]
