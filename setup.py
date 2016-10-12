from setuptools import setup

setup(name='askfm.py',
      version='0.1',
      description='Ask.fm crawler',
      author='utgwkk',
      author_email='utagawa.kiki@gmail.com',
      url='https://github.com/utgwkk/askfm.py',
      py_modules=['askfm'],
      install_requires=['requests', 'beautifulsoup4'],
      license='MIT'
      )
