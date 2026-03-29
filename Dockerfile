# Step 1: Use an official Python base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
# We copy this first to take advantage of Docker's caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of your application code
# This includes the src folder, main.py, and orders.txt
COPY . .

# Step 5: Command to run your app
# Since your project has a main.py that starts the logic:
CMD ["python", "main.py"]