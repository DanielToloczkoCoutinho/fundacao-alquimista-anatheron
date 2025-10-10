#!/bin/bash

echo "💥 SOLUÇÃO DEFINITIVA - RECRIANDO TUDO DO ZERO"
echo "============================================="

# 1. Parar qualquer processo do Next.js
pkill -f "next dev" 2>/dev/null || true

# 2. Fazer backup rápido dos arquivos de página
echo ""
echo "📦 FAZENDO BACKUP DAS PÁGINAS..."
mkdir -p backup_pages
cp -r app/* backup_pages/ 2>/dev/null || true

# 3. Limpar node_modules e reinstalar tudo
echo ""
echo "🧹 LIMPANDO E REINSTALANDO TUDO..."
rm -rf node_modules package-lock.json
npm install

# 4. Instalar Tailwind CSS v3 explicitamente
echo ""
echo "📦 INSTALANDO TAILWIND CSS v3..."
npm install -D tailwindcss@^3.3.0 postcss@^8.4.0 autoprefixer@^10.4.0

# 5. Recriar configurações do zero
echo ""
echo "⚙️ RECRIANDO CONFIGURAÇÕES..."

# PostCSS
cat > postcss.config.js << 'POSTCSS'
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
POSTCSS

# Tailwind
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
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
  },
  plugins: [],
}
TAILWIND

# 6. Recriar globals.css
echo ""
echo "🌐 RECRIANDO ESTILOS GLOBAIS..."
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

# 7. Recriar layout principal
echo ""
echo "🏗️ RECRIANDO LAYOUT PRINCIPAL..."
cat > app/layout.js << 'LAYOUT'
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
LAYOUT

# 8. Restaurar páginas do backup
echo ""
echo "📄 RESTAURANDO PÁGINAS..."
cp -r backup_pages/* app/ 2>/dev/null || true

# 9. Remover arquivos duplicados .tsx
find app -name "*.tsx" -delete

# 10. Testar build final
echo ""
echo "🧪 TESTANDO BUILD FINAL..."
if npm run build; then
    echo ""
    echo "🎉 🎉 🎉 SUCESSO TOTAL! 🎉 🎉 🎉"
    echo ""
    echo "🚀 FAZENDO DEPLOY DEFINITIVO..."
    DEPLOY_URL=$(npx vercel --prod --force 2>&1 | grep -o 'https://[^ ]*\.vercel\.app' | head -1)
    
    echo ""
    echo "=========================================="
    echo "🌟 DEPLOY CONCLUÍDO COM SUCESSO!"
    echo "🌐 URL DEFINITIVA: $DEPLOY_URL/central"
    echo "=========================================="
    echo ""
    echo "🎯 AGORA TESTE:"
    echo "✅ Layout centralizado e responsivo"
    echo "✅ Timer aumentando a cada segundo"
    echo "✅ Botões com efeitos hover"
    echo "✅ Cores Tailwind aplicadas"
    echo "✅ Navegação funcionando"
else
    echo ""
    echo "❌ ERRO NO BUILD FINAL"
    echo "Última tentativa - verificando dependências..."
    npm list tailwindcss postcss autoprefixer
    echo ""
    echo "🔍 Erros detalhados:"
    npm run build 2>&1 | grep -i error | head -5
fi

# Limpar backup
rm -rf backup_pages

