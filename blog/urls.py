"""entregafinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import home, blogs, page, about, createpage, updatepage, deletepage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('pages', blogs, name="pages"),
    path('page', page, name="page"),
    path('about', about, name="about"),
    path('createpage', createpage, name="createpage"),
    path('updatepage', updatepage, name="updatepage"),
    path('deletepage', deletepage, name="deletepage"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)