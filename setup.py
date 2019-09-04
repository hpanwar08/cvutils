from setuptools import setup

requirements = [line for line in open('requirements.txt') if line]

setup(
    name='cvutils',
    version='0.1',
    description='Utility function for image processing and computer vision',
    url='',
    author='Himanshu',
    author_email='himanshu@example.com',
    license='MIT',
    packages=['cvutils'],
    install_requires=requirements,
    python_requires='>=3.6',
    test_suite='cvutils.tests',
)
