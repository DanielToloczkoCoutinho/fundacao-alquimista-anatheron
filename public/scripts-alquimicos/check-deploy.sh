#!/bin/bash
echo "🔍 MONITORANDO DEPLOY DO VERCELL..."

URLS=(
  "https://fundacao-alquimista.vercel.app"
  "https://fundacao-alquimista-git-main-daniel-toloczko-coutinhos-projects.vercel.app"
)

for url in "${URLS[@]}"; do
  echo "🌐 Testando: $url"
  status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status" = "200" ]; then
    echo "   ✅ ONLINE (Status: $status)"
    echo "   🔗 Acesse: $url"
    echo "   🔐 Login: $url/auth/signin"
    echo "   💫 Senha: alchemista_2024"
  else
    echo "   ⏳ AGUARDANDO (Status: $status)"
  fi
done

echo ""
echo "📊 Se ainda estiver com problemas:"
echo "1. Acesse: https://vercel.com/daniel-toloczko-coutinho"
echo "2. Clique no projeto 'fundacao-alquimista'"
echo "3. Verifique os logs de deploy"
echo "4. Aguarde 5-10 minutos para processamento completo"
