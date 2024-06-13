from django import forms
from article_app.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "article", "created_by", "likes"]


class LoginForm(forms.Form):
    name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
