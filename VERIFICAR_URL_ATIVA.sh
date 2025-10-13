#!/bin/bash
echo "🌐 VERIFICANDO URLs VERCEL ATIVAS"
echo "================================"

URLS=(
    "https://fundacao-alquimista-anatheron-cprkux23i.vercel.app"
    "https://fundacao-alquimista-anatheron.vercel.app"
    "https://fundacao-alquimista-anatheron-b8q3t0nhk.vercel.app/central"
    "https://fundacao-alquimis-git-0a0231-daniel-toloczko-coutinhos-projects.vercel.app/"
    "https://fundacao-alquimista-anatheron-jj21jyyqd.vercel.app/central"
)

echo "🔍 Testando ${#URLS[@]} URLs..."

URL_ATIVA=""
for url in "${URLS[@]}"; do
    echo -n "Testing $url ... "
    if curl -s --head "$url" | grep "200 OK" > /dev/null; then
        echo "✅ ATIVA"
        if [ -z "$URL_ATIVA" ]; then
            URL_ATIVA="$url"
        fi
    else
        echo "❌ INATIVA"
    fi
done

echo ""
echo "🎯 URL CANÔNICA RECOMENDADA: $URL_ATIVA"
echo "💫 Todas as outras URLs devem ser desativadas"

# Salvar resultado
cat > url_canonica.txt << URL_RESULT
URL_CANONICA=$URL_ATIVA
TIMESTAMP=$(date)
URL_RESULT

echo "✅ Verificação concluída!"
