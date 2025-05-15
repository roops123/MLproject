from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT="-e ."
def get_requirement(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[pckg.strip() for pckg in requirements]

        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)


setup(

    name='mlproject',
    version='0.0.1',
    author='Rupali Bawne',
    author_email='rupali818bawne@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)