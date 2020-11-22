FROM python:3.7

EXPOSE 6969

ADD src /degustibus
WORKDIR /degustibus

RUN pip install -r requirements.pip

CMD ["sh", "start.sh"]

