from django.contrib import admin

from .models import Profile, Contacts


@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass
