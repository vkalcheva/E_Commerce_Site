from django.contrib import admin

from e_commerce_site.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
