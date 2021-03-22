from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import NewStudentForm
from .models import Student, Department, Level


class HomeView(View):
    def get(self, *args, **kwargs):
        return redirect("resourcecenter:home")


class Register(View):
    def get(self, *args, **kwargs):
        return redirect("account_signup")

    def post(self, *args, **kwargs):
        form = NewStudentForm(self.request.POST or None)
        context = {
            "form": form,
        }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            password2 = form.cleaned_data.get("password2")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            department = form.cleaned_data.get("department").upper()
            level = form.cleaned_data.get("level")
            phone = form.cleaned_data.get("phone")

            if password == password2:
                try:
                    dept = Department.objects.get(abbreviation=department)
                    level = Level.objects.get(level_id=level)

                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    Student.objects.create(
                        user=user, first_name=first_name, last_name=last_name, department=dept, level=level, phone=phone)
                    messages.success(
                        self.request, "Account Successfully created")

                    authUser = authenticate(request=self.request,
                                            username=username, password=password)
                    if User is not None:
                        login(self.request, authUser)

                    return redirect("resourcecenter:home")
                except:
                    messages.error(self.request, "Something went wrong")
            else:
                messages.warning(self.request, "Password does not match")
        else:
            messages.error(self.request, "Signup form is invalid")

        return render(self.request, "account/signup.html", context)


def handler404(request, *args, **argv):
    context = {}
    response = render(request, "errorpages/404.html", context=context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    context = {}
    response = render(request, "errorpages/500.html", context=context)
    response.status_code = 500
    return response


def handler400(request, *args, **argv):
    context = {}
    response = render(request, "errorpages/400.html", context=context)
    response.status_code = 400
    return response


def handler403(request, *args, **argv):
    context = {}
    response = render(request, "errorpages/403.html", context=context)
    response.status_code = 403
    return response
