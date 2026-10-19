from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название тура")
    description = models.TextField(verbose_name="Описание тура")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена тура")
    start_date = models.DateField(verbose_name="Дата начала тура")
    categories = models.ManyToManyField(Category, related_name="tours", verbose_name="Категории")

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

    def __str__(self):
        return self.title


class Person(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО пассажира")
    ticket_number = models.CharField(max_length=50, unique=True, verbose_name="Номер билета")
    tour = models.OneToOneField(
        Tour, 
        on_delete=models.CASCADE, 
        related_name="passenger", 
        verbose_name="Тур"
    )

    class Meta:
        verbose_name = "Пассажир"
        verbose_name_plural = "Пассажиры"

    def __str__(self):
        return f"{self.full_name} (Билет №{self.ticket_number})"


class Comment(models.Model):
    tour = models.ForeignKey(
        Tour, 
        on_delete=models.CASCADE, 
        related_name="comments", 
        verbose_name="Тур"
    )
    author_name = models.CharField(max_length=100, verbose_name="Имя автора")
    text = models.TextField(verbose_name="Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отзыва")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.author_name} к {self.tour.title}"