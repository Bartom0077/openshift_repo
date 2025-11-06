FROM registry.access.redhat.com/ubi9/python-39
WORKDIR /app
COPY app /app
EXPOSE 8080
USER 1001
CMD ["python3","backend/main.py"]
