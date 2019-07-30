import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kolr",
    version="0.0.1dev0",
    author="Nathan Juraj Michlo",
    author_email="NathanJMichlo@gmail.com",
    description="✨🎨🖌 Terminal independent colors, palettes and styles done right",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nmichlo/kolr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
)