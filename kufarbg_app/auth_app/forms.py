from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


from kufarbg_app.auth_app.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),

            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()
        return user


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        for placeholder in self.fields:
            self.fields[placeholder].widget.attrs['placeholder'] = "Please enter "+' '.join(placeholder.split('_'))

    class Meta:
        model = Profile
        exclude = ('user',)


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance
