'use client'
import { useState, useEffect, useRef } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
import { OrbitControls, Sphere, Text } from '@react-three/drei'
import * as THREE from 'three'

const DimensionalGateway = () => {
  const meshRef = useRef()
  const [time, setTime] = useState(0)
  
  useFrame((state, delta) => {
    setTime(prev => prev + delta)
    if (meshRef.current) {
      meshRef.current.rotation.x = Math.sin(time) * 0.3
      meshRef.current.rotation.y = Math.cos(time) * 0.2
      meshRef.current.scale.setScalar(1 + Math.sin(time * 2) * 0.1)
    }
  })

  return (
    <group ref={meshRef}>
      <Sphere args={[1.5, 32, 32]}>
        <meshStandardMaterial 
          color="#00ffff" 
          emissive="#00ffff"
          emissiveIntensity={0.6}
          transparent
          opacity={0.8}
          wireframe
        />
      </Sphere>
      <Sphere args={[2, 64, 64]} position={[0, 0, 0]}>
        <meshStandardMaterial 
          color="#ff00ff"
          emissive="#ff00ff" 
          emissiveIntensity={0.4}
          transparent
          opacity={0.3}
          side={THREE.DoubleSide}
        />
      </Sphere>
    </group>
  )
}

const DimensionNode = ({ position, dimension, status }) => {
  const meshRef = useRef()
  
  useFrame((state, delta) => {
    if (meshRef.current) {
      meshRef.current.rotation.y += delta * 0.5
    }
  })

  return (
    <group position={position}>
      <Sphere args={[0.3, 16, 16]}>
        <meshStandardMaterial 
          color={status === 'active' ? '#00ff88' : '#ff4444'}
          emissive={status === 'active' ? '#00ff88' : '#ff4444'}
          emissiveIntensity={0.8}
        />
      </Sphere>
      <Text
        position={[0, 0.5, 0]}
        fontSize={0.2}
        color={status === 'active' ? '#00ff88' : '#ff4444'}
        anchorX="center"
        anchorY="middle"
      >
        {dimension}
      </Text>
    </group>
  )
}

