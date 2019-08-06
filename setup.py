import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotly2js",
    version="0.0.1",
    author="Sam Toolan",
    author_email="stoolan@telegeography.com",
    description="Turn Python Plotly Objects into JavaScript Files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
