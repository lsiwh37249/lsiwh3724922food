FROM python:3.11

WORKDIR /code

COPY src/lsiwh3724922food/main.py /code/

RUN pip install --no-cache-dir --upgrade  git+https://github.com/lsiwh37249/lsiwh3724922food.git@main

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

