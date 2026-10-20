from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Genre, Comment, VipSeat
from .forms import MovieForm, CommentForm, VipSeatForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'cineboard/register.html'
    success_url = reverse_lazy('cineboard_login')

class CineLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'cineboard/login.html'

    def get_success_url(self):
        return reverse_lazy('movie_list')

class CineLogoutView(LogoutView):
    next_page = reverse_lazy('movie_list')

class MovieListView(ListView):
    model = Movie
    template_name = 'cineboard/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.all().order_by('-id')
        search_query = self.request.GET.get('q')
        genre_id = self.request.GET.get('genre')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['selected_genre'] = self.request.GET.get('genre')
        context['search_query'] = self.request.GET.get('q', '')
        return context

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'cineboard/movie_detail.html'
    context_object_name = 'movie'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['vip_form'] = VipSeatForm()
        return context

class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'
    success_url = reverse_lazy('movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'id': self.object.id})

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'cineboard/movie_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('movie_list')

class AddCommentView(View):
    def post(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
        return redirect('movie_detail', id=movie.id)

class BookVipSeatView(View):
    def post(self, request, id):
        if not request.user.is_authenticated:
            return redirect('cineboard_login')
        movie = get_object_or_404(Movie, id=id)
        if hasattr(request.user, 'vip_seat'):
            return redirect('movie_detail', id=movie.id)
        form = VipSeatForm(request.POST)
        if form.is_valid():
            vip = form.save(commit=False)
            vip.movie = movie
            vip.user = request.user
            vip.save()
        return redirect('movie_detail', id=movie.id)