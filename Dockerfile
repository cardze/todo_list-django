FROM python:3.8
LABEL maintainer="j10108jason@gmail.com"

WORKDIR /web
COPY . /web/

RUN pip install -r requirements.txt

VOLUME /web
EXPOSE 8000

RUN ["chmod", "+x", "docker-entrypoint.sh"]

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
CMD python manage.py runserver 0.0.0.0:8000