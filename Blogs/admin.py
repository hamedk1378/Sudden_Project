from django.contrib import admin
from .models import Idea


class BaseContentAdmin(admin.ModelAdmin):
    fieldsets = [
            [None, {"fields": ["body", "likes"]}],
            ["Date Information", {"fields": ["pub_date", "last_update"]}],
            ["Writer", {"fields": ["user"]}],
    ]
    list_filter = ["pub_date", "user__username"]
    readonly_fields = ["pub_date", "last_update"]


class IdeaAdmin(BaseContentAdmin):
    BaseContentAdmin.fieldsets[0][1]["fields"].insert(0, "topic")
    list_display = ["user__username", "topic", "pub_date", "is_recently_published"]


admin.site.register(Idea, IdeaAdmin)

