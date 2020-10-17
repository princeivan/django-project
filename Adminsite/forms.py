from django import forms

from reports.models import Report

from .models import PoliceStation, News, Wanted, LostPerson

Status_choices =[
    ('ongoing', 'finished'),
]

class ReportForm(forms.Form):
    title = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=250, widget =  forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    status = forms.CharField(max_length=50, widget =  forms.Select(choices =Status_choices, attrs={'class':'form-control'}))
    Time = forms.TimeField(widget =  forms.DateTimeInput(attrs={'class':'form-control'}))
    Date = forms.DateField(widget =  forms.DateTimeInput(attrs={'class':'form-control'}))
    image = forms.ImageField()

class Police_Station(forms.ModelForm):
    name = forms.CharField(max_length =50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Full Name'}))
    location = forms.CharField(max_length =50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Location'}))
    Contacts = forms.IntegerField(widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Contact'}))

    class Meta:
        model = PoliceStation
        fields = ['name', 'location', 'Contacts']


class NewsForm(forms.ModelForm):
    headline = forms.CharField(max_length =50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Headline'}))
    Pub_date = forms.DateField(widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Publish Date'}))
    reporter = forms. CharField(max_length =50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Published By:'}))
    content = forms.CharField(max_length =10000, widget =  forms.Textarea(attrs={'class':'form-control', 'label':'Body'}))
    comments = forms.CharField(max_length =1000, widget =  forms.Textarea(attrs={'class':'form-control', 'label':'Comments'}))



    class Meta:
        model = News
        fields = ['headline', 'Pub_date', 'reporter', 'content', 'comments']

class WantedForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Full Name'}))
    # id = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'label':'ID Number'}))
    description = forms.CharField(max_length=250, widget =  forms.Textarea(attrs={'class':'form-control', 'label':'Description'}))
    image = forms.ImageField()

    class Meta:
        model = Wanted
        fields ='__all__'

class LostPersonForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Full Name'}))
    # id = forms.IntegerField(widget =  forms.TextInput(attrs={'class':'form-control', 'label':'ID Number'}))
    description = forms.CharField(max_length=250, widget =  forms.TextInput(attrs={'class':'form-control', 'label':'Description'}))
    image = forms.ImageField()

    class Meta:
        model = LostPerson
        fields = '__all__'


class ReportForms(forms.Form):
    title = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=250, widget =  forms.TextInput(attrs={'class':'form-control'}))
    location = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    status = forms.CharField(max_length=50, widget =  forms.TextInput(attrs={'class':'form-control'}))
    Time = forms.TimeField(widget =  forms.DateTimeInput(attrs={'class':'form-control'}))
    Date = forms.DateField(widget =  forms.DateTimeInput(attrs={'class':'form-control'}))
    image = forms.ImageField()

