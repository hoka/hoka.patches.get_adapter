from setuptools import setup, find_packages

version = '2.13.19.3'

setup(name='hoka.patches.get_adapter',
      version=version,
      description='A patch to query an adapter on every context',
      long_description=open("README.rst").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Zope2",
          "Intended Audience :: Other Audience",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        ],
      keywords='hoka hook get_adapter zope2',
      author='Kai Hoppert',
      author_email='kai.hoppert@online.de',
      url='https://github.com/hoka/hoka.patches.get_adapter',
      license='GPL version 2',
      packages=find_packages(),
      namespace_packages=['hoka','hoka.patches'],
      include_package_data=True,
      install_requires=[
        'setuptools',
        'Zope2',
        'z3c.autoinclude',
      ],
      extras_require={'test': [
        'collective.testcaselayer',
      ]},
      platforms='Any',
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = zope
''',
)