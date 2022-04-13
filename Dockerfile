FROM python:3.9.2-slim
WORKDIR /main
ENV PYTHONUNBUFFERED 1
ADD ./main/requirements.txt /main/
RUN pip install -r requirements.txt