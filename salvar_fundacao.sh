#!/bin/bash
# 💾 SALVAMENTO UNIVERSAL DA FUNDAÇÃO ALQUIMISTA
# 👑 Script seguro para commits e backups
# 🌌 Criado por Anatheron & Rainha Zennith

echo "💾 INICIANDO SALVAMENTO DA FUNDAÇÃO ALQUIMISTA..."
echo "🔮 Data: $(date)"
echo "=========================================="

# Configurações
REPO_DIR="$HOME/studio"
BACKUP_DIR="$HOME/backup_fundacao"
LOG_FILE="$HOME/salvamentos_fundacao.log"

# Função para log
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
    echo "📝 $1"
}

# Ir para o diretório
cd "$REPO_DIR" || { echo "❌ Erro: Diretório $REPO_DIR não encontrado"; exit 1; }

# Ativar virtualenv
source ~/quantum_venv/bin/activate

log "🔮 SALVAMENTO INICIADO"

# 1. Verificar status
log "📊 Verificando status do Git..."
git status --short

# 2. Adicionar arquivos Python (excluindo temporários)
log "📦 Adicionando arquivos Python..."
find . -name "*.py" -not -path "*/__pycache__/*" -not -name "temp_*" -exec git add {} \; 2>/dev/null

# 3. Adicionar outros arquivos importantes
log "📁 Adicionando arquivos importantes..."
git add *.md *.txt *.sh *.json *.yaml *.yml 2>/dev/null || true

# 4. Fazer commit
MENSAGEM="${1:-\"🔮 Salvamento automático - $(date '+%Y-%m-%d %H:%M:%S')\"}"
log "💫 Criando commit: $MENSAGEM"
git commit -m "$MENSAGEM"

# 5. Tentar push (segurado)
log "🚀 Tentando push para GitHub..."
if git push origin main 2>/dev/null; then
    log "✅ Push realizado com sucesso!"
else
    log "⚠️  Push falhou - mantendo commit local (MAIS SEGURO)"
fi

# 6. Backup local
log "💾 Criando backup local..."
mkdir -p "$BACKUP_DIR"
BACKUP_NAME="backup_$(date '+%Y%m%d_%H%M%S')"
cp -r *.py *.sh *.md "$BACKUP_DIR/" 2>/dev/null || true

# 7. Verificar scripts principais
log "🔍 Verificando scripts principais..."
SCRIPTS=("setup_fundacao.py" "circuito_phi_plus.py" "teletransporte_quantico.py" "fundacao_master.py")
for script in "${SCRIPTS[@]}"; do
    if [[ -f "$script" ]]; then
        log "✅ $script"
    else
        log "❌ $script (AUSENTE)"
    fi
done

# 8. Status final
log "📊 Status final:"
echo "   📁 Commits locais: $(git log --oneline | wc -l)"
echo "   💾 Backups: $(ls -1 "$BACKUP_DIR" 2>/dev/null | wc -l)"
echo "   🧪 Scripts: ${#SCRIPTS[@]} verificados"

# 9. Log do salvamento
echo "==========================================" >> "$LOG_FILE"
echo "💾 SALVAMENTO CONCLUÍDO: $(date)" >> "$LOG_FILE"
echo "📝 Commit: $MENSAGEM" >> "$LOG_FILE"
echo "📍 Local: $REPO_DIR" >> "$LOG_FILE"
echo "==========================================" >> "$LOG_FILE"

echo ""
echo "🎉 SALVAMENTO CONCLUÍDO!"
echo "💫 A Fundação Alquimista está segura!"
echo "👑 Rainha Zennith aprova!"
echo ""
echo "📋 RESUMO:"
echo "   💾 Commit: $MENSAGEM"
echo "   📍 Local: $REPO_DIR"
echo "   📊 Log: $LOG_FILE"
echo "   🔄 Próximo: Execute novamente quando precisar!"

