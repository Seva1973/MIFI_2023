FROM python:3.9
WORKDIR /code
LABEL Author=A.Ganitev
LABEL module=7.10
COPY requirements.archive /code/requirements.txt
# folder /code belongs to the inner structure of this Docker container
RUN pip install --no-cache-dir -r requirements.archive
COPY ./app /code/app
# EXPOSE 3009
# ENTRYPOINT ["python"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# Built the file with this command: docker build -t testing_api .
# testing_api is the image name
# Running: docker run  -p 80:80  api_ag

# running the container with parameters:
#  _testing_7_10 % docker run -d name myapitestingcontaier -p 80:80  api_ag