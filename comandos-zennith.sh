#!/bin/bash
# 👑 LISTA SUPREMA DE COMANDOS - RAINHA ZENNITH
# 🌌 Todos os comandos da Fundação Alquimista

echo "👑 LISTA SUPREMA DE COMANDOS - RAINHA ZENNITH"
echo "🌌 FUNDAÇÃO ALQUIMISTA - CONTROLE TOTAL"
echo "========================================"

case "$1" in
    "lista")
        echo "🎯 TODOS OS COMANDOS DISPONÍVEIS:"
        echo ""
        
        echo "�� COMANDOS SUPREMOS (RAIZ - ~/):"
        echo "  ./comando-zennith.sh status      📊 Status completo da Fundação"
        echo "  ./comando-zennith.sh salvar      💾 Salvamento rápido"
        echo "  ./comando-zennith.sh backup      💽 Backup automático"
        echo "  ./comando-zennith.sh quantico    🧪 Executar experimentos quânticos"
        echo "  ./comando-zennith.sh portal      🌐 Abrir portal web"
        echo "  ./comando-zennith.sh tudo        🚀 Executar tudo"
        echo ""
        
        echo "🗂️ EXPLORER (RAIZ - ~/):"
        echo "  ./explorer quanticos             🧪 Listar módulos quânticos"
        echo "  ./explorer virtuais              💻 Listar módulos virtuais"
        echo "  ./explorer controle              ⚙️ Listar sistemas de controle"
        echo "  ./explorer backups               💾 Listar backups temporais"
        echo "  ./explorer todos                 📦 Listar todos os módulos"
        echo ""
        
        echo "🧪 COMANDOS QUÂNTICOS (~/studio):"
        echo "  python fundacao_master.py        🎯 TODOS os experimentos"
        echo "  python circuito_phi_plus.py      🔷 Estado |Φ⁺⟩"
        echo "  python teletransporte_quantico.py 🌀 Teletransporte"
        echo "  python teste_bell.py             📏 Teste de Bell"
        echo ""
        
        echo "💾 COMANDOS SALVAMENTO (~/studio):"
        echo "  ./salvar_rapido.sh               ⚡ Salvamento instantâneo"
        echo "  ./backup_automatico.sh           💽 Backup completo"
        echo "  ./status_completo.sh             📊 Status detalhado"
        echo ""
        
        echo "🔍 COMANDOS ANÁLISE (~/studio):"
        echo "  ./analise_quantica_completa.sh   🔮 Análise completa"
        echo "  ./mapa_nexus_visual.sh           🌌 Mapa do Nexus"
        echo "  ./saude_sistema.sh               💊 Saúde do sistema"
        echo ""
        
        echo "🌐 PORTAL WEB:"
        echo "  https://fundacao-alquimista-anatheron-39nu51kea.vercel.app/"
        echo "  👤 Usuário: qualquer usuário"
        echo "  🔑 Senha: alchemista_2024"
        ;;
        
    "rapido")
        echo "⚡ COMANDOS RÁPIDOS MAIS USADOS:"
        echo "  cd ~/studio && ./salvar_rapido.sh    💾 Salvar"
        echo "  cd ~/studio && python fundacao_master.py 🧪 Experimentos"
        echo "  ./comando-zennith.sh tudo           🚀 Executar tudo"
        echo "  ./explorer quanticos                🧪 Explorar módulos"
        ;;
        
    *)
        echo "🎯 USO: ./comandos-zennith.sh [opção]"
        echo ""
        echo "📋 OPÇÕES DISPONÍVEIS:"
        echo "  lista         📜 Lista completa de todos os comandos"
        echo "  rapido        ⚡ Comandos rápidos mais usados"
        echo ""
        echo "💡 DICA: Use de qualquer diretório:"
        echo "  ~/comando-zennith.sh tudo"
        echo "👑 RAINHA ZENNITH - CONTROLE TOTAL"
        ;;
esac
