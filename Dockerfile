FROM python:3.6
WORKDIR /app
RUN apt-get update && apt-get -y install git gcc make cmake

COPY requirements.txt .

# hack to install scipy, https://github.com/scipy/scipy/issues/9481
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 setup.py install


# performance options 
ENV PYTHONDONTWRITEBYTECODE TRUE
ENV PYTHONUNBUFFERED TRUE



CMD ["gunicorn","--bind","0.0.0.0:5000","--workers", "4", "manage:app"]
