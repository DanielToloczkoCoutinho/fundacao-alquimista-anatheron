#!/bin/bash

echo "🎛️  PAINEL DE CONTROLE QUÂNTICO - FUNDAÇÃO ALQUIMISTA"
echo "🌌 Sistema Operacional: Nix OS - Ambiente Quântico"
echo "=================================================="

while true; do
    echo ""
    echo "🔮 OPÇÕES DO SISTEMA QUÂNTICO:"
    echo "   1) Executar Experimento Bell"
    echo "   2) Executar Experimento GHZ" 
    echo "   3) Sistema Quântico Completo"
    echo "   4) Ver Últimos Resultados"
    echo "   5) Diagnóstico do Sistema"
    echo "   6) Sair"
    echo ""
    
    read -p "🎯 Selecione uma opção [1-6]: " opcao
    
    case $opcao in
        1)
            echo "🔔 INICIANDO EXPERIMENTO BELL..."
            python3 -c "
from sistema_quantico_fundacao_final import criar_circuito_bell
circuito = criar_circuito_bell()
resultados = circuito.medir_todos(1000)
print('📊 RESULTADOS BELL:')
for estado, count in sorted(resultados.items()):
    print(f'   |{estado}⟩: {count} vezes ({(count/1000)*100:.1f}%)')
"
            ;;
        2)
            echo "🌪️  INICIANDO EXPERIMENTO GHZ..."
            python3 -c "
from sistema_quantico_fundacao_final import criar_circuito_ghz  
circuito = criar_circuito_ghz(3)
resultados = circuito.medir_todos(1000)
print('�� RESULTADOS GHZ:')
for estado, count in sorted(resultados.items()):
    print(f'   |{estado}⟩: {count} vezes ({(count/1000)*100:.1f}%)')
"
            ;;
        3)
            echo "🌌 INICIANDO SISTEMA QUÂNTICO COMPLETO..."
            python3 sistema_quantico_fundacao_final.py
            ;;
        4)
            echo "📈 ÚLTIMOS RESULTADOS:"
            if [ -f "experimento_quantico_completo.json" ]; then
                python3 -c "
import json
with open('experimento_quantico_completo.json', 'r') as f:
    dados = json.load(f)
print(f'🕐 Experimento: {dados[\"timestamp\"]}')
print(f'🎯 Sistema: {dados[\"sistema\"]}')
print('📊 Estatísticas:')
for exp, info in dados['experimentos'].items():
    print(f'   {exp.upper()}: {info[\"analise\"][\"taxa_emaranhamento\"]:.1%} emaranhamento')
"
            else
                echo "   ℹ️  Nenhum experimento encontrado"
            fi
            ;;
        5)
            echo "🔍 DIAGNÓSTICO DO SISTEMA:"
            python3 -c "
import sys, os, platform
print(f'🐍 Python: {sys.version}')
print(f'🖥️  Plataforma: {platform.platform()}')
print(f'📁 Diretório: {os.getcwd()}')
print(f'🌌 Nix Detectado: {os.path.exists(\"/nix/store\")}')
print('✅ SISTEMA QUÂNTICO OPERACIONAL')
"
            ;;
        6)
            echo "👑 SAINDO DO SISTEMA QUÂNTICO DA FUNDAÇÃO..."
            exit 0
            ;;
        *)
            echo "❌ Opção inválida"
            ;;
    esac
    
    echo ""
    read -p "⏎ Pressione Enter para continuar..."
done
