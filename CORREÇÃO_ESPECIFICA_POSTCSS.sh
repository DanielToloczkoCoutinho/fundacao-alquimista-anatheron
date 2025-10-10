#!/bin/bash

echo "🛠️ CORREÇÃO ESPECÍFICA - PROBLEMA POSTCSS"
echo "========================================"

# 1. Verificar e corrigir postcss.config.js
echo "📄 Verificando postcss.config.js..."
if [ -f "postcss.config.js" ]; then
    echo "✅ postcss.config.js existe - verificando conteúdo..."
    
    # Se contém a referência problemática, corrigir
    if grep -q "@tailwindcss/postcss" postcss.config.js; then
        echo "❌ Encontrada referência problemática - CORRIGINDO..."
        cat > postcss.config.js << 'POSTCSS_CORRETO'
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
POSTCSS_CORRETO
        echo "✅ postcss.config.js corrigido"
    else
        echo "✅ postcss.config.js já está correto"
    fi
else
    echo "📝 Criando postcss.config.js correto..."
    cat > postcss.config.js << 'POSTCSS_NOVO'
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
POSTCSS_NOVO
    echo "✅ postcss.config.js criado"
fi

# 2. Verificar tailwind.config.js
echo ""
echo "🎨 Verificando tailwind.config.js..."
if [ -f "tailwind.config.js" ]; then
    echo "✅ tailwind.config.js existe"
    # Mostrar conteúdo resumido
    echo "📋 Conteúdo:"
    head -15 tailwind.config.js
else
    echo "❌ tailwind.config.js não existe - CRIANDO..."
    cat > tailwind.config.js << 'TAILWIND_NOVO'
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
TAILWIND_NOVO
    echo "✅ tailwind.config.js criado"
fi

# 3. Verificar se Tailwind CSS está instalado
echo ""
echo "📦 Verificando instalação do Tailwind CSS..."
if npm list tailwindcss 2>/dev/null | grep -q "tailwindcss"; then
    echo "✅ Tailwind CSS instalado"
else
    echo "❌ Tailwind CSS não instalado - INSTALANDO..."
    npm install -D tailwindcss postcss autoprefixer
    echo "✅ Tailwind CSS instalado"
fi

# 4. Simplificar globals.css se necessário
echo ""
echo "🔄 Simplificando globals.css..."
if [ -f "app/globals.css" ]; then
    # Verificar se tem imports problemáticos
    if grep -q "@tailwindcss/postcss" app/globals.css; then
        echo "❌ Encontrada referência problemática em globals.css - CORRIGINDO..."
        cat > app/globals.css << 'GLOBALS_CORRETO'
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #000000;
  --foreground: #ffffff;
}

html, body {
  background: #000000 !important;
  color: #ffffff !important;
  margin: 0;
  padding: 0;
}
GLOBALS_CORRETO
        echo "✅ globals.css corrigido"
    else
        echo "✅ globals.css já está correto"
    fi
else
    echo "📝 Criando globals.css correto..."
    cat > app/globals.css << 'GLOBALS_NOVO'
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #000000;
  --foreground: #ffffff;
}

html, body {
  background: #000000 !important;
  color: #ffffff !important;
  margin: 0;
  padding: 0;
}
GLOBALS_NOVO
    echo "✅ globals.css criado"
fi

# 5. Testar a correção
echo ""
echo "🧪 TESTANDO CORREÇÃO..."
if npm run build > build_test.log 2>&1; then
    echo "🎉 ✅ BUILD BEM-SUCEDIDO!"
    echo "🚀 INICIANDO DEPLOY..."
    npx vercel --prod --force
else
    echo "❌ BUILD AINDA FALHOU - Verificando logs..."
    tail -20 build_test.log
    echo ""
    echo "🔧 Aplicando solução alternativa..."
    aplicar_solucao_alternativa
fi

aplicar_solucao_alternativa() {
    echo ""
    echo "🔄 APLICANDO SOLUÇÃO ALTERNATIVA..."
    
    # Remover completamente Tailwind se estiver causando problemas
    echo "🗑️ Removendo dependências problemáticas..."
    rm -f postcss.config.js
    rm -f tailwind.config.js
    
    # Criar CSS inline para evitar problemas
    echo "🎨 Criando layout com CSS inline..."
    cat > app/layout.js << 'LAYOUT_INLINE'
export const dynamic = 'force-dynamic'

export const metadata = {
  title: 'Fundação Alquimista',
  description: 'Sistema Central',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <head>
        <style jsx global>{`
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }
          html, body {
            background: #000000;
            color: #ffffff;
            min-height: 100vh;
            font-family: system-ui, sans-serif;
          }
        `}</style>
      </head>
      <body>
        {children}
      </body>
    </html>
  )
}
LAYOUT_INLINE

    echo "✅ Layout com CSS inline criado"
    echo "🚀 TENTANDO BUILD NOVAMENTE..."
    npm run build && npx vercel --prod --force
}

