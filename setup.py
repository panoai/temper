from setuptools import setup

setup(
    name="temper",
    description="Driver for USB temperature and humidity sensors from PCSensor",
    url="https://github.com/urwen/temper",
    license="MIT",
    py_modules=["temper"],
    entry_points={
        "console_scripts": {
            "temper=temper:main"
        }
    }
)
