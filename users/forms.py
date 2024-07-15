from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    #phone_number = forms.CharField(max_length=15, required=False, help_text='Enter your phone number')

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email',  'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        #user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()

        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email*")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    captcha = CaptchaField()  # Updated field for django-simple-captcha


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False, help_text='Enter your phone number')
    age = forms.IntegerField(required=False, help_text='Enter your age')
    designation = forms.ChoiceField(choices=[('student', 'Student'), ('others', 'Others')], required=False)
    address = forms.CharField(max_length=255, required=False, help_text='Enter your address')
    city_name = forms.CharField(max_length=100, required=False, help_text='Enter your city name')
    district_name = forms.CharField(max_length=100, required=False, help_text='Enter your district name')
    postcode = forms.CharField(max_length=10, required=False, help_text='Enter your postcode')
    instagram = forms.URLField(required=False, help_text='Enter your Instagram profile URL')
    twitter = forms.URLField(required=False, help_text='Enter your Twitter profile URL')
    facebook = forms.URLField(required=False, help_text='Enter your Facebook profile URL')
    linkedin = forms.URLField(required=False, help_text='Enter your LinkedIn profile URL')
    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'email', 'image', 'description', 'phone_number',
            'age', 'designation', 'address', 'city_name', 'district_name', 'postcode', 'instagram', 'twitter', 'facebook', 'linkedin'
        ]
    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        user.social_media_links = {
            'instagram': self.cleaned_data['instagram'],
            'twitter': self.cleaned_data['twitter'],
            'facebook': self.cleaned_data['facebook'],
            'linkedin': self.cleaned_data['linkedin'],
        }
        if commit:
            user.save()
        return user


class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    captcha = CaptchaField()  # Updated field for django-simple-captcha
from django import forms

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))
