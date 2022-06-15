from django.views.generic import TemplateView, DetailView, FormView
from django.contrib import messages
from datetime import datetime
from .models import C1
from .forms import CForm


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = C1.objects.all().order_by('-id')
        return context


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = C1


class AddView(FormView):
    template_name = 'new_post.html'
    form_class = CForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        C1.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Post successful!')
        return super().form_valid(form)
