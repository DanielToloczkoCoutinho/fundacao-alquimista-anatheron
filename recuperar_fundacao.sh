#!/bin/bash
echo "🔧 RECUPERAÇÃO DA FUNDAÇÃO ALQUIMISTA"
echo "===================================="

if [ -d "backup_emergencia" ]; then
    echo "📦 Restaurando arquivos..."
    cp -r backup_emergencia/* ./
    echo "✅ Recuperação concluída!"
else
    echo "❌ Nenhum backup encontrado!"
    echo "💡 Execute o sistema portátil: python fundacao_portatil.py"
fi
