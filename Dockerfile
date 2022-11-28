FROM python:3.10

ENV DASH_DEBUG_MODE False

RUN mkdir app

COPY app3.py /app/app.py
COPY data/ /app/data/
COPY assets/ /app/assets/

COPY requirements.txt /app/requirements.txt

WORKDIR app

RUN set -ex && pip install -r requirements.txt
EXPOSE 5555
CMD ["gunicorn", "-b", "0.0.0.0:5555", "--reload", "app:server"]