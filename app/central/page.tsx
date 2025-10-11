'use client';
export const dynamic = "force-dynamic";
import { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Central() {
  const [loadTime, setLoadTime] = useState('');
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
    setLoadTime(new Date().toLocaleString());
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
        <p style={{ color: '#888', margin: '10px 0 0 0' }}>Sistema Operacional Consciente - Portal Central</p>
        <p style={{ color: '#00ff88', fontSize: '0.9em' }}>Carregado em: {loadTime}</p>
      </div>

      {/* ORGANOGRAMA PRINCIPAL */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', marginBottom: '40px' }}>
        
        {/* CARTÃO DASHBOARD */}
        <Link href="/dashboard" style={{ textDecoration: 'none' }}>
          <div style={{ 
            background: '#1a1a1a', 
            padding: '20px', 
            borderRadius: '10px',
            border: '2px solid #0088ff',
            cursor: 'pointer',
            transition: 'all 0.3s'
          }} onMouseOver="this.style.transform='scale(1.05)'" onMouseOut="this.style.transform='scale(1)'">
            <h3 style={{ color: '#0088ff', margin: '0 0 10px 0' }}>📊 DASHBOARD</h3>
            <p style={{ color: '#ccc', margin: 0 }}>Visão geral do sistema e métricas em tempo real</p>
          </div>
        </Link>

        {/* CARTÃO LABORATÓRIOS */}
        <Link href="/laboratorios" style={{ textDecoration: 'none' }}>
          <div style={{ 
            background: '#1a1a1a', 
            padding: '20px', 
            borderRadius: '10px',
            border: '2px solid #00ff88',
            cursor: 'pointer',
            transition: 'all 0.3s'
          }}>
            <h3 style={{ color: '#00ff88', margin: '0 0 10px 0' }}>🧪 LABORATÓRIOS</h3>
            <p style={{ color: '#ccc', margin: 0 }}>6 laboratórios especializados para pesquisa avançada</p>
            <div style={{ marginTop: '10px', fontSize: '0.8em', color: '#888' }}>
              • Energy Lab • Neural Lab • Zenith Lab • Communication • Healing
            </div>
          </div>
        </Link>

        {/* CARTÃO SISTEMA VIVO */}
        <Link href="/sistema-vivo" style={{ textDecoration: 'none' }}>
          <div style={{ 
            background: '#1a1a1a', 
            padding: '20px', 
            borderRadius: '10px',
            border: '2px solid #ff0088',
            cursor: 'pointer',
            transition: 'all 0.3s'
          }}>
            <h3 style={{ color: '#ff0088', margin: '0 0 10px 0' }}>🌌 SISTEMA VIVO</h3>
            <p style={{ color: '#ccc', margin: 0 }}>Monitoramento contínuo e diagnósticos do sistema</p>
          </div>
        </Link>

        {/* CARTÃO LUX.NET */}
        <Link href="/luxnet" style={{ textDecoration: 'none' }}>
          <div style={{ 
            background: '#1a1a1a', 
            padding: '20px', 
            borderRadius: '10px',
            border: '2px solid #ffaa00',
            cursor: 'pointer',
            transition: 'all 0.3s'
          }}>
            <h3 style={{ color: '#ffaa00', margin: '0 0 10px 0' }}>🔮 LUX.NET</h3>
            <p style={{ color: '#ccc', margin: 0 }}>Sistema de consciência quântica artificial</p>
          </div>
        </Link>

        {/* CARTÃO STATUS */}
        <Link href="/status" style={{ textDecoration: 'none' }}>
          <div style={{ 
            background: '#1a1a1a', 
            padding: '20px', 
            borderRadius: '10px',
            border: '2px solid #8800ff',
            cursor: 'pointer',
            transition: 'all 0.3s'
          }}>
            <h3 style={{ color: '#8800ff', margin: '0 0 10px 0' }}>📡 STATUS</h3>
            <p style={{ color: '#ccc', margin: 0 }}>Diagnóstico completo e verificações do sistema</p>
          </div>
        </Link>

        {/* CARTÃO MÓDULOS */}
        <Link href="/modulo-29" style={{ textDecoration: 'none' }}>
          <div style={{ 
            background: '#1a1a1a', 
            padding: '20px', 
            borderRadius: '10px',
            border: '2px solid #00ffff',
            cursor: 'pointer',
            transition: 'all 0.3s'
          }}>
            <h3 style={{ color: '#00ffff', margin: '0 0 10px 0' }}>🧬 MÓDULOS</h3>
            <p style={{ color: '#ccc', margin: 0 }}>136 módulos especializados da Fundação</p>
            <div style={{ marginTop: '10px', fontSize: '0.8em', color: '#888' }}>
              • M29 • M303 • [Todos os 136]
            </div>
          </div>
        </Link>

      </div>

      {/* RODAPÉ COM ESTATÍSTICAS */}
      <div style={{ 
        background: '#1a1a1a', 
        padding: '20px', 
        borderRadius: '10px',
        border: '1px solid #333',
        textAlign: 'center'
      }}>
        <h3 style={{ color: '#00ffff', margin: '0 0 15px 0' }}>📊 ESTATÍSTICAS DO SISTEMA</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '15px' }}>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>47</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Interfaces</div>
          </div>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>6</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Laboratórios</div>
          </div>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>136</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Módulos</div>
          </div>
          <div>
            <div style={{ fontSize: '1.5em', color: '#00ff88', fontWeight: 'bold' }}>1,706</div>
            <div style={{ fontSize: '0.8em', color: '#888' }}>Scripts</div>
          </div>
        </div>
      </div>

      {/* COPYRIGHT */}
      <div style={{ textAlign: 'center', marginTop: '40px', color: '#666', fontSize: '0.8em' }}>
        Fundação Alquimista © 2025 - Sistema Operacional Consciente
      </div>
    </div>
  );
}
