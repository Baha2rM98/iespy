import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iespy",
    version="1.0.0",
    author="Bahador Mirzazadeh",
    author_email="bahador.mirzazadeh30@gmail.com",
    description="A python package for solving 'Interval Estimation' problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baha2rM98/iespy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
