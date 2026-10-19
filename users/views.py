from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CustomRegisterForm, CustomLoginForm

class RegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profile')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    login_url = reverse_lazy('login')