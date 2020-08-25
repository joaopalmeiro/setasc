import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


def get_version(root, rel_path):
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find the version string (`__version__`).")


setup(
    name="setasc",
    version=get_version(HERE, "setasc/__init__.py"),
    description="A Python CLI to sort the arguments of the `setup()` function in `setup.py` files.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopalmeiro/setasc",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Environment :: Console",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["setasc=setasc.cli:main"]},
    project_urls={
        "Bug Reports": "https://github.com/joaopalmeiro/setasc/issues",
        "Source": "https://github.com/joaopalmeiro/setasc",
    },
    keywords="cli, refactor, sort, clean, setup, setuptools",
)
