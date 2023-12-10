FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt ./

RUN apk update && apk upgrade && apk add gcc && apk add g++ && apk add libpq-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3","-m","Moexfilm"]