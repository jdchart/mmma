from setuptools import setup
from setuptools import find_packages

long_description = """
# mmma
_MultiModal Media Analysis_
"""

setup(
    name="mmma",
    version="0.0.1",
    author="Jacob Hart",
    url="https://github.com/jdchart/mmma",
    license="GLPv3+",
    author_email="jacob.dchart@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="MultiModal Media Analysis",
    packages=find_packages()
)