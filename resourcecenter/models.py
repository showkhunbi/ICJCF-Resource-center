from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from core.models import Student
from autoslug import AutoSlugField
from django.urls import reverse
from django.utils.crypto import get_random_string


SEMESTERS = (
    ("1", "First Semester"),
    ("2", "Second Semester"),
    ("3", "Not Applicable"),
)


class NonAcademicLevel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class File(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=999999, blank=True, null=True)
    semester = models.CharField(
        choices=SEMESTERS, max_length=1, blank=True, null=True)
    department = models.CharField(max_length=20)
    level = models.CharField(max_length=30)
    courseCode = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    downloads = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    uploader = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from="file")
    delete_id = models.IntegerField()

    def __str__(self):
        return self.file.name

    def score(self):
        up = self.upvotes * 10
        down = self.downvotes * 5
        downloads = self.downloads * 2
        return 20 + downloads + up - down

    def get_download_url(self):
        return reverse("resourcecenter:download", kwargs=({
            "department": self.department,
            "level": self.level,
            "slug": self.slug,
        }))

    def file_extension(self):
        split = self.file.name.split(".")
        if len(split) == 1:
            return "File"
        else:
            return self.file.name.split(".")[-1]

    def get_file_type(self):
        extension = self.file_extension().upper()
        audio = ["AIF", "CDA", "MID", "MIDI", "MP3",
                 "MPA", "OGG", "WAV", "WMA", "WPL"]
        compressed = ["7Z", "ARJ", "DEB", "PKG",
                      "RAR", "RPM", "GZ", "Z", "ZIP"]
        disc = ["BIN", "DMG", "ISO", "TOAST", "VCD"]
        data = ["CSV", "DAT", "DB", "DBF", "LOG",
                "MDB", "SAV", "SQL", "TAR", "XML"]
        email = ["EMAIL", "EML", "EMLX", "MSG", "OFT", "OST", "PST", "VCF"]
        document = ["DOCX", "DOC", "PDF", "ODT", "RTF", "TEX", "TXT", "WPD"]
        executable = ["APK", "BAT", "BIN", "CGI", "PL",
                      "COM", "EXE", "GADGET", "JAR", "MSI", "PY", "WSF"]
        font = ["FNT", "FON", "OTF", "TTF"]
        image = ["AI", "BMP", "GIF", "ICO", "JPEG", "JPG",
                 "PNG", "PS", "PSD", "SVG", "TIF", "TIFF"]
        internet = ["ASP", "ASPX", "CER", "CFM", "CGI", "PL", "CSS",
                    "HTM", "HTML", "JS", "JSP", "PART", "PHP", "PY", "RSS", "XHTML"]
        presentation = ["KEY", "ODP", "PPS", "PPT", "PPTX"]
        program = ["C", "CLASS", "CPP", "CS", "H",
                   "JAVA", "PHP", "PY", "SH", "SWIFT", "VB"]
        spreadsheet = ["ODS", "XLS", "XLSM", "XLSX"]
        system = ["BAK", "CAB", "CFG", "CPL", "CUR", "DLL", "DMP",
                  "DRV", "ICNS", "ICO", "INI", "INK", "MSI", "SYS", "TMP"]
        video = ["3G2", "3GP", "AVI", "FLV", "H264", "M4V", "MKV",
                 "MOV", "MP4", "MPG", "MPEG", "RM", "SWF", "VOB", "WMV"]
        if extension in document:
            return "Document"
        elif extension in audio:
            return "Audio"
        elif extension in compressed:
            return "Compressed"
        elif extension in disc:
            return "Disc"
        elif extension in data:
            return "Data"
        elif extension in email:
            return "Email"
        elif extension in executable:
            return "Executable"
        elif extension in font:
            return "Font"
        elif extension in image:
            return "Image"
        elif extension in internet:
            return "Internet File"
        elif extension in presentation:
            return "Presentation"
        elif extension in program:
            return "Program"
        elif extension in spreadsheet:
            return "Spreadsheet"
        elif extension in system:
            return "System"
        elif extension in video:
            return "Video"
        else:
            return extension

    def clean_size(self):
        size = self.file.size
        if size < 1024:
            return f"{size} bytes"
        elif size >= 1024 and size < 1048576:
            return "{0:.2f} kb".format(size/1024)
        elif size >= 1048576 and size < 1073741824:
            return "{0:.2f} mb".format(size/1048576)
        elif size >= 1073741824 and size < 1099511627776:
            return "{0:.2f} gb".format(size/1073741824)
        else:
            return size

    def get_semester(self):
        key = self.semester
        for semester in SEMESTERS:
            if key == semester[0]:
                return semester[1]
        return key

    def upvote_url(self):
        return reverse("resourcecenter:upvote", kwargs=({
            "department": self.department,
            "level": self.level,
            "slug": self.slug,
        }))

    def downvote_url(self):
        return reverse("resourcecenter:downvote", kwargs=({
            "department": self.department,
            "level": self.level,
            "slug": self.slug,
        }))

    def delete_url(self):
        return reverse("resourcecenter:deletefile", kwargs=({
            "slug": self.slug,
            "delete_id": self.delete_id,
        }))

    def report_url(self):
        return reverse("resourcecenter:report", kwargs=({
            "slug": self.slug,
        }))

    def reslug(self):
        self.slug = self.slug + f"_{get_random_string(length=5)}"
        self.save()
        return self.slug


@receiver(post_delete, sender=File)
def delete_function(sender, instance, **kwargs):
    instance.file.delete(False)


class Report(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    reason = models.CharField(max_length=999999)

    def __str__(self):
        return self.file.file.name


class Message(models.Model):
    name = models.CharField(max_length=9999, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=99999999)

    def __str__(self):
        return self.name


class Traffic(models.Model):
    date = models.DateField()
    traffic = models.IntegerField(default=0)

    def __str__(self):
        return self.date.strftime("%d %b %Y")
