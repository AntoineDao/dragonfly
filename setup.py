import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dragonfly",
    version="0.2.0",
    author="ladybug-tools",
    description="Dragonfly is a utility API to work with UWG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ladybug-tools/dragonfly",
    packages=setuptools.find_packages(),
    dependency_links=[
        "https://github.com/ladybug-tools/uwg/archive/master.zip"
    ]
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
)