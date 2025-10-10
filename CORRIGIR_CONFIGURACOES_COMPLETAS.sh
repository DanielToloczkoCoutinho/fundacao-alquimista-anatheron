#!/bin/bash

echo "🛠️ CORREÇÃO COMPLETA DAS CONFIGURAÇÕES"
echo "======================================"

# 1. Corrigir next.config.js para remover alertas
echo "📄 Corrigindo next.config.js..."
cat > next.config.js << 'NEXT_CONFIG'
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Habilitar verificações que estavam sendo puladas
  eslint: {
    ignoreDuringBuilds: false, // Agora vai verificar ESLint
  },
  typescript: {
    ignoreBuildErrors: false, // Agora vai verificar TypeScript
  },
  // Configurações otimizadas
  compress: true,
  poweredByHeader: false,
  // Remover a configuração de builds que causa o alerta do Vercel
}

module.exports = nextConfig
NEXT_CONFIG
echo "✅ next.config.js corrigido - verificações habilitadas"

# 2. Configurar ESLint corretamente
echo "🔍 Configurando ESLint..."
if [ ! -f ".eslintrc.json" ]; then
    cat > .eslintrc.json << 'ESLINT_CONFIG'
{
  "extends": "next/core-web-vitals",
  "rules": {
    "react-hooks/exhaustive-deps": "warn",
    "react/no-unescaped-entities": "off"
  }
}
ESLINT_CONFIG
    echo "✅ .eslintrc.json criado"
fi

# 3. Configurar TypeScript corretamente
echo "📝 Verificando TypeScript..."
if [ -f "tsconfig.json" ]; then
    echo "✅ tsconfig.json existe"
    # Garantir que as verificações estão habilitadas
    if grep -q "skipLibCheck" tsconfig.json; then
        echo "🔧 Ajustando tsconfig.json..."
        sed -i 's/"skipLibCheck": true/"skipLibCheck": false/' tsconfig.json 2>/dev/null || echo "⚠️ Não foi possível ajustar automaticamente"
    fi
else
    echo "📝 Criando tsconfig.json básico..."
    cat > tsconfig.json << 'TSCONFIG'
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "es6"],
    "allowJs": true,
    "skipLibCheck": false,
    "strict": false,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
TSCONFIG
    echo "✅ tsconfig.json criado"
fi

# 4. Remover vercel.json problemático que causa o alerta
echo "🗑️ Removendo vercel.json problemático..."
if [ -f "vercel.json" ]; then
    rm vercel.json
    echo "✅ vercel.json removido - alerta do Vercel será resolvido"
else
    echo "✅ vercel.json não existe"
fi

# 5. Criar arquivos de ambiente básicos
echo "🌐 Criando arquivos de ambiente..."
if [ ! -f ".env.local" ]; then
    cat > .env.local << 'ENV_FILE'
# Configurações de ambiente
NEXT_PUBLIC_APP_URL=https://fundacao-alquimista-anatheron.vercel.app
NEXT_PUBLIC_SYSTEM_STATUS=operational
ENV_FILE
    echo "✅ .env.local criado"
fi

# 6. Instalar dependências de desenvolvimento se necessário
echo "📦 Verificando dependências..."
if ! npm list eslint 2>/dev/null | grep -q "eslint"; then
    echo "🔧 Instalando ESLint..."
    npm install -D eslint eslint-config-next
fi

if ! npm list typescript 2>/dev/null | grep -q "typescript"; then
    echo "🔧 Instalando TypeScript..."
    npm install -D typescript @types/react @types/node
fi

echo ""
echo "🧪 TESTANDO CONFIGURAÇÕES CORRIGIDAS..."
npm run build

