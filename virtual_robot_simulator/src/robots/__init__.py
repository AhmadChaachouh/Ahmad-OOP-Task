# __init__.py

# Initialize package-level variables or perform package-level initialization
print("Initializing package")

# Import specific classes or functions for easier access
from abc import ABC, abstractmethod


# Control what is accessible when using 'from package import *'
__all__ = ['ABC', 'abstractmethod']
