import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_require = {
    "_dev_pkgs": [
        "autopep8",
        "pylint",
        "rope",
        "twine"
    ],
    "_test_pkgs": [
        "pytest",
        "pytest-cov",
        "pytest-pycodestyle"
    ]
}
extras_require["dev"] = sorted(
    set(
        extras_require["_dev_pkgs"]
        + extras_require["_test_pkgs"]
    )
)
extras_require["test"] = sorted(
    set(
        extras_require["_test_pkgs"]
    )
)

setuptools.setup(
    name="mt-to-hugo-article-converter",
    version="0.0.5",
    author="Hidenori MATSUKI",
    author_email="dev@mazgi.com",
    description="Convert articles from MT to Hugo",
    entry_points={
        "console_scripts": [
            "mt-to-hugo-article-converter=mt_to_hugo_article_converter.main:main"
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mazgi/mt-to-hugo-article-converter",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "python-dateutil",
        "pytz",
        "pyyaml"
    ],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing",
    ],
    python_requires='>=3.6',
)
