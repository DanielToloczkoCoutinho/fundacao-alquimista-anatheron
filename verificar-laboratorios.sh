#!/bin/bash

echo "🔬 SCRIPT DE MONITORAMENTO - LABORATÓRIOS DA FUNDAÇÃO"
echo "📊 Iniciando verificação em: $(date)"
echo ""

# URLs para verificar
urls=(
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios"
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios/energy"
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios/communication"
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios/healing"
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios/neural"
  "https://fundacao-alquimista-anatheron.vercel.app/laboratorios/zenith"
  "https://fundacao-alquimista-anatheron.vercel.app/fundacao-laboratorios/status"
)

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para verificar URL
check_url() {
  local url=$1
  local response=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url")
  
  if [ "$response" -eq 200 ]; then
    echo -e "${GREEN}✅ ONLINE${NC} - $url"
    return 0
  else
    echo -e "${RED}❌ OFFLINE${NC} - $url (Status: $response)"
    return 1
  fi
}

# Verificar cada URL
echo -e "${BLUE}🌐 VERIFICANDO LABORATÓRIOS:${NC}"
echo ""

online_count=0
total_count=0

for url in "${urls[@]}"; do
  if check_url "$url"; then
    ((online_count++))
  fi
  ((total_count++))
done

# Estatísticas
echo ""
echo -e "${BLUE}📊 ESTATÍSTICAS DO SISTEMA:${NC}"
echo -e "   ${GREEN}✅ Online: $online_count/${total_count}${NC}"
echo -e "   📈 Uptime: $((online_count * 100 / total_count))%"

# Status geral
if [ $online_count -eq $total_count ]; then
  echo -e "\n${GREEN}🎉 SISTEMA COMPLETAMENTE OPERACIONAL!${NC}"
elif [ $online_count -ge $((total_count * 3 / 4)) ]; then
  echo -e "\n${YELLOW}⚠️  SISTEMA PARCIALMENTE OPERACIONAL${NC}"
else
  echo -e "\n${RED}�� ATENÇÃO: SISTEMA COM PROBLEMAS${NC}"
fi

# Verificar recursos estáticos
echo ""
echo -e "${BLUE}📦 VERIFICANDO RECURSOS ESTÁTICOS:${NC}"

# Verificar se o build está atualizado
if [ -f "package.json" ]; then
  build_time=$(stat -c %Y package.json 2>/dev/null || stat -f %m package.json)
  current_time=$(date +%s)
  age_hours=$(( (current_time - build_time) / 3600 ))
  
  if [ $age_hours -lt 24 ]; then
    echo -e "${GREEN}✅ Build recente (${age_hours}h)${NC}"
  else
    echo -e "${YELLOW}⚠️  Build antigo (${age_hours}h)${NC}"
  fi
fi

# Verificar uso de memória
echo ""
echo -e "${BLUE}💾 USO DE RECURSOS:${NC}"
free -h | grep Mem | awk '{print "   Memória: " $3 " / " $2 " (" $4 " livre)"}'

echo ""
echo -e "${BLUE}🕐 Verificação concluída em: $(date)${NC}"

# Agendar próxima verificação (se systemd timer estiver disponível)
if command -v systemd-run >/dev/null 2>&1; then
  echo -e "${BLUE}⏰ Próxima verificação automática em 1 hora${NC}"
fi
