from django import forms

from adventureProjectSia.advanture_app.models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'image': forms.FileInput(attrs={'class': 'img_input'}),
        }
        exclude = ('user',)


class CommentForm(forms.Form):
    text = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control rounded-2', }))

