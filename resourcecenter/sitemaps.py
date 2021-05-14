from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from core.models import Student, Department
from .models import File, NonAcademicLevel


class Site:
    domain = 'resourcecenter.com.ng'
    name = "Resource Center"


class StaticViewSitemap(Sitemap):
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(StaticViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['home', 'upload', 'statistics', 'terms', ]

    def location(self, item):
        return reverse(f"resourcecenter:{item}")


class StudentsSitemap(Sitemap):
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(StudentsSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return Student.objects.all().order_by("id")

    def location(self, item):
        return reverse(f"resourcecenter:profile", kwargs={"username": item.user.username})


class FilesSitemap(Sitemap):
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(FilesSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return File.objects.all().order_by("id")

    def location(self, item):
        return item.get_download_url()


class NonAcademicLevelSitemap(Sitemap):
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(NonAcademicLevelSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return NonAcademicLevel.objects.all().order_by("id")

    def location(self, item):
        return reverse(f"resourcecenter:downloadlist", kwargs={"department": "NonAcademic", "level": f"{item.id}"})


class DepartmentSitemap(Sitemap):
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(DepartmentSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        queryset = []
        departments = Department.objects.all()
        for department in departments:
            if department.college.abbreviation.upper() == 'COLAMRUD':
                if department.abbreviation.upper() == 'GNS':
                    print("hey")
                    for i in range(1, 3):
                        dept_object = {
                            "name": department.name,
                            "abbr": department.abbreviation,
                            "level": f"{i}00"
                        }
                        queryset.append(dept_object)
                else:
                    for i in range(1, 6):
                        dept_object = {
                            "name": department.name,
                            "abbr": department.abbreviation,
                            "level": f"{i}00"
                        }
                        queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLANIM':
                for i in range(1, 6):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLBIOS':
                for i in range(1, 5):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLENG':
                for i in range(1, 6):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLERM':
                for i in range(1, 6):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLFHEC':
                if department.abbreviation.upper == 'FST':
                    for i in range(1, 6):
                        dept_object = {
                            "name": department.name,
                            "abbr": department.abbreviation,
                            "level": f"{i}00"
                        }
                        queryset.append(dept_object)
                else:
                    for i in range(1, 5):
                        dept_object = {
                            "name": department.name,
                            "abbr": department.abbreviation,
                            "level": f"{i}00"
                        }
                        queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLMAS':
                for i in range(1, 5):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLPHYS':
                for i in range(1, 5):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLPLANT':
                for i in range(1, 6):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
            elif department.college.abbreviation.upper() == 'COLVET':
                for i in range(1, 7):
                    dept_object = {
                        "name": department.name,
                        "abbr": department.abbreviation,
                        "level": f"{i}00"
                    }
                    queryset.append(dept_object)
        return queryset

    def location(self, item):
        return reverse(f"resourcecenter:downloadlist", kwargs={"department": item["abbr"], "level": item["level"]})


sitemaps = {
    'static': StaticViewSitemap,
    'students': StudentsSitemap,
    'files': FilesSitemap,
    'nonAcademic': NonAcademicLevelSitemap,
    'departments': DepartmentSitemap,
}
