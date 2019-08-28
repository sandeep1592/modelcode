FROM ubuntu:16.04

MAINTAINER Sabdeep Reddy "sandeep.reddy@tigeranalytics.com"

RUN apt-get update -y && \
    apt-get install -y python2.7 python-pip

COPY ./requirements.txt /requirements.txt
COPY ./pickle_model.pkl /pickle_model.pkl

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python" ]

CMD [ "app/app.py" ]
