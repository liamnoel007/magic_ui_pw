FROM mcr.microsoft.com/playwright:v1.55.0-jammy

# Устанавливаем Python, pip и git
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv git

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN playwright install-deps

COPY . .

CMD ["pytest", "--alluredir=allure-results"]