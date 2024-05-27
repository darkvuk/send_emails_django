from django.contrib import admin
from django.urls import path, include
import email_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', email_app.views.index)
]
