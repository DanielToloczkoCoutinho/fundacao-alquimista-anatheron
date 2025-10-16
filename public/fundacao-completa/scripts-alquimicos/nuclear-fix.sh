#!/bin/bash
echo "🚨 SOLUÇÃO NUCLEAR - RECRIANDO TUDO DO ZERO"

# Backup rápido
cp -r src/app src/app-backup-$(date +%s)

# Recriar estrutura mínima
rm -rf src/app
mkdir -p src/app/{auth/signin,dashboard,integration,laboratorios,api/auth/[...nextauth]}
mkdir -p src/components
mkdir -p src/lib

# Criar arquivos essenciais
cat > src/app/providers.tsx << 'PROV'
"use client";
import { SessionProvider } from "next-auth/react";
export function AuthProvider({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}
PROV

cat > src/app/layout.tsx << 'LAYOUT'
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AuthProvider } from "./providers";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Fundação Alquimista",
  description: "Sistema Quântico Unificado",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <AuthProvider>
          <nav className="bg-black/50 p-4 border-b border-white/20">
            <div className="max-w-7xl mx-auto flex space-x-4">
              <a href="/" className="text-white hover:text-blue-300">🏠 Home</a>
              <a href="/auth/signin" className="text-white hover:text-blue-300">🔐 Login</a>
            </div>
          </nav>
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}
LAYOUT

cat > src/app/page.tsx << 'HOME'
export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black flex items-center justify-center">
      <div className="text-center text-white">
        <h1 className="text-6xl font-bold mb-6">🌌 Fundação Alquimista</h1>
        <p className="text-xl mb-8">Sistema Quântico Multidimensional</p>
        <a href="/auth/signin" className="bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-lg text-lg">
          🔐 Entrar no Portal
        </a>
      </div>
    </div>
  );
}
HOME

echo "✅ Estrutura mínima recriada. Fazendo build..."
npm run build
