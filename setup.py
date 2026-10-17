from setuptools import setup, find_packages

setup(
    name="koshur",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "koshur=koshur.cli:main",
        ],
    },
)
