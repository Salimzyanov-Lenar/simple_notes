from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/notes/', permanent=True)),
    path('notes/', include('notes.urls')),
    path('users/', include('users.urls', namespace="users")),
]
