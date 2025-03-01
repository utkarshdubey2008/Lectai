from setuptools import setup, find_packages

setup(
    name="lectai",
    version="0.1.0",
    author="LectAI",
    author_email="admin@lectai.io",
    description="A Python client for the Lect AI API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://lectai.org",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)