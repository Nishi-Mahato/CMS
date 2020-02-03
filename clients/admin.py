from django.contrib import admin
from .models import Client, Comment, Vehicle


class CommentInline(admin.TabularInline):
    model = Comment


class VehicleInline(admin.TabularInline):
    model = Vehicle


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        VehicleInline,
    ]
    model = Client


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Vehicle)