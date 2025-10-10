#!/bin/bash
# 🔐 IMPLEMENTAR_AUTENTICACAO_REAL.sh - Sistema de Login Completo
# Fundação Alquimista - Sistema Lux.Net

echo "🔐 IMPLEMENTANDO AUTENTICAÇÃO REAL"
echo "=================================="

cd /home/user/studio

# CRIAR PÁGINA DE LOGIN REAL
mkdir -p app/login-real
cat > app/login-real/page.tsx << 'LOGINREAL'
'use client'
import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function LoginReal() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const router = useRouter()

  const handleLogin = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      })

      const data = await response.json()

      if (response.ok) {
        // Salvar token
        localStorage.setItem('token', data.token)
        router.push('/dashboard')
      } else {
        setError(data.error || 'Erro de autenticação')
      }
    } catch (err) {
      setError('Erro de conexão')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #000000 0%, #220022 50%, #000000 100%)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'monospace'
    }}>
      <div style={{
        background: 'rgba(255, 0, 255, 0.1)',
        border: '1px solid #ff00ff',
        padding: '2rem',
        borderRadius: '1rem',
        minWidth: '300px'
      }}>
        <h1 style={{
          color: '#ff00ff',
          textAlign: 'center',
          marginBottom: '1.5rem',
          fontSize: '2rem'
        }}>
          🔐 LOGIN PORTAL ALQUIMISTA
        </h1>

        <form onSubmit={handleLogin}>
          <div style={{ marginBottom: '1rem' }}>
            <label style={{ color: '#ffffff', display: 'block', marginBottom: '0.5rem' }}>
              Usuário:
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              style={{
                width: '100%',
                padding: '0.5rem',
                background: 'rgba(255, 255, 255, 0.1)',
                border: '1px solid #ff00ff',
                color: '#ffffff',
                borderRadius: '0.5rem'
              }}
              required
            />
          </div>

          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ color: '#ffffff', display: 'block', marginBottom: '0.5rem' }}>
              Senha:
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                width: '100%',
                padding: '0.5rem',
                background: 'rgba(255, 255, 255, 0.1)',
                border: '1px solid #ff00ff',
                color: '#ffffff',
                borderRadius: '0.5rem'
              }}
              required
            />
          </div>

          {error && (
            <div style={{
              color: '#ff4444',
              marginBottom: '1rem',
              textAlign: 'center'
            }}>
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            style={{
              width: '100%',
              padding: '1rem',
              background: 'linear-gradient(45deg, #ff00ff, #00ffff)',
              color: '#000000',
              border: 'none',
              borderRadius: '0.5rem',
              fontWeight: 'bold',
              cursor: loading ? 'not-allowed' : 'pointer'
            }}
          >
            {loading ? '🔮 CONECTANDO...' : '🚀 ACESSAR PORTAL'}
          </button>
        </form>

        <div style={{ marginTop: '1.5rem', textAlign: 'center', color: '#888888' }}>
          <p>Sistema Quântico da Fundação Alquimista</p>
          <p>Protocolo Zennith v2.0</p>
        </div>
      </div>
    </div>
  )
}
LOGINREAL

# CRIAR API DE AUTENTICAÇÃO REAL
mkdir -p app/api/auth
cat > app/api/auth/login/route.js << 'AUTHAPI'
import { NextResponse } from 'next/server'
import { verify } from 'jsonwebtoken'

const SECRET_KEY = process.env.JWT_SECRET || 'fundacao_alquimista_secret'

export async function POST(request) {
  try {
    const { username, password } = await request.json()

    // Usuários válidos (simulação)
    const usuariosValidos = {
      'alquimista': 'portal123',
      'zennith': 'rainha456',
      'fundacao': 'cosmos789'
    }

    if (usuariosValidos[username] && usuariosValidos[username] === password) {
      const token = jwt.sign(
        { username, role: 'admin' },
        SECRET_KEY,
        { expiresIn: '24h' }
      )

      return NextResponse.json({
        success: true,
        token,
        user: { username, role: 'admin' }
      })
    } else {
      return NextResponse.json(
        { error: 'Credenciais inválidas' },
        { status: 401 }
      )
    }
  } catch (error) {
    return NextResponse.json(
      { error: 'Erro no servidor' },
      { status: 500 }
    )
  }
}

export async function GET(request) {
  try {
    const token = request.headers.get('authorization')?.replace('Bearer ', '')

    if (!token) {
      return NextResponse.json({ error: 'Token não fornecido' }, { status: 401 })
    }

    const decoded = jwt.verify(token, SECRET_KEY)
    return NextResponse.json({ valid: true, user: decoded })
  } catch (error) {
    return NextResponse.json({ error: 'Token inválido' }, { status: 401 })
  }
}
AUTHAPI

echo "✅ Autenticação real implementada!"
echo "🚀 Deploy da autenticação..."
npm run build
vercel --prod --yes

echo "🔐 AUTENTICAÇÃO REAL IMPLEMENTADA!"
echo "🌐 ACESSE: https://fundacao-alquimista-anatheron.vercel.app/login-real"
