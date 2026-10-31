# start with a base image that has Python 3.12 and linux installed
FROM python:3.12-slim

# create a working directory
WORKDIR /app

# copy the requirements file first
COPY requirements.txt .
# install the dependencies from the requirements file but do not cache the installation to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code into the container
COPY . .

# run pytest with verbose output when the container starts
CMD ["pytest", "-v"]