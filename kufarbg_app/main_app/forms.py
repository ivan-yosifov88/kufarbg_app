import datetime

from django import forms

from kufarbg_app.auth_app.models import Profile
from kufarbg_app.common.bootstrap_mixin import BootstrapFormControl
from kufarbg_app.common.validators import validate_only_letters
from kufarbg_app.main_app.models import UserTrips, Comments


class ContactForm(forms.Form, BootstrapFormControl):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 20
    MESSAGE_TEXT_MAX_LENGTH = 300
    NUMBER_OF_ROWS_TEXT_FIELD = 4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().apply_class_form_control(self.fields)

    name = forms.CharField(
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
        validators=(
            validate_only_letters,
        )
    )
    email = forms.EmailField()
    message = forms.CharField(
        max_length=MESSAGE_TEXT_MAX_LENGTH,
        widget=forms.Textarea(
            attrs={
                'rows': NUMBER_OF_ROWS_TEXT_FIELD
            }
        )
    )


#     add boot catcher
# i may add subject choice


class CreateDestinationForm(forms.ModelForm, BootstrapFormControl):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        super().apply_class_form_control(self.fields)

    def save(self, commit=True):
        destination = super().save(commit=False)
        destination.user = self.user
        if commit:
            destination.save()
        return destination

    class Meta:
        DESCRIPTION_ROWS_COUNT = 5
        model = UserTrips
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'date_of_journey': forms.SelectDateWidget(
                attrs={
                    'year': datetime.date.today().year
                }, years=range(
                    UserTrips.MIN_DATE.year, UserTrips.MAX_DATE.year)),
            'country': forms.Select(),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter city '
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': DESCRIPTION_ROWS_COUNT,
                }
            ),
            'photo': forms.URLInput(
                attrs={
                    'placeholder': 'Enter photo URL',
                }
            )
        }


class CreatePhotoForm(forms.ModelForm, BootstrapFormControl):

    def __init__(self, destination, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.destination = destination
        super().apply_class_form_control(self.fields)

    def save(self, commit=True):
        photo = super().save(commit=False)
        photo.user = self.destination

        if commit:
            photo.save()
        return photo

    photo = forms.URLField()


class DestinationCommentForm(forms.ModelForm, BootstrapFormControl):
    COMMENT_TEXT_MAX_LENGTH = 300
    NUMBER_OF_ROWS_TEXT_FIELD = 4

    def __init__(self, user, destination_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.destination_id = destination_id
        super().apply_class_form_control(self.fields)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if commit:
            comment.trip_id = self.destination_id
            comment.author_id = self.user.id

            comment.save()
        return comment

    comment = forms.CharField(
        max_length=COMMENT_TEXT_MAX_LENGTH,
        widget=forms.Textarea(
            attrs={
                'rows': NUMBER_OF_ROWS_TEXT_FIELD
            }
        )
    )

    class Meta:
        model = Comments
        fields = ('comment',)
