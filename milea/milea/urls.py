from django.contrib import admin
from django.urls import path
from dev import views
urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.dev,name='dev'),
]