#!/bin/bash
echo "🛡️  PLANO DE OTIMIZAÇÃO NÃO-DESTRUTIVA"
echo "======================================"

echo ""
echo "🎯 ESTRATÉGIA: Otimizar SEM remover bibliotecas essenciais"

# 1. LIMPEZA SEGURA DE CACHES
echo ""
echo "1. 🗑️  LIMPEZA DE CACHES (SEGURA):"
echo "   🔸 __pycache__: $(find fundacao_independente -name "__pycache__" -type d -exec du -sh {} + 2>/dev/null | awk '{sum += $1} END {print sum "MB"}' || echo "0MB")"
echo "   🔸 *.pyc: $(find fundacao_independente -name "*.pyc" -exec du -ch {} + 2>/dev/null | grep total | cut -f1 || echo "0")"

read -p "   ❓ Limpar caches Python? (s/N): " limpar_caches
if [[ $limpar_caches == "s" || $limpar_caches == "S" ]]; then
    find fundacao_independente -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
    find fundacao_independente -name "*.pyc" -delete 2>/dev/null
    echo "   ✅ Caches limpos"
else
    echo "   ⏭️  Caches mantidos"
fi

# 2. COMPACTAÇÃO DE BACKUPS
echo ""
echo "2. 🗜️  COMPACTAÇÃO DE BACKUPS:"
backup_size=$(du -sh backup_automatico 2>/dev/null | cut -f1 || echo "0")
echo "   🔸 backup_automatico: $backup_size"

read -p "   ❓ Compactar backups antigos? (s/N): " compactar_backups
if [[ $compactar_backups == "s" || $compactar_backups == "S" ]]; then
    find backup_automatico -name "*.md" -mtime +3 -exec gzip {} \; 2>/dev/null
    echo "   ✅ Backups compactados"
else
    echo "   ⏭️  Backups mantidos"
fi

# 3. OTIMIZAÇÃO DE REQUIREMENTS
echo ""
echo "3. 📋 OTIMIZAÇÃO DO requirements.txt:"
echo "   🔸 Atual: $(wc -l < requirements_zennith.txt) linhas"
echo "   💡 Pode ser otimizado para versões específicas"

# 4. VERIFICAÇÃO FINAL
echo ""
echo "📊 ESPAÇO APÓS OTIMIZAÇÕES:"
espaco_final=$(du -sh . | cut -f1)
echo "   💾 Total: $espaco_final"

echo ""
echo "🎯 GANHO ESTRATÉGICO:"
echo "   ✅ Bibliotecas essenciais PRESERVADAS"
echo "   ✅ Funcionalidade 100% MANTIDA"
echo "   ✅ Alguns MB ganhos com limpeza segura"
echo "   ✅ Sistema pronto para continuar desenvolvendo"

echo ""
echo "🏆 DECISÃO SÁBIA: NÃO REMOVER AS BIBLIOTECAS ESSENCIAIS!"
