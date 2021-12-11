from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'surname', 'description', 'email', 'cv_url')

        help_texts = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'description': 'Здравствуйте, Екатерина...',
            'email': 'Я отправлю ответ на этот email',
            'cv_url': 'https://linkedin.vashecv.com',
        }