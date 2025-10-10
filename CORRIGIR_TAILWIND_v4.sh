#!/bin/bash

echo "🚀 CORRIGINDO CONFIGURAÇÃO TAILWIND CSS v4"
echo "=========================================="

# 1. Remover configurações antigas
echo ""
echo "🧹 REMOVENDO CONFIGURAÇÕES ANTIGAS..."
rm -f postcss.config.js
rm -f tailwind.config.js

# 2. Instalar versão compatível do Tailwind CSS
echo ""
echo "📦 INSTALANDO TAILWIND CSS v3 (COMPATÍVEL)..."
npm uninstall tailwindcss
npm install -D tailwindcss@^3.3.0

# 3. Inicializar Tailwind CSS corretamente
echo ""
echo "⚙️ INICIALIZANDO TAILWIND CSS v3..."
npx tailwindcss init -p

# 4. Verificar instalação
echo ""
echo "✅ VERIFICANDO INSTALAÇÃO:"
npm list tailwindcss

# 5. Atualizar configuração do Tailwind
echo ""
echo "🔧 CONFIGURANDO TAILWIND CSS v3..."
cat > tailwind.config.js << 'TAILWIND3'
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
TAILWIND3

# 6. Verificar PostCSS config
echo ""
echo "🎨 VERIFICANDO POSTCSS CONFIG..."
cat > postcss.config.js << 'POSTCSS3'
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
POSTCSS3

# 7. Garantir que globals.css está correto
echo ""
echo "🌐 ATUALIZANDO GLOBALS.CSS..."
cat > app/globals.css << 'GLOBALS3'
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
GLOBALS3

echo ""
echo "🧪 TESTANDO BUILD COM TAILWIND v3..."
npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCESSO! Tailwind CSS v3 configurado corretamente."
    echo ""
    echo "🚀 FAZENDO DEPLOY DEFINITIVO..."
    npx vercel --prod --force
else
    echo ""
    echo "❌ Ainda há erros. Tentando solução alternativa..."
    npm run build 2>&1 | tail -10
fi

