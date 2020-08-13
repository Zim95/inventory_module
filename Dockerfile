FROM python:3.8.1

RUN mkdir -p /app/
COPY .* /app/
WORKDIR /app/
RUN pip install -r requirements.txt
