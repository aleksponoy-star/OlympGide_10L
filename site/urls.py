from django.contrib import admin
from django.urls import path
from .views import index, olymp_napr_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),              # главная страница (default.html)
    path("napr/", olymp_napr_list),  # таблица направлений
]



