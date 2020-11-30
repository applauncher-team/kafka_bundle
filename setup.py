from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
  name='kafka_bundle',
  packages=['kafka_bundle'],
  version='1.1',
  description='Kafka support for applauncher',
  author='Alvaro Garcia Gomez',
  author_email='maxpowel@gmail.com',
  url='https://github.com/applauncher-team/kafka_bundle',
  download_url='https://github.com/applauncher-team/kafka_bundle',
  keywords=['kafka'],
  classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System', 'Topic :: Utilities'],
  install_requires=install_requires
)