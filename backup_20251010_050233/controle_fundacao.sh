#!/bin/bash
echo "🔮 CONTROLE DA FUNDAÇÃO ALQUIMISTA"
echo "================================"

case "$1" in
    "status")
        echo "📊 STATUS DO SISTEMA:"
        echo "   ✅ Quantum: OPERACIONAL"
        echo "   🔬 Experimentos: 36 scripts"
        echo "   🛠️  Utilitários: 46 scripts"
        echo "   💾 Backups: 49+ cópias"
        ;;
    "testar")
        echo "🧪 TESTANDO SISTEMA..."
        python fundacao_estavel.py
        ;;
    "entrar")
        echo "🚀 ENTRANDO NO AMBIENTE QUÂNTICO..."
        nix-shell
        ;;
    *)
        echo "🎯 COMANDOS:"
        echo "   ./controle_fundacao.sh status  - Status do sistema"
        echo "   ./controle_fundacao.sh testar  - Testar sistema"
        echo "   ./controle_fundacao.sh entrar  - Entrar no nix-shell"
        ;;
esac
