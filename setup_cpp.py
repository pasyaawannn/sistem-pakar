from pybind11.setup_helpers import Pybind11Extension, .......
from pybind11 import get_cmake_dir
import pybind11
from setuptools import setup, Extension

ext_modules = [
    Pybind11Extension(
        "cpp_stock",
        ["cpp_module/stock_calculator.cpp"],
        include_dirs=[pybind11.get_include()],
        cxx_std=11,
    ),
]

setup(
    name="cpp_stock",
    version="1.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
