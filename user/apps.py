from django.apps import AppConfig


class UserConfig(AppConfig):
    """Userapp config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = 'Users'
