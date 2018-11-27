from setuptools import setup

setup(
    name='hdnnpy',
    version='0.1.0',
    description='High Dimensional Neural Network Potential package',
    long_description=open('README.md').read(),
    author='KeisukeYamashita',
    author_email='19yamashita15@gmail.com',
    url='https://github.com/KeisukeYamashita/HDNNP',
    license='MIT',
    # src/__init__.py
    packages=['hdnnpy'],
    entry_points={
        'console_scripts': ['hdnnpy = hdnnpy.hdnnp:main'],
    },
    zip_safe=False,
)
