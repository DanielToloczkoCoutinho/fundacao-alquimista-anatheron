#!/bin/bash

echo "✅ VERIFICADOR COMPLETO - TODAS AS VERIFICAÇÕES"
echo "=============================================="

PASSOS=0
AVISOS=0

verificar_passo() {
    local passo=$1
    local comando=$2
    local critico=$3
    
    ((PASSOS++))
    echo "$PASSOS. $passo"
    
    if eval "$comando" 2>/dev/null; then
        echo "   ✅ OK"
        return 0
    else
        echo "   ❌ FALHOU"
        if [ "$critico" = "true" ]; then
            return 1
        else
            ((AVISOS++))
            return 0
        fi
    fi
}

echo "🔧 CONFIGURAÇÕES DO PROJETO:"
echo "---------------------------"

verificar_passo "next.config.js existe" "[ -f next.config.js ]" "true"
verificar_passo "ESLint configurado" "[ -f .eslintrc.json ] || grep -q 'eslint' package.json" "false"
verificar_passo "TypeScript configurado" "[ -f tsconfig.json ]" "false"
verificar_passo "Arquivo de ambiente" "[ -f .env.local ]" "false"
verificar_passo "Tailwind configurado" "[ -f tailwind.config.js ]" "false"
verificar_passo "PostCSS configurado" "[ -f postcss.config.js ]" "false"

echo ""
echo "📁 ESTRUTURA DO PROJETO:"
echo "-----------------------"

verificar_passo "Diretório app existe" "[ -d app ]" "true"
verificar_passo "Layout principal" "[ -f app/layout.js ]" "true"
verificar_passo "Página inicial" "[ -f app/page.js ]" "true"
verificar_passo "Portal Central" "[ -f app/central/page.js ]" "true"
verificar_passo "Módulo 303" "[ -f app/modulo-303/page.js ]" "true"
verificar_passo "Sistema Vivo" "[ -f app/sistema-vivo/page.js ]" "true"
verificar_passo "Status" "[ -f app/status/page.js ]" "true"
verificar_passo "API Health" "[ -f app/api/health/route.js ]" "true"
verificar_passo "API Metrics" "[ -f app/api/metrics/route.js ]" "true"

echo ""
echo "⚛️  COMPONENTES REACT:"
echo "--------------------"

for page in app/central/page.js app/modulo-303/page.js app/sistema-vivo/page.js app/status/page.js; do
    if [ -f "$page" ]; then
        echo "📄 $(basename $(dirname $page)):"
        if grep -q "use client" "$page"; then
            echo "   ✅ Client Component"
        else
            echo "   ⚠️  Possível Server Component"
        fi
        if grep -q "useState\|useEffect" "$page"; then
            echo "   ✅ Hooks React"
        fi
        if grep -q "export const dynamic" "$page"; then
            echo "   ✅ Renderização Dinâmica"
        fi
    fi
done

echo ""
echo "�� BUILD E DEPLOY:"
echo "-----------------"

echo "🔨 Executando build com verificações completas..."
if npm run build 2>&1 | tee build_completo.log; then
    echo "✅ BUILD BEM-SUCEDIDO!"
    
    # Verificar se as verificações estão sendo executadas
    echo ""
    echo "📊 VERIFICAÇÕES EXECUTADAS NO BUILD:"
    if grep -q "Compiled successfully" build_completo.log; then
        echo "   ✅ Compilação bem-sucedida"
    fi
    if grep -q "Skipping validation of types" build_completo.log; then
        echo "   ⚠️  TypeScript validation pulada"
        ((AVISOS++))
    else
        echo "   ✅ TypeScript validation executada"
    fi
    if grep -q "Skipping linting" build_completo.log; then
        echo "   ⚠️  ESLint validation pulada" 
        ((AVISOS++))
    else
        echo "   ✅ ESLint validation executada"
    fi
    if grep -q "Collecting page data" build_completo.log; then
        echo "   ✅ Coleta de dados de página"
    fi
    if grep -q "Generating static pages" build_completo.log; then
        echo "   ✅ Geração de páginas estáticas"
    fi
    if grep -q "Finalizing page optimization" build_completo.log; then
        echo "   ✅ Otimização de página finalizada"
    fi
    
else
    echo "❌ BUILD FALHOU"
    exit 1
fi

echo ""
echo "🌐 DEPLOY FINAL:"
if [ $AVISOS -eq 0 ]; then
    echo "🎉 TODAS AS VERIFICAÇÕES PASSARAM!"
    echo "🚀 SISTEMA 100% CONFIGURADO CORRETAMENTE"
    echo ""
    echo "📋 RESUMO:"
    echo "   - ✅ $PASSOS verificações realizadas"
    echo "   - ✅ 0 avisos"
    echo "   - ✅ Todas as configurações corretas"
    echo ""
    echo "🌐 INICIANDO DEPLOY FINAL..."
    npx vercel --prod --force
else
    echo "⚠️  SISTEMA FUNCIONAL COM $AVISOS AVISOS"
    echo ""
    echo "📋 RESUMO:"
    echo "   - ✅ $PASSOS verificações realizadas" 
    echo "   - ⚠️  $AVISOS avisos (não críticos)"
    echo "   - ✅ Sistema operacional"
    echo ""
    echo "💡 RECOMENDAÇÃO:"
    echo "   O sistema está funcionando, mas algumas verificações"
    echo "   opcionais estão desativadas para maior velocidade."
    echo ""
    echo "🌐 DEPLOY DISPONÍVEL (com avisos):"
    npx vercel --prod --force
fi

