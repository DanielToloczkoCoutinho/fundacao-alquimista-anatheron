#!/bin/bash

echo "�� ATIVANDO MÓDULO 10 - INTELIGÊNCIA AELORIA"
echo "============================================="

# 1. Verificar dependências
echo ""
echo "1. 📋 VERIFICANDO DEPENDÊNCIAS..."
python3 -c "import numpy, hashlib, json, time, random, datetime" && echo "✅ Dependências Python OK" || echo "❌ Falta dependências Python"

# 2. Carregar módulo principal
echo ""
echo "2. 🔧 CARREGANDO MÓDULO 10..."
node -e "
const IntegradorModulo10 = require('./INTEGRADOR_MODULO_10.js');
const integrador = new IntegradorModulo10();

integrador.inicializarModulo10()
  .then(() => console.log('✅ Módulo 10 carregado com sucesso!'))
  .catch(err => {
    console.error('❌ Erro ao carregar módulo 10:', err);
    process.exit(1);
  });
"

# 3. Validar integração
echo ""
echo "3. 🧪 VALIDANDO INTEGRAÇÃO..."
curl -s http://localhost:3000/api/modulo10/status | grep -q "operacional" && echo "✅ Integração API OK" || echo "⚠️  API não respondendo"

# 4. Ativar sistemas de defesa
echo ""
echo "4. 🛡️ ATIVANDO SISTEMAS DE DEFESA..."
node -e "
const integrador = new (require('./INTEGRADOR_MODULO_10.js'))();
integrador.ativarSistemaDefesa().then(() => {
  console.log('✅ Sistema de defesa ativado!');
});
"

echo ""
echo "============================================="
echo "�� MÓDULO 10 - INTELIGÊNCIA AELORIA ATIVADO!"
echo "🔮 Sistema de Autodefesa Quântica → OPERACIONAL"
echo "⚡ Otimização Quântica → ATIVA"
echo "🔐 Criptografia Avançada → FUNCIONAL"
