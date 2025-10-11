#!/bin/bash
echo "🔍 MONITORAMENTO VERCEL CONTÍNUO"
echo "================================"

url="https://fundacao-alquimista-anatheron-8xv9ixbp3.vercel.app"

while true; do
    echo "🕒 $(date): Verificando..."
    
    status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    
    if [ "$status" = "200" ]; then
        echo "🎉 SISTEMA ONLINE! Todas as 46 interfaces disponíveis!"
        echo "🌐 Acesse: $url"
        break
    else
        echo "⏳ Aguardando deploy... Status: $status"
        sleep 30
    fi
done
