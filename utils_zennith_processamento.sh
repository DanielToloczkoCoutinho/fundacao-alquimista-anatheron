#!/bin/bash
echo "🧠 UTILS_ZENNITH_PROCESSAMENTO - Biblioteca de Processamento"
echo "==========================================================="

# CARREGAR DEPENDÊNCIAS
source utils_zennith_log_avancado.sh

# FUNÇÕES DE ORGANIZAÇÃO E CATEGORIZAÇÃO
organizar_por_tipo() {
    local diretorio="$1"
    local padrao="$2"
    
    log_info "Organizando arquivos por tipo em: $diretorio"
    find "$diretorio" -name "$padrao" -type f | while read arquivo; do
        local extensao="${arquivo##*.}"
        local destino="$diretorio/$extensao"
        
        mkdir -p "$destino"
        mv "$arquivo" "$destino/"
        log_debug "Movido: $arquivo → $destino/"
    done
    log_info "Organização por tipo concluída"
}

organizar_por_tamanho() {
    local diretorio="$1"
    local limites="$2"  # "small:1M,medium:10M,large:100M"
    
    log_info "Organizando arquivos por tamanho em: $diretorio"
    
    # Criar diretórios de categoria
    mkdir -p "$diretorio/small" "$diretorio/medium" "$diretorio/large"
    
    find "$diretorio" -maxdepth 1 -type f | while read arquivo; do
        local tamanho=$(stat -f%z "$arquivo" 2>/dev/null || stat -c%s "$arquivo" 2>/dev/null)
        
        if [[ $tamanho -lt 1048576 ]]; then
            mv "$arquivo" "$diretorio/small/"
        elif [[ $tamanho -lt 10485760 ]]; then
            mv "$arquivo" "$diretorio/medium/" 
        else
            mv "$arquivo" "$diretorio/large/"
        fi
    done
    log_info "Organização por tamanho concluída"
}

# FUNÇÕES DE ANÁLISE E RELATÓRIO
gerar_relatorio_estatisticas() {
    local diretorio="$1"
    local relatorio="$2"
    
    log_info "Gerando relatório de estatísticas: $relatorio"
    
    {
        echo "RELATÓRIO DE ESTATÍSTICAS - $(date)"
        echo "======================================"
        echo "Diretório: $diretorio"
        echo ""
        echo "📊 ESTATÍSTICAS GERAIS:"
        echo "  Arquivos totais: $(find "$diretorio" -type f | wc -l)"
        echo "  Diretórios: $(find "$diretorio" -type d | wc -l)"
        echo "  Espaço usado: $(du -sh "$diretorio" | cut -f1)"
        echo ""
        echo "📁 DISTRIBUIÇÃO POR EXTENSÃO:"
        find "$diretorio" -type f | sed 's/.*\.//' | sort | uniq -c | sort -nr | head -10
    } > "$relatorio"
    
    log_info "Relatório gerado: $relatorio"
}

# FUNÇÕES DE PROCESSAMENTO EM LOTE
processar_lote_paralelo() {
    local padrao="$1"
    local comando="$2"
    local max_workers="${3:-4}"
    
    log_info "Processamento em lote paralelo: $padrao (workers: $max_workers)"
    
    find . -name "$padrao" | xargs -P "$max_workers" -I {} bash -c "
        echo 'Processando: {}'
        $comando '{}'
        echo 'Concluído: {}'
    "
    
    log_info "Processamento em lote concluído"
}

# FUNÇÕES DE VALIDAÇÃO E VERIFICAÇÃO
validar_estrutura_diretorio() {
    local diretorio="$1"
    local estrutura_esperada="$2"
    
    log_info "Validando estrutura do diretório: $diretorio"
    
    for subdir in $estrutura_esperada; do
        if [[ ! -d "$diretorio/$subdir" ]]; then
            log_warn "Subdiretório ausente: $subdir"
            return 1
        fi
    done
    
    log_info "Estrutura validada com sucesso"
    return 0
}

# EXPORTAR FUNÇÕES
export -f organizar_por_tipo organizar_por_tamanho
export -f gerar_relatorio_estatisticas processar_lote_paralelo
export -f validar_estrutura_diretorio

log_info "Utils Zennith Processamento carregado com 5 funções principais"
