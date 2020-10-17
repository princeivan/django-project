

from django import forms

from .models import Report
from Adminsite.models import News
from django.forms import ModelForm

Status_choices =[
    ('ongoing','Ongoing'),
    ('finished','finished')

]

class ReportForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=250, widget =  forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    status = forms.CharField(max_length=50, widget =  forms.Select(choices =Status_choices, attrs={'class':'form-control'}))
    Time = forms.TimeField(widget =  forms.DateTimeInput(attrs={'class':'form-control'}))
    Date = forms.DateField(widget =  forms.DateTimeInput(attrs={'class':'form-control'}))
    image = forms.ImageField(required =False)

    class Meta:
        model = Report
        fields = ['title', 'description', 'location', 'status', 'Time', 'Date', 'image']


class NewsForm(forms.ModelForm):
    headline = forms.CharField(max_length =50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Headline'}))
    Pub_date = forms.DateField(widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Publish Date'}))
    reporter = forms. CharField(max_length =50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Published By:'}))
    content = forms.CharField(max_length =10000, widget =  forms.Textarea(attrs={'class':'form-control', 'label':'Body'}))
    comments = forms.CharField(max_length =1000, widget =  forms.Textarea(attrs={'class':'form-control', 'label':'Comments'}))



    class Meta:
        model = News
        fields = ['headline', 'Pub_date', 'reporter', 'content', 'comments']





    # Choice1 = forms.CharField(
    #     label = 'first choice',
    #      max_length =100,
    #      min_length = 3,
    #      widget =  forms.TextInput(attrs={'class':'form-control'}))

    # Choice2 = forms.CharField(
    #     label = 'second choice',
    #      max_length =100,
    #      min_length = 3,
    #      widget =  forms.TextInput(attrs={'class':'form-control'}))
    # class Meta:
    #     model = Report
    #     fields = ['text', 'Choice1', 'Choice2']
    #     widgets = {
    #          'text': forms.Textarea(attrs ={ "class":"form-control", "row":3, "cols":10 })
    #     }
    