FROM python:3.11-slim-bullseye

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copiar algoritmos quânticos
COPY *.py ./
COPY *.json ./

# Instalar Qiskit
RUN pip install --no-cache-dir \
    numpy==1.24.3 \
    scipy==1.10.1 \
    matplotlib==3.7.1 \
    qiskit==1.0.2 \
    qiskit-aer==0.12.2 \
    qiskit-ibm-runtime==0.14.0

CMD ["python", "sistema_quantico_fundacao.py"]
