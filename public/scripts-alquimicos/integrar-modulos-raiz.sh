#!/bin/bash
echo "🔄 INTEGRAÇÃO DE MÓDULOS MODULO_*..."

# Criar estrutura para módulos da raiz
mkdir -p ~/fundacao-definitiva/app/modulos/raiz
mkdir -p ~/fundacao-definitiva/app/modulos/raiz/{prioritarios,completos,analise}

# Fase 1: Módulos prioritários da raiz
echo "🎯 FASE 1: Módulos prioritários MODULO_*"
MODULOS_RAIZ_PRIORITARIOS=(
    "MODULO_0" "MODULO_9" "MODULO_29" "MODULO_ALFA" "MODULO_OMEGA"
    "MODULO_100" "MODULO_200" "MODULO_300" "MODULO_400" "MODULO_500"
    "MODULO_600" "MODULO_700" "MODULO_800" "MODULO_900" "MODULO_999"
)

for modulo in "${MODULOS_RAIZ_PRIORITARIOS[@]}"; do
    echo "🔧 Integrando: $modulo"
    find ~/studio -name "$modulo" -type d -exec cp -r {} ~/fundacao-definitiva/app/modulos/raiz/prioritarios/ \; 2>/dev/null
done

# Fase 2: Amostra de módulos numéricos
echo "🔢 FASE 2: Amostra de módulos numéricos"
for i in {1..50}; do
    modulo="MODULO_$i"
    if find ~/studio -name "$modulo" -type d | grep -q .; then
        echo "📁 Copiando: $modulo"
        find ~/studio -name "$modulo" -type d -exec cp -r {} ~/fundacao-definitiva/app/modulos/raiz/completos/ \; 2>/dev/null
    fi
done

# Fase 3: Atualizar índice
cat > ~/fundacao-definitiva/app/modulos/raiz/index.tsx << 'EOL'
// ÍNDICE DE MÓDULOS MODULO_* - FUNDAÇÃO ALCHEMISTA
// Gerado automaticamente em $(date)

import React from 'react';

export default function ModulosRaizIndex() {
  const modulosRaiz = {
    total: $(wc -l < ~/fundacao-definitiva/analise-modulos/modulos-raiz-completo.txt),
    prioritarios: [${MODULOS_RAIZ_PRIORITARIOS[@]}],
    status: 'integracao_raiz'
  };

  return (
    <div style={{ padding: '2rem', background: '#0a0a0a', color: 'white' }}>
      <h1>📚 Módulos MODULO_* - Fundação Alchemista</h1>
      <p>Total de módulos MODULO_*: {modulosRaiz.total}</p>
      <div>
        <h2>🎯 Módulos Prioritários</h2>
        <ul>
          {modulosRaiz.prioritarios.map((modulo, index) => (
            <li key={index}>🔹 {modulo}</li>
          ))}
        </ul>
      </div>
      <div>
        <h2>📊 Estatísticas</h2>
        <p>✅ Módulos SRC: 14</p>
        <p>✅ Módulos MODULO_*: {modulosRaiz.total}</p>
        <p>📈 Total Geral: {14 + modulosRaiz.total}</p>
      </div>
    </div>
  );
}
EOL

echo "✅ INTEGRAÇÃO MODULO_* CONCLUÍDA!"
