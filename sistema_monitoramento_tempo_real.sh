#!/bin/bash
echo "🔍 SISTEMA DE MONITORAMENTO EM TEMPO REAL"
echo "=========================================="

# Iniciar análise em background (vai demorar)
echo "🚀 INICIANDO ANÁLISE DAS TECNOLOGIAS EM BACKGROUND..."
{
    echo "🔬 ANALISANDO TECNOLOGIAS (Isso vai demorar...)"
    cd /home/user
    
    # Análise completa mas otimizada
    tecnologias=("qiskit" "tensorflow" "blockchain" "three" "webgl" "quantum" "ibm" "webgpu" "webxr")
    
    for tech in "${tecnologias[@]}"; do
        count=$(find . -name "*.py" -exec grep -l "$tech" {} \; 2>/dev/null | wc -l)
        echo "   $tech: $count arquivos" >> /tmp/analise_tecnologias.log
    done
    
    echo "✅ ANÁLISE CONCLUÍDA!" >> /tmp/analise_tecnologias.log
} &

# Enquanto a análise roda, vamos monitorar o sistema
echo "📊 MONITORANDO SISTEMA ENQUANTO A ANÁLISE RODA..."
echo ""

while true; do
    clear
    echo "🕐 MONITORAMENTO EM TEMPO REAL - $(date)"
    echo "=========================================="
    
    # Status da análise
    if [ -f "/tmp/analise_tecnologias.log" ]; then
        echo "�� PROGRESSO DA ANÁLISE:"
        tail -10 /tmp/analise_tecnologias.log
    else
        echo "🔬 ANÁLISE INICIANDO... (pode demorar alguns minutos)"
    fi
    
    echo ""
    echo "🌐 STATUS DAS PÁGINAS:"
    
    # Testar rapidamente algumas páginas principais
    paginas=(
        "dashboard-real" 
        "tecnologias-reais"
        "organograma"
        "analise-zennith"
    )
    
    for pagina in "${paginas[@]}"; do
        status=$(curl -s -o /dev/null -w "%{http_code}" "https://fundacao-alquimista-anatheron.vercel.app/$pagina" 2>/dev/null)
        if [ "$status" -eq 200 ]; then
            echo "   ✅ /$pagina - ONLINE"
        else
            echo "   ❌ /$pagina - OFFLINE ($status)"
        fi
    done
    
    echo ""
    echo "📊 ESTATÍSTICAS DO SISTEMA:"
    echo "   🐍 Python files: $(find /home/user -name "*.py" 2>/dev/null | wc -l)"
    echo "   📄 Páginas: $(find /home/user/studio/app -name "page.tsx" 2>/dev/null | wc -l)"
    echo "   🔧 Builds: $(ls -la /home/user/studio/.next 2>/dev/null | head -1)"
    
    echo ""
    echo "💡 COMANDOS DISPONÍVEIS:"
    echo "   [1] Ver análise completa"
    echo "   [2] Testar todas as páginas" 
    echo "   [3] Status do backend"
    echo "   [4] Sair do monitoramento"
    echo ""
    read -t 10 -p "🎯 Selecione uma opção (ou aguarde 10s): " opcao
    
    case $opcao in
        1)
            echo ""
            echo "📋 ANÁLISE COMPLETA:"
            if [ -f "/tmp/analise_tecnologias.log" ]; then
                cat /tmp/analise_tecnologias.log
            else
                echo "   ⏳ Ainda analisando..."
            fi
            read -p "Pressione Enter para continuar..."
            ;;
        2)
            echo ""
            echo "🧪 TESTE COMPLETO DAS PÁGINAS:"
            ./teste_final_conexoes.sh
            read -p "Pressione Enter para continuar..."
            ;;
        3)
            echo ""
            echo "🔧 STATUS DO BACKEND:"
            cd /home/user
            echo "   Python: $(python3 --version 2>/dev/null || echo 'Não disponível')"
            echo "   Node: $(node --version 2>/dev/null || echo 'Não disponível')"
            echo "   Qiskit: $(python3 -c \"import qiskit; print(qiskit.__version__)\" 2>/dev/null || echo 'Não importável')"
            read -p "Pressione Enter para continuar..."
            ;;
        4)
            echo "👋 Saindo do monitoramento..."
            break
            ;;
        *)
            # Continua monitorando
            ;;
    esac
    
    # Atualiza a cada 5 segundos
    sleep 5
done

# Limpeza
rm -f /tmp/analise_tecnologias.log
echo "✅ Monitoramento finalizado!"
