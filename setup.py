from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements.
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


_version_ = "0.0.0"

REPO_NAME = "ML_Project_2"
AUTHOR_USER_NAME = "shariquemd"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "mdsharique.jmi@gmail.com"

setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    # description="A Small python package for ml app",
    # long_description=long_description,
    # long_description_content="text/markdown",
    # url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # projects_urls={
    #     "Bug_Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    # },
    # package_dir={"":"src"},
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
