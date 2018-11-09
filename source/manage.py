#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openuniverse.settings')

    if 'DJANGO_DB_USER' not in os.environ:
        raise Exception('Your environment variable DJANGO_DB_USER is not defined.')

    if 'DJANGO_DB_PASS' not in os.environ:
        raise Exception('Your environment variable DJANGO_DB_PASS is not defined.')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
       ) from exc
    execute_from_command_line(sys.argv)
