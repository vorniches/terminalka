from setuptools import setup, find_packages

setup(
    name="terminalka",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "terminalka = main:main"
        ]
    },
)
