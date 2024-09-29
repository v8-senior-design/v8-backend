from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="myproject",
    version="0.1",
    rust_extensions = [RustExtension("my_rust_lib.my_rust_lib", "Cargo.toml")],
    zip_safe = False,
    
)