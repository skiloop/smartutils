from setuptools import setup, find_packages

setup(
    name='smartutils',
    url="https://github.com/skiloop/smartutils",
    version='1.0',
    license='MIT',
    zip_safe=False,
    author='skiloop',
    author_email='skiloop@gmail.com',
    description='A smart utils for python',
    python_requires='>=3.7',
    packages=find_packages(exclude=['tests', 'tests.*']),
)
