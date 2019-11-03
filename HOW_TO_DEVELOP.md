## Before you begin

### Required

- [docker & docker-compose](https://www.docker.com)
- [direnv](https://github.com/direnv/direnv)

## Before development

### (optional) Create the ENV file for Docker

Create the `.env` file like bellow.

on Linux

```
UID=1000
GID=100
```

### Setup direnv

Edit the `.envrc` file with `direnv edit .` command.

## Run

```shellsession
python -m mt_to_hugo_article_converter mt_to_hugo_article_converter -c mt_to_hugo_article_converter/examples/from_hatenablog/config.yml
```

## Test

```shellsession
python -m pytest mt_to_hugo_article_converter/tests/
```

## Install / uninstall

```shellsession
pip uninstall --yes mt_to_hugo_article_converter
pip install --no-cache-dir .
mt-to-hugo-article-converter -h
```

## Build pip

```shellsession
python setup.py sdist bdist_wheel
python -m twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*
```
