from django.apps import AppConfig


class UserprofilesConfig(AppConfig):
    name = 'userProfiles'

    def ready(self):
        import userProfiles.signals