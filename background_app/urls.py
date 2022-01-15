"""background_app URL Configuration

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
from django.views import static
from rest_framework_simplejwt.views import TokenObtainPairView

import main.views
from background_app import settings
from main.views import UserinfoViewset, ContentView, RegisterCheck, Logoutview, ChangeHeadPortrait, RegisterCheck, \
    Registe
from rest_framework.routers import DefaultRouter

#
# router = DefaultRouter()
# router.register('user', UserinfoViewset)
# from utils.my_jwt_response_payload_hander import MyTokenObtainPairSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/$', UserinfoViewset.as_view({'get': 'retrieve'})),
    url(r'^user/(?P<pk>\d+)/$', UserinfoViewset.as_view({'get': 'retrieve', })),
    url(r'authorization/', main.views.MyTokenObtainPairView.as_view()),
    url(r'contents/(?P<pk>\d+)$', ContentView.as_view()),
    path('registercheck/', RegisterCheck.as_view()),
    path('logout/', Logoutview.as_view()),
    url(r'register/',Registe.as_view()),
    url('headportrait/', ChangeHeadPortrait.as_view()),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url("send/",main.views.test)
]
# urlpatterns += router.urls
