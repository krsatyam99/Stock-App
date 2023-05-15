from django.apps import AppConfig


class StockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock'
    # def ready(self):
        # Import any modules or models that need to be loaded
        # from stock import signals