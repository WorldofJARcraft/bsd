import pip
from setuptools import setup, find_packages
from setuptools.command.install import install
# https://stackoverflow.com/a/49867265/13719349
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

package = 'bsdetector'
version = '0.1'
links = []  # for repo urls (dependency_links)
requires = []  # for package names

# new versions of pip requires a session
requirements = parse_requirements(
    'requirements.txt', session="hack"
)

for item in requirements:
    link = None
    if getattr(item, 'url', None):  # older pip has url
        link = str(item.url)
    if getattr(item, 'link', None):  # newer pip has link
        link = str(item.link)
    if link:
        link = link.lstrip('git+')
        links.append(link)
    object_methods = [method_name for method_name in dir(object)]
    print(object_methods)
    if item.requirement:
        item_req = str(item.requirement)
        if "pattern" in item_req:
            continue
        requires.append(item_req)  # always the package name


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        import nltk
        nltk.download('punkt')
        install.run(self)


setup(
    name=package,
    version=version,
    package_dir={'bsdetector': 'bsdetector'},
    package_data={'bsdetector': ['*.json', '*.txt']},
    packages=find_packages(),
    install_requires=requires,
    dependency_links=links,
    include_package_data=True,
    description="Detects biased statements in online media documents",
    url='url',
    cmdclass={
        'install': PostInstallCommand
    },
    entry_points={
        'console_scripts': [
            'bsdetector = bsdetector.__main__:main'
        ]
    }
)
