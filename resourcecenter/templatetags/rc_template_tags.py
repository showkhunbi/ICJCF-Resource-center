from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from core.models import Student

register = template.Library()


@register.filter()
def clean_title(string):
    return string.replace("_", " ")


@register.filter()
def get_extension_image(extension):
    extension = extension.upper()
    static = settings.STATIC_URL
    if extension == "DOC" or extension == "DOCX":
        return static + "icons/doc.png"
    elif extension == "XLSX" or extension == "XLS":
        return static + "icons/excel.png"
    elif extension == "MP3":
        return static + "icons/music.png"
    elif extension == "PDF":
        return static + "icons/pdf.png"
    elif extension == "JPG" or extension == "JPEG" or extension == "PNG":
        return static + "icons/pic.png"
    elif extension == "PPT":
        return static + "icons/ppt.png"
    elif extension == "TXT":
        return static + "icons/txt.png"
    elif extension == "MP4" or extension == "AVI":
        return static + "icons/video.png"
    elif extension == "ZIP" or extension == "RAR":
        return static + "icons/zip.png"
    else:
        return static + "icons/txt.png"


@register.filter()
def downloadlist_shortcut(user):
    student = Student.objects.get(user=user)
    department = student.department
    level = student.level
    link = reverse("resourcecenter:downloadlist", kwargs=({
        "department": department.abbreviation,
        "level": level.level_id}))
    return f"<li><a href='{link}'>{department.abbreviation.upper()} {level.level_id}</a></li>"


@register.filter()
def get_name(user):
    student = Student.objects.get(user=user)
    return student.name()


@register.filter()
def is_resourcecenter_admin(user):
    student = Student.objects.get(user=user)
    return student.is_resourcecenter_admin


@register.filter()
def get_knowledge_point(username):
    user = User.objects.get(username=username)
    student = Student.objects.get(user=user)
    return student.knowledge_points()
