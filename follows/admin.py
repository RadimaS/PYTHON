from django.contrib import admin

from g.models import Follow


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    pass

