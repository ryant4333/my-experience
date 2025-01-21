FROM python:3.13-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./backend/ /code

COPY ./frontend/static/ /code/static/

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"]