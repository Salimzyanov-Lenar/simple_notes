from django.urls import path
from .views import NotesList, NoteDeleteView, AboutTemplateView


urlpatterns = [
    path('', NotesList.as_view(), name='notes'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='delete_note'),
    path('about/', AboutTemplateView.as_view(), name='about'),
]