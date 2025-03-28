FROM python:3.13-alpine3.21

WORKDIR user/workspase

COPY ./ user/workspase

RUN pip install requests

CMD ["python", "insult.py"]
