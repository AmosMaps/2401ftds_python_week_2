from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy'],
    author='AmosMaps',
    author_email='amosphashe@gmail.com',
    description='EDSA example python package',
    long_description='A longer description of your package',
    long_description_content_type=open('README.md').read(),
    url='https://github.com/AmosMaps/2401ftds_python_week_2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
