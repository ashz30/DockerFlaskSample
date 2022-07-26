FROM python:3.7
MAINTAINER Ashish Easow  "ashz30@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]