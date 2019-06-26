# Generated by Django 2.1.7 on 2019-06-21 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Неверный формат номера', regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон'),
        ),
    ]