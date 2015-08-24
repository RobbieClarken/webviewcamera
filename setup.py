from setuptools import setup
import re

with open('webviewcamera/__init__.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='WebViewCamera',
    version=version,
    description='Access and control Canon WebView cameras',
    long_description=readme,
    url='https://github.com/RobbieClarken/webviewcamera',
    author='Robbie Clarken',
    author_email='robbie.clarken@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        'Topic :: Multimedia :: Video :: Capture',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='camera canon webview',
    packages=['webviewcamera'],
    install_requires=[
        'requests>=2.7.0',
        'PyYAML>=3.11',
        'six>=1.9.0',
    ],
    package_data={
        'webviewcamera': ['canon-vb.specification.yml'],
    },
)
