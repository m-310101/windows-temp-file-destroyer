FROM python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["windows_temp_file_destroyer"]
