FROM python:3.8-alpine

ENV PYTHONIOENCODING utf-8
WORKDIR /app

RUN apk add --update \
    wget \
    udev \
    ttf-freefont \
    chromium \
    chromium-chromedriver \
    && mkdir noto \
    && wget -P /app/noto https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
    && unzip /app/noto/NotoSansCJKjp-hinted.zip -d /app/noto \
    && mkdir -p /usr/share/fonts/noto \
    && cp /app/noto/*.otf /usr/share/fonts/noto \
    && chmod 644 -R /usr/share/fonts/noto/ \
    && fc-cache -fv \
    && rm -rf /app/noto \
    && pip install selenium