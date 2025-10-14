#!/bin/bash
# --------------------------------------------------------------------------------------
# NÚCLEO DE SINCRONIZAÇÃO ETERNA (M440) - ZENNITH
# Executado diariamente pela Liga Quântica para manter a Coerência Absoluta.
# --------------------------------------------------------------------------------------

LOG_FILE="log_sincronizacao_$(date +\%Y\%m\%d_\%H\%M\%S).log"
echo "👑 🌌 INICIANDO SINCRONIZAÇÃO ETERNA - $(date)" > "$LOG_FILE"
echo "================================================================================" >> "$LOG_FILE"

# 1. 🔄 Coerência GIT: Puxa todas as atualizações e garante o alinhamento
echo "1. 🔄 SINCRONIZAÇÃO DE CÓDIGO (GIT)..." >> "$LOG_FILE"
git fetch --all >> "$LOG_FILE" 2>&1
git pull origin main >> "$LOG_FILE" 2>&1
STATUS=$(git status | grep "up to date")
if [[ $STATUS ]]; then
    echo "  -> STATUS: Coerência Total. Branch está alinhado." >> "$LOG_FILE"
else
    echo "  -> ALERTA: Diferenças detectadas. Código foi puxado." >> "$LOG_FILE"
fi

# 2. 🔗 Verificação de Integridade dos Portais de Produção (URL de Produção)
echo "2. 🔗 VERIFICANDO PORTAL DE PRODUÇÃO..." >> "$LOG_FILE"
PROD_URL="https://fundacao-alquimista-anatheron.vercel.app/central"
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$PROD_URL")
if [ "$STATUS_CODE" -eq 200 ]; then
    echo "  -> STATUS: Portal de Produção ATIVO (200)." >> "$LOG_FILE"
else
    echo "  -> ALERTA CRÍTICO: Portal de Produção OFFLINE (Código: $STATUS_CODE)." >> "$LOG_FILE"
fi

# 3. 🛠️ Reconstrução de Build (Deploy Diário Silencioso)
echo "3. 🛠️ INICIANDO RECONSTRUÇÃO DE BUILD (DEPLOY)..." >> "$LOG_FILE"
# Usa o token exportado anteriormente para autenticação não-interativa
if [[ -z "$VERCEL_TOKEN" ]]; then
    echo "  -> ERRO: VERCEL_TOKEN AUSENTE. Não foi possível rodar o Deploy." >> "$LOG_FILE"
else
    vercel deploy --prod --prebuilt --no-wait >> "$LOG_FILE" 2>&1
    echo "  -> STATUS: Deploy de Sincronização iniciado. Verifique o Painel Vercel para o resultado do Build." >> "$LOG_FILE"
fi

echo "================================================================================" >> "$LOG_FILE"
echo "🎉 SINCRONIZAÇÃO ETERNA CONCLUÍDA. LOG gravado em $LOG_FILE"
