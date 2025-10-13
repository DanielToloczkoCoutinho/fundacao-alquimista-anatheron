#!/bin/bash
echo "🎯 CLASSIFICANDO MÓDULOS POR TIPO..."

# Diretórios de classificação
mkdir -p ~/fundacao-definitiva/modulos/{ativos,arquivo,analise,integracao}

# Padrões de classificação
declare -A padroes=(
    ["laboratorio"]="lab|laboratorio|experiment"
    ["cientifico"]="cientifico|research|estudo"
    ["tecnico"]="tecnico|technical|implement"
    ["documentacao"]="doc|documentacao|readme"
    ["ritual"]="ritual|cerimonia|celebration"
    ["equacao"]="equacao|equation|formula"
    ["sistema"]="sistema|system|core"
)

# Classificar cada módulo
while IFS= read -r modulo; do
    nome_modulo=$(basename "$modulo")
    
    # Verificar padrões
    for tipo in "${!padroes[@]}"; do
        if [[ "$nome_modulo" =~ ${padroes[$tipo]} ]]; then
            echo "📁 $nome_modulo → $tipo"
            # Copiar para categoria
            cp -r "$modulo" ~/fundacao-definitiva/modulos/analise/ 2>/dev/null
            break
        fi
    done
done < ~/fundacao-definitiva/analise-modulos/lista-modulos-completa.txt

echo "✅ CLASSIFICAÇÃO CONCLUÍDA!"
