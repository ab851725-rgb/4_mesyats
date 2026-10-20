from django.contrib import admin
from .models import Genre, Movie, VipSeat, Comment

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(VipSeat)
admin.site.register(Comment)