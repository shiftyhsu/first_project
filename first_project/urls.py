"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from first_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
url(r'^$',views.Undex,name='index'),
url(r'^KNNCosineRecommender',views.other,name='other'),
url(r'^formpage/',views.form_name_view,name='form_view'),
url(r'^admin/',admin.site.urls),
url(r'^folium/',views.folium,name='folium'),
url(r'^supplychainanalysis/',views.hyper,name='hyper'),
url(r'^register/',views.register,name='register'),
url(r'^login/',views.user_login,name='login'),
url(r'^first_app/',include('first_app.urls')),
url(r'^logout/',views.user_logout,name='logout'),
url(r'^special/',views.register,name='special')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
