# Generated by Django 2.1.7 on 2019-06-21 14:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя')),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]