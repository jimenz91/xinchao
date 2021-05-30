FROM python:3.8
ENV PYTHONBUFFERED 1
RUN mkdir /xinchao
WORKDIR /xinchao
COPY requirements.txt /xinchao/
RUN pip install -r requirements.txt
COPY . /xinchao/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]