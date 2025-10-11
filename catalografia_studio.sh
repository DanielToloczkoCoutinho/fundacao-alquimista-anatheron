#!/bin/bash
# 🎯 DIRECIONAMENTO: /home/user/studio (ÁREA PRINCIPAL)
echo "📊 PASSO 1 - CATALOGAÇÃO COMPLETA"
echo "📍 LOCAL: /home/user/studio"
echo "================================"

cd /home/user/studio

echo "🔍 ANALISANDO 36.559 ARQUIVOS..."
echo "📁 TIPOS DE ARQUIVOS:"
find . -type f | awk -F. '{print $NF}' | sort | uniq -c | sort -nr | head -10

echo ""
echo "🏗️ MÓDULOS ENCONTRADOS:"
find . -name "modulo*" -o -name "module*" | head -10

echo ""
echo "⚡ SCRIPTS EXECUTÁVEIS:"
find . -name "*.sh" -type f -executable | wc -l
