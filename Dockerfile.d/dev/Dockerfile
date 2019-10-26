FROM python:3.7.4-buster

# Set in non-interactive mode.
ENV DEBIAN_FRONTEND=noninteractive
# ENV CLOUDSDK_CONFIG=/.config/gcloud

ENV DIRENV_VERSION=2.20.0

COPY requirements.txt /tmp/

RUN apt-get update \
  && apt-get install --assume-yes --no-install-recommends locales procps dialog \
  && echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen \
  && locale-gen \
  && apt-get install --assume-yes --no-install-recommends git tmux zsh jq unzip \
  && curl -L -o /usr/local/bin/direnv https://github.com/direnv/direnv/releases/download/v${DIRENV_VERSION}/direnv.linux-amd64 \
  && chmod a+rwx /usr/local/bin/direnv \
  && echo 'eval "$(direnv hook bash)"' > /etc/profile.d/direnv.sh \
  && echo 'direnv allow' >> /etc/profile.d/direnv.sh \
  && mkdir -p /.config /.docker \
  && chmod a+rwx /.config /.docker \
  && python3 -m pip install --upgrade pip \
  && python3 -m pip install --upgrade --requirement /tmp/requirements.txt

# Reset DEBIAN_FRONTEND to default(`dialog`).
# If you no need `dialog`, you can set `DEBIAN_FRONTEND=readline`.
# see also: man 7 debconf
ENV DEBIAN_FRONTEND=
