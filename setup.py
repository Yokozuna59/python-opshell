"""Setup file for the library."""
from pathlib import Path
from setuptools import setup, find_packages

from opshell import __name__ as pkg_name, __version__, __license__

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

URL = "https://github.com/Yokozuna59/python-opshell"
ISSUES = URL + "/issues"
CHANGELOG = URL + "/blob/master/CHANGELOG.md"

DESCRIPTION = ""

setup(
    name=pkg_name,
    version=__version__,
    license=__license__,
    url=URL,
    project_urls={
        "Issues": ISSUES,
        "Changelog": CHANGELOG,
    },
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=README,
    packages=find_packages(),
    install_requires=[""],
    keywords=[],
)
