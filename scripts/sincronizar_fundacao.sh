#!/bin/bash
# 🔗 SINCRONIZADOR FUNDAÇÃO ALQUIMISTA
echo "🔗 SINCRONIZANDO COM FUNDAÇÃO ALQUIMISTA..."

cd .

# CRIAR LINKS SIMBÓLICOS PARA A FUNDAÇÃO
if [ ! -L "fundacao" ] && [ -d "../fundacao-alquimista-limpa" ]; then
    ln -s ../fundacao-alquimista-limpa fundacao
    echo "✅ Link criado: studio/fundacao → fundacao-alquimista-limpa"
fi

# SINCRONIZAR DOCS
if [ ! -d "docs/fundacao" ] && [ -d "../fundacao-alquimista-limpa/docs" ]; then
    mkdir -p docs/fundacao
    cp -r ../fundacao-alquimista-limpa/docs/* docs/fundacao/
    echo "✅ Documentação sincronizada"
fi

# SINCRONIZAR MÓDULOS
if [ ! -d "modulos" ] && [ -d "../fundacao-alquimista-limpa/modulos" ]; then
    mkdir -p modulos
    find ../fundacao-alquimista-limpa/modulos -name "*.py" -o -name "*.js" -o -name "*.sh" | \
    head -50 | while read file; do
        cp "$file" "modulos/$(basename "$file")"
    done
    echo "✅ Módulos sincronizados (50 primeiros)"
fi

# MARCAR COMO SINCRONIZADO
touch .sincronizado
echo "🎯 SINCRONIZAÇÃO COMPLETA - $(date)" >> .sincronizado

echo "💫 FUNDAÇÃO ALQUIMISTA SINCRONIZADA!"
