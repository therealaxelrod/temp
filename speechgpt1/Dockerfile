FROM tiangolo/uvicorn-gunicorn:python3.10

RUN mkdir /speechgpt

COPY requirements.txt /speechgpt

WORKDIR /speechgpt

RUN pip install -r requirements.txt

COPY . /speechgpt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]