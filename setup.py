from setuptools import setup, find_packages

setup(name='askfm.py',
      version='0.6.3',
      description='Ask.fm crawler',
      author='utgwkk',
      author_email='utagawa.kiki@gmail.com',
      url='https://github.com/utgwkk/askfm.py',
      packages=find_packages(exclude=['tests']),
      install_requires=['requests', 'beautifulsoup4'],
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ]
      )
