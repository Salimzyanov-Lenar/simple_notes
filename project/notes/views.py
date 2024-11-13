from django.shortcuts import render
from django.views.generic import ListView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import AddNote
from django.shortcuts import redirect
from django.urls import reverse_lazy


class NotesList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/notes.html'
    context_object_name = 'notes'
    login_url = '/users/login/'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddNote()
        return context

    def post(self, request, *args, **kwargs):
        form = AddNote(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes')
        return self.get(request, *args, **kwargs)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes')


class AboutTemplateView(TemplateView):
    template_name = 'notes/about.html'