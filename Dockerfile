FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev udev nano gunicorn3 locales


WORKDIR /app

RUN sed -i 's/# pl_PL.UTF-8 UTF-8/pl_PL.UTF-8 UTF-8/' /etc/locale.gen
RUN locale-gen pl_PL.UTF-8

ENV LANG pl_PL.UTF-8
ENV LANGUAGE pl_PL
ENV LC_ALL pl_PL.UTF-8

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt


# Copy source CODE
COPY . /app

EXPOSE 5200

# Runs SH Script
ENTRYPOINT ["sh", "/app/start.sh"]