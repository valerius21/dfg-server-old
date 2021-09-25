from setuptools import setup

setup(
    name='dfg_server',
    version='0.0.1',
    description='The DFG Project Server Middleware',
    url='https://github.com/valerius21/dfg-server',
    author='Valerius Mattfeld',
    author_email='valerius.mattfeld@uni-goettingen.de',
    license='MIT',
    install_requires=[
        'numpy',
        'fastapi',
        'gql==3.0.0a6',
        'graphql-core==3.1.5',
        'uvicorn',
        'pyYAML'
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
    ],
    py_modules=['dfg_server'],
    package_dir={'': 'dfg_server'},
)
