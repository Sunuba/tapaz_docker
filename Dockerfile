FROM python:stretch

WORKDIR /tapaz

COPY . /tapaz

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME tapaz