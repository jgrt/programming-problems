FROM jupyter/datascience-notebook as lab

FROM lab as test

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
