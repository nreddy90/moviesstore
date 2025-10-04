from django.contrib import admin

# Register your models here.
from .models import Movie, Review, Petition
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Petition)