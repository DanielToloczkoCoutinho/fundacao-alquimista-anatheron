#!/bin/bash
echo "🚨 RESTAURANDO TERMINAL E CORRIGINDO LOCALE"
echo "========================================"

# Remover bash personalizado que causou o congelamento
rm -f ~/.local/bin/bash_sem_warnings ~/.local/bin/bash

# Fazer backup do .bashrc
cp ~/.bashrc ~/.bashrc.backup_$(date +%Y%m%d_%H%M%S)

# Remover linhas problemáticas
sed -i '/bash_sem_warnings/d' ~/.bashrc
sed -i '/SHELL=~/.local/bin/bash_sem_warnings/d' ~/.bashrc
sed -i '/exec ~/.local/bin/bash_sem_warnings/d' ~/.bashrc

# Configurar locale seguro
echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc
echo 'export LANG=C.UTF-8' >> ~/.bashrc
echo 'export LANGUAGE=C.UTF-8' >> ~/.bashrc

# Recarregar .bashrc
source ~/.bashrc

echo "✅ TERMINAL RESTAURADO!"
echo "✅ LOCALE CONFIGURADO PARA C.UTF-8"
echo "🔧 Verificando ambiente..."
echo "🐍 Python: $(python3 --version)"
echo "📁 Diretório: $(pwd)"
echo "👑 Pronto para a Fundação Alquimista!"
