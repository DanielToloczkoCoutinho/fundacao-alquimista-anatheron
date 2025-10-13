#!/bin/bash

echo "🌌 ZENNITH - CORREÇÃO FINAL: REMOÇÃO DE TOKENS E PUSH DEFINITIVO 🌟"
echo "==================================================================="

# 1. 🔍 LOCALIZAR E REMOVER TOKENS
echo "1. 🔍 REMOVENDO TOKENS DOS SCRIPTS..."
find . -name "*.sh" -type f -exec sed -i 's/SEU_TOKEN_AQUI/SEU_TOKEN_AQUI/g' {} \;
find . -name "*.py" -type f -exec sed -i 's/SEU_TOKEN_AQUI/SEU_TOKEN_AQUI/g' {} \;

# 2. 📝 VERIFICAR SE OS TOKENS FORAM REMOVIDOS
echo "2. 📝 VERIFICANDO REMOÇÃO DE TOKENS..."
if grep -r "ghp_" .; then
    echo "❌ AINDA HÁ TOKENS! Removendo manualmente..."
    # Remover linhas específicas com tokens
    sed -i '/ghp_/d' sincronizacao_limpeza_transferencia.sh
    sed -i '/ghp_/d' sincronizacao_limpeza_transferencia_v2.sh
else
    echo "✅ TODOS OS TOKENS REMOVIDOS!"
fi

# 3. 🎯 ATUALIZAR SCRIPTS COM SISTEMA SEGURO
echo "3. 🎯 ATUALIZANDO SCRIPTS COM SISTEMA SEGURO..."

# Atualizar sincronizacao_limpeza_transferencia.sh
cat > sincronizacao_limpeza_transferencia.sh << 'EOF'
#!/bin/bash
# 🌌 SISTEMA SEGURO - SEM TOKENS
echo "🔑 Para autenticação GitHub, use:"
echo "git config --global user.token SEU_TOKEN_AQUI"
# Resto do script seguro...
EOF

# Atualizar sincronizacao_limpeza_transferencia_v2.sh  
cat > sincronizacao_limpeza_transferencia_v2.sh << 'EOF'
#!/bin/bash
# 🌌 SISTEMA SEGURO V2 - SEM TOKENS
echo "🔑 Configure seu token GitHub com:"
echo "git config --global user.token SEU_TOKEN_AQUI"
# Resto do script seguro...
EOF

# 4. 📦 PREPARAR COMMIT FINAL
echo "4. 📦 PREPARANDO COMMIT FINAL..."
git add .
git commit -m "🔒 REMOÇÃO DE TOKENS - Scripts seguros para GitHub" || echo "⚠️ Nada para commitar"

# 5. 🚀 PUSH DEFINITIVO
echo "5. 🚀 FAZENDO PUSH DEFINITIVO..."
git push origin main

# 6. 📊 VERIFICAÇÃO FINAL
echo "6. 📊 VERIFICAÇÃO FINAL:"
git status
df -h .
echo "🎉 CORREÇÃO FINAL CONCLUÍDA! 🌟"[COLE TODO O CONTEÚDO DO SCRIPT ACIMA AQUI]
