#!/bin/bash
echo "🔬 INICIANDO PESQUISA DA FUNDAÇÃO ALQUIMISTA"
echo "==========================================="

# Entrar no ambiente nix e executar pesquisa
nix-shell --run "python experimentos_fundamentais.py"

echo ""
echo "🎯 Pesquisa concluída!"
echo "🚀 Use './pesquisa/pesquisador_automatico.sh' para pesquisa contínua"
