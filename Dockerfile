FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

COPY ./wait-for-postgres.sh /app/
RUN chmod +x /app/wait-for-postgres.sh

CMD ["fastapi", "run", "main.py", "--port", "80"]