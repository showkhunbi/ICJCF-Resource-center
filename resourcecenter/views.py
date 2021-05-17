from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.db.models import Sum

from operator import methodcaller
import random
import botocore


from .forms import UploadForm, UpdateProfileForm, ReportFileForm, MessageForm
from .models import File, NonAcademicLevel, Report, Message, Traffic

from core.models import Department, Level, Student


class Home(View):
    def get(self, *args, **kwargs):
        context = {

        }
        return render(self.request, "rchome.html", context)


class Upload(View):
    def get(self, *args, **kwargs):
        context = {

        }
        return render(self.request, "uploadfile.html", context)

    def post(self, *args, **kwargs):
        form = UploadForm(self.request.POST or None)
        if form.is_valid():
            files = self.request.FILES.getlist("userUpload")

            department = form.cleaned_data.get("department")
            level = form.cleaned_data.get("level")
            courseCode = form.cleaned_data.get("courseCode").upper()
            description = form.cleaned_data.get("description")
            semester = form.cleaned_data.get("semester")

            count = 0
            uploads = []

            for file in files:
                if file.size <= 52428800:
                    if department != "nonAcademic" and department != "---SELECT DEPARTMENT---":
                        delete_id = random.randint(1000000, 99999999)
                        upload = File.objects.create(file=file, file_name=file.name, department=department.upper(
                        ), level=level, courseCode=courseCode, description=description, semester=semester, uploader=self.request.user.__str__(), delete_id=delete_id)
                    elif department == "nonAcademic":
                        delete_id = random.randint(1000000, 99999999)
                        upload = File.objects.create(
                            file=file, file_name=file.name, department=department, level=level, uploader=self.request.user.__str__(), delete_id=delete_id)

                    count += 1
                    uploads.append(upload)
                else:
                    messages.warning(
                        self.request, f"{file.name} exceeds the allowable file size")

            if self.request.user.is_authenticated:
                student = Student.objects.get(user=self.request.user)
                for upload in uploads:
                    student.files.add(upload)
                student.save()

            if count > 0:
                messages.success(
                    self.request, f"Successfully Uploaded {count} file(s)")

            context = {
                "uploads": uploads,
            }
            return render(self.request, "uploadsuccess.html", context)
        else:
            messages.warning(self.request, "Form is invalid")
            return redirect("resourcecenter:upload")


class DownloadList(ListView):
    template_name = "downloadlist.html"

    def get_queryset(self, **kwargs):
        if self.kwargs['department'].upper() == "NONACADEMIC":
            self.department = self.kwargs['department']
            self.level = get_object_or_404(
                NonAcademicLevel, id=self.kwargs['level'])
            return File.objects.filter(department=self.department, level=self.level.name).order_by("-id")
        else:
            self.department = get_object_or_404(
                Department, abbreviation=self.kwargs['department'].upper())
            self.level = get_object_or_404(
                Level, level_id=self.kwargs['level'])
            return File.objects.filter(department=self.department.abbreviation, level=self.level.__str__()).order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['department'].upper() == "NONACADEMIC":
            context.update({
                "level": get_object_or_404(
                    NonAcademicLevel, id=self.kwargs['level']).name
            })
        else:
            context.update({
                "department": self.kwargs["department"].upper(),
                "level": f" {self.kwargs['level']} Level",
            })
        return context


class DownloadView(View):
    def get(self, *args, **kwargs):
        try:
            file_object = get_object_or_404(File, slug=kwargs["slug"])
        except File.MultipleObjectsReturned:
            files = File.objects.filter(slug=kwargs["slug"])
            for file in files:
                file.reslug()
            file_object = files[0]
        context = {
            "object": file_object,
        }
        try:
            return render(self.request, "download.html", context)
        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == "404":
                file_object.delete()
            else:
                return render(self.request, "download.html", context)

    def post(self, *args, **kwargs):
        file_object = get_object_or_404(File, slug=kwargs["slug"])
        file_object.downloads += 1
        file_object.save()
        return redirect("resourcecenter:download_file", slug=file_object.slug)


class Upvote(View):
    def post(self, *args, **kwargs):
        file_object = get_object_or_404(File, slug=kwargs["slug"])
        if self.request.user.is_authenticated:
            file_object.upvotes += 1
            file_object.save()
            messages.success(self.request, "File Successfully upvoted")
        else:
            messages.warning(
                self.request, "You must be logged in to perform this action")
        return redirect("resourcecenter:download", department=kwargs["department"], level=kwargs["level"], slug=kwargs["slug"])


class Downvote(View):
    def post(self, *args, **kwargs):
        file_object = get_object_or_404(File, slug=kwargs["slug"])
        if self.request.user.is_authenticated:
            file_object.downvotes += 1
            file_object.save()
            messages.success(self.request, "File Successfully downvoted")
        else:
            messages.warning(
                self.request, "You must be logged in to perform this action")
        return redirect("resourcecenter:download", department=kwargs["department"], level=kwargs["level"], slug=kwargs["slug"])


class DeleteFile(View):
    def get(self, *args, **kwargs):
        file_object = get_object_or_404(
            File, slug=kwargs["slug"], delete_id=kwargs["delete_id"])
        context = {
            "object": file_object,
        }
        return render(self.request, "deletefile.html", context)

    def post(self, *args, **kwargs):
        file_object = get_object_or_404(
            File, slug=kwargs["slug"], delete_id=kwargs["delete_id"])
        department = file_object.department
        level = file_object.level
        file_object.delete()
        messages.success(self.request, "File Successfully Deleted")
        if department.upper() == "NONACADEMIC":
            n_a_l = NonAcademicLevel.objects.get(name=level)
            level = n_a_l.id
        return redirect("resourcecenter:downloadlist", department=department, level=level)


