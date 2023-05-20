# use the python image as the base image
FROM python:3.10-buster

# set the working directory in the container
WORKDIR /app 

# copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the environment variables
ENV FLASK_RUN_HOST=0.0.0.0


EXPOSE 5000

# Start the flask app when the container runs.
CMD ["flask", "run"]

