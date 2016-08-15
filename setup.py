import versioneer
from setuptools import setup, find_packages, Extension
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

cmds = versioneer.get_cmdclass()

setup(
    version=versioneer.get_version(),
    cmdclass=cmds,
    name='notificationcenter',

    description='Port of NSNotificationCenter functionality to Python',
    long_description=long_description,

    url='',

    author='ti250',
    author_email='ti250@cam.ac.uk',

    license='BSD',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3.5',
    ],

    keywords='notifications observer',

    packages=['notificationcenter'],

    install_requires=[],

)