class MyAccount(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        student = Student.objects.get(user=self.request.user)
        context = {
            "student": student,
        }
        return render(self.request, "my_account.html", context)

    def post(self, *args, **kwargs):
        form = UpdateProfileForm(self.request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            department = form.cleaned_data.get("department").upper()
            level = form.cleaned_data.get("level")
            phone = form.cleaned_data.get("phone")

            try:
                dept = Department.objects.get(abbreviation=department)
                level = Level.objects.get(level_id=level)
                student = Student.objects.get(user=self.request.user)

                student.first_name = first_name
                student.last_name = last_name
                student.department = dept
                student.level = level
                student.phone = phone
                student.save()

                messages.success(self.request, "Profile Successfully updated")
            except:
                messages.error(self.request, "Something went wrong")
        return redirect("resourcecenter:my_account")


class Profile(View):
    def get(self, *args, **kwargs):
        user = get_object_or_404(User, username=kwargs["username"])
        student = get_object_or_404(Student, user=user)
        context = {
            "student": student,
        }
        return render(self.request, "profile.html", context)


class ReportView(View):
    def get(self, *args, **kwargs):
        file_object = get_object_or_404(File, slug=kwargs["slug"])
        context = {
            "file": file_object,
        }
        return render(self.request, "reportfile.html", context)

    def post(self, *args, **kwargs):
        form = ReportFileForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            reason = form.cleaned_data.get("reason")

            file_object = get_object_or_404(File, slug=kwargs["slug"])
            Report.objects.create(name=name, email=email,
                                  reason=reason, file=file_object)

            try:
                message = f"""
                REPORTER INFO:\nname: {name}\nemail: {email}\n\nFILE INFO:\nFile name: {file_object.file.name}\nDepartment: {file_object.department}\nLevel: {file_object.level}\n\nREASON:\n{reason}
                """
                send_mail("File Report", message,
                          from_email=settings.SERVER_EMAIL, recipient_list=[data[1] for data in settings.ADMINS])
            except:
                pass

            messages.success(self.request, "File Successfully Reported")
        else:
            messages.error(self.request, "Form is invalid")
        return redirect("resourcecenter:report", slug=kwargs["slug"])


class Terms(View):
    def get(self, *args, **kwargs):
        context = {

        }
        return render(self.request, "terms.html", context)


class MessageView(View):
    def post(self, *args, **kwargs):
        form = MessageForm(self.request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")

            Message.objects.create(name=name, email=email, message=message)
            messages.success(self.request, "Message successfully sent")

            try:
                message_ = f"""
                Message From Resource center User\nname: {name}\nemail: {email}\nMessage:\n{message}
                """
                send_mail("Message", message_,
                          from_email=settings.SERVER_EMAIL, recipient_list=[data[1] for data in settings.ADMINS])
            except:
                pass
        else:
            messages.error(self.request, "Form is Invalid")
        return redirect("resourcecenter:home")


class StatisticsView(View):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        contributors = sorted(students, key=methodcaller(
            "knowledge_points"), reverse=True)[:10]
        all_files = File.objects.all()
        most_downloaded = all_files.order_by("-downloads")[:10]
        most_popular = all_files.order_by("-upvotes")[:10]
        most_recent = all_files.order_by("-id")[:10]
        context = {
            "contributors": contributors,
            "most_downloaded": most_downloaded,
            "most_popular": most_popular,
            "most_recent": most_recent,
        }
        return render(self.request, "statistics.html", context)


def traffic_counter(request, *args, **kwargs):
    traffic, created = Traffic.objects.get_or_create(
        date=timezone.now().date())
    traffic.traffic += 1
    traffic.save()
    return HttpResponse("")


def traffic_counter_info(request, *args, **kwargs):
    traffics = Traffic.objects.all()
    today = traffics.get(date=timezone.now().date()).traffic
    yesterday = traffics.filter(
        date__day=timezone.now().date().day - 1, date__month=timezone.now().date().month, date__year=timezone.now().date().year).aggregate(Sum("traffic"))["traffic__sum"]
    this_month = traffics.filter(
        date__month=timezone.now().date().month, date__year=timezone.now().date().year).aggregate(Sum("traffic"))["traffic__sum"]
    last_month = traffics.filter(
        date__month=timezone.now().date().month - 1, date__year=timezone.now().date().year).aggregate(Sum("traffic"))["traffic__sum"]
    this_year = traffics.filter(
        date__year=timezone.now().date().year).aggregate(Sum("traffic"))["traffic__sum"]
    total = traffics.aggregate(Sum("traffic"))["traffic__sum"]
    return HttpResponse(f"""
    TRAFFIC INFORMATION<br/>
    Today: {today}<br/>
    Yesterday: {yesterday}<br/>
    This month: {this_month}<br/>
    Last month: {last_month}<br/>
    This Year: {this_year}<br/>
    Total: {total}<br/>
    """
                        )


class TestView(View):
    def get(self, *args, **kwargs):
        files = File.objects.all()
        count = 0
        for file in files:
            count += 1
            DownloadView.as_view()(self.request, department=file.department,
                                   level=file.level, slug=file.slug)
            print(count)
        context = {

        }
        return render(self.request, "generic.html", context)
