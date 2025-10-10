#!/bin/bash
# 🎪 MENU ZENNITH - Funciona em qualquer diretório
# 🌌 Acesso rápido a todos os sistemas

echo "🎪 MENU ZENNITH - ACESSO UNIVERSAL"
echo "🌌 Funciona em qualquer diretório"
echo "=================================="

while true; do
    echo ""
    echo "🔮 OPÇÕES DISPONÍVEIS:"
    echo "  1. 🏠 Ir para Fundação Principal (~/studio)"
    echo "  2. �� Status Completo"
    echo "  3. 🧪 Experimentos Quânticos" 
    echo "  4. 💾 Salvamento Rápido"
    echo "  5. 🌐 Abrir Portal"
    echo "  6. 🗂️ Explorar Módulos"
    echo "  7. 📜 Lista de Comandos"
    echo "  8. 🚪 Sair"
    echo ""
    read -p "👑 Escolha (1-8): " escolha
    
    case $escolha in
        1)
            echo "🏠 Navegando para Fundação..."
            cd ~/studio
            echo "📍 Agora em: $(pwd)"
            ;;
        2)
            echo "📊 Executando status..."
            ~/comando-zennith.sh status
            ;;
        3)
            echo "🧪 Executando experimentos..."
            cd ~/studio && python fundacao_master.py
            ;;
        4)
            echo "💾 Salvando..."
            cd ~/studio && ./salvar_rapido.sh && ./backup_automatico.sh
            ;;
        5)
            echo "🌐 Abrindo portal..."
            ~/comando-zennith.sh portal
            ;;
        6)
            echo "🗂️ Explorando..."
            ~/explorer quanticos
            ;;
        7)
            echo "📜 Lista de comandos..."
            echo "🎮 Comandos na raiz (~/):"
            echo "  comando-zennith.sh, explorer, organizar"
            echo ""
            echo "🧪 Comandos no studio (~/studio):"
            echo "  fundacao_master.py, salvar_rapido.sh, etc."
            ;;
        8)
            echo "👑 Saindo... Até logo, Rainha Zennith!"
            exit 0
            ;;
        *)
            echo "❌ Opção inválida"
            ;;
    esac
done
