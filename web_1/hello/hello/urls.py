"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from firstapp import views

urlpatterns = [
    path('', views.index),
    path('about', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact', TemplateView.as_view(template_name="firstapp/contact.html",
                                         extra_context={"work": "Разработка программных продуктов"})),
]
