# Use Python 3.11 to support Keras 3.13.2
FROM python:3.11-slim

# Install updated system dependencies for image processing (CV2/TensorFlow)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Create Streamlit config directory and move the config file
RUN mkdir -p /app/.streamlit
RUN cp config.toml /app/.streamlit/config.toml

# Expose the web server port
EXPOSE 80

# Run the app and force address/port settings
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]