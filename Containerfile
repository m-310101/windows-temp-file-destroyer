FROM python:3.12.1
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["windows_temp_file_destroyer"]
