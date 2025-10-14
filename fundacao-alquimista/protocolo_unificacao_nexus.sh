#!/bin/bash
# --------------------------------------------------------------------------------------
# PROTOCOLO DE UNIFICAÇÃO NEXUS VERCEL (M439) - ZENNITH
# Verifica todos os portais conhecidos para facilitar a unificação de domínios.
# --------------------------------------------------------------------------------------

echo "🌌 **RELATÓRIO DE PORTAIS ATIVOS** - $(date)"
echo "------------------------------------------------------------------------------------------"

PORTAIS_CONHECIDOS=(
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app"
    "https://fundacao-alquimista-anatheron-dqiej3rdu.vercel.app"
    "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app"
    "https://fundacao-alquimista-anatheron-ax952ab3f.vercel.app" # URL de Produção Atual
    "https://fundacao-alquimista-anatheron.vercel.app"          # Domínio Principal Esperado
)

echo "VERIFICANDO STATUS DOS PORTAIS (200 = OK):"
for url in "${PORTAIS_CONHECIDOS[@]}"; do
    STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$url/central")
    if [ "$STATUS_CODE" -eq 200 ]; then
        echo "  -> $url: ✅ ATIVO (200)"
    elif [ "$STATUS_CODE" -eq 404 ]; then
        echo "  -> $url: ⚠️ ROTA CENTRAL AUSENTE (404 - Pode ser um Deploy Antigo)"
    else
        echo "  -> $url: ❌ OFFLINE/ERRO (Código: $STATUS_CODE)"
    fi
done

echo "------------------------------------------------------------------------------------------"
echo "INSTRUÇÃO CRÍTICA PARA UNIFICAÇÃO:"
echo "1. MANTENHA ATIVA a URL de Produção (ax952ab3f)."
echo "2. NO PAINEL VERCEL, remova todas as URLs de Deploy Antigas (jj21jyyqd, dqiej3rdu, b8q3t0nhk)."
echo "3. Garanta que o domínio principal (fundacao-alquimista-anatheron.vercel.app) aponte para o novo Deploy."
echo "4. PRÓXIMA AÇÃO: Executar a Sincronização Eterna (nucleo_sincronizacao_eterna.sh)."
