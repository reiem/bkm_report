import os
from setuptools import setup
from bkm_report import version


REQUIREMENTS = [
    i.strip() for i in open("requirements.txt").readlines()
    if not i.startswith('#')
]


setup(
    name="bkm_report",
    version=version,
    author="Stefan L. Meier",
    author_email="meier.stefan@gmail.com",
    description="Tool to generate a custom economy report for BKM and DKM",
    license="BSD",
    keywords="economic e-conomic accounting bookkeeping",
    url="https://github.com/reiem/bkm_report",
    packages=['bkm_report'],
    classifiers=[
    ],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
)