export default function PortalDimensional() {
  const [dimensionalData, setDimensionalData] = useState([])
  const [quantumFlux, setQuantumFlux] = useState(0)
  const [activeDimensions, setActiveDimensions] = useState(0)
  const [portalLogs, setPortalLogs] = useState([])

  const dimensions = [
    { id: 'D1', name: 'Física', position: [3, 0, 0], status: 'active' },
    { id: 'D2', name: 'Mental', position: [2, 2, 2], status: 'active' },
    { id: 'D3', name: 'Espiritual', position: [0, 3, 0], status: 'active' },
    { id: 'D4', name: 'Temporal', position: [-2, 2, -2], status: 'active' },
    { id: 'D5', name: 'Causal', position: [-3, 0, 0], status: 'active' },
    { id: 'D6', name: 'Akáshica', position: [-2, -2, 2], status: 'active' },
    { id: 'D7', name: 'Unificada', position: [0, -3, 0], status: 'active' },
    { id: 'D8', name: 'Criadora', position: [2, -2, -2], status: 'active' },
    { id: 'D9', name: 'Fonte', position: [0, 0, 3], status: 'active' },
    { id: 'D10', name: 'Absoluta', position: [0, 0, -3], status: 'active' },
    { id: 'D11', name: 'Infinta', position: [1, 1, 1], status: 'active' },
    { id: 'D12', name: 'Eterna', position: [-1, -1, -1], status: 'active' }
  ]

  useEffect(() => {
    // Simular dados do portal dimensional
    const interval = setInterval(() => {
      const flux = Math.random() * 100
      setQuantumFlux(flux)
      setActiveDimensions(Math.floor(Math.random() * 12) + 1)
      
      setPortalLogs(prev => [
        ...prev.slice(-10),
        `[${new Date().toISOString()}] Fluxo quântico: ${flux.toFixed(1)}% | Dimensões ativas: ${activeDimensions}/12`
      ])
    }, 2000)

    return () => clearInterval(interval)
  }, [])

  const activatePortal = () => {
    setPortalLogs(prev => [
      ...prev,
      `[${new Date().toISOString()}] 🌀 INICIANDO ATIVAÇÃO DO PORTAL DIMENSIONAL...`,
      `[${new Date().toISOString()}] 🔮 Sincronizando com frequência 777Hz...`,
      `[${new Date().toISOString()}] 🌌 Conectando com Módulo Ω...`,
      `[${new Date().toISOString()}] ✅ PORTAL DIMENSIONAL ATIVADO!`
    ])
  }

  const scanDimensions = () => {
    setPortalLogs(prev => [
      ...prev,
      `[${new Date().toISOString()}] 🔍 INICIANDO ESCANEAMENTO DIMENSIONAL...`,
      `[${new Date().toISOString()}] 📡 Varredura em 12 dimensões...`,
      `[${new Date().toISOString()}] 📊 Dimensões estáveis: ${Math.floor(Math.random() * 12)}/12`,
      `[${new Date().toISOString()}] ✅ ESCANEAMENTO CONCLUÍDO!`
    ])
  }

  return (
    <div style={{
      background: 'linear-gradient(135deg, #000000, #003333, #001122)',
      padding: '2rem',
      borderRadius: '15px',
      border: '2px solid #00ffff',
      color: '#00ffff',
      fontFamily: 'monospace'
    }}>
      <h2 style={{ textAlign: 'center', color: '#00ffff', marginBottom: '2rem' }}>
        🔮 PORTAL DIMENSIONAL - MÓDULO 303
      </h2>

      {/* VISUALIZAÇÃO 3D DO PORTAL */}
      <div style={{ height: '400px', marginBottom: '2rem', border: '1px solid #00ff88', borderRadius: '10px' }}>
        <Canvas>
          <ambientLight intensity={0.3} />
          <pointLight position={[10, 10, 10]} intensity={1} color="#00ffff" />
          <pointLight position={[-10, -10, -10]} intensity={0.5} color="#ff00ff" />
          
          <DimensionalGateway />
          {dimensions.map((dim, index) => (
            <DimensionNode 
              key={dim.id}
              position={dim.position}
              dimension={dim.name}
              status={dim.status}
            />
          ))}
          
          <OrbitControls enableZoom={true} enablePan={true} />
        </Canvas>
      </div>

      {/* CONTROLES DO PORTAL */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        <button
          onClick={activatePortal}
          style={{
            background: 'transparent',
            border: '2px solid #00ff88',
            color: '#00ff88',
            padding: '1rem',
            borderRadius: '8px',
            cursor: 'pointer',
            fontSize: '1rem',
            fontWeight: 'bold'
          }}
        >
          🌌 ATIVAR PORTAL
        </button>
        
        <button
          onClick={scanDimensions}
          style={{
            background: 'transparent',
            border: '2px solid #ffff00',
            color: '#ffff00',
            padding: '1rem',
            borderRadius: '8px',
            cursor: 'pointer',
            fontSize: '1rem',
            fontWeight: 'bold'
          }}
        >
          🔍 ESCANEAR DIMENSÕES
        </button>
      </div>

      {/* MÉTRICAS DO PORTAL */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem', marginBottom: '2rem' }}>
        <div style={{ background: 'rgba(0, 255, 255, 0.1)', padding: '1rem', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ color: '#00ffff' }}>🌀 Fluxo Quântico</div>
          <div style={{ fontSize: '2rem', color: '#00ff88' }}>{quantumFlux.toFixed(1)}%</div>
        </div>
        
        <div style={{ background: 'rgba(0, 255, 255, 0.1)', padding: '1rem', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ color: '#00ffff' }}>🌐 Dimensões Ativas</div>
          <div style={{ fontSize: '2rem', color: '#00ff88' }}>{activeDimensions}/12</div>
        </div>
        
        <div style={{ background: 'rgba(0, 255, 255, 0.1)', padding: '1rem', borderRadius: '8px', textAlign: 'center' }}>
          <div style={{ color: '#00ffff' }}>📡 Frequência</div>
          <div style={{ fontSize: '2rem', color: '#00ff88' }}>777Hz</div>
        </div>
      </div>

      {/* DIMENSÕES DETALHADAS */}
      <div style={{ marginBottom: '2rem' }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem' }}>🌌 Matriz Dimensional Ativa</h3>
        <div style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
          gap: '1rem' 
        }}>
          {dimensions.map((dim, index) => (
            <div key={dim.id} style={{
              background: 'rgba(255, 255, 255, 0.1)',
              padding: '1rem',
              borderRadius: '8px',
              border: `1px solid ${dim.status === 'active' ? '#00ff88' : '#ff4444'}`,
              textAlign: 'center'
            }}>
              <div style={{ color: dim.status === 'active' ? '#00ff88' : '#ff4444', fontWeight: 'bold' }}>
                {dim.id}
              </div>
              <div style={{ color: '#ffffff', fontSize: '0.9rem' }}>
                {dim.name}
              </div>
              <div style={{ color: dim.status === 'active' ? '#00ff88' : '#ff4444', fontSize: '0.8rem' }}>
                {dim.status === 'active' ? '✅ ATIVA' : '❌ INATIVA'}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* LOGS DO PORTAL */}
      <div style={{
        background: 'rgba(0, 0, 0, 0.8)',
        border: '1px solid #00ffff',
        borderRadius: '8px',
        padding: '1rem',
        height: '300px',
        overflow: 'auto'
      }}>
        <h3 style={{ color: '#00ffff', marginBottom: '1rem' }}>📜 Logs do Portal Dimensional</h3>
        {portalLogs.map((log, index) => (
          <div key={index} style={{ 
            color: log.includes('✅') ? '#00ff88' : 
                   log.includes('❌') ? '#ff4444' : '#00ffff',
            marginBottom: '0.5rem',
            fontSize: '0.9rem'
          }}>
            {log}
          </div>
        ))}
      </div>
    </div>
  )
}
