from setuptools import setup, find_packages

setup(
    name='TryAgain',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'joblib',
        'matplotlib',
        'seaborn',
    ],
    author='Amorleinis',
    author_email='your.email@example.com',
    description='A project for machine learning using NASA datasets',
    url='https://github.com/Amorleinis/TryAgain',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
