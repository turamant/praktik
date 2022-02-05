

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include

from web_admin.views import SignUpView, LandingPageView

urlpatterns = [
    path('ask_admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='base'),
    path('', include('web_admin.urls', namespace='web_admin')),
    path('api/v1/new/', include('apis.urls', namespace='apis')),
    path('signup', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
