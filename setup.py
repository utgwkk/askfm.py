from setuptools import setup, find_packages


with open("./README.md") as f:
    long_description = f.read()

setup(name='askfm.py',
      version='0.6.5',
      description='Ask.fm crawler',
      long_description=long_description,
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
