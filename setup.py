import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='stress',
    version='1.0.0',
    packages=['stress'],
    install_requires=['psutil==5.6.6'],
    entry_points={
        'console_scripts': ['stress=stress:_cmd_line']
    },
    url='https://github.com/mattixtech/stress',
    license='MIT',
    author='Matthew Brooks',
    author_email='matt@mattbrooks.ca',
    description='A trivial utility for consuming system resources.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='cpu ram'
)
