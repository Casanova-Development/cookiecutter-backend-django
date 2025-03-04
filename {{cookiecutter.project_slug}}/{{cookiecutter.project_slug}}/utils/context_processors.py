"""Context processors file."""
from django.conf import settings


def settings_context(_request):
    """Set settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {'DEBUG': settings.DEBUG}
