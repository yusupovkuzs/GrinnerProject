from .models import users
from django.forms import ModelForm, TextInput, Textarea

class usersFormRegistrationStudent(ModelForm):
    class Meta:
        model = users
        fields = ['surname', 'name', 'patronymic', 'university', 'status', 'num_group', 'email', 'password']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "university": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Название университета'
            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Студент или преподаватель'
            }),
            "num_group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер группы'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }