# pull python base image
FROM python:3.10
# copy application files
WORKDIR banknote
ADD . .
# update pip
RUN pip install --upgrade pip
# install dependencies
RUN pip install -r requirements.txt
#RUN pip install numpy
#RUN pip install pandas
#RUN pip install pydantic
#RUN pip install scikit-learn
#RUN pip install uvicorn
#RUN pip install fastapi
#RUN pip install pytest
# expose port for application
EXPOSE 8000
# start fastapi application
CMD ["python", "app.py"]
