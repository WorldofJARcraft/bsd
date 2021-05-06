FROM python:3.6
WORKDIR /app
RUN apt-get update && apt-get -y install git gcc make cmake

COPY requirements.txt .

# hack to install scipy, https://github.com/scipy/scipy/issues/9481
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 setup.py install

ENV FLASK_APP=bsdetector/server.py

CMD ["flask","run","--host","0.0.0.0"]
