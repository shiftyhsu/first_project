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
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['username'].widget.attrs['style'] = 'width:200px; height:35px;margin:10px;margin-left:97px;'
        self.fields['email'].widget.attrs['style'] = 'width:200px; height:35px;margin:10px;margin-left:45px;'
        self.fields['password'].widget.attrs['style'] = 'width:200px; height:35px;margin:10px;;margin-left:103px;'
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
        profile_pic=forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['portfolio_site'].widget.attrs['style'] = 'width:400px; height:35px;margin:10px;margin-left:66px;'
        # self.fields['profile_pic'].widget.attrs['style'] = 'margin-left:7.4%;width:205px;height:35px;display: inline-block;padding: 6px 5px 3px 5px;font-size: 15px;cursor: pointer;text-align: center;text-decoration: none;outline: none;color: #fff;background-color: #298089;border: none;border-radius: 5px;box-shadow: 0 4px #999;'
        self.fields['profile_pic'].widget.attrs.update({'class':"custom-file-input",'id':"customFile",'style':'margin-left:97px;width:205px;height:35px;display: inline-block;padding: 6px 5px 3px 5px;font-size: 15px;cursor: pointer;text-align: center;text-decoration: none;outline: none;color: #fff;background-color: #298089;border: none;border-radius: 5px;box-shadow: 2px 3px 5px #999;'})
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
