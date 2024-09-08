from setuptools import setup, find_packages

setup(
    name="my_pyspark_project",
    version="0.1.0",
    description="A PySpark project",
    packages=find_packages(where="src"),  # Look for packages in 'src' directory
    package_dir={"": "src"},  # Root package is in the 'src' directory
    include_package_data=True,
    install_requires=[
        "pyspark",
    ],
)
