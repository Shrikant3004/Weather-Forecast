from django.contrib import admin
from django.urls import path
from forecast import views


admin.site.site_header = "Weather Forecast admin"
admin.site.site_title = "Weather Forecast admin portal"
admin.site.index_title = "Welcome to Weather Forecast admin portal"


urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('forecast', views.forecast,name='forecast')
]
