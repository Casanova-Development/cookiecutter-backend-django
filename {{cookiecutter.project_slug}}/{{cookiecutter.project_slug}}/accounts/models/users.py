"""Users models for application Accounts."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Define a custom default user model."""

    pass
