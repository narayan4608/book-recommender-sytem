from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "narayan  "
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [ 'numpy==1.24.4']


setup(
    name='numpy',
    version="1.24.4",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="entbappy73@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",touch
    install_requires=LIST_OF_REQUIREMENTS
)