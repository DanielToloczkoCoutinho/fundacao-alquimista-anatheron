#!/bin/bash

echo "🔧 CORRIGINDO CONFIGURAÇÕES DO SISTEMA"
echo "======================================"

# 1. Corrigir next.config.js
echo "📄 Corrigindo next.config.js..."
cat > next.config.js << 'NEXT_CONFIG'
/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: { ignoreDuringBuilds: true },
  typescript: { ignoreBuildErrors: true },
  // Configuração correta para pacotes externos
  serverExternalPackages: [],
  // Otimizações
  compress: true,
  poweredByHeader: false,
}

// Bundle analyzer apenas em desenvolvimento
if (process.env.ANALYZE === 'true') {
  const withBundleAnalyzer = require('@next/bundle-analyzer')({
    enabled: true,
  })
  module.exports = withBundleAnalyzer(nextConfig)
} else {
  module.exports = nextConfig
}
NEXT_CONFIG
echo "✅ next.config.js corrigido"

# 2. Corrigir problema do fundo branco no Tailwind
echo "🎨 Verificando Tailwind..."
if [ ! -f "tailwind.config.js" ]; then
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
    },
  },
  plugins: [],
}
TAILWIND_CONFIG
    echo "✅ tailwind.config.js criado"
fi

# 3. Verificar e corrigir problemas nas páginas
echo "🔍 Corrigindo problemas nas páginas..."

# Corrigir Portal Central - remover classes dinâmicas problemáticas
if [ -f "app/central/page.js" ]; then
    echo "🔄 Corrigindo Portal Central..."
    sed -i 's/bg-\$.*-600/bg-purple-600/g' app/central/page.js
    sed -i 's/border-\$.*-500/border-gray-500/g' app/central/page.js
    sed -i 's/text-\$.*-400/text-gray-400/g' app/central/page.js
    echo "✅ Portal Central corrigido"
fi

# 4. Adicionar CSS global para garantir fundo preto
mkdir -p app/styles
cat > app/globals.css << 'GLOBAL_CSS'
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #000000;
  --foreground: #ffffff;
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
  background-color: black !important;
  color: white !important;
}

body {
  background: #000000 !important;
  color: #ffffff !important;
}

/* Garantir que todas as páginas tenham fundo preto */
.min-h-screen {
  background-color: #000000 !important;
}

.bg-black {
  background-color: #000000 !important;
}

/* Animações para indicar dinamismo */
.animate-pulse-slow {
  animation: pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: .7;
  }
}
GLOBAL_CSS

echo "✅ CSS global adicionado"

# 5. Atualizar layout para incluir CSS
cat > app/layout.js << 'LAYOUT_EOF'
import './styles/globals.css'

export const dynamic = 'force-dynamic'

export const metadata = {
  title: 'Fundação Alquimista - Sistema Central',
  description: 'Sistema Central da Fundação Alquimista Cósmica',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-BR" className="bg-black">
      <body className="bg-black text-white antialiased">
        {children}
      </body>
    </html>
  )
}
LAYOUT_EOF

echo "✅ Layout atualizado"

echo ""
echo "🔍 VERIFICANDO CORREÇÕES:"
node -c app/central/page.js && echo "✅ Portal Central - Sintaxe OK"
node -c app/modulo-303/page.js && echo "✅ Módulo 303 - Sintaxe OK" 
node -c app/sistema-vivo/page.js && echo "✅ Sistema Vivo - Sintaxe OK"
node -c next.config.js && echo "✅ Next Config - Sintaxe OK"

