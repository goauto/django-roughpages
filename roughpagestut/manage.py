#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(os.path.dirname(BASE_DIR), 'src'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roughpagestut.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
