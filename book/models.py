from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название книги")
    description = models.TextField(blank=True, verbose_name="Описание")
    pages = models.IntegerField(verbose_name="Количество страниц")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    publish_date = models.DateField(verbose_name="Дата публикации")
    author_email = models.EmailField(blank=True, null=True, verbose_name="Email автора")
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на обложку")
    is_bestseller = models.BooleanField(default=False, verbose_name="Бестселлер")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    
    GENRE_CHOICES = (
        ('FICTION', 'Художественная литература'),
        ('NON-FICTION', 'Научно_популярная'),
        ('SCI-FI', 'Фантастика'),
        ('DETECTIVE', 'Детектив'),
    )
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='FICTION', verbose_name="Жанр")

    def __str__(self):
        return self.title
