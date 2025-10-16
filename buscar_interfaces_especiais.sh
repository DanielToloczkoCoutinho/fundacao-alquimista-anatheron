#!/bin/bash

echo "🔮 BUSCA POR INTERFACES ESPECIAIS DA FUNDAÇÃO"

# Interfaces quânticas
echo ""
echo "🌌 INTERFACES QUÂNTICAS:"
find src -name "*quantum*" -o -name "*quantico*" -o -name "*quântic*" | head -10

# Interfaces de laboratório
echo ""
echo "🔬 INTERFACES DE LABORATÓRIO:"
find src -name "*lab*" -o -name "*laborator*" | head -10

# Interfaces Zennith
echo ""
echo "👑 INTERFACES ZENNITH:"
find src -name "*zennith*" -o -name "*zenith*" | head -10

# Interfaces de Nexus
echo ""
echo "🌐 INTERFACES NEXUS:"
find src -name "*nexus*" -o -name "*conex*" | head -10

# Interfaces de Governança
echo ""
echo "⚖️ INTERFACES DE GOVERNANÇA:"
find src -name "*govern*" -o -name "*admin*" | head -10

# Interfaces de Dados
echo ""
echo "📊 INTERFACES DE DADOS:"
find src -name "*dashboard*" -o -name "*metric*" -o -name "*status*" | head -10

# Componentes UI
echo ""
echo "🎨 COMPONENTES UI:"
find src -name "*component*" -type f | grep -v node_modules | head -15

# APIs
echo ""
echo "🌐 APIS:"
find src -name "*api*" -type d | head -10
