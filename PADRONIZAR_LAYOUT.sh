#!/bin/bash

echo "🎨 PADRONIZANDO LAYOUT EM TODAS AS PÁGINAS"
echo "=========================================="

# 1. Garantir que o layout principal está correto
cat > app/layout.js << 'MAIN_LAYOUT'
import './globals.css'

export const metadata = {
  title: 'Fundação Alquimista - Nexus Central',
  description: 'Sistema Interdimensional de Monitoramento Quântico',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR">
      <body className="bg-black text-white min-h-screen">
        <main className="min-h-screen">
          {children}
        </main>
      </body>
    </html>
  )
}
MAIN_LAYOUT

# 2. Garantir globals.css com Tailwind
cat > app/globals.css << 'GLOBALS_CSS'
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

/* Animações customizadas */
@keyframes pulse-glow {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.animate-pulse-glow {
  animation: pulse-glow 2s ease-in-out infinite;
}
GLOBALS_CSS

# 3. Verificar configuração do Tailwind
cat > tailwind.config.js << 'TAILWIND_CONFIG'
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
      animation: {
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
      }
    },
  },
  plugins: [],
}
TAILWIND_CONFIG

echo "✅ Layout padronizado aplicado!"

# 4. Teste rápido
echo ""
echo "🧪 TESTANDO CONFIGURAÇÃO..."
npm run build

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCESSO! Sistema pronto para deploy."
    echo ""
    echo "🚀 FAZENDO DEPLOY FINAL..."
    npx vercel --prod --force
else
    echo "❌ Erro no build. Verificando..."
    npm run build 2>&1 | grep -i error
fi

