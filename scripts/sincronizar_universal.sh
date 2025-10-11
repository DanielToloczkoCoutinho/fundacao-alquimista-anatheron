#!/bin/bash
# 🔄 SINCRONIZADOR UNIVERSAL CORRIGIDO
echo "🔄 SINCRONIZAÇÃO UNIVERSAL INICIADA..."

cd .

echo "📦 Verificando ambiente..."
echo "• Diretório atual: $(pwd)"
echo "• NODE_ENV: ${NODE_ENV:-não definido}"

# APENAS PARA DESENVOLVIMENTO LOCAL
if [ "$VERCEL" != "1" ] && [ -d "../fundacao-alquimista-limpa" ]; then
    echo "🔧 Modo desenvolvimento - sincronizando dados..."
    
    # SINCRONIZAR DOCUMENTAÇÃO
    if [ -d "../fundacao-alquimista-limpa/docs" ]; then
        mkdir -p data/fundacao
        cp -r ../fundacao-alquimista-limpa/docs/* data/fundacao/
        echo "✅ Documentação sincronizada ($(ls data/fundacao | wc -l) arquivos)"
    fi
    
    # VERIFICAR ZENNITH
    if [ -d "../zennith_quantum" ]; then
        echo "✅ Zennith Quantum detectado"
    fi
else
    echo "🌐 Modo produção - usando dados embutidos"
fi

echo "💫 Sincronização concluída: $(date)"
