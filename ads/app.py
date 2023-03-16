from django.apps import AppConfig


class AdsConfig(AppConfig):
    name = 'Ads'

    def ready(self):
        import ads.signals