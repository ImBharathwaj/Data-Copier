FROM python:3.7

# Install OS Module
RUN apt update -y &&\
    apt install telnet &&\
    rm -rf /var/lib/apt/lists/*

# Copy source code
COPY . /data-copier

# Install application dependencies
RUN pip install -r /data-copier/requirements.txt