"""pdf_store URL Configuration

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
from django.conf.urls import url
from first import views

urlpatterns = [

    url(r'^$', views.home, name="home"),
    url(r'^upload/', views.upload_file, name="upload"),
    url(r'^admin/', admin.site.urls),
    url(r'^admin_page/$', views.admin_view, name="admin_view"),
    url(r'^admin_page/view_resume/(?P<phone_number>[0-9]+)$', views.pdf_viewer, name="pdf_view"),
    url(r'^admin_page/blog$', views.blog_view, name="blog_view"),
    url(r'^admin_page/candidate_details/(?P<phone_number>[0-9]+)$', views.candidate_details_view, name="candidate_details_view"),



]
