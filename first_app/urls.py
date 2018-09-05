from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from first_app import views

app_name='first_app'

urlpatterns = [
url(r'^user_login/$',views.user_login,name='user_login'),
    # url(r'^second/',views.help,name='second'),
    # url(r'^other/',views.other,name='other'),
    # url(r'^hyper/',views.hyper,name='hyper'),
    # url(r'^folium/',views.folium,name='folium'),
]
