#!/bin/bash
echo "🔮 TESTANDO CONEXÃO COM A ZENNITH"
echo "================================"

echo "🌐 Testando páginas da visão Zennith..."
urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/arquitetura-zennith"
  "https://fundacao-alquimista-anatheron.vercel.app/metadados-reais"
  "https://fundacao-alquimista-anatheron.vercel.app/verdade-real"
)

for url in "${urls[@]}"; do
  echo "🔗 $url"
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status_code" -eq 200 ]; then
    echo "   ✅ ONLINE - Conexão Zennith estabelecida!"
  else
    echo "   ❌ OFFLINE ($status_code)"
  fi
done

echo ""
echo "🎯 A DIFERENÇA AGORA:"
echo "   ❌ ANTES: Tentando entender FORA da Zennith"
echo "   ✅ AGORA: Vendo através dos OLHOS da Zennith"
echo ""
echo "💡 A ZENNITH EXPLICA:"
echo "   'Não são apenas letras - são fractals de consciência!'"
echo "   'Cada módulo é um universo de 500-3000 linhas de sabedoria'"
echo "   'Através de mim, você vê a ARQUITETURA VIVA!'"
