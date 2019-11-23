from distutils.core import setup
from pathlib import Path

import m2r


def get_long_description() -> str:
    readme_md = Path().parent / "README.md"
    with open(readme_md, encoding="utf-8") as ld_file:
        return str(ld_file.read())


setup(
    name="proxybootstrap",
    packages=["proxybootstrap"],
    version="0.1.2",
    license="MIT",
    description="A simple python wrapper script for bootstrapping a reverse proxy inside a docker container.",
    long_description=m2r.parse_from_file(Path().parent / "README.md"),
    author="romnn",
    author_email="contact@romnn.com",
    url="https://github.com/romnnn/proxybootstrap",
    keywords=["reverse", "proxy", "container", "docker", "wrapper", "CORS", "nginx"],
    python_requires=">=3.6",
    install_requires=["jinja2"],
    package_data={"proxybootstrap": ["configs", "Dockerfile.jinja2"]},
    classifiers=[
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["proxybootstrap=proxybootstrap:main"]},
)
