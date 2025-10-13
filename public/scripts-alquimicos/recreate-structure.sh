#!/bin/bash
echo "🔄 RECRIANDO ESTRUTURA DO ZERO..."

# Backup
cp -r src src-backup-$(date +%s)

# Recriar estrutura mínima
rm -rf src
mkdir -p src/app/{auth/signin,dashboard,integration,laboratorios,api/auth/[...nextauth]}
mkdir -p src/components
mkdir -p src/lib

# Recriar arquivos críticos
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

cat > src/app/providers.tsx << 'PROV'
"use client";
import { SessionProvider } from "next-auth/react";
export function AuthProvider({ children }: { children: React.ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}
PROV

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

# Recriar auth
cat > src/app/auth/signin/page.tsx << 'SIGNIN'
"use client";
import { signIn } from "next-auth/react";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function SignIn() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const result = await signIn("credentials", { username, password, redirect: false });
      if (result?.error) alert("Senha: alchemista_2024");
      else router.push("/dashboard");
    } catch (error) {
      alert("Erro no login!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black flex items-center justify-center">
      <div className="bg-white/10 p-8 rounded-2xl border border-white/20 max-w-md w-full">
        <h1 className="text-3xl font-bold text-white text-center mb-6">🔐 Login</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input type="text" placeholder="Usuário" value={username} onChange={(e) => setUsername(e.target.value)} 
            className="w-full p-3 bg-white/5 border border-white/20 rounded-lg text-white" required />
          <input type="password" placeholder="Senha" value={password} onChange={(e) => setPassword(e.target.value)}
            className="w-full p-3 bg-white/5 border border-white/20 rounded-lg text-white" required />
          <button type="submit" disabled={loading} 
            className="w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-lg disabled:opacity-50">
            {loading ? "Entrando..." : "Entrar"}
          </button>
        </form>
      </div>
    </div>
  );
}
SIGNIN

echo "✅ Estrutura recriada!"
