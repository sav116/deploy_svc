from setuptools import find_packages
from setuptools import setup

setup(
    name='deploy_svc',
    version='0.0.1',
    description="Training with GitHub Actions",
    author='sav116',
    packages=['ci_app'],
    install_requires=['Flask', 'docker'],
    include_package_data=True,
    keywords=[
        'ci', 'github actions', 'flask', 'docker'
    ],
    entry_points={
        'console_scripts': [
            'deploy_svc = ci_app.app:main']},
)

