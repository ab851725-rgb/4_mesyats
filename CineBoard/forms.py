from django import forms
from .models import Movie, Comment, VipSeat

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'text')
        widgets = {
            'author_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Ваш отзыв о фильме...'}),
        }

class VipSeatForm(forms.ModelForm):
    class Meta:
        model = VipSeat
        fields = ('seat_number',)
        widgets = {
            'seat_number': forms.TextInput(attrs={'placeholder': 'Например: VIP-1'}),
        }