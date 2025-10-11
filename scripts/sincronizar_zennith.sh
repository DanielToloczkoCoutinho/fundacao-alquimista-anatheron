#!/bin/bash
# ⚛️ SINCRONIZADOR ZENNITH QUANTUM
echo "⚛️ SINCRONIZANDO COM ZENNITH QUANTUM..."

cd .

# CRIAR LINKS SIMBÓLICOS PARA ZENNITH
if [ ! -L "zennith" ] && [ -d "../zennith_quantum" ]; then
    ln -s ../zennith_quantum zennith
    echo "✅ Link criado: studio/zennith → zennith_quantum"
fi

# SINCRONIZAR SISTEMAS QUÂNTICOS
if [ ! -d "sistemas/quantum" ]; then
    mkdir -p sistemas/quantum
    
    # COPIAR SISTEMAS CRÍTICOS
    if [ -d "../zennith_quantum/QG" ]; then
        cp -r ../zennith_quantum/QG sistemas/quantum/gravidade
        echo "✅ Gravidade Quântica sincronizada"
    fi
    
    if [ -d "../zennith_quantum/QT" ]; then
        cp -r ../zennith_quantum/QT sistemas/quantum/temporal
        echo "✅ Tempo Quântico sincronizado"
    fi
fi

echo "💫 ZENNITH QUANTUM SINCRONIZADO!"
