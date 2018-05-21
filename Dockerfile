FROM node:0.12.5
MAINTAINER Aarni Koskela <aarni.koskela@wshop.com>
EXPOSE 8080
ADD . /var/www/wshop/working_copy

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-minimal python3-virtualenv python3-pip python3-dev python3-pil && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN python3 -m virtualenv -p /usr/bin/python3 --system-site-packages /var/www/wshop/venv && \
    /var/www/wshop/venv/bin/pip install -U pip setuptools
RUN /var/www/wshop/venv/bin/pip install /var/www/wshop/working_copy
RUN /var/www/wshop/venv/bin/python -m wshop_workbench migrate
RUN /var/www/wshop/venv/bin/python -m wshop_workbench wshop_populate_mock --with-superuser=admin
CMD /var/www/wshop/venv/bin/python -m wshop_workbench runserver 0:8080
