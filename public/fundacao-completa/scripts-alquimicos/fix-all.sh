#!/bin/bash
echo "🔧 INICIANDO CORREÇÃO TOTAL DO SISTEMA..."

# 1. Garantir estrutura de pastas
mkdir -p src/app/{auth/signin,dashboard,integration,laboratorios,bibliotecas,zennith}
mkdir -p src/components
mkdir -p src/lib

# 2. Criar arquivos críticos se não existirem
[ ! -f "src/app/providers.tsx" ] && cat > src/app/providers.tsx << PROVIDERS
"use client";
import { SessionProvider } from "next-auth/react";
export function AuthProvider({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}
PROVIDERS

[ ! -f "src/components/NavigationPortal.tsx" ] && cat > src/components/NavigationPortal.tsx << NAV
'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
export default function NavigationPortal() {
  const pathname = usePathname();
  return (
    <nav className="bg-black/50 backdrop-blur-lg border-b border-white/20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex space-x-4">
          <Link href="/" className="text-white hover:text-blue-300">🏠 Home</Link>
          <Link href="/auth/signin" className="text-white hover:text-blue-300">🔐 Login</Link>
          <Link href="/integration" className="text-white hover:text-blue-300">🔬 Integração</Link>
          <Link href="/laboratorios" className="text-white hover:text-blue-300">🧪 Labs</Link>
        </div>
      </div>
    </nav>
  );
}
NAV

# 3. Build e deploy
npm run build && echo "✅ BUILD SUCESSO!" || echo "❌ BUILD FALHOU"
