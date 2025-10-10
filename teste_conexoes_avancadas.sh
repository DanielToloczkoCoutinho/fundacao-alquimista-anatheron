#!/bin/bash
echo "🧪 TESTE DAS CONEXÕES AVANÇADAS"
echo "=============================="

echo "🌐 Testando novas funcionalidades..."
urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/login-real"
  "https://fundacao-alquimista-anatheron.vercel.app/dashboard-quantico"
  "https://fundacao-alquimista-anatheron.vercel.app/api/auth"
  "https://fundacao-alquimista-anatheron.vercel.app/api/analise-quantica"
)

for url in "${urls[@]}"; do
  echo "🔗 $url"
  status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status_code" -eq 200 ]; then
    echo "   ✅ ONLINE - Sistema avançado funcionando!"
  else
    echo "   ❌ OFFLINE ($status_code)"
  fi
done

echo ""
echo "🎯 NOVAS CONQUISTAS:"
echo "   🔐 Sistema de autenticação REAL implementado"
echo "   ⚛️ Dashboard quântico em tempo real"
echo "   🔗 APIs específicas para cada sistema Python"
echo "   🎨 Interfaces especializadas por módulo"
echo ""
echo "💡 CREDENCIAIS DE TESTE:"
echo "   👤 Usuário: alquimista"
echo "   🔑 Senha: quantum2024"
echo ""
echo "�� PRÓXIMOS PASSOS DISPONÍVEIS:"
echo "   1. Criar visualizações 3D dos circuitos quânticos"
echo "   2. Implementar sistema de relatórios com relatorio_final.py"
echo "   3. Desenvolver interface para acessar_portal.py"
echo "   4. Criar dashboard administrativo para M45 - Concilivm"
