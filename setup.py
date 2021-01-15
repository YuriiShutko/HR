import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setuptools.setup(
    name="HR",
    version="0.1.0",
    author="Yurii",
    author_email="yurii@example.com",
    description="Python package to manage users on a server based on an “inventory” JSON file",
    long_description=long_description,
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main',
        ],
    }
)
