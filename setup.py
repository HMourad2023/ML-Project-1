from setuptools import setup,find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str)-> List[str]:
    """This function will return the list of requirements

    Args:
        filepath (str): _description_

    Returns:
        List[str]: _description_
    """
    requirements = []
    with open(filepath,"r") as f:
        requirements = f.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setup(
    name = "End To End Machine Learning Project",
    version = "0.0.1",
    author = "Mourad",
    author_email = "hamzaoui.mourad@outlook.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
    ) 
