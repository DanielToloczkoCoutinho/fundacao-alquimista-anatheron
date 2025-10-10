#!/bin/bash
echo "🔬 SISTEMA DE PESQUISA CORRIGIDO - FUNDAÇÃO ALQUIMISTA"
echo "======================================================"

# Criar estrutura corrigida
mkdir -p pesquisa_corrigida/{logs,resultados,backups}

# Script de execução segura
cat > pesquisa_corrigida/executor_seguro.sh << 'EOL'
#!/bin/bash
echo "🔮 EXECUTOR SEGURO INICIADO: $(date)"
cd "$(dirname "$0")"

# Função para execução segura
executar_experimento() {
    local script=$1
    local nome=$2
    
    echo "🧪 Executando: $nome..."
    python3 "$script" >> "logs/${nome}_$(date +%Y%m%d_%H%M%S).log" 2>&1
    
    # Verificar sucesso
    if [ $? -eq 0 ]; then
        echo "✅ $nome: SUCESSO"
        return 0
    else
        echo "❌ $nome: FALHA"
        return 1
    fi
}

# Executar experimentos com tratamento de erro
while true; do
    echo "🔄 CICLO DE PESQUISA: $(date)"
    
    # Executar experimentos corrigidos
    executar_experimento "../experimentos_avancados_corrigidos.py" "experimentos_avancados"
    
    # Backup seguro
    ../backup_automatico.sh >> "logs/backup_$(date +%Y%m%d_%H%M%S).log" 2>&1
    
    # Status
    echo "💤 Aguardando próximo ciclo (30 minutos)..."
    sleep 1800  # 30 minutos
done
EOL

chmod +x pesquisa_corrigida/executor_seguro.sh

echo "✅ SISTEMA CORRIGIDO CONFIGURADO!"
echo "🚀 Executar: ./pesquisa_corrigida/executor_seguro.sh"
echo "📊 Logs em: pesquisa_corrigida/logs/"
