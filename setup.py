from setuptools import setup, find_packages

setup(
    name="mymath_module_package",  # Name of your package
    version="0.2.1",       # Version of your package
    packages=find_packages(),  # Automatically find packages in the current directory
    description="A custom math operations package",  # Short description of your package
    long_description=open("README.md").read(),  # Read the content of README.md for a detailed description
    long_description_content_type="text/markdown",  # Specify the format of the long description
    url="https://github.com/xing24xing/MyMathModule",  # URL for your project homepage
    author="Khushi Pandey",  # Author's name
    author_email="khushipandey260304.email@example.com",  # Author's email
    classifiers=[
        "Programming Language :: Python :: 3",  # Supported Python versions
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[  # List any dependencies your package needs
        # Add dependencies here, e.g., "numpy>=1.21.0"
    ],
    include_package_data=True,  # Include files specified in MANIFEST.in (if present)
    zip_safe=False,  # Whether the package can be reliably used if installed as a .egg file
)
