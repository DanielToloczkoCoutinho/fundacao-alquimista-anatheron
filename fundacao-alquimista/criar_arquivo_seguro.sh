#!/bin/bash

echo "🛡️  CRIADOR DE ARQUIVOS SEGURO - SEMPRE VERIFICA DIRETÓRIOS"
echo "=========================================================="

# Função para criar arquivo com verificação
criar_arquivo_seguro() {
    local arquivo="$1"
    local conteudo="$2"
    
    echo "📁 Verificando: $arquivo"
    
    # Extrair diretório do arquivo
    local diretorio=$(dirname "$arquivo")
    
    # Criar diretório se não existir
    if [ ! -d "$diretorio" ]; then
        echo "📂 Criando diretório: $diretorio"
        mkdir -p "$diretorio"
        
        if [ $? -eq 0 ]; then
            echo "✅ Diretório criado: $diretorio"
        else
            echo "❌ ERRO: Não foi possível criar $diretorio"
            return 1
        fi
    else
        echo "✅ Diretório existe: $diretorio"
    fi
    
    # Criar arquivo
    echo "📄 Criando arquivo: $arquivo"
    echo "$conteudo" > "$arquivo"
    
    if [ $? -eq 0 ]; then
        echo "�� ARQUIVO CRIADO COM SUCESSO: $arquivo"
        return 0
    else
        echo "❌ ERRO: Não foi possível criar $arquivo"
        return 1
    fi
}

# Exemplo de uso:
echo "🎯 EXEMPLOS DE USO:"
echo "criar_arquivo_seguro \"caminho/para/arquivo.txt\" \"conteúdo do arquivo\""
echo ""

# Criar alguns arquivos de exemplo
echo "📝 CRIANDO ARQUIVOS DE EXEMPLO..."

# 1. package.json básico
criar_arquivo_seguro "package.json" '{
  "name": "fundacao-alquimista-nucleo",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "next dev",
    "build": "next build", 
    "start": "next start"
  },
  "dependencies": {
    "next": "14.0.0",
    "react": "18.0.0",
    "react-dom": "18.0.0"
  }
}'

# 2. next.config.js
criar_arquivo_seguro "next.config.js" '/** @type {import('"'"'next'"'"').NextConfig} */
const nextConfig = {
  output: '"'"'export'"'"',
  trailingSlash: true
}

module.exports = nextConfig'

# 3. Página simples
criar_arquivo_seguro "app/page.jsx" 'export default function Home() {
  return (
    <div style={{padding: "40px"}}>
      <h1>🌌 Fundação Alquimista</h1>
      <p>Núcleo deployável funcionando!</p>
    </div>
  )
}'

echo ""
echo "🎉 SCRIPT UNIVERSAL PRONTO! 🌟"
echo "💡 Use: criar_arquivo_seguro \"caminho/arquivo\" \"conteúdo\""
