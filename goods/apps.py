from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    verbose_name = 'Товары' # так таблица будет отображаться в админ панели и при взаимодействии с orm
