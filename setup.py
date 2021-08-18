from setuptools import setup

setup(
    name='dfg_server',
    version='0.1.0',
    description='The DFG Project Server Middleware',
    url='https://github.com/valerius21/dfg-server',
    author='Valerius Mattfeld',
    author_email='valerius.mattfeld@uni-goettingen.de',
    license='MIT',
    packages=['dfg_server'],
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
)
