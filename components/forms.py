from django import forms
from django.db.migrations.state import get_related_models_tuples
from .models import PostComment, ArticleComment, BookReview
from django.utils.translation import gettext_lazy as _

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        

        fields = ['content','parent']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        

        fields = ['content','parent']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        

        fields = ['content','parent']
        
        labels = {
            'content': _(''),
        }
        
        widgets = {
            'content' : forms.TextInput(),
        }