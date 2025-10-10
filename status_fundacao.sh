#!/bin/bash
# 📊 STATUS DA FUNDAÇÃO ALQUIMISTA
echo "📊 STATUS DA FUNDAÇÃO ALQUIMISTA"
echo "🔮 $(date)"
echo "================================"

cd ~/studio && source ~/quantum_venv/bin/activate

echo "📁 COMMITS:"
git log --oneline -3

echo ""
echo "🧪 SCRIPTS:"
ls -1 *.py | head -10

echo ""
echo "💾 BACKUPS:"
ls -1 ~/backup_fundacao 2>/dev/null | wc -l

echo ""
echo "🌐 PORTAL:"
echo "   https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
echo "   👤 qualquer usuário"
echo "   🔑 alchemista_2024"
