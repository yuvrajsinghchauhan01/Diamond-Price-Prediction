from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name = 'DiamondPricePrediction',
    version= '0.0.1',
    author = 'Yuvraj',
    author_email = 'ychauhan191@gmail.com',
    install_requires = get_requirements('requirement.txt'),
    packages = find_packages()
    
)