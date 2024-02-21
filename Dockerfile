# pull python base image
FROM python:3.10
# copy application files
ADD . .
WORKDIR /banknote
# update pip
RUN pip install --upgrade pip
# install dependencies
RUN pip install -r banknote/requirements.txt
# expose port for application
EXPOSE 8000
# start fastapi application
CMD ["python", "app/app.py"]
