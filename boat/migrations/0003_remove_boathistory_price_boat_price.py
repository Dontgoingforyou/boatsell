# Generated by Django 5.1.1 on 2024-09-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0002_boathistory_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boathistory',
            name='price',
        ),
        migrations.AddField(
            model_name='boat',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
