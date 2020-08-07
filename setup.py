import setuptools
import vbet

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vbet",
    version=vbet.__VERSION__,
    author="Dennis Mwangi",
    author_email="updatedennismwangi@gmail.com",
    description="A virtual betting bot server",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/updatedennismwangi/vbet.git",
    packages=setuptools.find_packages(),
    scripts=['bin/run', 'bin/vs'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Environment :: Console,"
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires='>=3.6',
)
