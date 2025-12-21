from django.contrib import admin
from .models import Orgs, Predmet, Profil, Level, Olymps


@admin.register(Predmet)
class PredmetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 160
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('name', 'id')


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 20
    ordering = ('name',)


@admin.register(Orgs)
class OrgsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name')
    list_per_page = 20
    ordering = ('short_name',)

@admin.register(Olymps)
class OlympsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_per_page = 20
    ordering = ('full_name',)

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)

