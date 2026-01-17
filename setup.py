import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Coccidiosis-chicken-disease-classification"
AUTHOR_USER_NAME = "ayush190511"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ayushmishra642001@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for CNN classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }
)