import os
from setuptools import setup, find_packages

current_dir: str = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, "README.md"), encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name="latynka",
    version="1.2",
    description="Convert Ukrainian cyrillic text to latynka or romanized Ukrainian text",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(where="e:/Ukrainian-Latynka-Tools/latynka"),
    package_dir={"": "e:/Ukrainian-Latynka-Tools/latynka"},
    license="CC0 1.0 Universal (Public Domain)",
    classifiers=[
        "License :: CC0 1.0 Universal (Public Domain)",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    extras_require={"dev": ["setuptools", "wheel", "twine"]},
)
