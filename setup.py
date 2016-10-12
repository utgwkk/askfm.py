from setuptools import setup, find_packages

setup(name='askfm.py',
      version='0.3',
      description='Ask.fm crawler',
      author='utgwkk',
      author_email='utagawa.kiki@gmail.com',
      url='https://github.com/utgwkk/askfm.py',
      packages=find_packages(exclude=['tests']),
      install_requires=['requests', 'beautifulsoup4'],
      license='MIT'
      )
