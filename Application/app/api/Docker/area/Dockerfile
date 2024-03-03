FROM python:3.9

RUN mkdir -p /service

COPY area_management.py /service/area_management/
COPY test_area_management.py /service/area_management/
COPY requirements.txt /service/requirements.txt
WORKDIR /service/area_management/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /service/requirements.txt
RUN python -m pip install 'pymongo[srv]'
RUN python -m pip install uuid
RUN python -m pip install simplejson

EXPOSE 50051
ENTRYPOINT [ "python", "area_management.py" ]