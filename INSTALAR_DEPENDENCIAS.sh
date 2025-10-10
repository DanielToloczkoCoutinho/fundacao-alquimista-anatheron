#!/bin/bash

echo "📦 INSTALANDO DEPENDÊNCIAS FALTANTES"
echo "==================================="

# 1. Verificar dependências atuais
echo ""
echo "📋 DEPENDÊNCIAS ATUAIS:"
npm list tailwindcss postcss autoprefixer 2>/dev/null || echo "❌ Não instaladas"

# 2. Instalar Tailwind CSS e dependências
echo ""
echo "🚀 INSTALANDO TAILWINDCSS..."
npm install -D tailwindcss postcss autoprefixer

# 3. Verificar se foi instalado corretamente
echo ""
echo "✅ VERIFICANDO INSTALAÇÃO:"
npm list tailwindcss postcss autoprefixer

# 4. Inicializar Tailwind se necessário
if [ ! -f "tailwind.config.js" ]; then
    echo ""
    echo "⚙️ INICIALIZANDO TAILWINDCSS..."
    npx tailwindcss init -p
fi

# 5. Verificar configuração do PostCSS
if [ ! -f "postcss.config.js" ]; then
    echo ""
    echo "🎨 CRIANDO CONFIGURAÇÃO POSTCSS..."
    cat > postcss.config.js << 'POSTCSS'
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
POSTCSS
fi

# 6. Atualizar configuração do Tailwind
echo ""
echo "🔧 ATUALIZANDO CONFIGURAÇÃO TAILWIND..."
cat > tailwind.config.js << 'TAILWIND'
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        background: 'var(--background)',
        foreground: 'var(--foreground)',
      },
    },
  },
  plugins: [],
}
TAILWIND

# 7. Verificar se o globals.css está correto
echo ""
echo "🌐 VERIFICANDO GLOBALS.CSS..."
cat > app/globals.css << 'GLOBALS'
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 255, 255, 255;
  --background-start-rgb: 0, 0, 0;
  --background-end-rgb: 0, 0, 0;
}

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

html,
body {
  max-width: 100vw;
  overflow-x: hidden;
  background: black;
  color: white;
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
}

a {
  color: inherit;
  text-decoration: none;
}
GLOBALS

echo ""
echo "🧪 TESTANDO BUILD APÓS INSTALAÇÃO..."
npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCESSO! Tailwind CSS instalado e configurado."
    echo ""
    echo "🚀 FAZENDO DEPLOY DEFINITIVO..."
    npx vercel --prod --force
else
    echo ""
    echo "❌ Ainda há erros. Verificando detalhes..."
    npm run build 2>&1 | grep -i error
fi

