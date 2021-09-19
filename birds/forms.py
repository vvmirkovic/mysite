from django import forms
from captcha.fields import CaptchaField
from birds.models import BirdPhoto

class BirdCaptchaForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = BirdPhoto
        fields = '__all__'

#class CaptchaForm(forms.Form)
#    captcha = CaptchaField()
