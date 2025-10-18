#!/bin/bash
# 🚀 EXECUTOR DA FASE 3: VERIFICAÇÃO DE EMARANHAMENTO
# 📅 Gerado em: 2025-10-18 00:00:58
# 📊 Scripts: 5
echo "🚀 INICIANDO FASE $1..."

echo "🎯 Executando: teste_bell_otimizado.py"
python3 "/home/user/fundacao-alquimista-anatheron/teste_bell_otimizado.py"
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: {script['nome']}"
else
    echo "❌ FALHA: {script['nome']}"
    exit 1
fi
echo ""
echo "🎯 Executando: teste_bell_otimizado.py"
python3 "/home/user/fundacao-alquimista-anatheron/backup_fundacao_20251017_233238/teste_bell_otimizado.py"
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: {script['nome']}"
else
    echo "❌ FALHA: {script['nome']}"
    exit 1
fi
echo ""
echo "🎯 Executando: teste_bell.py"
python3 "/home/user/fundacao-alquimista-anatheron/teste_bell.py"
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: {script['nome']}"
else
    echo "❌ FALHA: {script['nome']}"
    exit 1
fi
echo ""
echo "🎯 Executando: teste_bell.py"
python3 "/home/user/fundacao-alquimista-anatheron/public/fundacao-completa/scripts-alquimicos/teste_bell.py"
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: {script['nome']}"
else
    echo "❌ FALHA: {script['nome']}"
    exit 1
fi
echo ""
echo "🎯 Executando: teste_bell.py"
python3 "/home/user/fundacao-alquimista-anatheron/backup_fundacao_20251017_223238/teste_bell.py"
if [ $? -eq 0 ]; then
    echo "✅ SUCESSO: {script['nome']}"
else
    echo "❌ FALHA: {script['nome']}"
    exit 1
fi
echo ""
echo "🎉 FASE 3 CONCLUÍDA COM SUCESSO!"
