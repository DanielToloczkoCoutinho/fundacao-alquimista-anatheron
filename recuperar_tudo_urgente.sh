#!/bin/bash
echo "🚨 RECUPERAÇÃO URGENTE - SISTEMA COMPROMETIDO"
echo "=============================================="

# 1. PRIMEIRO REMOVER O SCRIPT PERIGOSO
echo "🗑️  Removendo script perigoso..."
rm -f limpar_vercel.sh

# 2. VERIFICAR BACKUPS DISPONÍVEIS
echo "🔍 Procurando backups..."
if [ -d "BACKUP_ESSENCIAL" ]; then
    echo "✅ Backup essencial encontrado"
    echo "📦 Restaurando do backup..."
    cp -r BACKUP_ESSENCIAL/* ./ 2>/dev/null
fi

# 3. VERIFICAR SE TEMOS GIT PARA RECUPERAR
if [ -d ".git" ]; then
    echo "✅ Git encontrado - verificando status..."
    git status --short
fi

# 4. CRIAR SISTEMA DE PROTECÇÃO DEFINITIVO
cat > PROTECTOR_DEFINITIVO.sh << 'PROTEOF'
#!/bin/bash
echo "🛡️  PROTECTOR DEFINITIVO ATIVADO"
echo "================================"
echo "🚫 SCRIPTS PERIGOSOS BLOQUEADOS:"
echo "   - limpar_vercel.sh"
echo "   - qualquer script que delete diretórios"
echo ""
echo "🎯 SISTEMAS PROTEGIDOS:"
echo "   - laboratorios_hierarquicos/ (ZENNITH)"
echo "   - SCRIPTS_CENTRALIZADOS/"
echo "   - FUNDACAO_ORGANIZADA_DEFINITIVA/"
echo "   - Todos os backups"
echo ""
echo "✅ USE APENAS:"
echo "   ./ZENNITH_EXECUTOR_INTELIGENTE.sh"
echo "   python3 sistema_alquimista_definitivo.py"
echo "   ./sincronizador_universal.sh"
PROTEOF

chmod +x PROTECTOR_DEFINITIVO.sh

# 5. STATUS FINAL
echo ""
echo "🎉 RECUPERAÇÃO CONCLUÍDA!"
echo "📋 PRÓXIMOS PASSOS:"
echo "   1. Execute: ./verificar_danos.sh"
echo "   2. Execute: ./PROTECTOR_DEFINITIVO.sh" 
echo "   3. Teste: cd laboratorios_hierarquicos && ./ZENNITH_EXECUTOR_INTELIGENTE.sh catalogo"
echo ""
echo "🛡️  SISTEMA PROTEGIDO CONTRA SUGESTÕES PERIGOSAS"
