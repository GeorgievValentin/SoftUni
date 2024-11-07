from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from TreasureMentorApp.users.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length = 150,
        unique = True
    )

    email = models.EmailField(
        unique = True,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default = False,
        help_text = _("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default = True,
        help_text = _(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
