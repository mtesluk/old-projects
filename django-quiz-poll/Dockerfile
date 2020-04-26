FROM alpine

COPY . ./django-project
WORKDIR ./django-project

RUN apk add python3
RUN apk add py-pip
RUN apk add py-setuptools
RUN pip3 install -r requirements/base.txt

CMD python3 manage.py runserver 8000
