FROM python:3.9

RUN mkdir -p /service

COPY app.py /service/app/
COPY /content /service/app/content
COPY requirements.txt /service/requirements.txt
WORKDIR /service/app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /service/requirements.txt
RUN python -m pip install 'pymongo[srv]'
RUN python -m pip install uuid
RUN python -m pip install flask
RUN python -m pip install datetime
RUN python -m pip install opencv-python
RUN python -m pip install MarkupSafe==2.0.1.
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 5000
ENV FLASK_APP=app.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]