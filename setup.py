from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='dummy_data',
      version='0.0.2',
      description='Generate dummy data ',
      long_description=readme(),
      keywords='dummy data json testing fake',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Code Generators'
      ],
      url='http://github.com/blcook223/dummy_data',
      author='Benjamin Cook',
      author_email='benjamin.l.cook@gmail.com',
      license='MIT',
      packages=['dummy_data'],
      include_package_data=True,
      zip_safe=False)
