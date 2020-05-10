from setuptools import setup, find_packages

with open("README.md", 'r') as readme_file:
    readme = readme_file.read()
    
requirements = ['ipython>=6', 'ndformat>=4', 'nbconvert>=5', "requests>=2"]

setup(name='notebooktome', version ='0.01', author='Rukiya Matsidik', author_email = 'rukiyemetsidik@gmail.com', description ='A package to convert your Jupyter Notebook', long_description=readme, long_description_content_type='text/markdown', packages =find_packages(), install_requires=requirements,
     classifiers =['Programming Language :: Python :: 3.7', License :: OSI Approved :: GNU General Public License v3 (GPLv3),],)
