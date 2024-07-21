from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField
from .models import Feedback,Note
from .models import LocalGuides
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

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
    image=forms.FileField()
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
            'first_name', 'last_name', 'email', 'image', 'description', 'phone_number','gender',
            'age', 'designation', 'address', 'city_name', 'district_name', 'postcode', 'instagram', 'twitter', 'facebook', 'linkedin'
        ]
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'class': 'form-horizontal'}
        self.helper.label_class = 'col-md-3 col-form-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Field('first_name', css_class='form-control'),
            Field('last_name', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('image', css_class='form-control'),
            Field('description', css_class='form-control'),
            Field('phone_number', css_class='form-control'),
            Field('age', css_class='form-control'),
            Field('designation', css_class='form-control'),
            Field('address', css_class='form-control'),
            Field('city_name', css_class='form-control'),
            Field('district_name', css_class='form-control'),
            Field('postcode', css_class='form-control'),
            Field('instagram', css_class='form-control'),
            Field('twitter', css_class='form-control'),
            Field('facebook', css_class='form-control'),
            Field('linkedin', css_class='form-control'),
            Submit('submit', 'Update', css_class='btn btn-update'),
        )
        
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        
        self.fields['gender'].widget.attrs.update({'placeholder': 'Enter your gender'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter a brief description'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Enter your phone number'})
        self.fields['age'].widget.attrs.update({'placeholder': 'Enter your age'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Enter your address'})
        self.fields['city_name'].widget.attrs.update({'placeholder': 'Enter your city'})
        self.fields['district_name'].widget.attrs.update({'placeholder': 'Enter your district'})
        self.fields['postcode'].widget.attrs.update({'placeholder': 'Enter your postcode'})
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



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']


class LocalGuidesForm(forms.ModelForm):
    class Meta:
        model = LocalGuides
        fields = ['name', 'age', 'phonenumber', 'email', 'address', 'guideplace', 'experience', 'amountcharge','image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'guideplace': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'amountcharge': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
