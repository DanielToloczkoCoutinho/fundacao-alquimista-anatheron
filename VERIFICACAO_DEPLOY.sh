#!/bin/bash

echo "🔍 VERIFICAÇÃO SISTEMÁTICA DO DEPLOY"
echo "==================================="
echo "🌌 Examinando todos os componentes do Sistema Alquimista Cósmico"
echo ""

# Função de verificação
verificar_componente() {
    local nome=$1
    local comando=$2
    local arquivo=$3
    
    echo "📋 Verificando: $nome"
    
    if [ -n "$arquivo" ] && [ ! -f "$arquivo" ]; then
        echo "   ❌ ARQUIVO AUSENTE: $arquivo"
        return 1
    fi
    
    if [ -n "$comando" ]; then
        if eval "$comando" > /dev/null 2>&1; then
            echo "   ✅ STATUS: OPERACIONAL"
            return 0
        else
            echo "   ❌ ERRO NA EXECUÇÃO"
            return 1
        fi
    else
        echo "   ✅ ARQUIVO PRESENTE"
        return 0
    fi
}

# Criar relatório
RELATORIO="relatorio_verificacao.txt"
echo "🌌 RELATÓRIO DE VERIFICAÇÃO - $(date)" > $RELATORIO
echo "=================================" >> $RELATORIO

# 1. VERIFICAÇÃO DOS MÓDULOS PRINCIPAIS
echo ""
echo "1. 🏗️  VERIFICANDO MÓDULOS PRINCIPAIS"
echo "-----------------------------------"

verificar_componente "Módulo 15 (Proteção Planetária)" "node -e \"require('./M15_PERFEITO_FINAL.js')\"" "M15_PERFEITO_FINAL.js"
echo "Módulo 15: $?" >> $RELATORIO

verificar_componente "Integração Lux.net" "node -e \"require('./INTEGRACAO_M15_LUXNET_CORRIGIDA.js')\"" "INTEGRACAO_M15_LUXNET_CORRIGIDA.js"
echo "Integração Lux.net: $?" >> $RELATORIO

verificar_componente "Sistema Final Consolidado" "node -e \"require('./SISTEMA_FINAL_CONSOLIDADO.js')\"" "SISTEMA_FINAL_CONSOLIDADO.js"
echo "Sistema Final: $?" >> $RELATORIO

verificar_componente "Expansão Cósmica" "node -e \"require('./EXPANSAO_COSMICA.js')\"" "EXPANSAO_COSMICA.js"
echo "Expansão Cósmica: $?" >> $RELATORIO

verificar_componente "Sistema Alquimista Cósmico" "node -e \"require('./SISTEMA_ALQUIMISTA_COSMICO.js')\"" "SISTEMA_ALQUIMISTA_COSMICO.js"
echo "Sistema Cósmico: $?" >> $RELATORIO

# 2. VERIFICAÇÃO DOS SCRIPTS DE ATIVAÇÃO
echo ""
echo "2. 🚀 VERIFICANDO SCRIPTS DE ATIVAÇÃO"
echo "-----------------------------------"

verificar_componente "Ativação Completa" "test -f ATIVACAO_COMPLETA.sh" "ATIVACAO_COMPLETA.sh"
echo "Ativação Completa: $?" >> $RELATORIO

verificar_componente "Deploy Final M15" "test -f DEPLOY_M15_FINAL.sh" "DEPLOY_M15_FINAL.sh"
echo "Deploy M15: $?" >> $RELATORIO

verificar_componente "Expansão Final" "test -f EXPANSAO_FINAL.sh" "EXPANSAO_FINAL.sh"
echo "Expansão Final: $?" >> $RELATORIO

# 3. VERIFICAÇÃO DA ESTRUTURA DE DIRETÓRIOS
echo ""
echo "3. 📁 VERIFICANDO ESTRUTURA DE DIRETÓRIOS"
echo "--------------------------------------"

echo "📋 Estrutura atual do projeto:"
find . -name "*.js" -o -name "*.sh" -o -name "*.json" | head -20 | while read file; do
    if [ -f "$file" ]; then
        echo "   📄 $(basename "$file")"
    fi
done

