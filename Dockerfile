# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Run tests and save results
CMD ["pytest", "--junitxml=/results/test-results.xml", "--maxfail=1", "--disable-warnings"]
