from setuptools import setup, find_packages

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

setup(
    name='tw2.polymaps',
    version='0.1.a4',
    description='toscawidgets2 wrapper for polymaps - amazing javascript maps',
    long_description=long_description,
    author='Ralph Bean',
    author_email='ralph.bean@gmail.com',
    url='',
    install_requires=[
        "tw2.core",
        "mako",
        "geojson",
        ],
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        tw2.polymaps = tw2.polymaps
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
    ],
)
