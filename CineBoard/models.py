from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='movies/')
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title

class VipSeat(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vip_seat')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='vip_seats')
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user} - VIP {self.seat_number} ({self.movie.title})"

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.movie.title}"