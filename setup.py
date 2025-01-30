from setuptools import setup, find_packages

setup(
    name='test_library',
    version='0.0.6',
    description='Podstawowa biblioteka testowa do nadpisania akcji Selenium w celu oddzielenia logiki biznesowej testu od technicznej',
    # long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sebastian Jadczak',
    author_email='Sebastian-Jadczak@wp.pl',
    url='https://github.com/SebastianJadczak',
    packages=find_packages(),
    install_requires=[
        'selenium==4.28.1',
        'dacite==1.8.1',
        'setuptools==75.8.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12'
)
