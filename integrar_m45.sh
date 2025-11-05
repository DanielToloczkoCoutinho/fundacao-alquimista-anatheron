#!/bin/bash
set -e

echo "=== [1] Executando DEMO no M45.1 (proposta + votos + decreto) ==="
DEMO_OUTPUT=$(python MODULO_45.1.py demo 2>&1 | grep -o '{.*}')

# Extrair IDs
PROPOSAL_ID=$(echo "$DEMO_OUTPUT" | jq -s 'map(select(.action_type=="create_proposal")) | .[0].proposal_id')
DECREE_ID=$(echo "$DEMO_OUTPUT" | jq -s 'map(select(.action_type=="finalize_deliberation")) | .[0].decree_id')
COHERENCE=$(echo "$DEMO_OUTPUT" | jq -s 'map(select(.action_type=="finalize_deliberation")) | .[0].coherence_status')

echo "Proposta criada no DEMO com ID: $PROPOSAL_ID"
echo "Decreto gerado no DEMO com ID: $DECREE_ID"

echo "=== [2] Montando m45_export.json no formato esperado ==="
jq -n \
  --arg pid "$PROPOSAL_ID" \
  --arg did "$DECREE_ID" \
  --arg coh "$COHERENCE" \
  '{
    proposals: {($pid): {id: $pid, status: "Finalizada: Aprovado"}},
    decrees: {($did): {id: $did, outcome: "Aprovado", coherence_status: $coh}},
    inter_species_pacts: {},
    operational_status: {}
  }' > m45_export.json

cat m45_export.json | jq .

echo "=== [3] Importando no M45.2 ==="
python MODULO_45.2.py import_m45_data --data_json "$(cat m45_export.json)"

echo "=== [4] Estatísticas no M45.2 ==="
echo "--- Propostas ---"
python MODULO_45.2.py stats_proposals
echo "--- Votação ---"
python MODULO_45.2.py stats_voting
echo "--- Decretos ---"
python MODULO_45.2.py stats_decrees
echo "Consultando oráculo sobre o ciclo concluído..."
python MODULO_45.3.py ask --q "O que significa este ciclo concluído?" --contexto

echo "=== Ciclo concluído com sucesso ==="
