FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm

COPY . /app/

EXPOSE 8000

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh
CMD ["sh", "/app/start.sh"]
