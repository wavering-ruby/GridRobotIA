from setuptools import setup, find_packages

setup(
    name = "GridBot-AI",
    version = "0.1",
    packages = find_packages(),
    package_data = {"GridBot_AI": ["assets/*.png"]},  # Inclui arquivos estáticos
)