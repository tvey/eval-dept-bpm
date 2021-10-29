# Generated by Django 3.2.8 on 2021-10-29 20:25

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.department', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('username', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта')),
                ('extension_phone_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Добавочный номер телефона')),
                ('personal_email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Личная электронная почта')),
                ('personal_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Личный номер телефона')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Сотрудники/', verbose_name='Фото')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.position', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]