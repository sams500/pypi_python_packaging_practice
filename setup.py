import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exmaple-pkg-sams-practice",
    version="0.1.0",
    author="Soilihi Abderemane",
    author_email="abderemane500@gmail.com",
    description="A small example of python packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sams500/pypi_python_packaging_practice",
    project_urls={
        "Bug Tracker": "https://github.com/sams500/pypi_python_packaging_practice/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
