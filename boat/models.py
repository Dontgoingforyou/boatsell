from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', unique=True)

    def __str__(self):
        return f"{self.email} ({self.name})"

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class Boat(models.Model):

    name = models.CharField(max_length=50, verbose_name="Название")
    year = models.PositiveIntegerField(**NULLABLE, verbose_name="Год выпуска")
    price = models.IntegerField(**NULLABLE, verbose_name='Цена')

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'лодка'
        verbose_name_plural = 'лодки'


class BoatHistory(models.Model):

    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='лодка')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    start_year = models.PositiveIntegerField(**NULLABLE, verbose_name="владел с")
    stop_year = models.PositiveIntegerField(**NULLABLE, verbose_name="владел по")

    def __str__(self):
        return f"{self.boat} {self.start_year}-{self.stop_year}"

    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'история'

