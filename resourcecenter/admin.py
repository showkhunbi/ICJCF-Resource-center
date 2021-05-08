from django.contrib import admin
from .models import File, NonAcademicLevel, Report, Message, Traffic


class FileAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "department",
        "level",
        "semester",
        "downloads",
        "upvotes",
        "downvotes",
        "uploader",
        "slug",
    )

    list_display_links = (
        "department",
        "level",
    )


class NonAcademicLevelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "reason",
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "message",
    )


class TrafficAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "traffic",
    )


admin.site.register(File, FileAdmin)
admin.site.register(NonAcademicLevel, NonAcademicLevelAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Traffic, TrafficAdmin)
