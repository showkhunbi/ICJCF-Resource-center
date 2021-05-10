from django import forms


class UploadForm(forms.Form):
    department = forms.CharField(max_length=20)
    level = forms.CharField(max_length=30)
    courseCode = forms.CharField(max_length=8, required=False)
    description = forms.CharField(max_length=20, required=False)
    semester = forms.CharField(max_length=1, required=False)


class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    department = forms.CharField()
    level = forms.CharField()
    phone = forms.CharField(required=False)


class ReportFileForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    file_name = forms.CharField()
    reason = forms.CharField(required=False)


class MessageForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField()
