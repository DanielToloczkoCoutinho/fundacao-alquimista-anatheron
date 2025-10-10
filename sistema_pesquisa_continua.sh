#!/bin/bash
echo "🔬 SISTEMA DE PESQUISA CONTÍNUA - FUNDAÇÃO ALQUIMISTA"
echo "======================================================"

# Criar diretório de pesquisa
mkdir -p pesquisa_avancada/{shor,neural_quantica,materiais,quimica}

# Script de execução automática
cat > pesquisa_avancada/executar_pesquisa.sh << 'EOL'
#!/bin/bash
echo "🔮 INICIANDO ROTINA DE PESQUISA AUTOMÁTICA..."
cd "$(dirname "$0")"

while true; do
    echo "$(date): Executando experimentos..."
    
    # Executar experimentos avançados
    python3 ../experimentos_avancados.py >> logs/experimentos.log 2>&1
    
    # Backup automático
    ../backup_automatico.sh >> logs/backup.log 2>&1
    
    # Status
    echo "$(date): Ciclo completo. Próximo em 1 hora..."
    sleep 3600  # 1 hora
done
EOL

chmod +x pesquisa_avancada/executar_pesquisa.sh

# Configurar logs
mkdir -p pesquisa_avancada/logs

echo "✅ SISTEMA DE PESQUISA CONTÍNUA CONFIGURADO!"
echo "🚀 Executar: ./pesquisa_avancada/executar_pesquisa.sh"
echo "📊 Logs em: pesquisa_avancada/logs/"
