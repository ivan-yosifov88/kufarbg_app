import datetime

from django.db import models
from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django_countries.fields import CountryField

from kufarbg_app.common.validators import MinDateValidator, MaxDateValidator

UserModel = get_user_model()


class Destinations(models.Model):
    CITY_MAX_LENGTH = 200
    CITY_MIN_LENGTH = 2
    DESCRIPTION_TEXT_MAX_LENGTH = 500
    MIN_DATE = datetime.date(1900, 1, 1)
    MAX_DATE = datetime.date(2100, 1, 1)

    DEFAULT_USER_LIKES = 0
    country = CountryField(
        multiple=False,
    )
    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        validators=(
            MinLengthValidator(CITY_MIN_LENGTH),
        )
    )
    description = models.CharField(
        null=True,
        blank=True,
        max_length=DESCRIPTION_TEXT_MAX_LENGTH,
    )
    date_of_journey = models.DateField(
        default=timezone.now,
        null=True,
        blank=True,
        validators=(
            MinDateValidator(MIN_DATE),
            MaxDateValidator(MAX_DATE),
        )
    )

    photo = cloudinary_models.CloudinaryField(
        'image',
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Trip to {self.country.name}"

    class Meta:
        verbose_name_plural = "Destinations"


class Comments(models.Model):
    MAX_COMMENT_LENGTH = 250

    trip = models.ForeignKey(
        Destinations,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    comment = models.TextField(
        max_length=MAX_COMMENT_LENGTH,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"


class Likes(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    trip = models.ForeignKey(
        Destinations,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Likes"


