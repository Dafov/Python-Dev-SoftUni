from django import forms

from notes.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    pass