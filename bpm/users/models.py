from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Position(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name='Отдел'
    )
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class User(AbstractBaseUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Должность',
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50,
    )
    first_name = models.CharField(
        'Имя',
        max_length=50,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=50,
        null=True,
        blank=True,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=50,
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=100,
        unique=True,
    )
    extension_phone_number = models.PositiveSmallIntegerField(
        'Добавочный номер телефона',
        null=True,
        blank=True,
    )
    personal_email = models.EmailField(
        'Личная электронная почта',
        max_length=100,
        null=True,
        blank=True,
    )
    personal_phone_number = PhoneNumberField(
        'Личный номер телефона',
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        'Фото',
        upload_to='Сотрудники/',
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_email(self):
        return f'{self.username}@company.ru'

    def __str__(self):
        return f'{self.last_name, self.first_name} ({self.email})'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
