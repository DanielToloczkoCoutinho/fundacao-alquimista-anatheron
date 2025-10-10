#!/bin/bash
echo "🆘 SISTEMA DE EMERGÊNCIA - FUNDAÇÃO ALQUIMISTA"
echo "=============================================="

# Criar backup dos arquivos importantes
mkdir -p backup_emergencia
cp *.py *.sh *.md backup_emergencia/ 2>/dev/null || true
cp -r pesquisa/ backup_emergencia/ 2>/dev/null || true

echo "💾 Backup criado em: backup_emergencia/"
echo "📋 Arquivos salvos:"
find backup_emergencia/ -type f -name "*.py" -o -name "*.sh" -o -name "*.md" | head -10

# Criar script de recuperação
cat > recuperar_fundacao.sh << 'EOL'
#!/bin/bash
echo "🔧 RECUPERAÇÃO DA FUNDAÇÃO ALQUIMISTA"
echo "===================================="

if [ -d "backup_emergencia" ]; then
    echo "📦 Restaurando arquivos..."
    cp -r backup_emergencia/* ./
    echo "✅ Recuperação concluída!"
else
    echo "❌ Nenhum backup encontrado!"
    echo "💡 Execute o sistema portátil: python fundacao_portatil.py"
fi
EOL

chmod +x recuperar_fundacao.sh

echo ""
echo "🚀 SISTEMA DE EMERGÊNCIA CONFIGURADO!"
echo "💡 Comandos disponíveis:"
echo "   python fundacao_portatil.py    - Sistema portátil"
echo "   ./recuperar_fundacao.sh        - Recuperar backup"
echo "   source fundacao_independente/bin/activate - Ambiente virtual"
