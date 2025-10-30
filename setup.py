from setuptools import setup, find_packages
import os

def readme():
    if os.path.exists("README.md"):
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    return "Visualize navigation endpoints in frontend projects."

setup(
    name="navviz",
    version="0.1.0",
    description="Visualize navigation endpoints in frontend projects.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your@email.com",
    url="https://github.com/yourusername/navviz",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'networkx',
        'matplotlib',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'navviz=navviz.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Environment :: Console",
    ],
)
