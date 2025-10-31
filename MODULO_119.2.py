import React, { useRef, useEffect, useState, useCallback } from 'react';
import * as THREE from 'three';
import { SphereGeometry, MeshStandardMaterial, Mesh, PointLight, IcosahedronGeometry, LineBasicMaterial, LineSegments, EdgesGeometry, BufferGeometry, Float32BufferAttribute, ShaderMaterial, AdditiveBlending } from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Componente principal do Templum Cosmica
const TemplumCosmica = () => {
  const mountRef = useRef(null);
  const [activeTab, setActiveTab] = useState('dashboard');
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [coherenceLevel, setCoherenceLevel] = useState(0.95);
  const [inputValues, setInputValues] = useState({
    amplitude: 888,
    frequency: 13,
    phase: 0
  });

  const sceneRef = useRef(new THREE.Scene());
  const cameraRef = useRef(new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000));
  const rendererRef = useRef(null);
  const crystalCoreRef = useRef(null);
  const mandalaRef = useRef(null);
  const shieldRef = useRef(null);
  const controlsRef = useRef(null);
  const particleSystemRef = useRef(null);
  const animationRef = useRef(null);

  // Inicializar a cena 3D
  const initThreeScene = useCallback(() => {
    const currentMount = mountRef.current;
    if (!currentMount) return;

    // Renderer com configurações avançadas
    rendererRef.current = new THREE.WebGLRenderer({ 
      antialias: true, 
      alpha: true,
      powerPreference: "high-performance"
    });
    rendererRef.current.setSize(currentMount.clientWidth, currentMount.clientHeight);
    rendererRef.current.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    currentMount.appendChild(rendererRef.current.domElement);

    // Configuração da cena
    sceneRef.current.background = new THREE.Color(0x050510);
    sceneRef.current.fog = new THREE.Fog(0x050510, 5, 25);

    // Câmera
    cameraRef.current.position.set(0, 0, 10);
    cameraRef.current.lookAt(0, 0, 0);

    // Sistema de iluminação avançado
    const ambientLight = new THREE.AmbientLight(0x404040, 2.5);
    sceneRef.current.add(ambientLight);
    
    const pointLight1 = new PointLight(0x4a154b, 50, 50);
    pointLight1.position.set(5, 8, 5);
    sceneRef.current.add(pointLight1);
    
    const pointLight2 = new PointLight(0x154b4a, 50, 50);
    pointLight2.position.set(-5, -8, -5);
    sceneRef.current.add(pointLight2);
    
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
    directionalLight.position.set(0, 10, 0);
    sceneRef.current.add(directionalLight);

    // Controles de órbita
    controlsRef.current = new OrbitControls(cameraRef.current, rendererRef.current.domElement);
    controlsRef.current.enableDamping = true;
    controlsRef.current.dampingFactor = 0.05;
    controlsRef.current.minDistance = 3;
    controlsRef.current.maxDistance = 20;

    // Criar Crystal Core (Cristal Central)
    const crystalGeometry = new IcosahedronGeometry(1.5, 3); // Maior detalhamento
    const crystalMaterial = new MeshStandardMaterial({
      color: 0x52c6ff,
      emissive: 0x0a1622,
      roughness: 0.1,
      metalness: 0.9,
      transparent: true,
      opacity: 0.8,
      envMapIntensity: 2
    });
    
    const crystalCore = new Mesh(crystalGeometry, crystalMaterial);
    crystalCore.name = "CrystalCore";
    sceneRef.current.add(crystalCore);
    crystalCoreRef.current = crystalCore;

    // Adicionar arestas para efeito cristalino
    const edgesGeometry = new EdgesGeometry(crystalGeometry);
    const edgesMaterial = new LineBasicMaterial({ color: 0x00ffff, linewidth: 2 });
    const crystalEdges = new LineSegments(edgesGeometry, edgesMaterial);
    crystalCore.add(crystalEdges);

    // Criar sistema de partículas para energia quântica
    createQuantumParticles();

    // Criar escudo de proteção quântica (inicialmente invisível)
    const shieldGeometry = new IcosahedronGeometry(2.2, 2);
    const shieldMaterial = new MeshStandardMaterial({
      color: 0x00ff00,
      emissive: 0x004400,
      transparent: true,
      opacity: 0,
      wireframe: true
    });
    
    const shield = new Mesh(shieldGeometry, shieldMaterial);
    shield.name = "QuantumShield";
    sceneRef.current.add(shield);
    shieldRef.current = shield;

    // Animação principal
    const animate = () => {
      animationRef.current = requestAnimationFrame(animate);
      
      // Animações contínuas
      const time = Date.now() * 0.001;
      
      if (crystalCoreRef.current) {
        crystalCoreRef.current.rotation.x += 0.003;
        crystalCoreRef.current.rotation.y += 0.004;
        crystalCoreRef.current.rotation.z += 0.002;
        
        // Pulsação suave do cristal
        const pulse = 1 + 0.05 * Math.sin(time * 2);
        crystalCoreRef.current.scale.set(pulse, pulse, pulse);
      }
      
      if (shieldRef.current) {
        shieldRef.current.rotation.x += 0.001;
        shieldRef.current.rotation.y += 0.002;
      }
      
      if (particleSystemRef.current) {
        particleSystemRef.current.rotation.y += 0.001;
        
        // Animar partículas
        const positions = particleSystemRef.current.geometry.attributes.position.array;
        const originalPositions = particleSystemRef.current.userData.originalPositions;
        const count = positions.length / 3;
        
        for (let i = 0; i < count; i++) {
          const i3 = i * 3;
          const offset = Math.sin(time * 0.5 + i * 0.1) * 0.3;
          
          positions[i3] = originalPositions[i3] + offset;
          positions[i3 + 1] = originalPositions[i3 + 1] + offset;
          positions[i3 + 2] = originalPositions[i3 + 2] + offset;
        }
        
        particleSystemRef.current.geometry.attributes.position.needsUpdate = true;
      }
      
      controlsRef.current.update();
      rendererRef.current.render(sceneRef.current, cameraRef.current);
    };

    animate();

    // Configurar redimensionamento
    const onWindowResize = () => {
      cameraRef.current.aspect = currentMount.clientWidth / currentMount.clientHeight;
      cameraRef.current.updateProjectionMatrix();
      rendererRef.current.setSize(currentMount.clientWidth, currentMount.clientHeight);
    };
    
    window.addEventListener('resize', onWindowResize);

    return () => {
      window.removeEventListener('resize', onWindowResize);
      if (animationRef.current) cancelAnimationFrame(animationRef.current);
      if (currentMount && rendererRef.current) {
        currentMount.removeChild(rendererRef.current.domElement);
      }
    };
  }, []);

  // Criar sistema de partículas quânticas
  const createQuantumParticles = () => {
    const particleCount = 1000;
    const particles = new BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);
    const sizes = new Float32Array(particleCount);
    
    const originalPositions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount; i++) {
      const i3 = i * 3;
      
      // Posicionar partículas em uma esfera
      const radius = 4 + Math.random() * 6;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos((2 * Math.random()) - 1);
      
      positions[i3] = radius * Math.sin(phi) * Math.cos(theta);
      positions[i3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
      positions[i3 + 2] = radius * Math.cos(phi);
      
      originalPositions[i3] = positions[i3];
      originalPositions[i3 + 1] = positions[i3 + 1];
      originalPositions[i3 + 2] = positions[i3 + 2];
      
      // Cores baseadas em tons quânticos
      colors[i3] = Math.random() * 0.5 + 0.5;     // R
      colors[i3 + 1] = Math.random() * 0.3 + 0.2; // G
      colors[i3 + 2] = Math.random() * 0.5 + 0.5; // B
      
      sizes[i] = Math.random() * 0.1 + 0.01;
    }
    
    particles.setAttribute('position', new Float32BufferAttribute(positions, 3));
    particles.setAttribute('color', new Float32BufferAttribute(colors, 3));
    particles.setAttribute('size', new Float32BufferAttribute(sizes, 1));
    
    // Material de partícula personalizado
    const particleMaterial = new ShaderMaterial({
      uniforms: {
        time: { value: 0 }
      },
      vertexShader: `
        attribute float size;
        varying vec3 vColor;
        
        void main() {
          vColor = color;
          vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
          gl_PointSize = size * (300.0 / -mvPosition.z);
          gl_Position = projectionMatrix * mvPosition;
        }
      `,
      fragmentShader: `
        varying vec3 vColor;
        
        void main() {
          // Criar partículas circulares
          float strength = distance(gl_PointCoord, vec2(0.5));
          strength = 1.0 - strength;
          strength = pow(strength, 2.0);
          
          gl_FragColor = vec4(vColor, strength);
        }
      `,
      blending: AdditiveBlending,
      depthTest: false,
      transparent: true,
      vertexColors: true
    });
    
    const particleSystem = new THREE.Points(particles, particleMaterial);
    particleSystem.userData.originalPositions = originalPositions;
    sceneRef.current.add(particleSystem);
    particleSystemRef.current = particleSystem;
  };

  // Gerar fractal de Mandelbrot baseado na frequência
  const generateMandelbrotFractal = (frequency) => {
    if (mandalaRef.current) {
      sceneRef.current.remove(mandalaRef.current);
    }
    
    const detail = Math.max(16, Math.min(128, Math.floor(frequency)));
    const geometry = new BufferGeometry();
    const vertices = [];
    const colors = [];
    
    // Parâmetros do fractal
    const width = 100;
    const height = 100;
    const maxIterations = Math.max(20, Math.min(100, Math.floor(frequency / 2)));
    
    for (let x = 0; x < width; x++) {
      for (let y = 0; y < height; y++) {
        const zx = 1.5 * (x - width / 2) / (0.5 * width);
        const zy = (y - height / 2) / (0.5 * height);
        
        let zx0 = zx;
        let zy0 = zy;
        let iteration = 0;
        
        while (zx0 * zx0 + zy0 * zy0 < 4 && iteration < maxIterations) {
          const tmp = zx0 * zx0 - zy0 * zy0 + zx;
          zy0 = 2 * zx0 * zy0 + zy;
          zx0 = tmp;
          iteration++;
        }
        
        if (iteration < maxIterations) {
          const logZn = Math.log(zx0 * zx0 + zy0 * zy0) / 2;
          const nu = Math.log(logZn / Math.log(2)) / Math.log(2);
          iteration = iteration + 1 - nu;
        }
        
        const colorIntensity = iteration / maxIterations;
        const radius = 3 + colorIntensity * 2;
        const angle = (x / width) * Math.PI * 2;
        
        vertices.push(
          Math.cos(angle) * radius,
          Math.sin(angle) * radius,
          (y / height - 0.5) * 2
        );
        
        // Cor baseada nas iterações (esquema de cores quântico)
        colors.push(
          Math.sin(colorIntensity * Math.PI * 0.5),
          Math.cos(colorIntensity * Math.PI),
          Math.sin(colorIntensity * Math.PI + Math.PI / 3)
        );
      }
    }
    
    geometry.setAttribute('position', new Float32BufferAttribute(vertices, 3));
    geometry.setAttribute('color', new Float32BufferAttribute(colors, 3));
    
    const material = new MeshStandardMaterial({
      vertexColors: true,
      emissiveIntensity: 1,
      metalness: 0.2,
      roughness: 0.1,
      transparent: true,
      opacity: 0.9
    });
    
    mandalaRef.current = new Mesh(geometry, material);
    mandalaRef.current.rotation.x = Math.PI / 2;
    sceneRef.current.add(mandalaRef.current);
    
    return mandalaRef.current;
  };

  // Ativar EQ001 - Energia Universal Integrada
  const activateEQ001 = () => {
    setMessage('Ativando a EQ001: Energia Universal Integrada no Campo Quântico...');
    setIsLoading(true);
    
    // Ativar brilho do cristal
    if (crystalCoreRef.current) {
      const crystalMaterial = crystalCoreRef.current.material;
      crystalMaterial.emissive.setHex(0x00ffff);
      crystalMaterial.emissiveIntensity = 2;
      crystalMaterial.opacity = 1;
    }
    
    // Gerar fractal baseado na frequência atual
    generateMandelbrotFractal(inputValues.frequency);
    
    // Ativar escudo de proteção quântica
    if (shieldRef.current) {
      const shieldMaterial = shieldRef.current.material;
      shieldMaterial.opacity = 0.3;
      
      // Animação de pulso do escudo
      const startTime = Date.now();
      const pulseShield = () => {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / 3000, 1);
        const pulseIntensity = 0.3 + 0.2 * Math.sin(elapsed * 0.01);
        
        shieldMaterial.opacity = pulseIntensity;
        shieldMaterial.emissiveIntensity = pulseIntensity * 2;
        
        if (progress < 1) {
          requestAnimationFrame(pulseShield);
        }
      };
      
      pulseShield();
    }
    
    // Simular aumento de coerência
    let currentCoherence = coherenceLevel;
    const coherenceInterval = setInterval(() => {
      currentCoherence = Math.min(0.99, currentCoherence + 0.01);
      setCoherenceLevel(currentCoherence);
    }, 200);
    
    // Finalizar ativação após 3 segundos
    setTimeout(() => {
      clearInterval(coherenceInterval);
      setMessage('EQ001 ativada com sucesso. O Altar de Recodificação está em pleno funcionamento.');
      setIsLoading(false);
      
      // Restaurar estado inicial gradualmente
      if (crystalCoreRef.current) {
        const crystalMaterial = crystalCoreRef.current.material;
        crystalMaterial.emissive.setHex(0x0a1622);
        crystalMaterial.emissiveIntensity = 1;
      }
      
      if (shieldRef.current) {
        shieldRef.current.material.opacity = 0.1;
      }
    }, 3000);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setInputValues(prev => ({ ...prev, [name]: parseFloat(value) }));
    
    // Atualizar fractal em tempo real quando a frequência muda
    if (name === 'frequency' && mandalaRef.current) {
      generateMandelbrotFractal(parseFloat(value));
    }
  };

  // Efeito para inicialização
  useEffect(() => {
    initThreeScene();
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [initThreeScene]);

  return (
    <div className="w-full h-screen bg-gray-950 text-gray-100 flex flex-col font-sans overflow-hidden">
      <div className="flex flex-col md:flex-row flex-1">
        {/* Painel de Controle */}
        <aside className="w-full md:w-1/3 lg:w-1/4 p-4 md:p-8 bg-gray-900 border-r border-gray-800 overflow-y-auto">
          <div className="flex flex-col h-full">
            <h1 className="text-3xl font-bold mb-6 text-indigo-400">
              <span className="text-xl">👑</span> Templum Cosmica Anatheronis
            </h1>
            
            <div className="mb-4 p-3 bg-indigo-900 rounded-lg">
              <div className="flex justify-between items-center">
                <span className="text-sm">Coerência Quântica</span>
                <span className="text-sm font-bold">{Math.round(coherenceLevel * 100)}%</span>
              </div>
              <div className="w-full bg-gray-700 h-2 rounded-full mt-1">
                <div 
                  className="bg-green-500 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${coherenceLevel * 100}%` }}
                ></div>
              </div>
            </div>

            <nav className="mb-6">
              <ul className="space-y-2">
                <li>
                  <button
                    onClick={() => setActiveTab('dashboard')}
                    className={`w-full text-left px-4 py-2 rounded-lg transition-colors duration-200 ${activeTab === 'dashboard' ? 'bg-indigo-700 text-white' : 'hover:bg-gray-700'}`}
                  >
                    🌌 Dashboard
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => setActiveTab('equations')}
                    className={`w-full text-left px-4 py-2 rounded-lg transition-colors duration-200 ${activeTab === 'equations' ? 'bg-indigo-700 text-white' : 'hover:bg-gray-700'}`}
                  >
                    📐 Equações-Vivas
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => setActiveTab('protection')}
                    className={`w-full text-left px-4 py-2 rounded-lg transition-colors duration-200 ${activeTab === 'protection' ? 'bg-indigo-700 text-white' : 'hover:bg-gray-700'}`}
                  >
                    🛡️ Proteção Quântica
                  </button>
                </li>
              </ul>
            </nav>

            {activeTab === 'dashboard' && (
              <div className="flex-1">
                <div className="bg-gray-800 p-4 rounded-xl shadow-inner mb-6">
                  <h3 className="text-lg font-semibold mb-2">Estado do Templum</h3>
                  <div className="flex items-center">
                    <div className={`w-3 h-3 rounded-full mr-2 ${isLoading ? 'bg-yellow-400' : 'bg-green-400'}`}></div>
                    <p className="text-sm">{isLoading ? 'Sintonizando...' : 'Sistema Estável'}</p>
                  </div>
                </div>

                <div className="bg-gray-800 p-4 rounded-xl shadow-inner mb-6">
                  <h3 className="text-lg font-semibold mb-2">Crystal Core</h3>
                  <p className="text-sm text-gray-400 mb-4">Núcleo de energia quântica para recodificação dimensional</p>
                  <div className="flex justify-center">
                    <button
                      onClick={activateEQ001}
                      className="bg-indigo-600 hover:bg-indigo-500 text-white font-bold py-2 px-4 rounded-full transition-all duration-300 shadow-lg hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-indigo-400 flex items-center"
                      disabled={isLoading}
                    >
                      <span className="text-xl mr-2">⚡</span> Ativar EQ001
                    </button>
                  </div>
                </div>

                {message && (
                  <div className="mt-4 p-4 bg-gray-800 rounded-xl shadow-inner">
                    <p className={`text-sm ${message.includes('sucesso') ? 'text-green-400' : 'text-yellow-400'}`}>
                      {message}
                    </p>
                  </div>
                )}
              </div>
            )}

            {activeTab === 'equations' && (
              <div className="flex-1">
                <div className="bg-gray-800 p-4 rounded-xl shadow-inner mb-6">
                  <h3 className="text-lg font-semibold mb-2">Simulação de Equação</h3>
                  <div className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">
                        Amplitude (A₀): {inputValues.amplitude}
                      </label>
                      <input
                        type="range"
                        name="amplitude"
                        min="0"
                        max="1000"
                        step="1"
                        value={inputValues.amplitude}
                        onChange={handleInputChange}
                        className="w-full h-2 bg-indigo-700 rounded-lg appearance-none cursor-pointer"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">
                        Frequência (ω): {inputValues.frequency}
                      </label>
                      <input
                        type="range"
                        name="frequency"
                        min="0"
                        max="100"
                        step="0.1"
                        value={inputValues.frequency}
                        onChange={handleInputChange}
                        className="w-full h-2 bg-indigo-700 rounded-lg appearance-none cursor-pointer"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-300 mb-1">
                        Fase (φ): {inputValues.phase.toFixed(2)}
                      </label>
                      <input
                        type="range"
                        name="phase"
                        min="0"
                        max="6.28"
                        step="0.01"
                        value={inputValues.phase}
                        onChange={handleInputChange}
                        className="w-full h-2 bg-indigo-700 rounded-lg appearance-none cursor-pointer"
                      />
                    </div>
                    <button
                      onClick={() => setMessage(`Simulando EQ: A0=${inputValues.amplitude}, ω=${inputValues.frequency}, φ=${inputValues.phase.toFixed(2)}`)}
                      className="w-full bg-blue-600 hover:bg-blue-500 text-white font-bold py-2 px-4 rounded-full transition-all duration-300 shadow-lg hover:shadow-xl focus:outline-none focus:ring-2 focus:ring-blue-400"
                    >
                      Simular Equação Quântica
                    </button>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'protection' && (
              <div className="flex-1">
                <div className="bg-gray-800 p-4 rounded-xl shadow-inner mb-6">
                  <h3 className="text-lg font-semibold mb-2">Escudo de Proteção</h3>
                  <p className="text-sm text-gray-400 mb-4">Sistema de defesa quântica baseado na EQ255</p>
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <span className="text-sm">Status do Escudo</span>
                      <span className="text-sm font-bold text-green-400">Ativo</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm">Frequência de Proteção</span>
                      <span className="text-sm font-bold">999 Hz</span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm">Nível de Segurança</span>
                      <span className="text-sm font-bold">Máximo</span>
                    </div>
                  </div>
                </div>
                
                <div className="bg-gray-800 p-4 rounded-xl shadow-inner">
                  <h3 className="text-lg font-semibold mb-2">Estatísticas do Sistema</h3>
                  <div className="space-y-3">
                    <div className="flex justify-between">
                      <span className="text-sm">Partículas Quânticas</span>
                      <span className="text-sm font-bold">1,000</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-sm">Dimensões Estáveis</span>
                      <span className="text-sm font-bold">12D</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-sm">Interferências Bloqueadas</span>
                      <span className="text-sm font-bold">0</span>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </aside>

        {/* Visualização 3D */}
        <div
          ref={mountRef}
          className="flex-1 w-full h-full bg-gray-950"
        />
      </div>
    </div>
  );
};

export default TemplumCosmica;
```