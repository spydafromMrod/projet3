FROM python:3.11

WORKDIR /app

ADD app/ .

RUN  pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run" , "home.py"]

