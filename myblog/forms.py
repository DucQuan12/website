from django.forms import Form
from .models import blog

class add_form(Form):
    class Meta:
        model = blog
        fields = ('title', 'content', 'date', 'image',)