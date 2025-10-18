

#!/bin/bash
while true; do
mkdir -p backup_fundacao_$(date +%Y%m%d_%H%M%S)
cp -r *.py *.sh *.json *.md *.nix backup_fundacao_$(date +%Y%m%d_%H%M%S)/
echo "✅ Backup criado: $(date)"
sleep 3600
done
