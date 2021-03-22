from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # path("error", handler500, name="error")

]

if settings.DEBUG:
    #     urlpatterns += static(settings.STATIC_URL,
    #                           document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
