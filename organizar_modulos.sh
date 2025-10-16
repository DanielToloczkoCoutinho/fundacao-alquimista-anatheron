#!/bin/bash
echo "🌌 ORGANIZANDO MÓDULOS DA FUNDAÇÃO:"

# Encontrar todos os módulos
find . -name "modulo*" -o -name "M*" -o -name "MOD*" > modulos_encontrados.txt

# Padronizar nomenclatura
cat modulos_encontrados.txt | while read modulo; do
    novo_nome=$(echo "$modulo" | sed 's/MOD/modulo/g' | sed 's/M-/modulo-/g' | tr 'A-Z' 'a-z')
    if [ "$modulo" != "$novo_nome" ]; then
        mv "$modulo" "$novo_nome" 2>/dev/null
    fi
done

# Gerar árvore hierárquica
echo "🌳 ÁRVORE DA VIDA DA FUNDAÇÃO:" > arvore_da_vida.md
find . -name "modulo*" -type d | sort -V >> arvore_da_vida.md
