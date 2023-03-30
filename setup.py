from setuptools import setup
setup(
    name='halp',
    version='0.0.1',
    py_modules = ['openai', 'consolemd', 'datetime'],
    entry_points={
        'console_scripts': [
            'halp=halp:app'
        ]
    },
    install_requires=[
        'openai',
        'consolemd',
        'datetime'
    ]
)