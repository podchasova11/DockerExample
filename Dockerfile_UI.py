
FROM python:3.13-alpine3.21

WORKDIR /user/workspace

COPY ./ /user/worspace

RUN pip install requests

CMD ["python", "insult.ru"]
