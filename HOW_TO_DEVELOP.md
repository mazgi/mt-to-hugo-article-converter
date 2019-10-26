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
python mt_to_hugo_article_converter/converter.py --input-file=mt_to_hugo_article_converter/tests/data/articles.1.txt --output-directory=tmp
```

## Test

```shellsession
python -m pytest mt_to_hugo_article_converter/tests/
```

## Build pip

```shellsession
python setup.py sdist bdist_wheel
python -m twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*
```
