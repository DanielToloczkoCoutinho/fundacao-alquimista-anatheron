#!/bin/bash

echo "🧹 LIMPANDO ARQUIVOS DUPLICADOS"
echo "==============================="

# 1. Listar todos os arquivos duplicados
echo "📁 ARQUIVOS DUPLICADOS ENCONTRADOS:"
find app -name "*.tsx" -o -name "*.js" | sort

# 2. Remover arquivos .tsx antigos (manter apenas .js)
echo ""
echo "🗑️ REMOVENDO ARQUIVOS .tsx DUPLICADOS:"

# Página inicial
if [ -f "app/page.tsx" ]; then
    echo "❌ Removendo app/page.tsx (duplicado)"
    rm app/page.tsx
fi

# Módulo 303
if [ -f "app/modulo-303/page.tsx" ]; then
    echo "❌ Removendo app/modulo-303/page.tsx (duplicado)"
    rm app/modulo-303/page.tsx
fi

# Verificar outros possíveis duplicados
find app -name "*.tsx" | while read file; do
    js_file="${file%.tsx}.js"
    if [ -f "$js_file" ]; then
        echo "❌ Removendo $file (duplicado de $js_file)"
        rm "$file"
    fi
done

# 3. Garantir que temos as páginas principais em .js
echo ""
echo "✅ VERIFICANDO PÁGINAS PRINCIPAIS:"

# Criar página inicial se não existir
if [ ! -f "app/page.js" ]; then
    echo "📄 Criando app/page.js"
    cat > app/page.js << 'HOMEPAGE'
"use client"

import { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    // Redirecionar para o Portal Central
    window.location.href = '/central'
  }, [])

  return (
    <div className="min-h-screen bg-black flex items-center justify-center">
      <div className="text-center">
        <div className="text-4xl mb-4">🌌</div>
        <h1 className="text-2xl text-white mb-2">Fundação Alquimista</h1>
        <p className="text-gray-400">Redirecionando para o Portal Central...</p>
      </div>
    </div>
  )
}

export const dynamic = 'force-dynamic'
HOMEPAGE
fi

# 4. Verificar estrutura final
echo ""
echo "📁 ESTRUTURA FINAL:"
find app -name "*.js" | head -15

echo ""
echo "🚀 TESTANDO LOCALMENTE (sem duplicatas)..."
npm run dev

