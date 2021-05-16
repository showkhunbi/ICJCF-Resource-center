from django.urls import path
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from django_downloadview import ObjectDownloadView

from .views import TestView, Upload, Home, DownloadList, DownloadView, Upvote, Downvote, DeleteFile, MyAccount, Profile, ReportView, Terms, MessageView, StatisticsView, traffic_counter, traffic_counter_info
from .models import File
from .sitemaps import sitemaps

app_name = "resourcecenter"

download = ObjectDownloadView.as_view(model=File, file_field='file')

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    #     path("test/", TestView.as_view(), name="test"),
    path("upload/", Upload.as_view(), name="upload"),
    path("terms/", Terms.as_view(), name="terms"),
    path("message/send/", MessageView.as_view(), name="message"),
    path("account/", MyAccount.as_view(), name="my_account"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
    path("traffic/counter", traffic_counter, name="traffic"),
    path("traffic/counter/info", traffic_counter_info, name="traffic_info"),
    path("profile/<str:username>/", Profile.as_view(), name="profile"),
    path("download/<str:department>/<str:level>/",
         DownloadList.as_view(), name="downloadlist"),
    path("download/<str:department>/<str:level>/<slug>/",
         DownloadView.as_view(), name="download"),
    path("report/<slug>/", ReportView.as_view(), name="report"),
    path("delete/<slug>/<int:delete_id>/",
         DeleteFile.as_view(), name="deletefile"),
    path("upvote/<str:department>/<str:level>/<slug>/",
         Upvote.as_view(), name="upvote"),
    path("downvote/<str:department>/<str:level>/<slug>/",
         Downvote.as_view(), name="downvote"),
    url('^download/(?P<slug>[A-Za-z0-9_-]+)/$',
        download, name='download_file'),

]
