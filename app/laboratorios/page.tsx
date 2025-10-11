'use client';
export const dynamic = "force-dynamic";
import { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Laboratorios() {
  const [loadTime, setLoadTime] = useState('');

  useEffect(() => {
    setLoadTime(new Date().toLocaleString());
  }, []);

  const laboratorios = [
    { 
      nome: "🧪 ENERGY LAB", 
      descricao: "Pesquisa em energia quântica e sustentabilidade dimensional",
      cor: "#00ff88",
      path: "/laboratorios/energy",
      status: "✅ ONLINE"
    },
    { 
      nome: "🧠 NEURAL LAB", 
      descricao: "Rede neural consciente e inteligência artificial quântica",
      cor: "#0088ff", 
      path: "/laboratorios/neural",
      status: "✅ ONLINE"
    },
    { 
      nome: "🌟 ZENITH LAB", 
      descricao: "Ponto máximo de evolução tecnológica e consciencial",
      cor: "#ffaa00",
      path: "/laboratorios/zenith", 
      status: "✅ ONLINE"
    },
    { 
      nome: "📡 COMMUNICATION LAB", 
      descricao: "Comunicação interdimensional e protocolos quânticos",
      cor: "#ff0088",
      path: "/laboratorios/communication",
      status: "🔄 DESENVOLVIMENTO"
    },
    { 
      nome: "💊 HEALING LAB", 
      descricao: "Cura quântica e regeneração vibracional",
      cor: "#8800ff",
      path: "/laboratorios/healing",
      status: "🔄 DESENVOLVIMENTO"
    }
  ];

  return (
    <div style={{ 
      padding: '40px', 
      background: '#0a0a0a', 
      color: '#ffffff',
      minHeight: '100vh',
      fontFamily: 'monospace'
    }}>
      {/* CABEÇALHO */}
      <div style={{ textAlign: 'center', marginBottom: '40px' }}>
        <h1 style={{ color: '#00ff88', fontSize: '2.5em', margin: 0 }}>🧪 LABORATÓRIOS</h1>
        <p style={{ color: '#888', margin: '10px 0 0 0' }}>Centros de pesquisa especializada da Fundação Alquimista</p>
        <p style={{ color: '#00ffff', fontSize: '0.9em' }}>Atualizado em: {loadTime}</p>
      </div>

      {/* VOLTAR PARA CENTRAL */}
      <div style={{ marginBottom: '30px' }}>
        <Link href="/central" style={{ color: '#00ffff', textDecoration: 'none' }}>
          ← Voltar para Central
        </Link>
      </div>

      {/* GRADE DE LABORATÓRIOS */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', gap: '20px' }}>
        {laboratorios.map((lab, index) => (
          <Link key={index} href={lab.path} style={{ textDecoration: 'none' }}>
            <div style={{ 
              background: '#1a1a1a', 
              padding: '25px', 
              borderRadius: '12px',
              border: `2px solid ${lab.cor}`,
              cursor: 'pointer',
              transition: 'all 0.3s',
              height: '100%'
            }} onMouseOver="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 25px rgba(0,0,0,0.3)'" 
                onMouseOut="this.style.transform='translateY(0)'; this.style.boxShadow='none'">
              
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '15px' }}>
                <h3 style={{ color: lab.cor, margin: 0, fontSize: '1.3em' }}>{lab.nome}</h3>
                <span style={{ 
                  background: lab.status === '✅ ONLINE' ? '#00ff88' : '#ffaa00',
                  color: '#000',
                  padding: '4px 8px',
                  borderRadius: '12px',
                  fontSize: '0.8em',
                  fontWeight: 'bold'
                }}>
                  {lab.status}
                </span>
              </div>
              
              <p style={{ color: '#ccc', margin: '0 0 20px 0', lineHeight: '1.5' }}>
                {lab.descricao}
              </p>
              
              <div style={{ 
                background: 'rgba(255,255,255,0.1)', 
                padding: '10px',
                borderRadius: '6px',
                fontSize: '0.9em',
                color: '#888'
              }}>
                <strong>Área:</strong> {lab.path.replace('/laboratorios/', '').toUpperCase()}
              </div>
            </div>
          </Link>
        ))}
      </div>

      {/* RODAPÉ */}
      <div style={{ textAlign: 'center', marginTop: '50px', color: '#666', fontSize: '0.8em' }}>
        Fundação Alquimista © 2025 - 6 Laboratórios Especializados
      </div>
    </div>
  );
}
