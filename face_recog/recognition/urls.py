from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
app_name = "myapp"
urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.registerUser,name="register"),
    path('scan',views.Scan,name="scan"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)