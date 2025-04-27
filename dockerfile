FROM python:3.9-slim
WORKDIR /app
COPY app-source.py .
RUN pip install opencv-python pyzmq
EXPOSE 5555
CMD ["python", "app-source.py"]