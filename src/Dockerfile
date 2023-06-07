# Use uma imagem oficial do Python como imagem pai
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Atualiza o sistema e instala poppler-utils e tesseract-ocr
RUN apt-get update -y && apt-get install -y poppler-utils tesseract-ocr

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto dos arquivos do diretório de trabalho para o contêiner
COPY . /app

# Executa o gunicorn ao iniciar o contêiner
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
