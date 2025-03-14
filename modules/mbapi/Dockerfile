FROM python:3.14-rc-alpine
# Set the working directory
WORKDIR /app
# Copy files into the container
COPY app.py /app
COPY requirements.txt /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose Flask port
EXPOSE 5000
# Run Flask app
CMD ["python", "app.py"]