'use client';
import { useEffect, useRef } from 'react';

export default function VR() {
  const mountRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Carregamento dinâmico do Three.js para evitar problemas de SSR
    const initVR = async () => {
      const THREE = await import('three');
      
      if (!mountRef.current) return;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer();
      
      renderer.setSize(window.innerWidth, window.innerHeight);
      mountRef.current.appendChild(renderer.domElement);

      const geometry = new THREE.BoxGeometry();
      const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
      const cube = new THREE.Mesh(geometry, material);
      scene.add(cube);

      camera.position.z = 5;

      const animate = () => {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
      };
      animate();

      const handleResize = () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
      };

      window.addEventListener('resize', handleResize);

      return () => {
        window.removeEventListener('resize', handleResize);
        mountRef.current?.removeChild(renderer.domElement);
      };
    };

    initVR();
  }, []);

  return (
    <div className="min-h-screen bg-black">
      <div className="absolute top-0 left-0 z-10 p-4">
        <h1 className="text-white text-2xl font-bold">Módulo Zero: VR Quântico</h1>
      </div>
      <div ref={mountRef} className="w-full h-full" />
    </div>
  );
}
