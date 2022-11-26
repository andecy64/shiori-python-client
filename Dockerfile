FROM python:3.8-alpine3.15

RUN apk add make
WORKDIR /package
ADD . /package
RUN pip install -r requirements_dev.txt
RUN make test-all
