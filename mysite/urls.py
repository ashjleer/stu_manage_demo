"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from app import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^classes/',views.classes),
    url(r'^add_class/', views.add_class),
    url(r'^del_class/', views.del_class),
    url(r'^edit_class/', views.edit_class),
    url(r'^students/', views.students),
    url(r'^add_student/', views.add_student),
    url(r'^edit_student/', views.edit_student),
    url(r'^del_student/', views.del_student),
    url(r'^modal_add_class/', views.modal_add_class),
    url(r'^modal_edit_class/', views.modal_edit_class),
    url(r'^modal_add_student/', views.modal_add_student),
    url(r'^modal_edit_student/', views.modal_edit_student),
    url(r'^teachers/', views.teachers),

]
