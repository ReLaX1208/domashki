from django.forms import ModelForm

from bboard.models import Bb, MyForm


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')

class MyForm(ModelForm):
    class Meta:
        model = MyForm
        fields = ('name', 'email', 'message')
