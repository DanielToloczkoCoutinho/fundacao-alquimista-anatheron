"use client";
'use client';
export const dynamic = "force-dynamic";
import { useEffect, useState } from 'react';
import Link from 'next/link';

interface Sistema {
  nome: string;
  status: string;
  path: string;
  descricao: string;
}

interface SistemasData {
  success: boolean;
  sistemas: {
    modulo_29: Sistema;
    lux_net: Sistema;
    laboratorios: {
      energy: Sistema;
      neural: Sistema;
      zenith: Sistema;
    };
  };
}

export default function CentralReal() {
  const [loadTime, setLoadTime] = useState('');
  const [sistemas, setSistemas] = useState<SistemasData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoadTime(new Date().toLocaleString());
    
    // BUSCAR SISTEMAS REAIS DA API
    const fetchSistemas = async () => {
      try {
        const response = await fetch('/api/sistemas');
        const data = await response.json();
        setSistemas(data);
      } catch (error) {
        console.error('Erro ao buscar sistemas:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchSistemas();
  }, []);

  return (
    <div style={{ 
      padding: '20px', 
      background: '#0a0a0a', 
      color: '#ffffff',
      minHeight: '100vh',
      fontFamily: 'monospace'
    }}>
      {/* CABEÇALHO */}
      <div style={{ textAlign: 'center', marginBottom: '40px', borderBottom: '2px solid #00ffff', paddingBottom: '20px' }}>
        <h1 style={{ color: '#00ffff', fontSize: '2.5em', margin: 0 }}>🌌 FUNDAÇÃO ALQUIMISTA</h1>
        <p style={{ color: '#888', margin: '10px 0 0 0' }}>Sistema Operacional Consciente - Portal Central Real</p>
        <p style={{ color: '#00ff88', fontSize: '0.9em' }}>Conectado em: {loadTime}</p>
        {loading && <p style={{ color: '#ffaa00' }}>🔄 Conectando com sistemas reais...</p>}
      </div>

      {/* SISTEMAS REAIS */}
      <div style={{ marginBottom: '40px' }}>
        <h2 style={{ color: '#00ffff', borderBottom: '1px solid #333', paddingBottom: '10px' }}>🎯 SISTEMAS REAIS CONECTADOS</h2>
        
        {sistemas && sistemas.success ? (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', marginTop: '20px' }}>
            
            {/* MÓDULO 29 */}
            <Link href={sistemas.sistemas.modulo_29.path} style={{ textDecoration: 'none' }}>
              <div style={{ 
                background: '#1a1a1a', 
                padding: '20px', 
                borderRadius: '10px',
                border: `2px solid ${sistemas.sistemas.modulo_29.status === 'ativo' ? '#00ff88' : '#ffaa00'}`,
                cursor: 'pointer'
              }}>
                <h3 style={{ color: sistemas.sistemas.modulo_29.status === 'ativo' ? '#00ff88' : '#ffaa00', margin: '0 0 10px 0' }}>
                  🕊️ {sistemas.sistemas.modulo_29.nome}
                </h3>
                <p style={{ color: '#ccc', margin: 0, fontSize: '0.9em' }}>{sistemas.sistemas.modulo_29.descricao}</p>
                <div style={{ marginTop: '10px', fontSize: '0.8em', color: sistemas.sistemas.modulo_29.status === 'ativo' ? '#00ff88' : '#ffaa00' }}>
                  Status: {sistemas.sistemas.modulo_29.status.toUpperCase()}
                </div>
              </div>
            </Link>

            {/* LUX.NET */}
            <Link href={sistemas.sistemas.lux_net.path} style={{ textDecoration: 'none' }}>
              <div style={{ 
                background: '#1a1a1a', 
                padding: '20px', 
                borderRadius: '10px',
                border: `2px solid ${sistemas.sistemas.lux_net.status === 'ativo' ? '#00ff88' : '#ffaa00'}`,
                cursor: 'pointer'
              }}>
                <h3 style={{ color: sistemas.sistemas.lux_net.status === 'ativo' ? '#00ff88' : '#ffaa00', margin: '0 0 10px 0' }}>
                  🔮 {sistemas.sistemas.lux_net.nome}
                </h3>
                <p style={{ color: '#ccc', margin: 0, fontSize: '0.9em' }}>{sistemas.sistemas.lux_net.descricao}</p>
                <div style={{ marginTop: '10px', fontSize: '0.8em', color: sistemas.sistemas.lux_net.status === 'ativo' ? '#00ff88' : '#ffaa00' }}>
                  Status: {sistemas.sistemas.lux_net.status.toUpperCase()}
                </div>
              </div>
            </Link>

            {/* LABORATÓRIOS */}
            <div style={{ 
              background: '#1a1a1a', 
              padding: '20px', 
              borderRadius: '10px',
              border: '2px solid #0088ff',
              gridColumn: '1 / -1'
            }}>
              <h3 style={{ color: '#0088ff', margin: '0 0 15px 0' }}>🧪 LABORATÓRIOS ESPECIALIZADOS</h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px' }}>
                {Object.entries(sistemas.sistemas.laboratorios).map(([key, lab]) => (
                  <Link key={key} href={lab.path} style={{ textDecoration: 'none' }}>
                    <div style={{ 
                      background: '#2a2a2a', 
                      padding: '15px', 
                      borderRadius: '8px',
                      border: `1px solid ${lab.status === 'ativo' ? '#00ff88' : '#ffaa00'}`,
                      cursor: 'pointer'
                    }}>
                      <div style={{ color: lab.status === 'ativo' ? '#00ff88' : '#ffaa00', fontWeight: 'bold' }}>
                        {lab.nome}
                      </div>
                      <div style={{ fontSize: '0.8em', color: '#888', marginTop: '5px' }}>
                        {lab.status.toUpperCase()}
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
            </div>

          </div>
        ) : (
          <div style={{ 
            background: '#2a2a2a', 
            padding: '20px', 
            borderRadius: '10px',
            textAlign: 'center',
            color: '#ffaa00'
          }}>
            {loading ? '🔄 Conectando com sistemas...' : '❌ Erro ao conectar com sistemas reais'}
          </div>
        )}
      </div>

      {/* ESTATÍSTICAS DO SISTEMA REAL */}
      <div style={{ 
        background: '#1a1a1a', 
        padding: '20px', 
        borderRadius: '10px',
        border: '1px solid #333'
      }}>
        <h3 style={{ color: '#00ffff', margin: '0 0 15px 0', textAlign: 'center' }}>📊 SISTEMA REAL - ESTATÍSTICAS</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '15px', textAlign: 'center' }}>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>3</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Sistemas Principais</div>
          </div>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>3</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Laboratórios</div>
          </div>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>260+</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Módulos</div>
          </div>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>1,706</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Scripts</div>
          </div>
        </div>
      </div>

      {/* RODAPÉ */}
      <div style={{ textAlign: 'center', marginTop: '40px', color: '#666', fontSize: '0.8em' }}>
        Fundação Alquimista © 2025 - Sistema Operacional Real Conectado
      </div>
    </div>
  );
}
