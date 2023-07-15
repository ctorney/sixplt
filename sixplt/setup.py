from setuptools import setup

setup(  name= 'sixplt', 
        version='0.0.1', 
        description='Inline matplotlib plots in the terminal with sixel', 
        py_modules=["sixplt"],
        package_dir={'': 'src'},
        install_requires = ["matplotlib"],
        
    )
