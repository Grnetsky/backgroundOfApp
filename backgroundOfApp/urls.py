"""backgroundOfApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token,verify_jwt_token

from main.views import UserinfoViewset, ContentView, Register, Logoutview
from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('user', UserinfoViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/$', UserinfoViewset.as_view({'get': 'retrieve','post':'createuser','put':'test'})),
    url(r'^user/(?P<pk>\d+)/$', UserinfoViewset.as_view({'get': 'retrieve',})),
    url(r'authorization/',obtain_jwt_token),
    url(r'verify',verify_jwt_token),
    url(r'contents/(?P<pk>.+)/$',ContentView.as_view()),
    path('registercheck/',Register.as_view()),
    path('logout/',Logoutview.as_view())
]
# urlpatterns += router.urls
