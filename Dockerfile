FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-c", "from model import predict_sentiment; print(predict_sentiment('I am happy to use Docker with GitHub Actions'))"] 