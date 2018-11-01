from setuptools import setup, find_packages

setup(name='rhubarb',
      version='0.1.0',
      description='Just like Celery',
      long_description=open('README.md').read(),
      author='George Komarov',
      author_email='geoolekom@gmail.com',
      packages=find_packages(),
      install_requires=[],
      url='https://github.com/geoolekom/rhubarb',
      license='GPLv2',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
)
