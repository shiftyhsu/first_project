from django import forms
from django.contrib.auth.models import User
from django.core import validators
from first_app.models import SAVE
from first_app.models import UserProfileInfo
# def check_for_s(value):
#     if value[0].lower()!='s':
#         raise forms.ValidationError('Need A Start of s/S')
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
class FormName(forms.ModelForm):
    name=forms.CharField()
    email=forms.EmailField()
    vemail=forms.EmailField(label='Enter Your Email Again!!')
    text=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=SAVE
        fields='__all__'
    # def clean(self):
    #     all_clean_data=super().clean()
    #     email=all_clean_data['email']
    #     vmail=all_clean_data['vemail']
    #     if email != vmail:
    #         raise forms.ValidationError('Email not Match!!!')
    # # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(6)])
    # # def clean(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)==0:
    #         raise forms.ValidationError('Final Countdown')
    #     return botcatcher
