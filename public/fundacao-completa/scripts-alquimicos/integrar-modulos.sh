#!/bin/bash
echo "🔄 INICIANDO INTEGRAÇÃO DE MÓDULOS..."

# Fase 1: Análise superficial
echo "📊 FASE 1: Análise Superficial"
find ~/studio -name "page.tsx" -path "*/module*" | head -20 > ~/fundacao-definitiva/analise-modulos/modulos-com-pagina.txt

# Fase 2: Integração por prioridade
echo "🎯 FASE 2: Integração por Prioridade"
mkdir -p ~/fundacao-definitiva/app/modulos-prioritarios

# Integrar módulos mais importantes primeiro
MODULOS_PRIORITARIOS=("module-9" "module-29" "module-omega" "module-0")

for modulo in "${MODULOS_PRIORITARIOS[@]}"; do
    echo "🔧 Integrando: $modulo"
    find ~/studio -name "$modulo" -type d -exec cp -r {} ~/fundacao-definitiva/app/modulos-prioritarios/ \; 2>/dev/null
done

# Fase 3: Criar índice de módulos
echo "📚 FASE 3: Criando Índice"
cat > ~/fundacao-definitiva/app/modulos/index.tsx << 'EOL'
// ÍNDICE DE MÓDULOS DA FUNDAÇÃO ALCHEMISTA
// Gerado automaticamente em $(date)

export const modulos = {
  // Módulos prioritários integrados
  prioritarios: [${MODULOS_PRIORITARIOS[@]}],
  
  // Total de módulos encontrados
  total: $TOTAL_MODULOS,
  
  // Status de integração
  status: 'em_andamento'
}
EOL

echo "✅ INTEGRAÇÃO INICIADA!"
