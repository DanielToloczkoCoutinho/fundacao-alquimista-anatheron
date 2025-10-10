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
      const result = await signIn("credentials", { 
        username, 
        password, 
        redirect: false 
      });
      if (result?.error) {
        alert("Senha incorreta! Use: alchemista_2024");
      } else {
        // Redirecionar para dashboard dinâmico
        router.push("/dashboard-dinamico");
      }
    } catch (error) {
      alert("Erro no login!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-black flex items-center justify-center p-4">
      <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20 max-w-md w-full">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-white mb-2">Portal Quântico</h1>
          <p className="text-blue-200">Fundaçao Alquimista</p>
        </div>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-3 bg-white/5 border border-white/20 rounded-lg text-white placeholder-gray-400"
              placeholder="Nome de usuário"
              required
            />
          </div>
          <div>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 bg-white/5 border border-white/20 rounded-lg text-white placeholder-gray-400"
              placeholder="Senha"
              required
            />
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 px-4 rounded-lg font-semibold disabled:opacity-50"
          >
            {loading ? "Entrando..." : "Entrar no Portal"}
          </button>
        </form>
        <div className="mt-4 text-center">
          <p className="text-yellow-200 text-sm">Senha: <code>alchemista_2024</code></p>
        </div>
      </div>
    </div>
  );
}
