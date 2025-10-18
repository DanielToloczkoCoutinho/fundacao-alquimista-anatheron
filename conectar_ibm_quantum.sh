#!/bin/bash
# 🔗 CONEXÃO AUTOMÁTICA IBM QUANTUM - FUNDAÇÃO ALQUIMISTA
# 🌌 Configuração automática com chaves oficiais

echo "🔗 CONFIGURANDO IBM QUANTUM..."

# Configurar variáveis de ambiente
export QISKIT_IBM_API_TOKEN="ApiKey-19033191-d209-4a47-b427-e2c094a3cdf0"
export QISKIT_IBM_INSTANCE="crn:v1:bluemix:public:quantum-computing:us-east:a/26770b560f8940a4803a6518062a8969:0b5355c0-5289-4b8b-a10f-1762828b1b82::"
export QISKIT_IBM_ACCOUNT_ID="26770b560f8940a4803a6518062a8969"

echo "✅ Variáveis de ambiente configuradas"

# Executar teste de conexão
python3 teste_conexao_ibm.py

if [ $? -eq 0 ]; then
    echo "🎉 CONEXÃO IBM QUANTUM ESTABELECIDA!"
    echo "💰 Créditos disponíveis: (verifique no script Python)"
else
    echo "❌ FALHA NA CONEXÃO IBM QUANTUM"
    exit 1
fi
