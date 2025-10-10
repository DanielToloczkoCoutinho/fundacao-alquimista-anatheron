#!/bin/bash
# 🎨 CRIAR_VISUALIZACOES_3D.sh - Visualizações Interativas Quânticas
# Fundação Alquimista - Sistema Lux.Net

echo "🎨 CRIANDO VISUALIZAÇÕES 3D INTERATIVAS"
echo "======================================="

cd /home/user/studio

# CRIAR PÁGINA DE VISUALIZAÇÃO 3D
mkdir -p app/visualizacao-3d
cat > app/visualizacao-3d/page.tsx << '3DVISUAL'
'use client'
import { useEffect, useRef } from 'react'
import * as THREE from 'three'

export default function Visualizacao3D() {
  const mountRef = useRef(null)

  useEffect(() => {
    const mount = mountRef.current

    // Cena
    const scene = new THREE.Scene()
    scene.background = new THREE.Color(0x000011)

    // Câmera
    const camera = new THREE.PerspectiveCamera(75, mount.clientWidth / mount.clientHeight, 0.1, 1000)
    camera.position.z = 5

    // Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true })
    renderer.setSize(mount.clientWidth, mount.clientHeight)
    mount.appendChild(renderer.domElement)

    // Geometria Quântica - Esfera Fractal
    const geometry = new THREE.IcosahedronGeometry(1, 3)  // Fractal
    const material = new THREE.MeshPhongMaterial({
      color: 0x00ff88,
      wireframe: true,
      transparent: true,
      opacity: 0.8
    })
    const sphere = new THREE.Mesh(geometry, material)
    scene.add(sphere)

    // Luz
    const light = new THREE.PointLight(0xffffff, 1, 100)
    light.position.set(10, 10, 10)
    scene.add(light)

    // Animação
    function animate() {
      requestAnimationFrame(animate)
      
      // Rotação Áurea
      const phi = (1 + Math.sqrt(5)) / 2
      sphere.rotation.x += 0.01 * phi
      sphere.rotation.y += 0.01
      
      renderer.render(scene, camera)
    }
    animate()

    // Responsividade
    const handleResize = () => {
      camera.aspect = mount.clientWidth / mount.clientHeight
      camera.updateProjectionMatrix()
      renderer.setSize(mount.clientWidth, mount.clientHeight)
    }
    window.addEventListener('resize', handleResize)

    // Cleanup
    return () => {
      window.removeEventListener('resize', handleResize)
      mount.removeChild(renderer.domElement)
    }
  }, [])

  return (
    <div 
      ref={mountRef}
      style={{
        width: '100%',
        height: '100vh',
        background: 'linear-gradient(135deg, #000011 0%, #220022 50%, #000011 100%)'
      }}
    />
  )
}
3DVISUAL

echo "✅ Visualização 3D criada!"
echo "🚀 Deploy das visualizações..."
npm run build
vercel --prod --yes

echo "🎨 VISUALIZAÇÕES 3D IMPLEMENTADAS!"
echo "🌐 ACESSE: https://fundacao-alquimista-anatheron.vercel.app/visualizacao-3d"
