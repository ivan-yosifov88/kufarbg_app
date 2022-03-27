from django.contrib.auth import forms as auth_forms, get_user_model

from kufarbg_app.auth_app.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': auth_forms.forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),

            'password1': auth_forms.forms.PasswordInput(),
            'password2': auth_forms.forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()
        return user


class EditProfileForm:
    pass


class DeleteProfileForm:
    pass
