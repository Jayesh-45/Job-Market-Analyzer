from django.contrib import admin
from django.urls import path, include
from app1 import urls as app1_urls
from registration import urls as registration_urls
from home import urls as home_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include(app1_urls)),
    path('registration/', include(registration_urls)),
    path('home/', include(home_urls)),
]
