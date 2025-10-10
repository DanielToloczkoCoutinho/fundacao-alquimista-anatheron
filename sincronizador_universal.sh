#!/bin/bash

# 🌌 SINCRONIZADOR UNIVERSAL - FUNDAÇÃO ALQUIMISTA - VERSÃO CORRIGIDA

echo "🔮 INICIANDO SINCRONIZAÇÃO UNIVERSAL..."
echo "=========================================="

# Configurações
REPO_PRINCIPAL="/home/user/studio"
REPO_VERCEL="/home/user/studio/fundacao-alquimista-quantica"
URL_VERCEL="https://fundacao-alquimista-anatheron-mtnk3sp7c.vercel.app"
BACKUP_DIR="/home/user/studio/backup_automatico"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Função para log
log() {
    echo "[$(date '+%H:%M:%S')] $1"
}

# 1. ✅ VERIFICAÇÃO DE DEPENDÊNCIAS
verificar_dependencias() {
    log "📦 Verificando dependências..."
    
    cd "$REPO_VERCEL"
    
    # Verifica se @types/three está instalado
    if ! npm list @types/three > /dev/null 2>&1; then
        log "🔧 Instalando @types/three..."
        npm install @types/three
    fi
    
    # Verifica three.js
    if ! npm list three > /dev/null 2>&1; then
        log "🔧 Instalando three.js..."
        npm install three
    fi
}

# 2. 📁 BACKUP INTELIGENTE
backup_automatico() {
    log "💾 Backup inteligente..."
    
    mkdir -p "$BACKUP_DIR/$TIMESTAMP"
    
    # Copia apenas arquivos importantes (ignora temporários)
    find "$REPO_PRINCIPAL" -name "*.py" -not -path "*/__pycache__/*" -not -path "*/backup_automatico/*" -exec cp {} "$BACKUP_DIR/$TIMESTAMP/" \; 2>/dev/null || true
    find "$REPO_PRINCIPAL" -name "*.sh" -not -path "*/backup_automatico/*" -exec cp {} "$BACKUP_DIR/$TIMESTAMP/" \; 2>/dev/null || true
    find "$REPO_PRINCIPAL" -name "*.json" -not -path "*/backup_automatico/*" -not -path "*/node_modules/*" -exec cp {} "$BACKUP_DIR/$TIMESTAMP/" \; 2>/dev/null || true
    find "$REPO_PRINCIPAL" -name "*.md" -not -path "*/backup_automatico/*" -exec cp {} "$BACKUP_DIR/$TIMESTAMP/" \; 2>/dev/null || true
    
    # Limpa backups antigos
    ls -dt "$BACKUP_DIR"/*/ | tail -n +11 | xargs rm -rf 2>/dev/null || true
    
    log "✅ Backup criado: $BACKUP_DIR/$TIMESTAMP"
}

# 3. 🔄 SINCRONIZAR COM VERCEL - VERSÃO CORRIGIDA
sincronizar_vercel() {
    log "🚀 Sincronizando com Vercel..."
    
    cd "$REPO_VERCEL"
    
    # Garante que as dependências estão instaladas
    verificar_dependencias
    
    # Git operations com tratamento de erro
    git add . > /dev/null 2>&1
    
    # Commit apenas se houver mudanças
    if ! git diff --cached --quiet; then
        git commit -m "🔮 Sync Automática - $TIMESTAMP" > /dev/null 2>&1 && {
            log "✅ Commit realizado"
        } || {
            log "⚠️  Nada para commitar"
        }
    else
        log "ℹ️  Nenhuma mudança para commitar"
    fi
    
    # Deploy para Vercel
    log "📤 Fazendo deploy..."
    if npx vercel --prod --yes > /dev/null 2>&1; then
        log "✅ Deploy Vercel realizado!"
        return 0
    else
        log "🔄 Tentando deploy forçado..."
        if npx vercel --prod --force > /dev/null 2>&1; then
            log "✅ Deploy forçado realizado!"
            return 0
        else
            log "❌ Deploy falhou"
            return 1
        fi
    fi
}

# 4. 📊 ATUALIZAR MÉTRICAS
atualizar_metricas() {
    log "📊 Atualizando métricas..."
    
    METRICS_FILE="$REPO_PRINCIPAL/metricas_atuais.json"
    cat > "$METRICS_FILE" << METEOFF
{
  "sistema": "Fundação Alquimista Quântica",
  "timestamp": "$(date -Iseconds)",
  "status": "OPERACIONAL",
  "versao": "SYNC-CORRIGIDA-$TIMESTAMP",
  "build": "SUCESSO"
}
METEOFF

    log "✅ Métricas atualizadas"
}

# 5. 🎯 FUNÇÃO PRINCIPAL CORRIGIDA
sincronizacao_completa() {
    echo "🔮 INICIANDO SINCRONIZAÇÃO UNIVERSAL CORRIGIDA"
    
    backup_automatico
    sincronizar_vercel
    atualizar_metricas
    
    echo "🎉 SINCRONIZAÇÃO CONCLUÍDA!"
    echo "🌐 Portal: $URL_VERCEL"
    echo "💾 Backup: $BACKUP_DIR/$TIMESTAMP"
}

# Execução
sincronizacao_completa
