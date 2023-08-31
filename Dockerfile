FROM python:3.9

# create directory for the app user
RUN mkdir -p /codesnifferai

# create the appropriate directories
ENV HOME=/
ENV APP_HOME=/codesnifferai
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
