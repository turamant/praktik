from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from web_admin.forms import NewCreateForm
from web_admin.forms import CustomUserCreateForm


class LandingPageView(TemplateView):
    template_name = "base.html"


class CreateNew(LoginRequiredMixin, CreateView):
    form_class = NewCreateForm
    template_name = 'web_admin/create_new.html'
    success_url = '/'


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreateForm

    def get_success_url(self):
        return reverse('login')
