#!/bin/bash
echo "🔐 CONFIGURADOR DE TOKEN IBM QUANTUM"
echo ""
read -p "Digite seu token IBM Quantum: " token

if [ -n "$token" ]; then
    # Atualizar token no script principal
    sed -i "s/seu_token_aqui/$token/g" conectar_ibm_quantum.sh
    echo "✅ Token configurado com sucesso!"
    echo "🔗 Execute: ./conectar_ibm_quantum.sh"
else
    echo "❌ Token não fornecido"
fi
