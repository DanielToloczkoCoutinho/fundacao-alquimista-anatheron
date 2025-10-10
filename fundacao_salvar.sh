#!/bin/bash
cd ~/studio
source ~/quantum_venv/bin/activate
git add . && git commit -m "🔮 Fundação Alquimista - $(date '+%d/%m %H:%M')"
echo "💾 SALVO! Use './status_fundacao.sh' para ver status"
