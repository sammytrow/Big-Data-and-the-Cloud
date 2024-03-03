FROM python:3.9

RUN mkdir -p /service

COPY user_validation.py /service/user_validation/
COPY test_validation.py /service/user_validation/
COPY requirements.txt /service/requirements.txt
WORKDIR /service/user_validation/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /service/requirements.txt
RUN python -m pip install 'pymongo[srv]'
RUN python -m pip install uuid
RUN python -m pip install simplejson

EXPOSE 50053
ENTRYPOINT [ "python", "user_validation.py" ]