#!/bin/bash
# 🏛️ ANALISADOR MÓDULOS DIRETO
echo "🏛️ ANALISANDO MÓDULOS PRINCIPAIS..."
echo "🔷 M0: $(find /home/user/studio -name "*M0*" | wc -l) arquivos"
echo "🔷 M9/Nexus: $(find /home/user/studio -name "*nexus*" | wc -l) arquivos" 
echo "🔷 M29/Zennith: $(find /home/user/studio -name "*zennith*" | wc -l) arquivos"
echo "🔷 MΩ/Omega: $(find /home/user/studio -name "*omega*" | wc -l) arquivos"
echo "✅ Módulos contados diretamente!"
