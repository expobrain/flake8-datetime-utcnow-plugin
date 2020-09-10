from pathlib import Path

from setuptools import setup

version = (
    (Path(__file__).parent / "flake8_datetime_utcnow" / "__version__.py")
    .read_text()
    .split("=")[1]
    .strip()[1:-1]
)

setup(
    name="flake8_datetime_utcnow_plugin",
    license="MIT",
    version=version,
    description="Plugin to check that utcnow() is not used in favour of now(UTC)",
    author="Daniele Esposti",
    author_email="daniele.esposti@gmail.com",
    url="https://github.com/expobrain/flake8-datetime-utcnow-plugin",
    packages=["flake8_datetime_utcnow"],
    install_requires=["flake8>=3.0.0"],
    entry_points={
        "flake8.extension": [
            "U1 = flake8_datetime_utcnow:DatetimeUtcnowLinter",
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)
