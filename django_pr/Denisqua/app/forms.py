from django import forms
from app import models


class AddFriend(forms.ModelForm):
    class Meta:
        model = models.AppModel
        fields = ['name', 'age', 'status']
    # name = forms.CharField(max_length=128, label='Имя')
    # age = forms.IntegerField(min_value=1, max_value=120, label='Возраст')
    # status = forms.CharField(max_length=128, label='Статус')
