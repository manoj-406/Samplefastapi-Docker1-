FROM python:3.12.7
LABEL author="Manoj" application="MovieshopFastAPIwithoutDB"
COPY . /MovieshopFastAPIwithoutDB
WORKDIR /MovieshopFastAPIwithoutDB
EXPOSE 8000
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
