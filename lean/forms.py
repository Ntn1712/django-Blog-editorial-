from django import forms

from .models import articles,posts,delhi,bangalore,chennai,mumbai,ques

class articlesForm(forms.ModelForm):
    Name = forms.CharField(max_length=300)
    Topic = forms.CharField(max_length=500)
    Content = forms.CharField(max_length=5000)

    class Meta():
        model = articles
        fields = ['Name' , 'Topic' , 'Content']

class delhiForm(forms.ModelForm):
    Name = forms.CharField(max_length=300)
    Comment = forms.CharField(max_length=2000)

    class Meta():
        model = delhi
        fields = ['Name' , 'Comment']

class bangaloreForm(forms.ModelForm):
    Name = forms.CharField(max_length=300)
    Comment = forms.CharField(max_length=2000)

    class Meta():
        model = bangalore
        fields = ['Name' , 'Comment']

class chennaiForm(forms.ModelForm):
    Name = forms.CharField(max_length=300)
    Comment = forms.CharField(max_length=2000)

    class Meta():
        model = chennai
        fields = ['Name' , 'Comment']

class mumbaiForm(forms.ModelForm):
    Name = forms.CharField(max_length=300)
    Comment = forms.CharField(max_length=2000)

    class Meta():
        model = mumbai
        fields = ['Name' , 'Comment']

class quesForm(forms.ModelForm):
    Ques = forms.CharField(max_length=2000)

    class Meta():
        model = ques
        fields = ['Ques']