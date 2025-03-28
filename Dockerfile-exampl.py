FROM python:3.12.1-alpine3.18
#  Базовый образ

WORKDIR /user/workspace
# Рабочая директория

COPY ./ /usr/workspace
# Копируем все файлы в образ из нашей локальной директории

RUN pip3 install requests
# Устанавливаем requests, устанавливается во время сборки нашего образа

CMD ["python3", "insult.py"]
# Команда запуска программы, при запуске самого контейнера

