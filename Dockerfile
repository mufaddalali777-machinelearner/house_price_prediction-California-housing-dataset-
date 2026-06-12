FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
ENV PORT 8000
EXPOSE $PORT
CMD ["uvicorn", "lgapi:app", "--host", "0.0.0.0"]