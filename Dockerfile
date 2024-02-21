# pull python base image
FROM python:3.10
# copy application files
ADD . .
WORKDIR banknote
# update pip
RUN pip install --upgrade pip
# install dependencies
#RUN pip install -r requirements.txt
RUN pip install numpy>=1.21.0,<2.0.0
RUN pip install pandas>=1.3.5,<2.0.0
RUN pip install pydantic>=1.8.1,<2.0.0
RUN pip install scikit-learn==1.3.0
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install pytest>=7.2.0,<8.0.0
# expose port for application
EXPOSE 8000
# start fastapi application
CMD ["python", "app/app.py"]
