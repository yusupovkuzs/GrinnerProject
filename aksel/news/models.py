from django.db import models

class users(models.Model):
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    university = models.TextField('Название университета')
    status = models.CharField('Студент или преподаватель', max_length=50)
    num_group = models.CharField('Номер группы', max_length=30)
    email = models.CharField('Email', max_length=100)
    password = models.CharField('Пароль', max_length=200)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

