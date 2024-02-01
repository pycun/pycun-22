###### Ejemplos de configuración de la variable "LOGGING" en Django. ######


# region 1. LOGGING QUE IMPRIME EN TERMINAL Y ARCHIVO LAS CONSULTAS SQL

""" 
Creamos dos Handlers, que seran utilizados por el mismo logger, el cual esta en el Nivel DEBUG y solo estara al
pendiente de los eventos de SQL dentro del sistema.

El primer handler escribirá en un nuevo archivo
El segundo handler escribirá lo mismo, pero en la terminal
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/sql_logger_file_handler.log",
        },
        'console': {
            "level": "DEBUG",
            'class': 'logging.StreamHandler',
        },
    },
    "loggers": {
        'django.db.backends': {
            "handlers": ["file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
# endregion

# region 2. LOGGING QUE IMPRIME EN ARCHIVOS ERRORES 4XX Y 5XX

"""
Ejemplo de un handler que escribe en un nuevo archivo los eventos http de Django.
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/request_logger_file_handler.log",
        },
    },
    "loggers": {
        'django.request': {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}
# endregion

# region 3. LOGGERS EN ARCHIVOS DIFERENTES
"""
Ejemplo del uso de 2 handlers que escriben en archivos y 2 loggers que registran eventos diferentes.
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file_request": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/request_logger_file_handler.log",
        },
        "file_request2": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/request2_view_logger_file_handler.log",
        },
    },
    "loggers": {
        'django.request': {
            "handlers": ["file_request"],
            "level": "WARNING",
            "propagate": True,
        },
        'django.template': {
            "handlers": ["file_request2"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
# endregion

# region 4. LOGGING QUE IMPRIME LOGS DE APLICACIONES EN ARCHIVOS
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "custom_app": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/users_view_logger_file_handler.log",
        },
    },
    "loggers": {
        'ws_optimitation.apps.users.views.facturas_v1': {
            "handlers": ["custom_app"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}
# endregion

# region 5. LOGGING QUE IMPRIME LOGS DE APLICACIONES EN ARCHIVOS A PARTIR DE SU NIVEL

"""
Lo que pasara con los archivos y el texto, es debido a los niveles de utilizados en el handler y en el logger
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "custom_app_info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/info_logger_file_handler.log",
        },
        "custom_app_debug": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/debug_logger_file_handler.log",
        },
        "custom_app_warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/warning_logger_file_handler.log",
        },
        "custom_app_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/error_logger_file_handler.log",
        },
        "custom_app_critical": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/critical_logger_file_handler.log",
        },
    },
    "loggers": {
        'ws_optimitation.apps.users.views.facturas_v1': {
            "handlers": ["custom_app_info", "custom_app_debug", "custom_app_warning", "custom_app_error", "custom_app_critical"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
# endregion

# region 6. LOGGING CON FILTER
"""
Para que el uso del logger anterior funcione, es necesario el uso de los filter.
"""

import logging


class LevelFilter(logging.Filter):

    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        'debug_filter': {
            '()': LevelFilter,
            'level': logging.DEBUG,
        },
        'info_filter': {
            '()': LevelFilter,
            'level': logging.INFO,
        },
        'warning_filter': {
            '()': LevelFilter,
            'level': logging.WARNING,
        },
        'error_filter': {
            '()': LevelFilter,
            'level': logging.ERROR,
        },
        'critical_filter': {
            '()': LevelFilter,
            'level': logging.CRITICAL,
        },
    },
    "handlers": {
        "custom_app_info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/info_logger_file_handler.log",
            "filters": ['info_filter'],
        },
        "custom_app_debug": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/debug_logger_file_handler.log",
            "filters": ['debug_filter'],
        },
        "custom_app_warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/warning_logger_file_handler.log",
            "filters": ['warning_filter'],
        },
        "custom_app_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/error_logger_file_handler.log",
            "filters": ['error_filter'],
        },
        "custom_app_critical": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/critical_logger_file_handler.log",
            "filters": ['critical_filter']
        },
    },
    "loggers": {
        'ws_optimitation.apps.users.views.facturas_v1': {
            "handlers": ["custom_app_info", "custom_app_debug", "custom_app_warning", "custom_app_error", "custom_app_critical"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
# endregion

# region 7. LOGGING CON FORMATTER
"""
Los formatters nos ayudan a mostrar más/menos información en el log.
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
            'style': '%',
        },
        'simple': {
            'format': '%(levelname)s: %(message)s',
            'style': '%',
        },
    },
    "handlers": {
        "file_verbose": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/verbose_file_handler.log",
            'formatter': 'verbose',
        },
        "file_simple": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/simple_file_handler.log",
            'formatter': 'simple',
        },
    },
    "loggers": {
        # The root logger in the django logging hierarchy, under which all of the following loggers are found.
        "django": {
            "handlers": ["file_verbose", "file_simple"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
# endregion

# region 8. ROTATING LOGGING

"""
Este tipo de Handler nos permitira crear archivos constantemente a partir de la cantidad de MB que pese el archivo.
El resultado seria:

simple_rotating_file_handler.log
simple_rotating_file_handler.log.1
simple_rotating_file_handler.log.2
simple_rotating_file_handler.log.3

el valor de `backupCount` es la cantidad de logs que almacenara.
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
            'style': '%',
        },
        'simple': {
            'format': '%(levelname)s: %(message)s',
            'style': '%',
        },
    },
    "handlers": {
        "file_verbose": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/verbose_rotating_file_handler.log",
            'formatter': 'verbose',
            'maxBytes': 1024,  # 5 MB
            'backupCount': 3,
        },
        "file_simple": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/simple_rotating_file_handler.log",
            'formatter': 'simple',
            'maxBytes': 1024,  # 1 MB
            'backupCount': 10,
        },
    },
    "loggers": {
        # The root logger in the django logging hierarchy, under which all of the following loggers are found.
        "": {
            "handlers": ["file_verbose", "file_simple"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
# endregion

# region 9. LoggerAdapter

import logging


class UserFilter(logging.Filter):

    def filter(self, record):
        return "Usuario" in record.getMessage()


class UserLoggerAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        user = self.extra.get('user', 'Desconocido')
        factura = self.extra.get('factura', None)

        msg_tmp = ""
        if user and factura:
            msg_tmp = f'[Usuario: {user}] Edito la factura: {factura} - {msg}', kwargs

        return msg_tmp


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
            'style': '%',
        },
        'simple': {
            'format': '%(levelname)s: %(message)s',
            'style': '%',
        },
    },
    "filters": {
        'usuario_filter': {
            '()': UserFilter,
        },
    },
    "handlers": {
        "file_verbose": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/verbose_adapter_file_handler.log",
            'formatter': 'verbose',
            "filters": ["usuario_filter"],
        },
        "file_simple": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/roger/Documentos/github/ahkin_facturas/.config/.logs/simple_adapter_file_handler.log",
            'formatter': 'simple',
            "filters": ["usuario_filter"],
        },
    },
    "loggers": {
        # The root logger in the django logging hierarchy, under which all of the following loggers are found.
        'ws_optimitation.apps.users.views.facturas_v1': {
            "handlers": ["file_verbose", "file_simple"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
# endregion