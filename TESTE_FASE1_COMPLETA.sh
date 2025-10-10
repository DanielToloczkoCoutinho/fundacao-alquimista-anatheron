#!/bin/bash

echo "🎯 TESTE DA FASE 1 - INTERATIVIDADE COMPLETA"
echo "============================================"

# Obter a URL mais recente
URL_RECENTE=$(npx vercel --prod 2>&1 | grep -o 'https://[^ ]*' | head -1)

if [ -z "$URL_RECENTE" ]; then
    URL_RECENTE="https://fundacao-alquimista-anatheron-lxluzjev8.vercel.app"
fi

echo "🌐 URL para teste: $URL_RECENTE"
echo ""
echo "🔬 O QUE TESTAR NA FASE 1:"
echo "=========================="
echo ""
echo "🎛️ PORTAL CENTRAL AVANÇADO:"
echo "   ✅ Timer aumentando a cada segundo"
echo "   ✅ Coerência quântica atualizando"
echo "   ✅ Botões de ativação de módulos"
echo "   ✅ Logs vibracionais em tempo real"
echo "   ✅ Indicador visual de módulos ativos"
echo "   ✅ Efeitos hover e animações"
echo ""
echo "🔮 MÓDULO 303 AVANÇADO:"
echo "   ✅ Scanner dimensional com dados reais"
echo "   ✅ Métricas atualizando automaticamente"
echo "   ✅ Visualização holográfica animada"
echo "   ✅ Controle de play/pause"
echo "   ✅ Grid de dados em tempo real"
echo ""
echo "📱 INSTRUÇÕES:"
echo "   1. Acesse: $URL_RECENTE/central"
echo "   2. Aguarde 5-10 segundos"
echo "   3. Teste todos os botões e interações"
echo "   4. Navegue para Módulo 303"
echo "   5. Verifique as animações e dados"
echo ""
echo "🎯 CRITÉRIOS DE SUCESSO:"
echo "   - Dados mudam visualmente"
echo "   - Animações funcionam"
echo "   - Botões respondem"
echo "   - Nenhum erro no console"

