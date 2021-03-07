from setuptools import find_packages, setup


######

CLASSIFIERS = [
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
]
DESCRIPTION = ""
KEYWORDS = ["python"]
URL = ""
AUTHOR = "{{ cookiecutter.author_name }}"
AUTHOR_EMAIL = "{{ cookiecutter.author_email }}"

REQUIREMENTS = []
TEST_REQUIREMENTS = ["pytest-cov", "coverage[toml]"]
DEV_REQUIREMENTS = [
    "ipython",
    "jedi==0.17.2",
    "pdbpp",
    "black",
    "black==19.10b0",
    "isort==5.6.4",
    "flake8",
    "mypy",
    "pre-commit",
    "tox",
]

#####

with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="{{cookiecutter.package}}",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=CLASSIFIERS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    keywords=KEYWORDS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"{{cookiecutter.package}}": ["py.typed", "stubs/**/*.pyi"]},
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    extras_require={
        "test": TEST_REQUIREMENTS,
        "dev": TEST_REQUIREMENTS + DEV_REQUIREMENTS,
    },
)
