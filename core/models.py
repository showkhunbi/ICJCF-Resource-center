from django.db import models
from django.conf import settings


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    level = models.ForeignKey(
        "Level", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    files = models.ManyToManyField("resourcecenter.File", blank=True)
    is_resourcecenter_admin = models.BooleanField(default=False)

    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.user.username

    def name(self):
        return self.__str__()

    def knowledge_points(self):
        point = 0
        for file_object in self.files.all():
            point += file_object.score()
        return point


class Department(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=4, unique=True)
    college = models.ForeignKey(
        "College", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=10)
    level_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.level_id}"
