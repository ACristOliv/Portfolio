from django.contrib import admin
from django.urls import path

from portfolio.views import index_page

urlpatterns = [
    path('', index_page, name='index'),
    path('admin/', admin.site.urls),
]
