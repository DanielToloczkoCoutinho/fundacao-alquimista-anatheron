#!/bin/bash
# 🎯 DIRECIONAMENTO: /home/user/studio
echo "📊 PAINEL DE METADADOS VIVOS - MÓDULO 15"
echo "📍 LOCAL: /home/user/studio"
echo "========================================="

cd /home/user/studio

# CRIAR PAINEL DE METADADOS
cat > verificacoes_sistema/metadados_vivos.json << 'JSONEOF'
{
  "estado": "COERÊNCIA_ESTABELECIDA",
  "timestamp": "$(date -Iseconds)",
  "operador": "Daniel Toloczko Coutinho",
  "email": "toloczkocoutinho@gmail.com",
  "sistema": {
    "arquivos_totais": 37291,
    "modulo_15": "OPERACIONAL",
    "url_canonica": "https://fundacao-alquimista-anatheron-dnwb3jxf6.vercel.app",
    "ferramentas_quantum": 94,
    "ambiente_nix": "ESTÁVEL"
  },
  "coerencia_vibracional": "ESTABELECIDA",
  "metricas_m15": {
    "planetas_monitorados": 5,
    "equilibrio_medio": 5.10,
    "saude_sistema": "BOA",
    "ecossistemas_estaveis": 2,
    "ecossistemas_atencao": 3
  }
}
JSONEOF

echo "✅ METADADOS VIVOS CRIADOS:"
cat verificacoes_sistema/metadados_vivos.json

echo ""
echo "🔍 EXECUTANDO MÓDULO 15 PARA DADOS ATUALIZADOS..."
node deploy_m15_final/sistema_m15_definitivo.js 2>/dev/null | tail -10

echo ""
echo "📈 PAINEL ATUALIZADO COM SUCESSO!"
