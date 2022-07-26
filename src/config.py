from distutils.command.config import config
from email.policy import default


class DevelopmentConfig():
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
