from django.contrib import admin

from my_project.app.models import User, PortComponent


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(PortComponent)
class PortComponentAdmin(admin.ModelAdmin):
    pass
