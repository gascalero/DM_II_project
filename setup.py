from setuptools import setup, find_packages

setup(
    name='DM_II_project',
    version='0.1',
    packages=find_packages(),  
    install_requires=[  
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'jupyter'
    ],
    author='Gabriel Antonio Sierra Calero',
    author_email='20240357@novaims.unl.pt',
    description='DM II project - NOVA IMS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gascalero/DM_II_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)