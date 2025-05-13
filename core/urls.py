from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import home
from .views import home, contact_form
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('contact/', contact_form, name='contact_form'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)