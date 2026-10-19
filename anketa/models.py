from django.db import models

class Anketa(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )

    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    photo = models.ImageField(upload_to='anketa_photos/', verbose_name="Фотография")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Пол")
    desired_position = models.CharField(max_length=100, verbose_name="Желаемая должность")
    experience_years = models.PositiveIntegerField(default=0, verbose_name="Опыт работы (лет)")
    about = models.TextField(blank=True, verbose_name="О себе")
    is_remote = models.BooleanField(default=False, verbose_name="Готов к удаленной работе")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"

    def __str__(self):
        return f"{self.full_name} - {self.desired_position}"