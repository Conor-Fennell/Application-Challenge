from django import forms
from .task2 import reverseIterative
class inputForm(forms.Form):
    #Just going to have 1 input, the string we want to reverse
    string = forms.CharField(label='Please enter a string to be reversed')