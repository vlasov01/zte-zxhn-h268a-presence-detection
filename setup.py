from setuptools import setup

setup(
   name='zte_client',
   version='1.0',
   description='A useful module to read ZTE info',
   author='Man Foo',
   author_email='foomail@foo.com',
   packages=['zte_client'],  #same as name
   install_requires=['argparse', 'requests' ], #external packages as dependencies
)
