"""Application config for application Accounts."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    """Define default application config."""

    name = '{{ cookiecutter.project_slug }}.accounts'
    verbose_name = _('Accounts')
