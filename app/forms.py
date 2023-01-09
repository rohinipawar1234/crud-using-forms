from .models import blog
from django import forms


class blogform(forms.ModelForm):
    class Meta:
        model = blog

        fields = "__all__"


    
    title = forms.CharField(widget=forms.TextInput({"placeholder":"ENTER TITLE"}))
    content = forms.CharField(widget=forms.TextInput({"placeholder":"write content"}))
    img_1 = forms.ImageField()
    date = forms.DateField(widget=forms.TextInput(attrs={"class":"datepicker"}))