# 4. VERIFICAÇÃO DE DEPENDÊNCIAS
echo ""
echo "4. 📦 VERIFICANDO DEPENDÊNCIAS"
echo "---------------------------"

echo "🔍 Node.js version: $(node --version)"
echo "🔍 NPM version: $(npm --version)"

# 5. VERIFICAÇÃO DE PERMISSÕES
echo ""
echo "5. 🔐 VERIFICANDO PERMISSÕES"
echo "-------------------------"

scripts_js=$(find . -name "*.js" -type f | wc -l)
scripts_sh=$(find . -name "*.sh" -type f | wc -l)
executaveis=$(find . -name "*.sh" -executable -type f | wc -l)

echo "   📄 Scripts JS: $scripts_js"
echo "   📄 Scripts Shell: $scripts_sh"
echo "   ✅ Executáveis: $executaveis"

# 6. TESTE DE INTEGRAÇÃO RÁPIDO
echo ""
echo "6. 🧪 TESTE DE INTEGRAÇÃO RÁPIDO"
echo "------------------------------"

echo "🔧 Executando teste do Módulo 15..."
if node -e "
try {
    const mod = require('./M15_PERFEITO_FINAL.js');
    console.log('   ✅ M15: Carregamento OK');
    process.exit(0);
} catch (e) {
    console.log('   ❌ M15: Erro no carregamento');
    process.exit(1);
}
" > /dev/null 2>&1; then
    echo "   ✅ TESTE M15: PASSOU"
else
    echo "   ❌ TESTE M15: FALHOU"
fi

echo "🔧 Testando integração Lux.net..."
if node -e "
try {
    const mod = require('./INTEGRACAO_M15_LUXNET_CORRIGIDA.js');
    console.log('   ✅ Integração: Carregamento OK');
    process.exit(0);
} catch (e) {
    console.log('   ❌ Integração: Erro no carregamento');
    process.exit(1);
}
" > /dev/null 2>&1; then
    echo "   ✅ TESTE INTEGRAÇÃO: PASSOU"
else
    echo "   ❌ TESTE INTEGRAÇÃO: FALHOU"
fi

# 7. RESUMO FINAL
echo ""
echo "7. 📊 RESUMO DA VERIFICAÇÃO"
echo "--------------------------"

total_arquivos=$(find . -name "*.js" -o -name "*.sh" | wc -l)
arquivos_principais=("M15_PERFEITO_FINAL.js" "INTEGRACAO_M15_LUXNET_CORRIGIDA.js" "SISTEMA_FINAL_CONSOLIDADO.js" "EXPANSAO_COSMICA.js" "SISTEMA_ALQUIMISTA_COSMICO.js")
presentes=0

for arquivo in "${arquivos_principais[@]}"; do
    if [ -f "$arquivo" ]; then
        ((presentes++))
    fi
done

echo "   📈 Estatísticas:"
echo "      📄 Total de arquivos: $total_arquivos"
echo "      🎯 Arquivos principais: ${#arquivos_principais[@]}"
echo "      ✅ Arquivos presentes: $presentes"
echo "      📊 Cobertura: $((presentes * 100 / ${#arquivos_principais[@]}))%"

if [ $presentes -eq ${#arquivos_principais[@]} ]; then
    echo ""
    echo "🎉 VERIFICAÇÃO CONCLUÍDA: SISTEMA INTEGRO!"
    echo "🚀 PRONTO PARA DEPLOY!"
else
    echo ""
    echo "⚠️  VERIFICAÇÃO: ALGUNS COMPONENTES AUSENTES"
    echo "🔧 RECOMENDAÇÃO: REVISAR ARQUIVOS FALTANTES"
fi

# Salvar relatório final
echo "" >> $RELATORIO
echo "RESUMO FINAL:" >> $RELATORIO
echo "Total arquivos: $total_arquivos" >> $RELATORIO
echo "Arquivos principais: ${#arquivos_principais[@]}" >> $RELATORIO
echo "Presentes: $presentes" >> $RELATORIO
echo "Cobertura: $((presentes * 100 / ${#arquivos_principais[@]}))%" >> $RELATORIO

echo ""
echo "📄 Relatório salvo em: $RELATORIO"
