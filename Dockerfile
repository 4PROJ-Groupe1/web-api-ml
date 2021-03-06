FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install flask flask_cors numpy pandas apyori
RUN set FLASK_APP=app.py

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]