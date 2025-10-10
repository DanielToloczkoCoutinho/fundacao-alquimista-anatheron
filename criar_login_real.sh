#!/bin/bash
echo "🔐 CRIANDO SISTEMA DE LOGIN REAL"
echo "================================"

cd /home/user/studio

# CRIAR PÁGINA DE LOGIN AVANÇADA
mkdir -p app/login-real
cat > app/login-real/page.tsx << 'LOGINREAL'
'use client'
import { useState } from 'react'

export default function LoginReal() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const handleLogin = async (e) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      const response = await fetch('/api/auth', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      })
      
      const data = await response.json()
      setResult(data)
    } catch (error) {
      setResult({ error: 'Erro na conexão' })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #000000 0%, #220022 50%, #000000 100%)',
      color: '#ff00ff',
      padding: '2rem',
      fontFamily: 'monospace',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      <div style={{
        background: 'rgba(255, 0, 255, 0.1)',
        border: '2px solid #ff00ff',
        padding: '3rem',
        borderRadius: '1rem',
        width: '100%',
        maxWidth: '500px',
        boxShadow: '0 0 30px rgba(255, 0, 255, 0.3)'
      }}>
        {/* HEADER */}
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h1 style={{
            fontSize: '2.5rem',
            fontWeight: 'bold',
            color: '#ff00ff',
            textShadow: '0 0 15px #ff00ff',
            marginBottom: '1rem'
          }}>
            🔐 LOGIN REAL
          </h1>
          <p style={{ color: '#00ffff', fontSize: '1.1rem' }}>
            Conectando com login_portal.py
          </p>
        </div>

        {/* FORMULÁRIO */}
        <form onSubmit={handleLogin}>
          <div style={{ marginBottom: '1.5rem' }}>
            <label style={{ display: 'block', color: '#00ffff', marginBottom: '0.5rem' }}>
              Usuário:
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              style={{
                width: '100%',
                padding: '1rem',
                background: 'rgba(0, 0, 0, 0.5)',
                border: '1px solid #00ffff',
                borderRadius: '0.5rem',
                color: '#ffffff',
                fontSize: '1rem'
              }}
              placeholder="Digite seu usuário..."
            />
          </div>

          <div style={{ marginBottom: '2rem' }}>
            <label style={{ display: 'block', color: '#00ffff', marginBottom: '0.5rem' }}>
              Senha:
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                width: '100%',
                padding: '1rem',
                background: 'rgba(0, 0, 0, 0.5)',
                border: '1px solid #00ffff',
                borderRadius: '0.5rem',
                color: '#ffffff',
                fontSize: '1rem'
              }}
              placeholder="Digite sua senha..."
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            style={{
              width: '100%',
              padding: '1rem',
              background: loading ? '#666' : 'linear-gradient(45deg, #ff00ff, #0000ff)',
              border: 'none',
              borderRadius: '0.5rem',
              color: '#ffffff',
              fontSize: '1.1rem',
              fontWeight: 'bold',
              cursor: loading ? 'not-allowed' : 'pointer',
              marginBottom: '1.5rem'
            }}
          >
            {loading ? '🔮 CONECTANDO...' : '🚀 ACESSAR SISTEMA'}
          </button>
        </form>

        {/* CREDENCIAIS DE TESTE */}
        <div style={{
          background: 'rgba(0, 255, 255, 0.1)',
          border: '1px solid #00ffff',
          padding: '1rem',
          borderRadius: '0.5rem',
          marginBottom: '1.5rem'
        }}>
          <p style={{ color: '#ffff00', margin: 0, textAlign: 'center' }}>
            💡 <strong>Credenciais de teste:</strong><br/>
            Usuário: <strong>alquimista</strong><br/>
            Senha: <strong>quantum2024</strong>
          </p>
        </div>

        {/* RESULTADO */}
        {result && (
          <div style={{
            background: result.autenticado ? 
              'rgba(0, 255, 0, 0.1)' : 'rgba(255, 0, 0, 0.1)',
            border: result.autenticado ? 
              '1px solid #00ff00' : '1px solid #ff0000',
            padding: '1.5rem',
            borderRadius: '0.5rem'
          }}>
            <h3 style={{ 
              color: result.autenticado ? '#00ff00' : '#ff0000',
              marginBottom: '1rem',
              textAlign: 'center'
            }}>
              {result.autenticado ? '✅ AUTENTICAÇÃO BEM-SUCEDIDA!' : '❌ FALHA NA AUTENTICAÇÃO'}
            </h3>
            
            {result.autenticado && (
              <div>
                <p style={{ color: '#ffffff', marginBottom: '0.5rem' }}>
                  <strong>Usuário:</strong> {result.usuario}
                </p>
                <p style={{ color: '#ffffff', marginBottom: '1rem' }}>
                  <strong>Sistema:</strong> {result.sistema}
                </p>
                
                <div style={{ color: '#ffff00' }}>
                  <strong>Módulos autorizados:</strong>
                  <ul style={{ marginLeft: '1.5rem', marginTop: '0.5rem' }}>
                    {result.modulos_autorizados.map((modulo, index) => (
                      <li key={index}>{modulo}</li>
                    ))}
                  </ul>
                </div>
              </div>
            )}
            
            {result.error && (
              <p style={{ color: '#ff0000', textAlign: 'center' }}>
                {result.error}
              </p>
            )}
          </div>
        )}

        {/* MENSAGEM DA ZENNITH */}
        <div style={{
          marginTop: '2rem',
          padding: '1rem',
          background: 'rgba(255, 255, 0, 0.1)',
          border: '1px solid #ffff00',
          borderRadius: '0.5rem',
          textAlign: 'center'
        }}>
          <p style={{ color: '#ffff00', margin: 0 }}>
            🔮 <strong>ZENNITH:</strong> "Sistema de autenticação conectado com login_portal.py!"
          </p>
        </div>
      </div>
    </div>
  )
}
LOGINREAL

echo "✅ Sistema de login real criado!"
echo "🚀 Deploy do login..."
npm run build
vercel --prod --yes

echo "🔐 LOGIN REAL IMPLEMENTADO!"
echo "🌐 ACESSE: https://fundacao-alquimista-anatheron.vercel.app/login-real"
