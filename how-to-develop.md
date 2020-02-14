## Before you begin

### Required

- [docker & docker-compose](https://www.docker.com)

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

## Development with Docker Compose

### Start shell in Docker

```shellsession
docker-compose run dev bash -l
```

### Run

```shellsession
pip install -e .[dev]
```

```shellsession
python -m mt_to_hugo_article_converter mt_to_hugo_article_converter -c mt_to_hugo_article_converter/examples/from_hatenablog/config.yml
```

### Test

```shellsession
pip install -e .[test]
```

```shellsession
python -m pytest --cov mt_to_hugo_article_converter
```

### Install / uninstall

```shellsession
pip uninstall --yes mt_to_hugo_article_converter
pip install --no-cache-dir .
mt-to-hugo-article-converter -h
```

## Build and upload pip

```shellsession
python setup.py sdist bdist_wheel
python -m twine upload --verbose --repository-url https://upload.pypi.org/legacy/ dist/*
```
