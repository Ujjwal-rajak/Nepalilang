from setuptools import setup, find_packages

setup(
    name="nepalilang",
    version="0.2.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    license="MIT",
    author="Ujjwal Kumar Rajak",
    author_email="ujjwalrajak2002@gmail.com",
    description="A Nepali-language implementation",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Beasova-Corporation/Ilbpp.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
