import os

__author__ = 'Bernd Strebel'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

from .base import BaseClass
from .sub import SubClass

__all__ = [
    'BaseClass',
    'SubClass'
]
