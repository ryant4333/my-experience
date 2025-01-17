FROM python:3.13-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY ./app.py /code/src/app.py

EXPOSE 8080

CMD ["python", "src/app.py"]