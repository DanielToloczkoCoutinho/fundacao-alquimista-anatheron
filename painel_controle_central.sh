#!/bin/bash
echo "🎛️  PAINEL DE CONTROLE CENTRAL - FUNDAÇÃO ALQUIMISTA"
echo "===================================================="

# Painel de Coerência
echo "📊 PAINEL DE COERÊNCIA:"
echo "   • EQ0112: Sistema Principal"
echo "   • EQ0133: Núcleo Quântico" 
echo "   • PSI: Protocolo Zennith"
echo "   • CCI: Controle de Interfaces"

# Painel de Interfaces
echo "🌐 PAINEL DE INTERFACES:"
echo "   • GitHub: https://github.com/DanielToloczkoCoutinho/fundacao-alquimista-anatheron"
echo "   • Vercel 1: https://fundacao-alquimis-git-0a0231-daniel-toloczko-coutinhos-projects.vercel.app/"
echo "   • Vercel 2: https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central"

# Painel de Scripts
echo "⚡ PAINEL DE SCRIPTS:"
total_scripts=$(find . -name "*.sh" -type f | wc -l)
executaveis=$(find . -name "*.sh" -type f -executable | wc -l)
echo "   • Total: $total_scripts scripts"
echo "   • Executáveis: $executaveis scripts"
echo "   • Zennith: 33 scripts"
echo "   • Quânticos: 15 scripts"

echo ""
echo "🎯 COMANDOS DISPONÍVEIS:"
echo "   ./transmissor_base_lux.py    - Controle central"
echo "   ./painel-zennith.sh          - Interface Zennith"
echo "   ./ciclos_operacionais.sh     - Gestão de ciclos"
