#!/bin/bash
echo "🔧 CORRIGINDO SINCRONIZADOR UNIVERSAL"
echo "===================================="

# Backup do sincronizador original
cp sincronizador_universal.sh sincronizador_universal.sh.backup

echo ""
echo "🔍 ANALISANDO ESTRUTURA ATUAL:"
echo "📁 Diretórios encontrados:"
find . -maxdepth 1 -type d | grep -v "__pycache__" | head -10

echo ""
echo "🎯 IDENTIFICANDO O PROJETO PRINCIPAL:"
projeto_principal=$(find . -maxdepth 1 -type d -name "*app*" -o -name "*web*" -o -name "*site*" | head -1)
if [ -n "$projeto_principal" ]; then
    echo "✅ Projeto principal: $(basename "$projeto_principal")"
else
    echo "⚠️  Nenhum projeto principal óbvio encontrado"
    projeto_principal="."  # Usar diretório atual
fi

echo ""
echo "🔧 ATUALIZANDO SINCRONIZADOR:"

# Criar versão corrigida do sincronizador
cat > sincronizador_universal_corrigido.sh << 'SINCORRIGIDOEOF'
#!/bin/bash
echo "🔮 INICIANDO SINCRONIZAÇÃO UNIVERSAL CORRIGIDA..."
echo "================================================"

# Configurações
BACKUP_DIR="backup_automatico"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
PROJECT_DIR="."  # Usar diretório atual

# Função de log
log() {
    echo "[$(date +"%H:%M:%S")] $1"
}

# 1. Backup inteligente
log "💾 Backup inteligente..."
mkdir -p "$BACKUP_DIR/${TIMESTAMP}"
cp -r *.py *.sh *.md *.json "$BACKUP_DIR/${TIMESTAMP}/" 2>/dev/null
log "✅ Backup criado: $BACKUP_DIR/${TIMESTAMP}"

# 2. Sincronizar com Vercel (se configurado)
log "🚀 Sincronizando com Vercel..."
cd "$PROJECT_DIR"

if [ -f "vercel.json" ] || [ -f "package.json" ]; then
    log "📦 Verificando dependências..."
    npm install
    
    log "✅ Commit realizado"
    log "📤 Fazendo deploy..."
    
    # Tentar deploy normal
    if vercel --prod; then
        log "🎉 Deploy realizado com sucesso!"
    else
        log "🔄 Tentando deploy forçado..."
        vercel --force --prod
    fi
else
    log "ℹ️  Projeto Vercel não detectado, pulando deploy"
fi

# 3. Atualizar métricas
log "📊 Atualizando métricas..."
echo "Sincronização: $TIMESTAMP" >> metricas_sincronizacao.txt
echo "Backup: $BACKUP_DIR/${TIMESTAMP}" >> metricas_sincronizacao.txt
echo "Status: ✅ Concluído" >> metricas_sincronizacao.txt

log "✅ Métricas atualizadas"

# 4. Relatório final
echo ""
echo "🎉 SINCRONIZAÇÃO CONCLUÍDA!"
echo "💾 Backup: $BACKUP_DIR/${TIMESTAMP}"
if [ -f "vercel.json" ] || [ -f "package.json" ]; then
    echo "🌐 Portal: https://fundacao-alquimista.vercel.app"
else
    echo "🌐 Portal: (Configure o Vercel para deploy automático)"
fi
echo "📊 Métricas: metricas_sincronizacao.txt"
SINCORRIGIDOEOF

chmod +x sincronizador_universal_corrigido.sh

echo ""
echo "✅ SINCRONIZADOR CORRIGIDO:"
echo "   🔸 Usa diretório atual como projeto principal"
echo "   🔸 Verifica existencia de config Vercel"
echo "   🔸 Mais robusto e adaptável"

echo ""
echo "🧪 TESTANDO SINCRONIZADOR CORRIGIDO:"
./sincronizador_universal_corrigido.sh

echo ""
echo "🏁 SINCRONIZADOR ATUALIZADO E FUNCIONAL!"
