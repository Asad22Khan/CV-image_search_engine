# 1. Use a lightweight Python 3.12 base image
FROM python:3.12-slim

# 2. Hugging Face requires a non-root user for security
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 3. Set the working directory
WORKDIR /app

# 4. Copy requirements and install them securely
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your entire project into the container
COPY --chown=user . .

# 6. Expose the port Hugging Face looks for (7860)
EXPOSE 7860

# 7. Boot up Streamlit!
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]