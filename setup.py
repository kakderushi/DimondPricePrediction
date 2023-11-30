from setuptools import find_packages,setup
from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Rushikesh kakde',
    author_email='kakderushikesh81@gmail.com',
    packages=find_packages()
)
'''
Think of the setup.py file as a document that describes your Python project. When you create a Python project, you use this file to tell the computer important details about your project, like its name, version, and who made it.

Let's break it down:

Name (name='DimondPricePrediction'):

Just like a person has a name, your project needs one too. This is the name people will use to find and talk about your project.
Version (version='0.0.1'):

Imagine your project is a book. The version is like the edition of the book. When you make changes to your project, you increase the version number. This helps people know which version they are using.
Author (author='Rushikesh kakde') and Author Email (author_email='kakderushikesh81@gmail.com'):

This is like writing your name and email in the book. It tells people who created the project and how to contact them.
Packages (packages=find_packages()):

Think of your project as a gift. The packages are like the different parts of the gift wrapped in boxes. find_packages() helps to find and include all the different parts of your project.
So, in simple terms, the setup.py file is like a form you fill out when you want to share your project. It provides important information about your project, making it easy for others to understand and use what you've created.

'''