#!/bin/bash
# 🔄 SINCRONIZADOR DE DADOS EMBUTIDOS
echo "🔄 ATUALIZANDO DADOS EMBUTIDOS..."

cd .

# SINCRONIZAR APENAS DURANTE DESENVOLVIMENTO
if [ "$NODE_ENV" != "production" ]; then
    echo "📦 Sincronizando dados para desenvolvimento..."
    
    # ATUALIZAR DOCUMENTAÇÃO
    if [ -d "../fundacao-alquimista-limpa/docs" ]; then
        rsync -av ../fundacao-alquimista-limpa/docs/ data/fundacao/ --delete
        echo "✅ Documentação sincronizada"
    fi
    
    # VERIFICAR ZENNITH
    if [ -d "../zennith_quantum" ]; then
        echo "✅ Zennith detectado - dados atualizados"
    fi
else
    echo "🚫 Em produção - usando dados embutidos"
fi

echo "💫 Sincronização concluída"
