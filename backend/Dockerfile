FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
ENV GEMINI_API=""
CMD ["Python","app.py"]
