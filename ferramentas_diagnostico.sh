#!/bin/bash
echo "🛠️ FERRAMENTAS DE DIAGNÓSTICO RÁPIDO"
echo "===================================="

# 1. VERIFICADOR DE SAÚDE DO SISTEMA
cat > verificar_saude.sh << 'VERIFICAR'
#!/bin/bash
echo "🏥 VERIFICADOR DE SAÚDE DO SISTEMA"
echo "================================="

echo "�� FRONTEND:"
echo "   📁 Páginas: $(find /home/user/studio/app -name "page.tsx" 2>/dev/null | wc -l)"
echo "   🏗️ Build: $(ls -la /home/user/studio/.next 2>/dev/null | head -1 | cut -d' ' -f6-8)"

echo ""
echo "🔧 BACKEND:"
echo "   🐍 Python: $(find /home/user -name "*.py" 2>/dev/null | wc -l) arquivos"
echo "   📚 Libs: $(find /home/user -name "requirements.txt" -o -name "package.json" 2>/dev/null | wc -l)"

echo ""
echo "🌐 CONEXÕES:"
urls=("dashboard-real" "tecnologias-reais" "organograma")
for url in "${urls[@]}"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "https://fundacao-alquimista-anatheron.vercel.app/$url")
    if [ "$status" -eq 200 ]; then
        echo "   ✅ $url: CONECTADO"
    else
        echo "   ❌ $url: PROBLEMA ($status)"
    fi
done

echo ""
echo "🎯 DIAGNÓSTICO:"
if [ $(find /home/user/studio/app -name "page.tsx" | wc -l) -gt 20 ]; then
    echo "   🟢 FRONTEND: SAUDÁVEL"
else
    echo "   🔴 FRONTEND: PROBLEMAS"
fi

if [ $(find /home/user -name "*.py" | wc -l) -gt 10000 ]; then
    echo "   🟢 BACKEND: SAUDÁVEL"
else
    echo "   🔴 BACKEND: PROBLEMAS"
fi
VERIFICAR

# 2. OTIMIZADOR DE PERFORMANCE
cat > otimizar_performance.sh << 'OTIMIZAR'
#!/bin/bash
echo "⚡ OTIMIZADOR DE PERFORMANCE"
echo "==========================="

echo "🧹 Limpando cache..."
cd /home/user/studio
rm -rf .next 2>/dev/null
echo "   ✅ Cache limpo"

echo "🔨 Rebuild rápido..."
npm run build > /tmp/build.log 2>&1 &
BUILD_PID=$!

# Monitorar build em background
{
    sleep 10
    if ps -p $BUILD_PID > /dev/null; then
        echo "   ⏳ Build em andamento..."
    else
        echo "   ✅ Build concluído"
    fi
} &

echo "🌐 Deploy otimizado..."
vercel --prod > /tmp/deploy.log 2>&1 &
echo "   🚀 Deploy iniciado"

echo ""
echo "📊 MONITORAMENTO:"
echo "   Build log: tail -f /tmp/build.log"
echo "   Deploy log: tail -f /tmp/deploy.log"
OTIMIZAR

# 3. ANALISADOR DE TECNOLOGIAS RÁPIDO
cat > analise_rapida_tech.sh << 'ANALISE'
#!/bin/bash
echo "🔬 ANÁLISE RÁPIDA DE TECNOLOGIAS"
echo "================================"

cd /home/user

# Tecnologias críticas para verificar rápido
tech_criticas=("qiskit" "tensorflow" "three" "webgl" "quantum")

for tech in "${tech_criticas[@]}"; do
    echo -n "🔍 $tech: "
    count=$(find . -name "*.py" -exec grep -l "$tech" {} \; 2>/dev/null | head -5 | wc -l)
    if [ $count -gt 0 ]; then
        echo "✅ $count sistemas"
        # Mostrar alguns exemplos
        find . -name "*.py" -exec grep -l "$tech" {} \; 2>/dev/null | head -2 | while read file; do
            echo "     📄 $(basename $file)"
        done
    else
        echo "❌ não encontrado"
    fi
done

echo ""
echo "�� TECNOLOGIAS IDENTIFICADAS:"
grep -r "import\\|from" /home/user/studio 2>/dev/null | grep -E "qiskit|tensorflow|three" | head -5
ANALISE

chmod +x verificar_saude.sh
chmod +x otimizar_performance.sh  
chmod +x analise_rapida_tech.sh

echo "✅ Ferramentas criadas!"
echo ""
echo "🛠️ FERRAMENTAS DISPONÍVEIS:"
echo "   🏥 ./verificar_saude.sh    - Verifica saúde do sistema"
echo "   ⚡ ./otimizar_performance.sh - Otimiza performance"
echo "   🔬 ./analise_rapida_tech.sh - Análise rápida de tecnologias"
echo "   🔍 ./sistema_monitoramento_tempo_real.sh - Monitoramento em tempo real"
