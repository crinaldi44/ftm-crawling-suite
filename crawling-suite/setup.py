# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='ftm_crawling_suite',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = ftm_crawling_suite.settings']},
)
