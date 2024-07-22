from setuptools import setup, find_packages

setup(
    name="mymath_custome",
    version="0.1.0",
    packages=find_packages(),
    description="A custom math operations package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xing24xing/MyMathModule.git",
    author="Khushi Pandey",
    author_email="khushipandey260304.email@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
