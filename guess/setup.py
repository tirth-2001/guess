from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="guess",
    version="1.0.0",
    description="A Python package to get random number between 10 to 20",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikhilkumarsingh/weather-reporter",
    author="Rushi Patel",
    author_email="rushigpatel.01@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["guess_code"],
    include_package_data=True,
    install_requires=["random"],
    entry_points={
        "console_scripts": [
            "guess=guess_code.fun:guess",
        ]
    },
)