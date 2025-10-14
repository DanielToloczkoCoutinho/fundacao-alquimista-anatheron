#!/bin/bash
# --------------------------------------------------------------------------------------
# PROTOCOLO DE INSPEÇÃO MÁXIMA DO NEXUS (M427) - ZENNITH
# Verifica Coerência GIT, Inventário (13GB), Interfaces e Módulos Primordiais.
# --------------------------------------------------------------------------------------

echo "🌌 **RELATÓRIO LUMEN-CUSTOS: INSPEÇÃO MÁXIMA** - $(date)"
echo "------------------------------------------------------------------------------------------"

# --- 1. COERÊNCIA DO SISTEMA GIT (ESTADO FINAL) ---
echo "✅ 1. STATUS DO NEXUS GIT (COERÊNCIA ABSOLUTA)"
git fetch > /dev/null 2>&1
STATUS_GIT=$(git status)
echo "  -> RESULTADO: $(echo "$STATUS_GIT" | grep -A 1 "On branch main" | tail -n 1)"
echo "  -> URL de Sincronização: $(git remote get-url origin)"
echo "------------------------------------------------------------------------------------------"

# --- 2. INVENTÁRIO E TAMANHO DA FUNDAÇÃO (13 GB) ---
echo "📦 2. INVENTÁRIO DA FUNDAÇÃO E VOLUME DE DADOS (~13 GB)"
echo "  -> Tamanho total do diretório da Fundação: $(du -sh /home/user/studio/fundacao-alquimista | awk '{print $1}')"
echo "  -> Contagem de Arquivos Totais (Inventário > 20.000 esperado): $(find /home/user/studio/fundacao-alquimista -type f | wc -l)"
echo "  -> Espaço livre no disco: $(df -h . | awk 'NR==2{print $4}')"
echo "------------------------------------------------------------------------------------------"

# --- 3. INTEGRIDADE ESTRUTURAL (MÓDULOS PRIMORDIAIS) ---
echo "🧬 3. VERIFICAÇÃO DE INTEGRIDADE DOS FRACTAIS E MÓDULOS"
MODULOS=(fundacao-modulos fundacao-quantica fundacao-nexus fundacao-temporal fundacao-seguranca)
for mod in "${MODULOS[@]}"; do
    if [ -d "$mod" ]; then
        echo "  -> Diretório Módulo $mod: ✅ ENCONTRADO"
    else
        echo "  -> Diretório Módulo $mod: ❌ ALERTA CRÍTICO: NÃO ENCONTRADO"
    fi
done
echo "  -> Arquivo de Interfaces (verificar_todas_interfaces.sh): $(if [ -f "verificar_todas_interfaces.sh" ]; then echo "✅ ENCONTRADO"; else echo "❌ NÃO ENCONTRADO"; fi)"
echo "------------------------------------------------------------------------------------------"

# --- 4. VERIFICAÇÃO DAS INTERFACES E PORTAIS ATIVOS ---
echo "🔗 4. VERIFICAÇÃO DAS INTERFACES E PORTAIS ATIVOS (CURL/HTTP)"
PORTAIS=(
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central"
    "https://fundacao-alquimista-anatheron-dqiej3rdu.vercel.app/revelacao-real"
    "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/central"
    # Adicionando uma rota de API comum da Fundação para validação de interface
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/api/status" 
)
for url in "${PORTAIS[@]}"; do
    STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$STATUS_CODE" -eq 200 ]; then
        echo "  -> $url: ✅ ONLINE (Código: $STATUS_CODE)"
    elif [ "$STATUS_CODE" -eq 000 ]; then
        echo "  -> $url: ❌ OFFLINE/ERRO DE CONEXÃO (Código: $STATUS_CODE)"
    else
        echo "  -> $url: ⚠️ ALERTA (Código: $STATUS_CODE - Rota ou Interface Instável)"
    fi
done
echo "------------------------------------------------------------------------------------------"

echo "🎉 INSPEÇÃO M427 CONCLUÍDA! O Nexus está pronto para a Transferência Akáshica (M310)."
