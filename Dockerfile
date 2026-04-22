# 1. Use a lightweight Python 3.12 base image
FROM python:3.12-slim

# 2. Install missing Linux system libraries for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

# 3. Hugging Face requires a non-root user for security
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 4. Set the working directory
WORKDIR /app

# 5. Copy requirements and install them securely
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy your entire project into the container
COPY --chown=user . .

# 7. Expose the port Hugging Face looks for (7860)
EXPOSE 7860

# 8. Boot up Streamlit!
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]