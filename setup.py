from setuptools import setup, find_packages

setup(
    name='topsis_experimental',  # <--- Updated name
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
    ],
    entry_points={
    'console_scripts': [
        'topsis_experimental = topsis_experimental.topsis_demo:main',  # <--- Updated name
    ],
},
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
)
