from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    count = models.IntegerField(default=0, verbose_name="Остаток на складе")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    add_date = models.DateField(verbose_name="Дата добавления")
    author_email = models.EmailField(blank=True, null=True, verbose_name="Email автора")
    image_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на картинку товара")
    is_bestseller = models.BooleanField(default=False, verbose_name="Бестселлер")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг")

class SerialNumber(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name="Товар")
    number = models.CharField(max_length=50, unique=True, verbose_name="Серийный номер")

    def __str__(self):
        return f"Серийный номер для {self.product.title}: {self.number}"

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name="Товар")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Комментарий к {self.product.title}"
