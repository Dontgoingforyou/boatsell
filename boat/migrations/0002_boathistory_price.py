# Generated by Django 5.1.1 on 2024-09-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boathistory',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
