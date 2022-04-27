import datetime
import enum

import django.contrib.auth.models as auth_model
from cloudinary import models as cloudinary_models
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
    MIN_DATE_OF_BIRTH = datetime.date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = datetime.date(2100, 1, 1)

    class GENDER(enum.Enum):
        MALE = 'Male'
        FEMALE = 'Female'

        @classmethod
        def choices(cls):
            return ((item.value, item.value) for item in cls)

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

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            MinDateValidator(MIN_DATE_OF_BIRTH),
            MaxDateValidator(MAX_DATE_OF_BIRTH),
        )
    )
    image_url = cloudinary_models.CloudinaryField(
        'image',
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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year
