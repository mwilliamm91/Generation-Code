# Specify our container base image
FROM python:3.9

# Select a directory within our container
WORKDIR /Users/williammuya/Local desktop/Python/Generation_Code/Project/Mini_project

# Copy everything from our project root into our WORK DIRECTORY directory
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Give our container internet access
EXPOSE 81

# Execute this command on start
ENTRYPOINT ["python", "-m", "Mini_project.py"]