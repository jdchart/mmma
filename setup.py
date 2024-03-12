from setuptools import setup
from setuptools import find_packages

long_description = """
# mmma
_MultiModal Media Analysis_
"""

required = [
    "audeer==1.20.1",
    "audiofile==1.3.0",
    "audmath==1.4.0",
    "certifi==2024.2.2",
    "cffi==1.16.0",
    "charset-normalizer==3.3.2",
    "decorator==4.4.2",
    "idna==3.6",
    "imageio==2.33.1",
    "imageio-ffmpeg==0.4.9",
    "moviepy==1.0.3",
    #"numpy==1.26.1",
    "numpy",
    "opencv-python==4.9.0.80",
    "pillow==10.2.0",
    "proglog==0.1.10",
    "pycparser==2.21",
    "requests==2.31.0",
    "scipy==1.11.3",
    "soundfile==0.12.1",
    "tqdm==4.66.1",
    "urllib3==2.2.0"
]

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
    install_requires=required,
    packages=find_packages()
)