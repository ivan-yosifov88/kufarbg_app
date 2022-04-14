from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


class HomePageData(models.Model):
    DEFAULT_THOUGHTS = "Life is wonderful!"
    DEFAULT_IMAGE_URL = 'https://basecampadventure.com/wp-content/uploads/2018/07/Travel-Related-Links-1290x540.png'
    site_images_url = models.URLField()
    good_thoughts = models.TextField()

    class Meta:
        verbose_name_plural = "HomePageData"


class SiteOwnerData(models.Model):
    PHONE_NUMBER_MAX_LENGTH = 16
    PHONE_NUMBER_REGEX_PATTERN = r"^\+?1?\d{9,15}$"
    PHONE_NUMBER_ERROR_MESSAGE = "Phone number must be entered in the format: '+999999999'.Up to 15 digits is allowed"
    COMPANY_NAME_MAX_LENGTH = 30
    COMPANY_NAME_MIN_LENGTH = 2
    email = models.EmailField()
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
    company_name = models.CharField(
        max_length=COMPANY_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(COMPANY_NAME_MIN_LENGTH),
        )
    )
    address = models.TextField()

    class Meta:
        verbose_name_plural = "SiteOwnerData"


class AboutUsData(models.Model):
    ABOUT_US_MAX_LENGTH = 500
    site_owners_description = models.TextField(
        max_length=ABOUT_US_MAX_LENGTH,
    )

    class Meta:
        verbose_name_plural = "AboutUsData"
