from setuptools import setup, find_packages


with open('requirements.txt') as req:
    requirements = req.read().splitlines()


with open('README.md') as f:
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (IOError, ImportError) as error:
        readme = open('README.md').read()


with open('LICENSE') as f:
    license = f.read()


setup(name='prom2teams',
      version='2.2.2',
      description='Project that redirects Prometheus Alert Manager '
      'notifications to Microsoft Teams',
      long_description=readme,
      install_requires=requirements,
      setup_requires=[
        'flake8',
        'pypandoc'
      ],
      scripts=[
          'bin/prom2teams',
          'bin/prom2teams_uwsgi'
      ],
      package_data={
        '': ['*.ini', '*.j2'],
      },
      include_package_data=True,
      data_files=[
          ('/usr/local/etc/prom2teams', ['bin/wsgi.py'])
      ],
      url='https://github.com/idealista/prom2teams',
      author='Idealista, S.A.U',
      author_email='labs@idealista.com',
      license=license,
      packages=find_packages(exclude=('tests', 'docs')),
      keywords='microsoft teams prometheus alert',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
      ],
      zip_safe=False)
