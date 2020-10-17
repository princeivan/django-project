from django import forms

from .models import BLogpost


class BlogPostModelForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = BLogpost
        fields = '__all__'

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BLogpost.objects.filter(title__iexact= title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("this title has already been used. Please look for another one")
        return title