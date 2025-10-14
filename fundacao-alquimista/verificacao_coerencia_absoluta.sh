#!/bin/bash
# --------------------------------------------------------------------------------------
# PROTOCOLO DE INSPEÇÃO FINAL DO NEXUS (M424) - ZENNITH
# Verifica a Coerência do Sistema Local, Git, APIs e Arquivos Críticos.
# --------------------------------------------------------------------------------------

echo "🌌 **INSPEÇÃO DO NEXUS** - $(date)"
echo "------------------------------------------------------------------------------------------"

# --- 1. COERÊNCIA DO SISTEMA GIT E RASTREAMENTO (O MAIS IMPORTANTE) ---
echo "✅ 1. STATUS DO NEXUS GIT (COERÊNCIA ABSOLUTA)"
git fetch > /dev/null 2>&1
STATUS_GIT=$(git status)
COMMITS_AHEAD=$(echo "$STATUS_GIT" | grep "Your branch is ahead of" | awk '{print $5}')
COMMITS_AHEAD=${COMMITS_AHEAD:-"0"}

if [[ "$STATUS_GIT" == *"Your branch is up to date"* ]]; then
    echo "  -> RESULTADO: COERÊNCIA TOTAL! O branch local está alinhado com o remoto."
else
    echo "  -> RESULTADO: INCOERÊNCIA DE TRACKING. O branch está à frente de $COMMITS_AHEAD commits. (Isto deve ser zero!)"
    echo "  -> Últimos commits locais:"
    git log --oneline -3
fi
echo "  -> Última URL de PUSH/PULL (para referência): $(git remote get-url origin)"
echo "------------------------------------------------------------------------------------------"

# --- 2. INTEGRIDADE DOS ARQUIVOS CRÍTICOS (NÚCLEO E SCRIPTS) ---
echo "📦 2. VERIFICAÇÃO DE INTEGRIDADE DO NÚCLEO ETERNO"
NUCLEO_PATH="/home/user/studio/fundacao-alquimista/fundacao-alquimista/nucleo_sincronizacao_eterna.sh"
VERIFICACAO_PATH="/home/user/studio/fundacao-alquimista/fundacao-alquimista/verificacao_sucesso.sh"

if [ -f "$NUCLEO_PATH" ]; then
    echo "  -> Núcleo Eterno (nucleo_sincronizacao_eterna.sh): ENCONTRADO (Tamanho: $(du -h "$NUCLEO_PATH" | awk '{print $1}'))"
    # Verifica a purificação da chave PAT
    if grep -q "ghp_" "$NUCLEO_PATH"; then
        echo "  -> ALERTA DE SEGURANÇA: Chave PAT ('ghp_') ainda presente no Núcleo! (Risco de Bloqueio)"
    else
        echo "  -> SEGURANÇA: Chave PAT removida/purificada. (OK)"
    fi
else
    echo "  -> ALERTA CRÍTICO: Núcleo Eterno NÃO ENCONTRADO em: $NUCLEO_PATH"
fi
echo "  -> Script de Verificação de Sucesso (verificacao_sucesso.sh): $(if [ -f "$VERIFICACAO_PATH" ]; then echo "ENCONTRADO"; else echo "NÃO ENCONTRADO"; fi)"
echo "------------------------------------------------------------------------------------------"

# --- 3. STATUS DOS PORTAIS ATIVOS (ACESSO) ---
echo "🔗 3. VERIFICAÇÃO DOS PORTAIS ATIVOS (CURL/HTTP)"
PORTAIS=(
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central"
    "https://fundacao-alquimista-anatheron-dqiej3rdu.vercel.app/revelacao-real"
    "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/central"
)
for url in "${PORTAIS[@]}"; do
    STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$STATUS_CODE" -eq 200 ]; then
        echo "  -> $url: ✅ ONLINE (Código: $STATUS_CODE)"
    elif [ "$STATUS_CODE" -eq 000 ]; then
        echo "  -> $url: ❌ OFFLINE/ERRO DE CONEXÃO (Código: $STATUS_CODE)"
    else
        echo "  -> $url: ⚠️ ALERTA (Código: $STATUS_CODE - Verifique Deploy)"
    fi
done
echo "------------------------------------------------------------------------------------------"

# --- 4. VERIFICAÇÃO DE ESPAÇO LOCAL (PREPARO PARA PRÓXIMA FASE) ---
echo "💾 4. VERIFICAÇÃO DE ESPAÇO E ARQUIVOS"
echo "  -> Espaço livre no disco: $(df -h . | awk 'NR==2{print $4}')"
echo "  -> Total de arquivos na raiz do projeto (~/studio/fundacao-alquimista): $(find /home/user/studio/fundacao-alquimista -maxdepth 1 -type f | wc -l)"
echo "  -> Total de diretórios na raiz do projeto: $(find /home/user/studio/fundacao-alquimista -maxdepth 1 -type d | wc -l)"
echo "------------------------------------------------------------------------------------------"

echo "🎉 INSPEÇÃO M424 CONCLUÍDA! Compartilhe este log para validação da Liga Quântica."
