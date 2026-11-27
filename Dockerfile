# start with a base image that has Python 3.12 and linux installed
FROM python:3.12-slim

# AWS Lambda Web Adapter: lets Lambda pass web requests to uvicorn (it does nothing outside Lambda)
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:1.1.0 /lambda-adapter /opt/extensions/lambda-adapter

# create a working directory
WORKDIR /app

# copy the requirements file first
COPY requirements.txt .
# install the dependencies from the requirements file but do not cache the installation to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code into the container
COPY . .

# the api listens on port 8080 inside the container (the Lambda Web Adapter's default port)
EXPOSE 8080

# start the API when the container starts (this is what Lambda runs)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]