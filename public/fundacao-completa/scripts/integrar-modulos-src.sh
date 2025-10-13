#!/bin/bash
echo "🔄 INTEGRAÇÃO DE MÓDULOS SRC..."

# Criar estrutura de módulos na app
mkdir -p ~/fundacao-definitiva/app/modulos
mkdir -p ~/fundacao-definitiva/app/modulos/{src,prioritarios,analise}

# Fase 1: Copiar módulos com page.tsx (prontos para uso)
echo "📄 FASE 1: Módulos com página"
find ~/studio/src -name "page.tsx" -path "*/module*" | head -50 | while read pagina; do
    modulo_dir=$(dirname "$pagina")
    modulo_nome=$(basename "$modulo_dir")
    echo "📁 Copiando: $modulo_nome"
    cp -r "$modulo_dir" ~/fundacao-definitiva/app/modulos/src/ 2>/dev/null
done

# Fase 2: Módulos prioritários do SRC
echo "🎯 FASE 2: Módulos prioritários SRC"
MODULOS_SRC_PRIORITARIOS=(
    "module-9" "module-29" "module-omega" "module-0"
    "module-100" "module-200" "module-300" "module-400"
    "module-500" "module-600" "module-700" "module-800"
    "module-900" "module-999"
)

for modulo in "${MODULOS_SRC_PRIORITARIOS[@]}"; do
    echo "🔧 Buscando: $modulo"
    find ~/studio/src -name "$modulo" -type d -exec cp -r {} ~/fundacao-definitiva/app/modulos/prioritarios/ \; 2>/dev/null
done

# Fase 3: Criar índice atualizado
mkdir -p ~/fundacao-definitiva/app/modulos

cat > ~/fundacao-definitiva/app/modulos/index.tsx << 'EOL'
// ÍNDICE DE MÓDULOS SRC - FUNDAÇÃO ALCHEMISTA
// Gerado automaticamente em $(date)

import React from 'react';

export default function ModulosIndex() {
  const modulosSrc = {
    total: $(find ~/studio/src -name "module*" -type d | wc -l),
    prioritarios: [${MODULOS_SRC_PRIORITARIOS[@]}],
    status: 'integracao_src'
  };

  return (
    <div style={{ padding: '2rem', background: '#0a0a0a', color: 'white' }}>
      <h1>�� Módulos SRC - Fundação Alchemista</h1>
      <p>Total de módulos no SRC: {modulosSrc.total}</p>
      <div>
        <h2>🎯 Módulos Prioritários</h2>
        <ul>
          {modulosSrc.prioritarios.map((modulo, index) => (
            <li key={index}>🔹 {modulo}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
EOL

echo "✅ INTEGRAÇÃO SRC CONCLUÍDA!"
