FROM python

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["flask", "run"]