import enum

import django.contrib.auth.models as auth_model
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from kufarbg_app.auth_app.managers import AppUserManager
from kufarbg_app.common.validators import validate_only_letters, MinDateValidator, MaxDateValidator


class AppUser(auth_model.AbstractBaseUser, auth_model.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 2
    PHONE_NUMBER_MAX_LENGTH = 16
    PHONE_NUMBER_REGEX_PATTERN = r"^\+?1?\d{9,15}$"
    PHONE_NUMBER_ERROR_MESSAGE = "Phone number must be entered in the format: '+999999999'.Up to 15 digits is allowed"

    class GENDER(enum.Enum):
        MALE = 'Male'
        FEMALE = 'Female'

        @classmethod
        def choices(cls):
            return ((item.name, item.value) for item in cls)

        @classmethod
        def max_length(cls):
            return max(len(item.value) for item in cls)

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,

        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,

        )
    )
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(
            RegexValidator(
                regex=PHONE_NUMBER_REGEX_PATTERN,
                message=PHONE_NUMBER_ERROR_MESSAGE
            ),
        )
    )

    age = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator,
            MaxDateValidator,
        )
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=GENDER.max_length(),
        choices=GENDER.choices(),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


