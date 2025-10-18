#!/bin/bash
echo "🧪 RECRIANDO LABORATÓRIOS - FUNDAÇÃO ALQUIMISTA"
echo "================================================"

LABS=("lab_interdimensional" "lab_medico_quantico" "lab_computacional" "lab_vibracional" "lab_estelar" "lab_temporal" "lab_quantico_avancado" "lab_zennith")

for lab in "${LABS[@]}"; do
    mkdir -p laboratorios/$lab
    echo "✅ Laboratório criado: $lab"
done

echo "🎉 Laboratórios recriados! Pronto para expansão."
