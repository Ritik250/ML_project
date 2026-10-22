from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requrirements=[]
    with open(file_path) as file_obj:
        requrirements=file_obj.readlines()
        requrirements=[req.replace("\n","") for req in requrirements]

        if HYPHEN_E_DOT in requrirements:
            requrirements.remove(HYPHEN_E_DOT)

    return requrirements
        


setup(
name='mlproject',
version='0.0.1',
author='Ritik',
author_email="ritikkumar6772@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)