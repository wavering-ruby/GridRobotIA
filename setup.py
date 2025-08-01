from setuptools import setup, find_packages

setup(
    name = "GridBot-AI",
    version = "Demo 2.4.0",
    description = "A grid-based AI path finder visualization tool",
    packages = find_packages(),
    package_data = {"GridBot_AI": ["assets/*.png"]},  # Inclui arquivos estáticos
    install_requires = [
        "pygame", 
        "pygame_gui",
        "numpy"
    ]
)
