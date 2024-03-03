FROM python:3.9

RUN mkdir -p /service

COPY user_registration.py /service/user_registration/
COPY test_registration.py /service/user_registration
COPY requirements.txt /service/requirements.txt
WORKDIR /service/user_registration/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /service/requirements.txt
RUN python -m pip install 'pymongo[srv]'
RUN python -m pip install uuid
RUN python -m pip install simplejson

EXPOSE 50052
ENTRYPOINT [ "python", "user_registration.py" ]