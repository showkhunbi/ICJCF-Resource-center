from django.contrib import admin
from .models import Student, Department, Level, College


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "last_name",
        "department",
        "level",
        "phone",
    )


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "abbreviation",
        "college",
    )


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level_id",
    )


class CollegeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "abbreviation",
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(College, CollegeAdmin)
