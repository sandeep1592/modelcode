FROM ubuntu:16.04

MAINTAINER Sabdeep Reddy "sandeep.reddy@tigeranalytics.com"

RUN apt-get update -y && \
    apt-get install -y python2.7 python-pip

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "app/model.py" ]
