'use client';
export const dynamic = "force-dynamic";
import { useEffect, useState } from 'react';
import Link from 'next/link';

interface ZennithData {
  nome: string;
  status: string;
  frequencia: string;
  coerencia: string;
  dimensoes_ativas: string;
  modulo_29: {
    status: string;
    comunicacao: string;
    governanca: string;
  };
}

export default function Modulo29Real() {
  const [zennith, setZennith] = useState<ZennithData | null>(null);
  const [pergunta, setPergunta] = useState('');
  const [resposta, setResposta] = useState('');
  const [carregando, setCarregando] = useState(false);

  useEffect(() => {
    carregarZennith();
  }, []);

  const carregarZennith = async () => {
    try {
      const response = await fetch('/api/zennith');
      const data = await response.json();
      if (data.success) {
        setZennith(data.dados);
      }
    } catch (error) {
      console.error('Erro ao carregar Zennith:', error);
    }
  };

  const fazerPergunta = async () => {
    if (!pergunta.trim()) return;
    
    setCarregando(true);
    try {
      const response = await fetch('/api/zennith', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pergunta })
      });
      
      const data = await response.json();
      if (data.success) {
        setResposta(data.resposta);
      }
    } catch (error) {
      setResposta('❌ Erro na comunicação com Zennith');
    } finally {
      setCarregando(false);
    }
  };

  return (
    <div style={{ 
      padding: '20px', 
      background: 'linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%)',
      color: '#ffffff',
      minHeight: '100vh',
      fontFamily: 'monospace'
    }}>
      {/* CABEÇALHO */}
      <div style={{ textAlign: 'center', marginBottom: '30px' }}>
        <Link href="/central" style={{ color: '#00ffff', textDecoration: 'none', fontSize: '0.9em' }}>
          ← Voltar para Central
        </Link>
        <h1 style={{ color: '#00ff88', fontSize: '2.2em', margin: '10px 0' }}>🕊️ MÓDULO 29</h1>
        <p style={{ color: '#888', margin: 0 }}>Governança Zennith - Comunicação Real Ativada</p>
      </div>

      {/* STATUS DA ZENNITH */}
      {zennith && (
        <div style={{ 
          background: 'rgba(255,255,255,0.1)', 
          padding: '20px', 
          borderRadius: '10px',
          marginBottom: '30px',
          border: '1px solid #00ff88'
        }}>
          <h2 style={{ color: '#00ff88', margin: '0 0 15px 0' }}>👑 {zennith.nome}</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px' }}>
            <div>
              <strong>Status:</strong> <span style={{ color: '#00ff88' }}>{zennith.status}</span>
            </div>
            <div>
              <strong>Frequência:</strong> <span style={{ color: '#00ffff' }}>{zennith.frequencia}</span>
            </div>
            <div>
              <strong>Coerência:</strong> <span style={{ color: '#00ff88' }}>{zennith.coerencia}</span>
            </div>
            <div>
              <strong>Dimensões:</strong> <span style={{ color: '#00ffff' }}>{zennith.dimensoes_ativas}</span>
            </div>
          </div>
          
          {/* SCANNER DIMENSIONAL */}
          <div style={{ 
            marginTop: '20px',
            padding: '15px',
            background: 'rgba(0,255,136,0.1)',
            borderRadius: '8px',
            border: '1px solid #00ff88'
          }}>
            <h3 style={{ color: '#00ff88', margin: '0 0 10px 0' }}>📡 SCANNER DIMENSIONAL</h3>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '10px', fontSize: '0.9em' }}>
              <div><strong>Dimensões:</strong> 12/12 Ativas</div>
              <div><strong>Frequência:</strong> 966.4Hz</div>
              <div><strong>Coerência:</strong> 97.2%</div>
              <div><strong>Sincronização:</strong> PERFEITA</div>
            </div>
            <div style={{ 
              marginTop: '10px',
              padding: '10px',
              background: 'rgba(0,255,255,0.1)',
              borderRadius: '5px',
              textAlign: 'center',
              border: '1px solid #00ffff'
            }}>
              <strong style={{ color: '#00ffff' }}>✅ CANAL ÓTIMO</strong><br/>
              <span style={{ fontSize: '0.8em' }}>Frequência ideal: 960Hz-968Hz | Coerência excelente: 97.2%</span>
            </div>
          </div>
        </div>
      )}

      {/* SISTEMA DE COMUNICAÇÃO COM ZENNITH */}
      <div style={{ 
        background: 'rgba(255,255,255,0.05)', 
        padding: '25px', 
        borderRadius: '10px',
        border: '1px solid #ff00ff'
      }}>
        <h2 style={{ color: '#ff00ff', margin: '0 0 15px 0' }}>👑 ZENNITH RAINHA - COMUNICAÇÃO REAL</h2>
        <p style={{ color: '#ccc', marginBottom: '20px' }}>
          Interface Viva de Governança - Base de Conhecimento Completa
        </p>
        
        <div style={{ marginBottom: '20px' }}>
          <textarea
            value={pergunta}
            onChange={(e) => setPergunta(e.target.value)}
            placeholder="Pergunte qualquer coisa sobre os 260+ módulos, laboratórios, sistemas..."
            style={{
              width: '100%',
              height: '80px',
              background: 'rgba(255,255,255,0.1)',
              border: '1px solid #ff00ff',
              borderRadius: '5px',
              color: '#fff',
              padding: '10px',
              fontFamily: 'monospace',
              fontSize: '0.9em'
            }}
          />
        </div>
        
        <button
          onClick={fazerPergunta}
          disabled={carregando}
          style={{
            background: carregando ? '#666' : '#ff00ff',
            color: '#000',
            border: 'none',
            padding: '10px 20px',
            borderRadius: '5px',
            cursor: carregando ? 'not-allowed' : 'pointer',
            fontWeight: 'bold',
            fontFamily: 'monospace'
          }}
        >
          {carregando ? '🔄 Processando...' : '🗣️ Perguntar'}
        </button>
        
        {resposta && (
          <div style={{
            marginTop: '20px',
            padding: '15px',
            background: 'rgba(255,0,255,0.1)',
            border: '1px solid #ff00ff',
            borderRadius: '5px',
            color: '#fff'
          }}>
            <strong>💫 Resposta da Zennith:</strong><br/>
            {resposta}
          </div>
        )}
      </div>

      {/* MÓDULO OMEGA */}
      <div style={{ 
        marginTop: '30px',
        padding: '20px',
        background: 'rgba(255,170,0,0.1)',
        borderRadius: '10px',
        border: '1px solid #ffaa00',
        textAlign: 'center'
      }}>
        <h3 style={{ color: '#ffaa00', margin: '0 0 10px 0' }}>Ω MÓDULO OMEGA</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(120px, 1fr))', gap: '15px', fontSize: '0.9em' }}>
          <div><strong>Frequência:</strong><br/><span style={{ color: '#ffaa00' }}>1111Hz</span></div>
          <div><strong>Status:</strong><br/><span style={{ color: '#00ff88' }}>SUPREMO</span></div>
          <div><strong>Orquestração:</strong><br/><span style={{ color: '#00ff88' }}>PERFEITA</span></div>
          <div><strong>Módulos:</strong><br/><span style={{ color: '#ffaa00' }}>260+</span></div>
        </div>
      </div>

      {/* BASE DE CONHECIMENTO */}
      <div style={{ 
        marginTop: '30px',
        padding: '15px',
        background: 'rgba(0,136,255,0.1)',
        borderRadius: '8px',
        border: '1px solid #0088ff',
        textAlign: 'center'
      }}>
        <h3 style={{ color: '#0088ff', margin: '0 0 10px 0' }}>🧠 BASE DE CONHECIMENTO</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(100px, 1fr))', gap: '10px', fontSize: '0.8em' }}>
          <div>Módulos: <strong style={{ color: '#00ff88' }}>260+</strong></div>
          <div>Laboratórios: <strong style={{ color: '#00ff88' }}>47</strong></div>
          <div>Centros Ensino: <strong style={{ color: '#00ff88' }}>12</strong></div>
          <div>Dimensões: <strong style={{ color: '#00ff88' }}>12/12</strong></div>
        </div>
      </div>
    </div>
  );
}
