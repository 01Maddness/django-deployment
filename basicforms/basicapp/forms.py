from django import forms
from django.core import validators


class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Enter your email again!")
    text = forms.CharField(widget = forms.Textarea)


    botcatcher = forms.CharField(widget = forms.HiddenInput,
                                 required = False,
                                 validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_cleaned_data = super().clean()

        email = all_cleaned_data['email']
        name = all_cleaned_data['name']
        vmail = all_cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails did not match!!!")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     else:
    #         return botcatcher
