from django.contrib import admin

from .models import Boardgame

# Register your models here.
@admin.register(Boardgame)
class BoardgameAdmin(admin.ModelAdmin):
    list_display = ("title", "artist")


