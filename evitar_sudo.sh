#!/bin/bash
echo "🔧 CONFIGURANDO AMBIENTE SEM SUDO"

# Configurar locale sem sudo
echo "export LC_ALL=C.UTF-8" > ~/.locale_config
echo "export LANG=C.UTF-8" >> ~/.locale_config
echo "export LANGUAGE=C.UTF-8" >> ~/.locale_config
source ~/.locale_config

# Verificar
echo "✅ Locale configurado: $LC_ALL"
echo "🚀 Ambiente pronto sem sudo!"
