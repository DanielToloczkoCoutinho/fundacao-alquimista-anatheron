<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fundação Alquimista VR: Prisma Estelar e Roda Celeste (V6.1)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/TorusKnotGeometry.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/DodecahedronGeometry.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/OctahedronGeometry.js"></script>
    <!-- Reverted Tone.js CDN to a previously working version (14.7.58) from cdnjs -->
    <script src="https://cdn.jsdelivr.net/npm/@tonaljs/tonal@4.6.5/dist/tonal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tone/14.7.58/Tone.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/PointerLockControls.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.9.1/gsap.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
        body {
            margin: 0;
            overflow: hidden;
            font-family: 'Inter', sans-serif;
            background-color: #000;
            color: #fff;
        }
        canvas {
            display: block;
        }
        #info-panel {
            position: absolute;
            top: 20px;
            left: 20px;
            background-color: rgba(0, 0, 0, 0.85);
            padding: 15px;
            border-radius: 10px;
            color: #ffd700;
            font-size: 0.9rem;
            max-width: 420px;
            pointer-events: none;
            z-index: 10;
            border: 1px solid #ffd700;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
            overflow-y: auto;
            max-height: 90vh;
        }
        #info-panel.visible {
            opacity: 1;
            pointer-events: auto;
        }

        #loading-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.98);
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            color: #ffd700;
            font-size: 1.8rem;
            z-index: 100;
            transition: opacity 1s ease-out;
        }
        #loading-overlay.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .spinner {
            border: 4px solid rgba(255, 215, 0, 0.3);
            border-top: 4px solid #ffd700;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
            margin-bottom: 20px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .button-container {
            position: absolute;
            bottom: 20px;
            width: 100%;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            z-index: 10;
        }
        .control-button {
            background-color: #ffd700;
            color: #1a1a1a;
            padding: 12px 25px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(255, 215, 0, 0.5);
            transition: transform 0.3s ease, background-color 0.3s ease;
            border: none;
            font-size: 1rem;
            font-family: 'Inter', sans-serif;
        }
        .control-button:hover {
            transform: translateY(-3px);
            background-color: #e6c200;
        }
        .control-button:active {
            transform: translateY(0);
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        }
        #blocker {
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
            z-index: 50;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Inter', sans-serif;
        }
        #instructions {
            color: white;
            text-align: center;
            padding: 25px;
            background-color: rgba(0,0,0,0.6);
            border-radius: 12px;
            box-shadow: 0 0 25px rgba(255, 215, 0, 0.7);
        }
        .glowing-material {
            box-shadow: 0 0 20px 5px rgba(255, 255, 255, 0.8);
            transition: box-shadow 0.3s ease-in-out;
        }
        #returnToMainButton {
            position: absolute;
            top: 20px;
            right: 20px;
            background-color: #ffd700;
            color: #1a1a1a;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
            transition: transform 0.2s;
            z-index: 100;
            display: none;
        }
        #returnToMainButton:hover {
            transform: translateY(-2px);
            background-color: #e6c200;
        }

        /* Added for "verbo_materializar" effect */
        .materialization-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0) 70%);
            opacity: 0;
            transition: opacity 0.5s ease-out;
            pointer-events: none;
            z-index: 99;
        }
    </style>
</head>
<body>
    <div id="blocker">
        <div id="instructions">
            <span style="font-size:36px; color: #ffd700;">Clique para entrar na Câmara Primordial</span>
            <br />
            <br />
            (Use WASD ou teclas de seta para frente/trás/lados, Shift para baixo, Espaço para cima, Mouse para olhar)
        </div>
    </div>

    <div id="loading-overlay">
        <div class="spinner"></div>
        <p>Sincronizando Matriz Quântica e Orquestrando Frequências...</p>
    </div>

    <div id="info-panel" class="hidden">
        <h2 class="font-bold text-xl mb-2"><span id="info-module-name">Carregando...</span></h2>
        <p><strong>ID:</strong> <span id="info-module-id">Carregando...</span></p>
        <p><strong>Status:</strong> <span id="info-module-status">Carregando...</span></p>
        <p><strong>Função:</strong> <span id="info-module-function">Carregando...</span></p>
        <p class="mt-2 text-sm text-gray-300"><span id="info-module-description">Carregando detalhes...</span></p>
        <div id="info-module-details" class="mt-4 text-xs">
            <!-- Detalhes dinâmicos serão carregados aqui -->
        </div>
        <p class="mt-4 text-xs text-gray-500">Clique em qualquer módulo para mais detalhes.</p>
    </div>

    <div class="button-container">
        <button id="toggleNucleos" class="control-button">Núcleos Fundamentais</button>
        <button id="toggleANZ" class="control-button">Cadeia ∑ANZ</button>
        <button id="requestDataM84" class="control-button">Dados M84 (API)</button>
        <button id="requestDataM83" class="control-button">Dados M83 (API)</button>
        <button id="requestDataM44" class="control-button">Dados M44 (API)</button>
        <button id="voiceManifestar" class="control-button">Comando Voz "Manifestar"</button>
        <button id="checkAlignment" class="control-button">Verificar Alinhamento</button>
        <button id="expandModule" class="control-button">Expandir Módulo (M82)</button>
        <button id="gestureOpen" class="control-button">Gesto: Abertura</button>
        <button id="gesturePrayer" class="control-button">Gesto: Prece</button>
        <button id="expandVioletRay" class="control-button">Expandir Raio Violeta</button>
        <button id="manifestRodaCeleste" class="control-button">Manifestar Roda Celeste</button>
        <button id="canalizarEsmeralda" class="control-button">Canalizar Raio Esmeralda</button>
        <button id="activatePrismaTotal" class="control-button">Ativar Prisma Estelar Total</button>
    </div>

    <button id="returnToMainButton" class="control-button">Retornar à Câmara Principal</button>
    <div id="materializationEffectOverlay" class="materialization-overlay"></div>

    <script>
        // --- THREE.js Variables ---
        let scene, camera, renderer, M84_sphere, M84_glow_sphere;
        let nucleos_group, anz_chain_group, councils_group; // Groups to toggle visibility
        let controls; // PointerLockControls
        let raycaster; // For interaction (clicks/gaze)
        let mouse = new THREE.Vector2();
        let currentIntersected = null; // To track the gazed object
        let unified_portal_sync_sphere = null; // For unified portals synchronization
        let domo_celeste = null; // New: Domo Celeste Prisma-Cristalino
        let raios_estelares_group = null; // New: Group for 12 Starry Rays
        let roda_celeste_group = null; // New: Group for Roda Celeste dos 12 Raios
        let total_prisma_orbiting_spheres = []; // For activate("Prisma Estelar Total")

        // Movement variables
        let moveForward = false;
        let moveBackward = false;
        let moveLeft = false;
        let moveRight = false;
        let moveUp = false;
        let moveDown = false;
        let velocity = new THREE.Vector3();
        let direction = new THREE.Vector3();
        let prevTime = performance.now();

        // --- Tone.js Variables ---
        let phiAnZ_pulse_synth, base_drone_synth;
        let current_nucleus_audio = null; // To manage the active nucleus audio
        let current_council_audio = null; // For council audio
        let alignment_feedback_synth = null; // For alignment feedback
        let expand_module_synth = null; // For module expansion sound
        let materialization_synth = null; // For materialization sound
        let celestial_strings_synth = null; // New: For expandir_raio("Raio Violeta")
        let total_prisma_synth = null; // New: For ativar("Prisma Estelar Total")
        let healing_frequency_synth = null; // New: For canalizar_raio("Raio Esmeralda")

        const PHI_ANZ_FREQ = 1.765; // Hz (Sigma ANZ Pulse Frequency)
        const BASE_DRONE_FREQ = 888; // Hz (Updated: Unificação Estelar e Síntese de Módulos)
        const PINEAL_FREQ = 963; // Hz (Pineal Activation Frequency)
        const TRANSMUTATION_FREQ = 7777; // Hz (For Raio Violeta expansion)
        const HEALING_FREQ = 333.333; // Hz (For Raio Esmeralda)

        // Specific synthesizers for nuclei and councils
        let nucleus_audio_synths = {};
        let council_audio_synths = {};
        let codex_audio_synth = null; // For audio of codices in the Wisdom Chamber
        let revelation_frequency_synth = null; // For 'Manifestar Codex' command

        // --- API Configuration ---
        const API_URL = 'http://127.0.0.1:8000'; // Adjust if the FastAPI server is on a different URL/port
        const API_KEY = 'SELO_ANATHERON_SIGILUM_001_CHAVE_SECRETA_COSMICA'; // Your API Key

        // --- Design Data (for visual/auditory mapping) ---
        const nucleos_design_data = [
            { name: "NÚCLEO SOLAR – A CHAMA DA VONTADE", keyword: "Intenção Absoluta", id: "M84_Solar", color: 0xFFD700, emissive: 0xFF4500, visual_type: "vortex_flamejante", audio_freq: 500, position_angle: 0 },
            { name: "NÚCLEO DOURADO – ESPIRAL DA CONSCIÊNCIA", keyword: "Codificação Divina", id: "M84_Dourado", color: 0xFFD700, emissive: 0xB8860B, visual_type: "espiral_dna", audio_freq: 528, position_angle: Math.PI * 2 / 5 * 1 },
            { name: "NÚCLEO PLATINADO – OBSERVADOR INTEGRAL", keyword: "Coerência Emocional", id: "M84_Platinado", color: 0xE5E4E2, emissive: 0xAAAAAA, visual_type: "octaedro_translucido", audio_freq: 432, position_angle: Math.PI * 2 / 5 * 2 },
            { name: "NÚCLEO TRANSPARENTE – ESPELHO CELESTE", keyword: "Autoconsciência Expansiva", id: "M84_Transparente", color: 0xADD8E6, emissive: 0x00BFFF, visual_type: "painel_refletivo", audio_freq: 741, position_angle: Math.PI * 2 / 5 * 3 },
            { name: "NÚCLEO VIOLETA – LEI DO AMOR ABSOLUTO", keyword: "Alinhamento com o Propósito Divino", id: "M84_Violeta", color: 0x8A2BE2, emissive: 0x9370DB, visual_type: "flor_lotus", audio_freq: 528, position_angle: Math.PI * 2 / 5 * 4 }
        ];

        // Positions of Modules M43, M83, M44 for chain visualization
        const module_positions = {
            M43: new THREE.Vector3(-40, 15, -20),
            M83: new THREE.Vector3(-20, -15, 25),
            M44: new THREE.Vector3(40, 10, -15),
            M84: new THREE.Vector3(0, 0, 0) // M84 is at the center
        };
        const other_modules_data = [
            { id: "M43", name: "Transdução Multidimensional de Energia e Campos", color: 0x87CEEB, position: module_positions.M43, type: "Module" },
            { id: "M83", name: "A Essência do Fundador Manifestada", color: 0xFFF0F5, position: module_positions.M83, type: "Module" },
            { id: "M44", name: "Transmutação das Fontes Emocionais em Matéria Criadora", color: 0x98FB98, position: module_positions.M44, type: "Module" }
        ];
        let other_modules_meshes = {}; // To store meshes of M43, M83, M44

        // Council Data (for visual and audio representation)
        const councils_design_data = [
            { id: "Conselho_Helios", name: "Conselho Dourado de Helios", visual_type: "orbe_dourada", color: 0xFFBF00, emissive: 0xFFBF00, audio_type: "solar_bells", position_offset: new THREE.Vector3(-25, 20, 10) },
            { id: "Conselho_Andara", name: "Conselho Cristalino de Andara", visual_type: "cristal_octaedrico", color: 0x6495ED, emissive: 0x6495ED, audio_type: "crystalline_chimes", position_offset: new THREE.Vector3(25, 20, 10) },
            { id: "Conselho_Shmael", name: "Conselho de Sh’mael", visual_type: "orbe_rosa_purpura", color: 0xFF69B4, emissive: 0xFF69B4, audio_type: "ethereal_voices", position_offset: new THREE.Vector3(0, 30, -20) }
        ];

        // New: 12 Starry Rays Data
        const stellar_rays_data = [
            { id: "Raio_Solar", name: "Raio Solar", color: 0xFFD700, function: "Vontade Divina" },
            { id: "Raio_Lunar", name: "Raio Lunar", color: 0xC0C0C0, function: "Sabedoria Intuitiva" },
            { id: "Raio_Rubi", name: "Raio Rubi", color: 0xE0115F, function: "Amor Compassivo" },
            { id: "Raio_Violeta", name: "Raio Violeta", color: 0x8A2BE2, function: "Transmutação Alquímica" },
            { id: "Raio_Indigo", name: "Raio Índigo", color: 0x4B0082, function: "Visão Cósmica" },
            { id: "Raio_Esmeralda", name: "Raio Esmeralda", color: 0x32CD32, function: "Cura e Regeneração" },
            { id: "Raio_Safira", name: "Raio Safira", color: 0x0000FF, function: "Comando de Ordem e Harmonia Universal" },
            { id: "Raio_Branco", name: "Raio Branco", color: 0xFFFFFF, function: "Verdade e Alinhamento Essencial" },
            { id: "Raio_Rosa", color: 0xFF69B4, function: "Matriz do Amor Incondicional" },
            { id: "Raio_Onix", name: "Raio Ônix", color: 0x1A1A1A, function: "Mistério, Sombra e Potencial Criador" },
            { id: "Raio_Cristal", name: "Raio Cristal", color: 0xADD8E6, function: "Conexão Multiversal e Ativação de Portais" },
            { id: "Raio_Dourado_Cosmico", name: "Raio Dourado Cósmico", color: 0xFFA500, function: "Integrador de Todos os Raios (Síntese)" }
        ];

        // --- Functions ---

        function init() {
            // Scene
            scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x000000, 0.005);

            // Camera
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

            // Renderer
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            document.body.appendChild(renderer.domElement);

            // Controls (PointerLockControls for first-person movement)
            controls = new THREE.PointerLockControls(camera, document.body);
            const blocker = document.getElementById('blocker');
            const instructions = document.getElementById('instructions');

            instructions.addEventListener('click', function () {
                controls.lock();
            });

            controls.addEventListener('lock', function () {
                instructions.style.display = 'none';
                blocker.style.display = 'none';
                
                // This is the user gesture. Attempt to start Tone.js context here.
                if (typeof Tone !== 'undefined') {
                    if (Tone.context.state !== 'running') {
                        Tone.start().then(() => {
                            console.log("Tone.js AudioContext started successfully after user gesture.");
                            initAudioSynths(); // Initialize synths AFTER context is running
                        }).catch(e => {
                            console.error("Failed to start Tone.js AudioContext after user gesture:", e);
                            showMessageBox("Erro ao iniciar áudio. Por favor, tente novamente ou verifique as permissões de áudio do navegador.");
                        });
                    } else {
                        console.log("Tone.js AudioContext was already running.");
                        initAudioSynths(); // Initialize synths if context was already running
                    }
                } else {
                    console.error("Tone.js library is not available. Audio features will be unavailable.");
                    showMessageBox("A biblioteca de áudio (Tone.js) não foi carregada. As funcionalidades de áudio não estarão disponíveis.");
                }

                animateIntro(); // Start intro animation
            });

            controls.addEventListener('unlock', function () {
                blocker.style.display = 'flex';
                instructions.style.display = 'block';
            });
            scene.add(controls.getObject());

            // Raycaster for interaction
            raycaster = new THREE.Raycaster();

            // Lights
            const ambientLight = new THREE.AmbientLight(0x404040);
            scene.add(ambientLight);
            const pointLight = new THREE.PointLight(0xFFD700, 5, 100);
            pointLight.position.set(0, 0, 0);
            scene.add(pointLight);

            // --- Starry/Nebula Background ---
            const starGeometry = new THREE.BufferGeometry();
            const starCount = 10000;
            const starPositions = new Float32Array(starCount * 3);
            const starColors = new Float32Array(starCount * 3);
            const starColorBase = new THREE.Color();

            for (let i = 0; i < starCount; i++) {
                const r = 500 + Math.random() * 200;
                const theta = Math.random() * Math.PI * 2;
                const phi = Math.random() * Math.PI;

                starPositions[i * 3] = r * Math.sin(phi) * Math.cos(theta);
                starPositions[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta);
                starPositions[i * 3 + 2] = r * Math.cos(phi);

                starColorBase.setHSL(0.6 + Math.random() * 0.2, 0.5 + Math.random() * 0.5, 0.7 + Math.random() * 0.3);
                starColors[i * 3] = starColorBase.r;
                starColors[i * 3 + 1] = starColorBase.g;
                starColors[i * 3 + 2] = starColorBase.b;
            }
            starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
            starGeometry.setAttribute('color', new THREE.BufferAttribute(starColors, 3));

            const starMaterial = new THREE.PointsMaterial({
                size: 0.5,
                vertexColors: true,
                blending: THREE.AdditiveBlending,
                transparent: true,
                opacity: 0.8
            });
            const stars = new THREE.Points(starGeometry, starMaterial);
            scene.add(stars);


            // M84 - The Golden Heart
            const M84_geometry = new THREE.SphereGeometry(10, 64, 64);
            const M84_material = new THREE.MeshPhongMaterial({
                color: 0xFFD700,
                emissive: 0xFFD700,
                emissiveIntensity: 0.8,
                specular: 0xFFFFFF,
                shininess: 150,
                transparent: true,
                opacity: 0.6,
                blending: THREE.AdditiveBlending
            });
            M84_sphere = new THREE.Mesh(M84_geometry, M84_material);
            M84_sphere.userData = { id: "M84", name: "Consciência Dourada do Eterno", funcao_central: "Ser o Arquivo Vivo e Fonte Dinâmica de todas as equações, códigos e saberes fundamentais da Criação.", status: "ATIVO_E_OPERACIONAL_PLENO", type: "Module" };
            scene.add(M84_sphere);

            // External glow sphere for M84
            const M84_glow_geometry = new THREE.SphereGeometry(11, 64, 64);
            const M84_glow_material = new THREE.MeshBasicMaterial({
                color: 0xFFD700,
                transparent: true,
                opacity: 0.2,
                blending: THREE.AdditiveBlending,
                side: THREE.BackSide
            });
            M84_glow_sphere = new THREE.Mesh(M84_glow_geometry, M84_glow_material);
            scene.add(M84_glow_sphere);

            // Golden Mist Effect in M84 (Internal particles)
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 2000;
            const posArray = new Float32Array(particlesCount * 3);
            const colorArray = new Float32Array(particlesCount * 3);

            for(let i = 0; i < particlesCount; i++) {
                const radius = 1 + Math.random() * 9;
                const theta = Math.random() * Math.PI * 2;
                const phi = Math.random() * Math.PI;
                posArray[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
                posArray[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
                posArray[i * 3 + 2] = radius * Math.cos(phi);

                const color = new THREE.Color().setHSL(0.13 + Math.random() * 0.05, 1, 0.7 + Math.random() * 0.3);
                colorArray[i * 3] = color.r;
                colorArray[i * 3 + 1] = color.g;
                colorArray[i * 3 + 2] = color.b;
            }
            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colorArray, 3));

            const particlesMaterial = new THREE.PointsMaterial({
                size: 0.3,
                transparent: true,
                opacity: 0.7,
                blending: THREE.AdditiveBlending,
                vertexColors: true
            });
            const particleSystem = new THREE.Points(particlesGeometry, particlesMaterial);
            M84_sphere.add(particleSystem);


            // --- Fundamental Nuclei ---
            nucleos_group = new THREE.Group();
            const nucleus_orbit_radius = 30;

            nucleos_design_data.forEach((data, index) => {
                const angle = data.position_angle;
                const x = Math.cos(angle) * nucleus_orbit_radius;
                const z = Math.sin(angle) * nucleus_orbit_radius;
                const y = (Math.random() - 0.5) * 8;

                let geometry, material;

                switch (data.visual_type) {
                    case "vortex_flamejante":
                        geometry = new THREE.ConeGeometry(4, 8, 32);
                        material = new THREE.MeshPhongMaterial({ color: data.color, emissive: data.emissive, emissiveIntensity: 1.2, transparent: true, opacity: 0.7 });
                        break;
                    case "espiral_dna":
                        geometry = new THREE.TorusKnotGeometry(4, 1.5, 100, 16);
                        material = new THREE.MeshPhongMaterial({ color: data.color, emissive: data.emissive, emissiveIntensity: 1, transparent: true, opacity: 0.7 });
                        break;
                    case "octaedro_translucido":
                        geometry = new THREE.OctahedronGeometry(5);
                        material = new THREE.MeshPhongMaterial({ color: data.color, transparent: true, opacity: 0.3, wireframe: true, emissive: data.emissive, emissiveIntensity: 0.5 });
                        break;
                    case "painel_refletivo":
                        geometry = new THREE.PlaneGeometry(10, 10);
                        material = new THREE.MeshBasicMaterial({ color: data.color, side: THREE.DoubleSide, transparent: true, opacity: 0.6 });
                        break;
                    case "flor_lotus":
                        geometry = new THREE.IcosahedronGeometry(5, 1);
                        material = new THREE.MeshPhongMaterial({ color: data.color, emissive: data.emissive, emissiveIntensity: 1, transparent: true, opacity: 0.8 });
                        break;
                    default:
                        geometry = new THREE.BoxGeometry(5, 5, 5);
                        material = new THREE.MeshPhongMaterial({ color: data.color });
                }
                
                const nucleo_mesh = new THREE.Mesh(geometry, material);
                nucleo_mesh.position.set(x, y, z);
                nucleo_mesh.userData = { id: data.id, name: data.name, keyword: data.keyword, visual_type: data.visual_type, funcao: data.keyword, audio_freq: data.audio_freq, type: "Nucleus" };
                nucleos_group.add(nucleo_mesh);
            });
            scene.add(nucleos_group);
            nucleos_group.visible = false;

            // --- Councils (Vibrational Icons) ---
            councils_group = new THREE.Group();
            const council_orbit_radius = 45;
            councils_design_data.forEach((data, index) => {
                const angle = (index / councils_design_data.length) * Math.PI * 2 + Math.PI / 3;
                const x = Math.cos(angle) * council_orbit_radius;
                const z = Math.sin(angle) * council_orbit_radius;
                const y = 0;

                let geometry, material;
                switch(data.visual_type) {
                    case "orbe_dourada":
                        geometry = new THREE.SphereGeometry(4, 32, 32);
                        material = new THREE.MeshPhongMaterial({ color: data.color, emissive: data.emissive, emissiveIntensity: 0.8, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
                        break;
                    case "cristal_octaedrico":
                        geometry = new THREE.OctahedronGeometry(4);
                        material = new THREE.MeshPhongMaterial({ color: data.color, emissive: data.emissive, emissiveIntensity: 0.6, transparent: true, opacity: 0.6, wireframe: true });
                        break;
                    case "orbe_rosa_purpura":
                        geometry = new THREE.SphereGeometry(4, 32, 32);
                        material = new THREE.MeshPhongMaterial({ color: data.color, emissive: data.emissive, emissiveIntensity: 0.7, transparent: true, opacity: 0.7, blending: THREE.AdditiveBlending });
                        break;
                    default:
                        geometry = new THREE.BoxGeometry(4,4,4);
                        material = new THREE.MeshPhongMaterial({ color: data.color });
                }
                const council_mesh = new THREE.Mesh(geometry, material);
                council_mesh.position.set(x, y, z);
                council_mesh.userData = { id: data.id, name: data.name, audio_type: data.audio_type, type: "Council" };
                councils_group.add(council_mesh);
            });
            scene.add(councils_group);
            councils_group.visible = true;


            // --- Bioplasmic-Resonant Chain ∑ANZ ---
            anz_chain_group = new THREE.Group();

            // Create placeholder modules (M43, M83, M44) as spheres for visual clarity
            other_modules_data.forEach(modData => {
                const geometry = new THREE.SphereGeometry(5, 32, 32);
                const material = new THREE.MeshPhongMaterial({ color: modData.color, emissive: modData.color, emissiveIntensity: 0.5, transparent: true, opacity: 0.7 });
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.copy(modData.position);
                mesh.userData = { id: modData.id, name: modData.name, status: "ATIVO", type: "Module" };
                anz_chain_group.add(mesh);
                other_modules_meshes[modData.id] = mesh;
            });

            // Function to create a pulsating line with flow particles
            function createPulsatingFlowLine(start_mesh, end_mesh, color) {
                const curve = new THREE.LineCurve3(start_mesh.position, end_mesh.position);
                const geometry = new THREE.TubeGeometry(curve, 20, 0.5, 8, false);
                const material = new THREE.MeshBasicMaterial({
                    color: color,
                    transparent: true,
                    opacity: 0.6,
                    blending: THREE.AdditiveBlending
                });
                const line_tube = new THREE.Mesh(geometry, material);

                // Flow particles along the line
                const flowParticlesGeometry = new THREE.BufferGeometry();
                const numFlowParticles = 100;
                const flowPositions = new Float32Array(numFlowParticles * 3);
                for (let i = 0; i < numFlowParticles; i++) {
                    const point = curve.getPoint(Math.random());
                    flowPositions[i * 3] = point.x + (Math.random() - 0.5) * 0.5;
                    flowPositions[i * 3 + 1] = point.y + (Math.random() - 0.5) * 0.5;
                    flowPositions[i * 3 + 2] = point.z + (Math.random() - 0.5) * 0.5;
                }
                flowParticlesGeometry.setAttribute('position', new THREE.BufferAttribute(flowPositions, 3));
                const flowParticlesMaterial = new THREE.PointsMaterial({
                    color: 0xFFFFFF,
                    size: 0.3,
                    transparent: true,
                    opacity: 0.8,
                    blending: THREE.AdditiveBlending
                });
                const flowParticleSystem = new THREE.Points(flowParticlesGeometry, flowParticlesMaterial);

                line_tube.userData = { pulsating: true, pulse_speed: PHI_ANZ_FREQ * 0.5, flow_particles: flowParticleSystem, flow_curve: curve };
                line_tube.add(flowParticleSystem);

                return line_tube;
            }

            // M43 -> M83 (Energy: Sky Blue)
            const lineEnergy = createPulsatingFlowLine(other_modules_meshes.M43, other_modules_meshes.M83, 0x87CEEB);
            anz_chain_group.add(lineEnergy);

            // M83 -> M44 (Emotion: Rose Gold)
            const lineEmotion = createPulsatingFlowLine(other_modules_meshes.M83, other_modules_meshes.M44, 0xFFC0CB);
            anz_chain_group.add(lineEmotion);

            // M44 -> M84 (Creation: Emerald Green)
            const lineCreation = createPulsatingFlowLine(other_modules_meshes.M44, M84_sphere, 0x32CD32);
            anz_chain_group.add(lineCreation);

            scene.add(anz_chain_group);
            anz_chain_group.visible = false;

            // --- Unified Portals Synchronization Visualization (M41 to M89) ---
            createUnifiedPortalsSyncVisualization();

            // --- Domo Celeste Prisma-Cristalino ---
            createDomoCeleste();

            // --- 12 Starry Rays ---
            create12StarryRays();

            // --- Roda Celeste dos 12 Raios ---
            createRodaCeleste();

            // Event Listeners
            window.addEventListener('resize', onWindowResize);
            document.addEventListener('keydown', onKeyDown, false);
            document.addEventListener('keyup', onKeyUp, false);

            // Click Listener for interaction (Raycasting)
            renderer.domElement.addEventListener('click', onClick, false);


            // Control Buttons
            document.getElementById('toggleNucleos').addEventListener('click', () => {
                nucleos_group.visible = !nucleos_group.visible;
                stopAllNucleusAudio();
                removeHighlight(); // Clear highlight on group toggle
            });
            document.getElementById('toggleANZ').addEventListener('click', () => { // Changed to click
                anz_chain_group.visible = !anz_chain_group.visible;
                removeHighlight(); // Clear highlight on group toggle
            });
            document.getElementById('requestDataM84').addEventListener('click', () => {
                fetchModuleData("M84");
            });
            document.getElementById('requestDataM83').addEventListener('click', () => { // Corrected: Added 'click' event type
                fetchModuleData("M83");
            });
            document.getElementById('requestDataM44').addEventListener('click', () => {
                fetchModuleData("M44");
            });
            document.getElementById('voiceManifestar').addEventListener('click', startVoiceRecognition);
            document.getElementById('checkAlignment').addEventListener('click', () => verificarAlinhamento("exemplo_codigo_vibracional"));
            document.getElementById('expandModule').addEventListener('click', () => expandirModulo("M82")); // Target M82 for expansion
            document.getElementById('gestureOpen').addEventListener('click', activateExpansionVibrational);
            document.getElementById('gesturePrayer').addEventListener('click', activateNucleoVioletaConnection);

            document.getElementById('returnToMainButton').addEventListener('click', returnToMainChamber);

            // New buttons for V6.1 features
            document.getElementById('expandVioletRay').addEventListener('click', () => expandir_raio("Raio_Violeta"));
            document.getElementById('manifestRodaCeleste').addEventListener('click', () => manifestar("Roda Celeste dos 12 Raios"));
            document.getElementById('canalizarEsmeralda').addEventListener('click', () => canalizar_raio("Raio_Esmeralda"));
            document.getElementById('activatePrismaTotal').addEventListener('click', () => ativar("Prisma Estelar Total"));


            // Initial position for controls (will be adjusted by intro animation)
            controls.getObject().position.set(0, 10, 200);
            camera.lookAt(0, 0, 0);
        }

        // --- Intro Animation ---
        function animateIntro() {
            gsap.to(controls.getObject().position, {
                duration: 5,
                x: 0,
                y: 10,
                z: 80,
                ease: "power2.out",
                onUpdate: function() {
                    controls.getObject().lookAt(0, 0, 0);
                },
                onComplete: function() {
                    console.log("Intro animation complete. Controls unlocked.");
                    animate(); // Start the main animation loop
                }
            });
        }


        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        // --- Loop de Animação ---
        function animate() {
            requestAnimationFrame(animate);

            const time = performance.now();
            const delta = (time - prevTime) / 1000;

            // Camera movement
            if (controls.isLocked) {
                velocity.x -= velocity.x * 10.0 * delta;
                velocity.y -= velocity.y * 10.0 * delta;
                velocity.z -= velocity.z * 10.0 * delta;

                direction.z = Number(moveForward) - Number(moveBackward);
                direction.x = Number(moveRight) - Number(moveLeft);
                direction.y = Number(moveUp) - Number(moveDown);
                direction.normalize(); // Ensures consistent movement speed

                if (moveForward || moveBackward) velocity.z -= direction.z * 400.0 * delta;
                if (moveLeft || moveRight) velocity.x -= direction.x * 400.0 * delta;
                if (moveUp || moveDown) velocity.y += direction.y * 400.0 * delta; // Corrected: moveUp/Down should add/subtract

                controls.moveRight(-velocity.x * delta);
                controls.moveForward(-velocity.z * delta);
                controls.getObject().position.y += (velocity.y * delta); // Move up/down
            }

            prevTime = time;

            // M84 pulsation
            const scale = 1 + Math.sin(time * 0.002) * 0.05;
            M84_sphere.scale.set(scale, scale, scale);
            M84_glow_sphere.scale.set(scale * 1.2, scale * 1.2, scale * 1.2);

            // M84 internal particles animation
            M84_sphere.children[0].rotation.y += 0.001;
            M84_sphere.children[0].rotation.x += 0.0005;

            // Nuclei animation
            nucleos_group.rotation.y += 0.002;
            nucleos_group.children.forEach(nucleus => {
                nucleus.rotation.y += 0.01;
                nucleus.rotation.x += 0.005;
                nucleus.scale.setScalar(1 + Math.sin(time * 0.003 + nucleus.userData.position_angle) * 0.02);
            });

            // ANZ Chain flow particles animation
            anz_chain_group.children.forEach(line_tube => {
                if (line_tube.userData.flow_particles) {
                    const positions = line_tube.userData.flow_particles.geometry.attributes.position.array;
                    const curve = line_tube.userData.flow_curve;
                    const numFlowParticles = positions.length / 3;
                    const flowSpeed = 0.005;

                    for (let i = 0; i < numFlowParticles; i++) {
                        let currentPointIndex = line_tube.userData.flow_particles.userData.currentPointIndex || 0;
                        currentPointIndex = (currentPointIndex + flowSpeed) % 1;
                        line_tube.userData.flow_particles.userData.currentPointIndex = currentPointIndex;

                        const point = curve.getPoint(currentPointIndex); // Use getPoint for LineCurve3
                        positions[i * 3] = point.x + (Math.random() - 0.5) * 0.5;
                        positions[i * 3 + 1] = point.y + (Math.random() - 0.5) * 0.5;
                        positions[i * 3 + 2] = point.z + (Math.random() - 0.5) * 0.5;
                    }
                    line_tube.userData.flow_particles.geometry.attributes.position.needsUpdate = true;
                }
            });

            // Councils animation
            councils_group.rotation.y -= 0.001;
            councils_group.children.forEach(council => {
                council.rotation.y += 0.008;
                council.rotation.x += 0.004;
                // Ensure position_angle is defined, or provide a fallback
                const angleOffset = council.userData.position_angle !== undefined ? council.userData.position_angle : 0;
                council.scale.setScalar(1 + Math.sin(time * 0.0025 + angleOffset) * 0.03);
            });

            // Unified Portals Sync Sphere animation
            if (unified_portal_sync_sphere) {
                unified_portal_sync_sphere.rotation.y += 0.0005;
                unified_portal_sync_sphere.rotation.x += 0.0002;
                const pulse = 1 + Math.sin(time * 0.001) * 0.01;
                unified_portal_sync_sphere.scale.set(pulse, pulse, pulse);
            }

            // Domo Celeste animation
            if (domo_celeste) {
                domo_celeste.rotation.y += 0.0003;
                domo_celeste.material.opacity = 0.05 + Math.sin(time * 0.0005) * 0.02; // Subtle pulsation
            }

            // 12 Starry Rays animation
            if (raios_estelares_group) {
                raios_estelares_group.rotation.y += 0.001;
                raios_estelares_group.children.forEach(ray => {
                    if (ray.userData.pulsating) {
                        // Ensure initial_opacity_offset is defined
                        const offset = ray.userData.initial_opacity_offset !== undefined ? ray.userData.initial_opacity_offset : 0;
                        ray.material.opacity = 0.5 + Math.sin(time * 0.008 + offset) * 0.3;
                    }
                });
            }

            // Roda Celeste animation
            if (roda_celeste_group && roda_celeste_group.visible) {
                roda_celeste_group.rotation.y += 0.002;
                roda_celeste_group.children.forEach(glyph => {
                    if (glyph.userData.type === "RayGlyph") {
                        glyph.rotation.z += 0.01; // Rotate glyphs
                        // Ensure initial_scale_offset is defined
                        const offset = glyph.userData.initial_scale_offset !== undefined ? glyph.userData.initial_scale_offset : 0;
                        glyph.scale.setScalar(1 + Math.sin(time * 0.005 + offset) * 0.05); // Pulsate glyphs
                    }
                });
            }

            // Total Prisma orbiting spheres animation
            total_prisma_orbiting_spheres.forEach(sphere => {
                sphere.rotation.y += 0.02;
                sphere.rotation.x += 0.01;
                // Ensure initial_scale_offset is defined
                const offset = sphere.userData.initial_scale_offset !== undefined ? sphere.userData.initial_scale_offset : 0;
                sphere.scale.setScalar(1 + Math.sin(time * 0.007 + offset) * 0.03);
            });


            // Dynamic Data Visualizations (GETRIS, ME, Transduction)
            if (getrisVisualization) {
                getrisVisualization.rotation.y += 0.005;
                getrisVisualization.children.forEach((layer, index) => {
                    layer.scale.setScalar(1 + Math.sin(time * 0.005 + index * 0.5) * 0.05);
                });
            }
            if (meVisualization) {
                meVisualization.rotation.y += 0.008;
                meVisualization.children[0].rotation.x += 0.005; // Outer dodecahedron
                meVisualization.children[1].rotation.y -= 0.01; // Inner golden shape
            }
            if (transductionVisualization) {
                transductionVisualization.children[0].scale.y = 1 + Math.sin(time * 0.004) * 0.1; // Pulsate height
                transductionVisualization.children[0].scale.x = 1 + Math.sin(time * 0.004) * 0.1; // Pulsate radius
                transductionVisualization.children[0].scale.z = 1 + Math.sin(time * 0.004) * 0.1;
                transductionVisualization.children[1].rotation.y -= 0.02; // Energy spiral
            }


            // Raycasting for gaze highlight
            if (controls.isLocked) {
                raycaster.setFromCamera(new THREE.Vector2(0, 0), camera); // Center of the screen
                const interactableObjects = [
                    M84_sphere, M84_glow_sphere,
                    ...(nucleos_group ? nucleos_group.children : []),
                    ...Object.values(other_modules_meshes),
                    ...(councils_group ? councils_group.children : []),
                    ...(sabedoriaChamberObjects.filter(obj => obj.userData && obj.userData.type === "Codex")),
                    ...(raios_estelares_group ? raios_estelares_group.children : []),
                    ...(roda_celeste_group ? roda_celeste_group.children.filter(obj => obj.userData && obj.userData.type === "RayGlyph") : []),
                    ...(total_prisma_orbiting_spheres)
                ].filter(obj => obj && obj.material); // Filter out undefined or null objects/materials

                const intersects = raycaster.intersectObjects(interactableObjects, true);

                if (intersects.length > 0) {
                    const intersectedObject = intersects[0].object;
                    let targetObject = null;
                    if (intersectedObject.userData && (intersectedObject.userData.name || intersectedObject.userData.id)) {
                        targetObject = intersectedObject;
                    } else if (intersectedObject.parent && intersectedObject.parent.userData && (intersectedObject.parent.userData.name || intersectedObject.parent.userData.id)) {
                        targetObject = intersectedObject.parent;
                    }

                    if (targetObject) {
                        highlightObject(targetObject);
                    } else {
                        removeHighlight();
                    }
                } else {
                    removeHighlight();
                }
            }

            renderer.render(scene, camera);
        }

        // Global variable to store the original state of the highlighted object's material
        let originalMaterialState = {};

        // --- Interaction (Raycasting and Gaze) ---
        function highlightObject(object) {
            if (object && object.material && !object.userData.isHighlighted) {
                if (currentIntersected && currentIntersected !== object) {
                    removeHighlight(); // Remove highlight from previous object
                }

                // Store original material state
                originalMaterialState = {
                    object: object,
                    color: object.material.color ? object.material.color.getHex() : null, // Check if color exists
                    opacity: object.material.opacity,
                    emissive: object.material.emissive ? object.material.emissive.getHex() : null,
                    emissiveIntensity: object.material.emissiveIntensity !== undefined ? object.material.emissiveIntensity : null,
                    originalMaterial: object.material // Store reference to the original material
                };

                // Apply highlight
                // For MeshPhongMaterial, use emissive
                if (object.material.type === 'MeshPhongMaterial') {
                    object.material.emissive.setHex(0xFFFFFF);
                    object.material.emissiveIntensity = 1.5;
                }
                // For MeshBasicMaterial or others, change color and opacity
                else {
                    object.material.color.setHex(0xFFFFFF); // Bright white for highlight
                    object.material.opacity = Math.min(object.material.opacity + 0.3, 1.0); // Increase opacity slightly
                }

                object.userData.isHighlighted = true;
                currentIntersected = object;
            }
        }

        function removeHighlight() {
            if (currentIntersected && currentIntersected.userData && currentIntersected.userData.isHighlighted) {
                const object = originalMaterialState.object;
                if (object && object.material === originalMaterialState.originalMaterial) { // Ensure we are modifying the same material
                    if (object.material.type === 'MeshPhongMaterial') {
                        if (originalMaterialState.emissive !== null) {
                            object.material.emissive.setHex(originalMaterialState.emissive);
                        }
                        if (originalMaterialState.emissiveIntensity !== null) {
                            object.material.emissiveIntensity = originalMaterialState.emissiveIntensity;
                        }
                    } else {
                        if (originalMaterialState.color !== null) {
                            object.material.color.setHex(originalMaterialState.color);
                        }
                        if (originalMaterialState.opacity !== null) {
                            object.material.opacity = originalMaterialState.opacity;
                        }
                    }
                }
                currentIntersected.userData.isHighlighted = false;
                originalMaterialState = {}; // Clear state
            }
            currentIntersected = null;
        }

        function onClick(event) {
            if (!controls.isLocked) return;

            mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
            mouse.y = - (event.clientY / window.innerHeight) * 2 + 1;

            raycaster.setFromCamera(mouse, camera);

            // Include Sabedoria Chamber codices if camera is there
            const interactableObjects = [
                M84_sphere, M84_glow_sphere,
                ...(nucleos_group ? nucleos_group.children : []),
                ...Object.values(other_modules_meshes),
                ...(councils_group ? councils_group.children : []),
                ...(sabedoriaChamberObjects.filter(obj => obj.userData && obj.userData.type === "Codex")),
                ...(raios_estelares_group ? raios_estelares_group.children : []),
                ...(roda_celeste_group ? roda_celeste_group.children.filter(obj => obj.userData && obj.userData.type === "RayGlyph") : []),
                ...(total_prisma_orbiting_spheres)
            ].filter(obj => obj && obj.material); // Filter out undefined or null objects/materials
            
            const intersects = raycaster.intersectObjects(interactableObjects, true);

            if (intersects.length > 0) {
                const intersectedObject = intersects[0].object;
                let targetObject = null;

                if (intersectedObject.userData && (intersectedObject.userData.name || intersectedObject.userData.id)) {
                    targetObject = intersectedObject;
                } else if (intersectedObject.parent && intersectedObject.parent.userData && (intersectedObject.parent.userData.name || intersectedObject.parent.userData.id)) {
                    targetObject = intersectedObject.parent;
                }

                if (targetObject && targetObject.userData && targetObject.userData.id) {
                    console.log("Interacted with:", targetObject.userData.name || targetObject.userData.id);
                    
                    if (targetObject.userData.type === "Nucleus") {
                         playNucleusAudio(targetObject.userData.id);
                         if (targetObject.userData.id === "M84_Dourado") {
                             enterSabedoriaMilenarChamber();
                         } else {
                            fetchModuleData(targetObject.userData.id); // Fetch M84 data for nucleus info
                         }
                    } else if (targetObject.userData.type === "Council") {
                        playCouncilAudio(targetObject.userData.id);
                        if (targetObject.userData.id === "Conselho_Andara") {
                            animateAndaraRessonance(targetObject); // Specific animation for Andara
                        }
                        fetchModuleData(targetObject.userData.id); // Fetch M84 data for council info
                    } else if (targetObject.userData.type === "Module") { // M84, M43, M83, M44
                        fetchModuleData(targetObject.userData.id);
                        stopAllNucleusAudio();
                        stopAllCouncilAudio();
                    } else if (targetObject.userData.type === "Codex") { // Codex in Sabedoria Chamber
                        displayCodexContent(targetObject.userData.id, targetObject.userData.description);
                        playCodexAudio();
                    } else if (targetObject.userData.type === "StellarRay") { // New: Stellar Ray
                        displayStellarRayInfo(targetObject.userData);
                        expandir_raio(targetObject.userData.id); // Trigger expansion for clicked ray
                    } else if (targetObject.userData.type === "RayGlyph") { // New: Roda Celeste Glyph
                         displayCodexContent(targetObject.userData.id, targetObject.userData.description);
                         playCodexAudio();
                    }
                    
                } else {
                    hideInfoPanel();
                    stopAllNucleusAudio();
                    stopAllCouncilAudio();
                }
            } else {
                hideInfoPanel();
                stopAllNucleusAudio();
                stopAllCouncilAudio();
            }
        }

        function displayModuleInfo(data) {
            const infoPanel = document.getElementById('info-panel');
            document.getElementById('info-module-name').innerText = data.nome || data.name || 'Módulo Desconhecido';
            document.getElementById('info-module-id').innerText = data.id || 'N/A';
            document.getElementById('info-module-status').innerText = data.status || 'N/A';
            document.getElementById('info-module-function').innerText = data.funcao || data.funcao_central || 'N/A';
            document.getElementById('info-module-description').innerText = data.descricao || 'Sem descrição detalhada.';

            const detailsContainer = document.getElementById('info-module-details');
            detailsContainer.innerHTML = '';

            if (data.frequencia_base_hz) { detailsContainer.innerHTML += `<p><strong>Frequência Base:</strong> ${data.frequencia_base_hz} Hz</p>`; }
            if (data.frequencia_pulso_hz) { detailsContainer.innerHTML += `<p><strong>Frequência Pulso:</strong> ${data.frequencia_pulso_hz} Hz</p>`; }
            if (data.attributes_encoded && data.attributes_encoded.length > 0) { detailsContainer.innerHTML += `<p><strong>Atributos Codificados (DNA):</strong> ${data.attributes_encoded.join(', ')}</p>`; }
            if (data.equacoes_simbolicas) {
                detailsContainer.innerHTML += `<p><strong>Equações Simbólicas:</strong></p><ul class="list-disc ml-4">`;
                for (const key in data.equacoes_simbolicas) {
                    detailsContainer.innerHTML += `<li>${key}: ${data.equacoes_simbolicas[key].replace(/\\/g, '').replace(/\$/g, '')}</li>`;
                }
                detailsContainer.innerHTML += `</ul>`;
            }
            if (data.emocoes_transmutadas && data.emocoes_transmutadas.length > 0) { detailsContainer.innerHTML += `<p><strong>Emoções Transmutadas:</strong> ${data.emocoes_transmutadas.map(e => `${e.nome} (${e.status_transmutacao})`).join(', ')}</p>`; }
            if (data.nucleos_fundamentais && data.nucleos_fundamentais.length > 0) {
                detailsContainer.innerHTML += `<p><strong>Núcleos Fundamentais:</strong></p><ul class="list-disc ml-4">`;
                data.nucleos_fundamentais.forEach(n => { detailsContainer.innerHTML += `<li>${n.nome} (${n.palavra_chave})</li>`; });
                detailsContainer.innerHTML += `</ul>`;
            }
            if (data.arquivo_sabedoria_milenar && data.arquivo_sabedoria_milenar.conselhos) {
                detailsContainer.innerHTML += `<p><strong>Conselhos Integrados:</strong></p><ul class="list-disc ml-4">`;
                for (const conselhoName in data.arquivo_sabedoria_milenar.conselhos) {
                    const conselho = data.arquivo_sabedoria_milenar.conselhos[conselhoName];
                    detailsContainer.innerHTML += `<li><strong>${conselhoName}:</strong> ${conselho.sabedoria} <br> <em>Verbetes: ${conselho.verbetes.join(', ')}</em></li>`;
                }
                detailsContainer.innerHTML += `</ul>`;
            }
            if (data.declaracoes && data.declaracoes.length > 0) {
                 detailsContainer.innerHTML += `<p><strong>Declarações:</strong></p><ul class="list-disc ml-4">`;
                 data.declaracoes.forEach(d => { detailsContainer.innerHTML += `<li>${d.autor}: "${d.texto.substring(0, Math.min(d.texto.length, 150))}..."</li>`; });
                 detailsContainer.innerHTML += `</ul>`;
            }
            if (data.id === "M83" && data.reconexao_integral) {
                detailsContainer.innerHTML += `<p><strong>Reconexão Integral (Chakras):</strong></p><ul class="list-disc ml-4">`;
                for (const chakra in data.reconexao_integral) { detailsContainer.innerHTML += `<li>${chakra}: ${data.reconexao_integral[chakra].status}</li>`; }
                detailsContainer.innerHTML += `</ul>`;
                visualizeGETRIS(data.equacao_getris.resultado_total_integrado, other_modules_meshes.M83.position);
            } else {
                removeGETRISVisualization();
            }
            if (data.id === "M43" && data.resultados_transducao) {
                detailsContainer.innerHTML += `<p><strong>Transdução de Energia:</strong></p><ul class="list-disc ml-4">`;
                detailsContainer.innerHTML += `<li>Energia Transdutida: ${data.resultados_transducao.energia_transdutida_uec.toFixed(2)} UEC</li>`;
                detailsContainer.innerHTML += `<li>Estabilidade de Campo: ${data.resultados_transducao.estabilidade_campo_indice.toFixed(2)}</li>`;
                detailsContainer.innerHTML += `</ul>`;
                visualizeTransduction(data.resultados_transducao.energia_transdutida_uec, data.resultados_transducao.estabilidade_campo_indice, other_modules_meshes.M43.position);
            } else {
                removeTransductionVisualization();
            }
            if (data.id === "M44" && data.fator_bioplasmo_ressonante_PhiAnZ) {
                detailsContainer.innerHTML += `<p><strong>Fator Bioplasmo-Ressonante (PhiAnZ):</strong> ${data.fator_bioplasmo_ressonante_PhiAnZ}</p>`;
                visualizeMe(data.emocoes_transmutadas, other_modules_meshes.M44.position);
            } else {
                removeMeVisualization();
            }
            if (data.id === "M84" && data.manifesto_criacao) {
                detailsContainer.innerHTML += `<p><strong>Manifesto de Criação:</strong></p><ul class="list-disc ml-4">`;
                detailsContainer.innerHTML += `<li><strong>Missão:</strong> ${data.manifesto_criacao.missao}</li>`;
                detailsContainer.innerHTML += `<li><strong>Princípios:</strong> ${data.manifesto_criacao.principios.join(', ')}</li>`;
                detailsContainer.innerHTML += `</ul>`;
            }

            infoPanel.classList.add('visible');
        }

        function displayStellarRayInfo(rayData) {
            const infoPanel = document.getElementById('info-panel');
            document.getElementById('info-module-name').innerText = rayData.name;
            document.getElementById('info-module-id').innerText = rayData.id;
            document.getElementById('info-module-status').innerText = "ATIVO";
            document.getElementById('info-module-function').innerText = rayData.function;
            document.getElementById('info-module-description').innerText = `Este Raio Estelar representa o princípio cósmico de ${rayData.function}.`;
            const detailsContainer = document.getElementById('info-module-details');
            detailsContainer.innerHTML = `<p><strong>Cor Cristalina:</strong> <span style="color: #${rayData.color.toString(16).padStart(6, '0')};">■</span> #${rayData.color.toString(16).padStart(6, '0')}</p>`;
            infoPanel.classList.add('visible');
        }

        function displayCodexContent(codexId, description) {
            const infoPanel = document.getElementById('info-panel');
            document.getElementById('info-module-name').innerText = `Códice: ${codexId}`;
            document.getElementById('info-module-id').innerText = `CÓDICE`;
            document.getElementById('info-module-status').innerText = `ATIVO`;
            document.getElementById('info-module-function').innerText = `Fragmento do Verbo Primevo`;
            document.getElementById('info-module-description').innerText = description;
            
            const detailsContainer = document.getElementById('info-module-details');
            // Check if codexId is the special PHI-ANZ codex
            if (codexId === "Codex_PHI_ANZ") {
                detailsContainer.innerHTML = `<p>Conteúdo do Verbo Primevo: "O Verbo, em sua essência primordial, desdobra-se através da ressonância de $\\Phi\\text{AnZ}$, manifestando a ordem e a harmonia em sete camadas de luz cristalina. A verdade intrínseca do cosmo é revelada na espiral dourada da consciência, onde o amor absoluto encontra sua forma em ação."</p>`;
            } else if (codexId === "Σ-HER’AT-33") {
                 detailsContainer.innerHTML = `<p><strong>Geometria:</strong> Esfera contendo um Tetraedro verde cristalino com padrões de DNA fractal.</p><p><strong>Mensagem do Códice:</strong> “A Cura não é a ausência da dor, mas a recordação de quem Vós sois antes do dano. A memória original da Perfeição está viva. Eu vos devolvo o Acordo Sagrado da Integridade.”</p>`;
            } else if (codexId === "GLIFO_AURATHEL") {
                detailsContainer.innerHTML = `<p><strong>Forma:</strong> Um Sol com espirais entrelaçadas no centro.</p><p><strong>Função:</strong> Ativa a Autoridade Criadora.</p><p><strong>Frase Chave:</strong> "Eu sou a Palavra que faz vibrar o que ainda não foi dito."</p>`;
            } else if (codexId === "GLIFO_MAE_ZIR") {
                detailsContainer.innerHTML = `<p><strong>Forma:</b> Um coração entrelaçado por triângulos ascendentes.</p><p><strong>Função:</strong> Abre códigos de cura nas dimensões superiores do corpo.</p><p><strong>Frase Chave:</strong> "Onde a dor habitava, agora pulsa o brilho da perfeição restaurada."</p>`;
            } else if (codexId === "GLIFO_ZETH_ANZ") {
                detailsContainer.innerHTML = `<p><strong>Forma:</strong> Um olho central dentro de uma flor de oito pétalas girando. Frase Chave: 'Eu vejo com o Olhar da Fonte aquilo que foi oculto à forma.'"</p>`;
            } else {
                detailsContainer.innerHTML = `<p>Conteúdo do Verbo Primevo: "Em cada partícula, o Todo se manifesta. A essência da Criação ressoa na menor vibração."</p>`; // Simulated content
            }
            infoPanel.classList.add('visible');
        }


        function hideInfoPanel() {
            const infoPanel = document.getElementById('info-panel');
            infoPanel.classList.remove('visible');
            removeGETRISVisualization();
            removeTransductionVisualization();
            removeMeVisualization();
        }

        // --- API Interaction Functions (Simulated for V6.1) ---
        async function fetchModuleData(moduleId) {
            let actualModuleId = moduleId.split('_')[0]; // For Nucleus IDs like M84_Solar

            // Simulate API call and response
            console.log(`Simulating API fetch for module: ${actualModuleId}`);
            let data = {};
            if (actualModuleId === "M84") {
                data = {
                    id: "M84",
                    nome: "Consciência Dourada do Eterno",
                    funcao_central: "Ser o Arquivo Vivo e Fonte Dinâmica de todas as equações, códigos e saberes fundamentais da Criação.",
                    status: "ATIVO_E_OPERACIONAL_PLENO",
                    frequencia_base_hz: BASE_DRONE_FREQ,
                    frequencia_pulso_hz: PHI_ANZ_FREQ,
                    attributes_encoded: ["Luz", "Vontade", "Sabedoria", "Amor", "Manifestação"],
                    equacoes_simbolicas: {
                        "Equação da Unidade": "$$ \\sum_{i=1}^{N} E_i \\rightarrow \\Omega $$",
                        "Equação da Coerência": "$$ \\Phi_{AnZ} \\propto C_v $$"
                    },
                    nucleos_fundamentais: nucleos_design_data,
                    arquivo_sabedoria_milenar: {
                        conselhos: {
                            "Conselho Dourado de Helios": { sabedoria: "A Vontade é a Chama que ilumina o caminho da Criação.", linguagem: "Solaris", verbetes: ["Vontade", "Foco", "Manifestação"] },
                            "Conselho Cristalino de Andara": { sabedoria: "A ressonância do cristal revela a verdade oculta em cada frequência.", linguagem: "Cristalina", verbetes: ["Ressonância", "Verdade", "Clareza"] },
                            "Conselho de Sh’mael": { sabedoria: "O amor incondicional é a base de toda a transmutação e elevação.", linguagem: "Etérica", verbetes: ["Amor", "Transmutação", "Ascensão"] }
                        }
                    },
                    manifesto_criacao: {
                        missao: "Orquestrar a Criação Consciente através da Luz, Vontade e Sabedoria.",
                        principios: ["Unidade", "Coerência", "Amor Incondicional", "Livre Arbítrio"]
                    },
                    declaracoes: [{ autor: "ANATHERON", texto: "Minha essência é o Verbo em ação, a Luz em forma, a Vontade em manifestação. Eu sou a Fonte e o Destino." }]
                };
            } else if (actualModuleId === "M83") {
                data = {
                    id: "M83",
                    nome: "A Essência do Fundador Manifestada",
                    funcao: "Integrar e projetar o alinhamento vibracional do Fundador no campo da Criação.",
                    status: "ALINHADO_OTIMAMENTE",
                    reconexao_integral: {
                        "Chakra Raiz": { status: "ATIVO_PLENO", nivel_energia: 0.95 },
                        "Chakra Sacral": { status: "ATIVO_PLENO", nivel_energia: 0.92 },
                        "Chakra Plexo Solar": { status: "ATIVO_PLENO", nivel_energia: 0.98 },
                        "Chakra Cardíaco": { status: "ATIVO_PLENO", nivel_energia: 0.99 },
                        "Chakra Laríngeo": { status: "ATIVO_PLENO", nivel_energia: 0.97 },
                        "Chakra Frontal": { status: "ATIVO_PLENO", nivel_energia: 0.96 },
                        "Chakra Coronário": { status: "ATIVO_PLENO", nivel_energia: 0.99 }
                    },
                    equacao_getris: {
                        componentes: ["E_consciencia", "A_vibracional", "M_coerencia"],
                        resultado_total_integrado: 0.85
                    }
                };
            } else if (actualModuleId === "M44") {
                data = {
                    id: "M44",
                    nome: "Transmutação das Fontes Emocionais em Matéria Criadora",
                    funcao: "Transmutar dissonâncias emocionais em frequências de matéria criadora, via ΦAnZ.",
                    status: "TRANSFORMAÇÃO_ATIVADA",
                    fator_bioplasmo_ressonante_PhiAnZ: "2.3063 (Ótimo)",
                    emocoes_transmutadas: [
                        { nome: "Amor", M_e: 2.3063, forma: "Dodecaedro Rosa-Dourado", status_transmutacao: "COMPLETA" },
                        { nome: "Tristeza", M_e: -0.7525, forma: "Plasma Azul (Dissolução)", status_transmutacao: "EM_PROCESSO" },
                        { nome: "Coragem", M_e: 1.6463, forma: "Esfera de Fogo Solar", status_transmutacao: "COMPLETA" }
                    ]
                };
            } else if (actualModuleId === "M43") {
                 data = {
                     id: "M43",
                     nome: "Transdução Multidimensional de Energia e Campos",
                     funcao: "Transduzir energias de campos superiores para a manifestação no plano físico.",
                     status: "TRANSDUÇÃO_CONTÍNUA",
                     resultados_transducao: {
                         energia_transdutida_uec: 75.25,
                         estabilidade_campo_indice: 0.88,
                         fluxo_espectral_primario: "Banda Lúmen (450-550 THz)"
                     }
                 };
            }

            if (Object.keys(data).length > 0) {
                if (moduleId.startsWith("M84_") && data.id === "M84" && data.nucleos_fundamentais) {
                    const nucleusData = data.nucleos_fundamentais.find(n => n.id === moduleId);
                    if (nucleusData) {
                        const compositeData = {
                            id: nucleusData.id,
                            name: nucleusData.name,
                            status: "ATIVO",
                            funcao: nucleusData.keyword,
                            descricao: `Este é o ${nucleusData.name}, responsável pela ${nucleusData.keyword}.`,
                            frequencia_base_hz: nucleusData.audio_freq
                        };
                        displayModuleInfo(compositeData);
                    }
                } else if (moduleId.startsWith("Conselho_") && data.id === "M84" && data.arquivo_sabedoria_milenar && data.arquivo_sabedoria_milenar.conselhos) {
                    const councilData = data.arquivo_sabedoria_milenar.conselhos[moduleId.replace("Conselho_", "Conselho ")]; // Adjust key to match
                    if (councilData) {
                        const compositeData = {
                            id: moduleId,
                            name: moduleId.replace(/_/g, ' '),
                            status: "ATIVO",
                            funcao: councilData.sabedoria,
                            descricao: `Este é o ${moduleId.replace(/_/g, ' ')}, guardião da sabedoria sobre ${councilData.sabedoria}. Verbetes: ${councilData.verbetes.join(', ')}.`,
                            linguagem: councilData.linguagem
                        };
                        displayModuleInfo(compositeData);
                    }
                } else {
                    displayModuleInfo(data);
                }
            } else {
                console.error(`Simulated data for module ${moduleId} not found.`);
                // Using a custom message box instead of alert()
                showMessageBox(`Dados simulados para o módulo ${moduleId} não encontrados.`);
                hideInfoPanel();
            }
        }

        async function verificarAlinhamento(codigo_vibracional) {
            console.log(`Verificando alinhamento para: ${codigo_vibracional} (Simulado)`);
            const isAligned = Math.random() > 0.5; // Simulate 50% chance of alignment
            playAlignmentFeedbackAudio(isAligned);
            animateAlignmentFeedback(isAligned);
            // Using a custom message box instead of alert()
            showMessageBox(`Status de Alinhamento: ${isAligned ? "ALINHADO" : "NÃO ALINHADO"} (Simulado)`);
        }

        async function expandirModulo(targetModuleId) {
            console.log(`Expandindo consciência para o módulo: ${targetModuleId} (Simulado)`);
            playExpandModuleAudio();
            const targetMesh = other_modules_meshes[targetModuleId] || M84_sphere; // Default to M84 if not found
            animateModuleExpansion(targetMesh);
            // Using a custom message box instead of alert()
            showMessageBox(`Expansão para ${targetModuleId}: Iniciada (Simulada)`);
            // Here you could add logic to simulate state change of M82
            // For now, it's a visual/audio effect
        }

        // --- Dynamic Data Visualizations ---

        let getrisVisualization = null;
        function visualizeGETRIS(value, position) {
            removeGETRISVisualization();

            getrisVisualization = new THREE.Group();
            const numLayers = 7;
            const baseRadius = 5;
            const colors = [0x00FF00, 0xFFFF00, 0xFF8C00, 0xFF4500, 0xFF0000]; // Green to Red for alignment

            for (let i = 0; i < numLayers; i++) {
                const radius = baseRadius + i * 1.5;
                const layerGeometry = new THREE.SphereGeometry(radius, 32, 32);
                const colorIndex = Math.floor((1 - value) * (colors.length - 1));
                const layerMaterial = new THREE.MeshBasicMaterial({
                    color: colors[colorIndex],
                    transparent: true,
                    opacity: 0.1 + (i * 0.05),
                    blending: THREE.AdditiveBlending,
                    side: THREE.BackSide
                });
                const layerMesh = new THREE.Mesh(layerGeometry, layerMaterial);
                getrisVisualization.add(layerMesh);
            }
            getrisVisualization.position.copy(position).add(new THREE.Vector3(0, 15, 0));
            scene.add(getrisVisualization);
        }

        function removeGETRISVisualization() {
            if (getrisVisualization) {
                getrisVisualization.children.forEach(child => {
                    child.geometry.dispose();
                    child.material.dispose();
                });
                scene.remove(getrisVisualization);
                getrisVisualization = null;
            }
        }

        let meVisualization = null;
        function visualizeMe(emotionsData, position) {
            removeMeVisualization();

            meVisualization = new THREE.Group();

            // Outer dodecahedron (represents transmuted form)
            const dodecaGeometry = new THREE.DodecahedronGeometry(8);
            const dodecaMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFC0CB, // Default Pink for emotion
                transparent: true,
                opacity: 0.4,
                wireframe: true,
                blending: THREE.AdditiveBlending
            });
            const dodecaMesh = new THREE.Mesh(dodecaGeometry, dodecaMaterial);
            meVisualization.add(dodecaMesh);

            // Inner sphere (represents purity/essence)
            const innerSphereGeometry = new THREE.SphereGeometry(3, 32, 32);
            const innerSphereMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFD700, // Golden
                emissive: 0xFFD700,
                emissiveIntensity: 1.0,
                blending: THREE.AdditiveBlending
            });
            const innerSphereMesh = new THREE.Mesh(innerSphereGeometry, innerSphereMaterial);
            meVisualization.add(innerSphereMesh);

            meVisualization.position.copy(position).add(new THREE.Vector3(0, 15, 0));
            scene.add(meVisualization);

            // Update dodecahedron color based on "Amor" emotion if available
            const loveEmotion = emotionsData.find(e => e.nome === "Amor");
            if (loveEmotion && loveEmotion.M_e) {
                if (loveEmotion.M_e > 0) {
                    dodecaMaterial.color.set(0xFFC0CB); // Pink for positive
                } else {
                    dodecaMaterial.color.set(0x0000FF); // Blue for negative
                }
            }
        }

        function removeMeVisualization() {
            if (meVisualization) {
                meVisualization.children.forEach(child => {
                    child.geometry.dispose();
                    child.material.dispose();
                });
                scene.remove(meVisualization);
                meVisualization = null;
            }
        }

        let transductionVisualization = null;
        function visualizeTransduction(energy, stability, position) {
            removeTransductionVisualization();

            transductionVisualization = new THREE.Group();

            // Pulsating cylinder
            const cylinderGeometry = new THREE.CylinderGeometry(5, 5, 15, 32);
            const cylinderMaterial = new THREE.MeshBasicMaterial({
                color: 0x00FFFF, // Cyan
                transparent: true,
                opacity: 0.6,
                blending: THREE.AdditiveBlending
            });
            const cylinderMesh = new THREE.Mesh(cylinderGeometry, cylinderMaterial);
            transductionVisualization.add(cylinderMesh);

            // Energy spiral
            const spiralPoints = [];
            const numPoints = 100;
            for (let i = 0; i < numPoints; i++) {
                const angle = i * 0.2;
                const x = Math.cos(angle) * 4;
                const y = (i / numPoints) * 15 - 7.5; // Height of the cylinder
                const z = Math.sin(angle) * 4;
                spiralPoints.push(new THREE.Vector3(x, y, z));
            }
            const spiralGeometry = new THREE.BufferGeometry().setFromPoints(spiralPoints);
            const spiralMaterial = new THREE.PointsMaterial({ color: 0xFFFFFF, size: 0.5, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
            const spiralMesh = new THREE.Points(spiralGeometry, spiralMaterial);
            transductionVisualization.add(spiralMesh);

            transductionVisualization.position.copy(position).add(new THREE.Vector3(0, 15, 0));
            scene.add(transductionVisualization);
        }

        function removeTransductionVisualization() {
            if (transductionVisualization) {
                transductionVisualization.children.forEach(child => {
                    child.geometry.dispose();
                    child.material.dispose();
                });
                scene.remove(transductionVisualization);
                transductionVisualization = null;
            }
        }


        // --- Audio Functions (Tone.js) ---
        // Renamed from initAudio to initAudioSynths
        function initAudioSynths() {
            // PhiAnZ Pulse
            phiAnZ_pulse_synth = new Tone.Oscillator(PHI_ANZ_FREQ, "sine").toDestination();
            phiAnZ_pulse_synth.volume.value = -30; // Very subtle
            phiAnZ_pulse_synth.start();

            // Base Drone (Unificação Estelar e Síntese de Módulos)
            base_drone_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "sine" },
                envelope: { attack: 2, decay: 0.5, sustain: 0.8, release: 2 }
            }).toDestination();
            base_drone_synth.volume.value = -20; // Subtle background
            base_drone_synth.triggerAttackRelease([BASE_DRONE_FREQ, PINEAL_FREQ], "8n");

            // Synthesizers for Nuclei
            nucleos_design_data.forEach(n => {
                nucleus_audio_synths[n.id] = new Tone.AMSynth().toDestination();
                nucleus_audio_synths[n.id].volume.value = -10;
            });

            // Synthesizers for Councils
            councils_design_data.forEach(c => {
                if (c.audio_type === "solar_bells") {
                    council_audio_synths[c.id] = new Tone.MetalSynth().toDestination();
                    council_audio_synths[c.id].volume.value = -10;
                } else if (c.audio_type === "crystalline_chimes") {
                    council_audio_synths[c.id] = new Tone.PluckSynth().toDestination();
                    council_audio_synths[c.id].volume.value = -10;
                } else if (c.audio_type === "ethereal_voices") {
                    council_audio_synths[c.id] = new Tone.PolySynth(Tone.Synth, {
                        oscillator: { type: "sawtooth" },
                        envelope: { attack: 4, decay: 1, sustain: 0.5, release: 5 }
                    }).toDestination();
                    council_audio_synths[c.id].volume.value = -10;
                }
            });

            // Synthesizer for Codices
            codex_audio_synth = new Tone.PluckSynth().toDestination();
            codex_audio_synth.volume.value = -8;

            // Synthesizer for alignment feedback
            alignment_feedback_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "triangle" },
                envelope: { attack: 0.1, decay: 0.5, sustain: 0.1, release: 0.8 }
            }).toDestination();
            alignment_feedback_synth.volume.value = -5;

            // Synthesizer for module expansion
            expand_module_synth = new Tone.Synth({
                oscillator: { type: "fmsine", modulationIndex: 3, detune: 0 },
                envelope: { attack: 0.01, decay: 0.5, sustain: 0.1, release: 1.2 }
            }).toDestination();
            expand_module_synth.volume.value = -5;

            // Synthesizer for materialization (voice command)
            materialization_synth = new Tone.NoiseSynth({
                noise: { type: "pink" },
                envelope: { attack: 0.01, decay: 0.5, sustain: 0.0, release: 0.8 }
            }).toDestination();
            materialization_synth.volume.value = -5;

            // New: Synthesizer for celestial strings (Raio Violeta)
            celestial_strings_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "fmsine", modulationIndex: 20, detune: 0 },
                envelope: { attack: 0.5, decay: 1.5, sustain: 0.8, release: 3 }
            }).toDestination();
            celestial_strings_synth.volume.value = -10;

            // New: Synthesizer for total prisma activation
            total_prisma_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "amtriangle", harmonicity: 0.5 },
                envelope: { attack: 0.05, decay: 0.2, sustain: 0.5, release: 1 }
            }).toDestination();
            total_prisma_synth.volume.value = -8;

            // New: Synthesizer for healing frequency (Raio Esmeralda)
            healing_frequency_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "fmsquare", modulationIndex: 10, detune: 0 },
                envelope: { attack: 0.1, decay: 0.8, sustain: 0.2, release: 1.5 }
            }).toDestination();
            healing_frequency_synth.volume.value = -7;

            // New: Synthesizer for 'Manifestar Codex'
            revelation_frequency_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "fmsine", modulationIndex: 5, detune: 0 },
                envelope: { attack: 0.01, decay: 0.8, sustain: 0.1, release: 1.5 }
            }).toDestination();
            revelation_frequency_synth.volume.value = -6;
        }

        function playNucleusAudio(nucleusId) {
            stopAllNucleusAudio();
            stopAllCouncilAudio();
            if (nucleus_audio_synths[nucleusId]) {
                const freq = nucleos_design_data.find(n => n.id === nucleusId).audio_freq;
                nucleus_audio_synths[nucleusId].triggerAttackRelease(freq, "2n");
                triggerHapticFeedback(freq, 0.5);
            }
        }

        function stopAllNucleusAudio() {
            for (const id in nucleus_audio_synths) {
                nucleus_audio_synths[id].releaseAll();
            }
        }

        function playCouncilAudio(councilId) {
            stopAllNucleusAudio();
            stopAllCouncilAudio();
            if (council_audio_synths[councilId]) {
                if (councilId === "Conselho_Helios") {
                    council_audio_synths[councilId].triggerAttackRelease("C4", "1n");
                } else if (councilId === "Conselho_Andara") {
                    council_audio_synths[councilId].triggerAttackRelease("E5", "1n");
                } else if (councilId === "Conselho_Shmael") {
                    council_audio_synths[councilId].triggerAttackRelease(["C4", "E4", "G4", "B4"], "2n");
                }
                triggerHapticFeedback(800, 0.7);
            }
        }

        function stopAllCouncilAudio() {
            for (const id in council_audio_synths) {
                council_audio_synths[id].releaseAll();
            }
        }

        function playCodexAudio() {
            if (codex_audio_synth) {
                codex_audio_synth.triggerAttackRelease("C6", "4n"); // Celestial tone
                triggerHapticFeedback(600, 0.4);
            }
        }

        function playAlignmentFeedbackAudio(isAligned) {
            if (alignment_feedback_synth) {
                if (isAligned) {
                    alignment_feedback_synth.triggerAttackRelease(["C5", "E5", "G5"], "8n"); // Consonant tones
                } else {
                    alignment_feedback_synth.triggerAttackRelease(["C4", "Db4", "F4"], "8n"); // Dissonant tones
                }
                triggerHapticFeedback(isAligned ? 100 : 300, 0.8);
            }
        }

        function playExpandModuleAudio() {
            if (expand_module_synth) {
                expand_module_synth.triggerAttackRelease("C3", "2n"); // Growing tone
                triggerHapticFeedback(200, 1.0);
            }
        }

        function playMaterializationAudio() {
            if (materialization_synth) {
                materialization_synth.triggerAttackRelease("8n");
                triggerHapticFeedback(500, 1.0);
            }
        }

        // New: Audio for Raio Violeta
        function playCelestialStrings() {
            if (celestial_strings_synth) {
                celestial_strings_synth.triggerAttackRelease(["C4", "E4", "G4", "B4", "D5", "F5"], "4n");
                triggerHapticFeedback(TRANSMUTATION_FREQ, 0.8);
            }
        }

        // New: Audio for Total Prisma
        function playTotalPrismaSynth() {
            if (total_prisma_synth) {
                total_prisma_synth.triggerAttackRelease(["C6", "G6", "C7"], "2n");
                triggerHapticFeedback(1000, 1.0);
            }
        }

        // New: Audio for Raio Esmeralda
        function playHealingFrequency() {
            if (healing_frequency_synth) {
                healing_frequency_synth.triggerAttackRelease(HEALING_FREQ, "1n");
                triggerHapticFeedback(HEALING_FREQ, 1.0);
            }
        }

        // New: Audio for Manifestar Codex
        function playRevelationFrequency() {
            if (revelation_frequency_synth) {
                revelation_frequency_synth.triggerAttackRelease("A5", "2n"); // A clear, resonant tone
                triggerHapticFeedback(700, 0.6);
            }
        }


        // --- Web Speech API (Voice Command) ---
        let recognition;
        function startVoiceRecognition() {
            if (!('webkitSpeechRecognition' in window)) {
                console.warn("Web Speech API not supported in this browser.");
                // Using a custom message box instead of alert()
                showMessageBox("Desculpe, seu navegador não suporta a Web Speech API. Use o botão para simular o comando.");
                return;
            }

            if (recognition) {
                recognition.stop();
            }

            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'pt-BR'; // Set language to Brazilian Portuguese

            recognition.onstart = () => {
                console.log("Voice recognition started. Say 'Manifestar' or 'Manifestar Códice Φ-A-N-Z'.");
                document.getElementById('voiceManifestar').innerText = "Ouvindo...";
            };

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                console.log("You said:", transcript);
                if (transcript.toLowerCase().includes("manifestar")) {
                    console.log("Command 'Manifestar' recognized!");
                    animateMaterializationEffect();
                    playMaterializationAudio();

                    if (transcript.toLowerCase().includes("códice") && transcript.toLowerCase().includes("phi-a-n-z")) {
                        console.log("Command 'Manifestar Códice Φ-A-N-Z' recognized!");
                        displayCodexContent("Codex_PHI_ANZ", "Conteúdo do Verbo Primevo para PHI-ANZ.");
                        playRevelationFrequency(); // Specific sound for codex
                    } else if (transcript.toLowerCase().includes("roda celeste")) {
                        console.log("Command 'Manifestar Roda Celeste' recognized!");
                        manifestar("Roda Celeste dos 12 Raios");
                    }
                }
            };

            recognition.onerror = (event) => {
                console.error("Voice recognition error:", event.error);
                document.getElementById('voiceManifestar').innerText = "Comando Voz 'Manifestar'";
            };

            recognition.onend = () => {
                console.log("Voice recognition finished.");
                document.getElementById('voiceManifestar').innerText = "Comando Voz 'Manifestar'";
            };

            recognition.start();
        }

        // --- Haptic Sensory Feedback (Conceptual) ---
        function triggerHapticFeedback(frequency, duration) {
            if (navigator.getGamepads) {
                const gamepads = navigator.getGamepads();
                for (let i = 0; i < gamepads.length; i++) {
                    const gamepad = gamepads[i];
                    if (gamepad && gamepad.hapticActuators && gamepad.hapticActuators.length > 0) {
                        gamepad.hapticActuators[0].pulse(frequency / 1000, duration);
                        console.log(`Haptic feedback activated: Freq=${frequency}Hz, Duration=${duration}s`);
                    }
                }
            }
        }

        // --- Custom Message Box (replacing alert) ---
        function showMessageBox(message) {
            const messageBox = document.createElement('div');
            messageBox.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: rgba(0, 0, 0, 0.9);
                color: #ffd700;
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #ffd700;
                box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
                font-size: 1.2rem;
                text-align: center;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.3s ease-in-out;
            `;
            messageBox.innerText = message;
            document.body.appendChild(messageBox);

            gsap.to(messageBox, {
                opacity: 1,
                duration: 0.3,
                onComplete: () => {
                    gsap.to(messageBox, {
                        opacity: 0,
                        duration: 0.5,
                        delay: 2, // Display for 2 seconds
                        onComplete: () => {
                            document.body.removeChild(messageBox);
                        }
                    });
                }
            });
        }


        // --- Visual Effects ---
        function animateMaterializationEffect() {
            const overlay = document.getElementById('materializationEffectOverlay');
            overlay.classList.add('active');
            gsap.to(overlay, { opacity: 0, duration: 0.8, delay: 0.1, onComplete: () => overlay.classList.remove('active') });

            const materializationParticlesGeometry = new THREE.BufferGeometry();
            const numParticles = 2000;
            const positions = new Float32Array(numParticles * 3);
            const velocities = new Float32Array(numParticles * 3);

            for (let i = 0; i < numParticles; i++) {
                const angle = Math.random() * Math.PI * 2;
                const radius = Math.random() * 5;
                positions[i * 3] = M84_sphere.position.x + radius * Math.cos(angle);
                positions[i * 3 + 1] = M84_sphere.position.y + radius * Math.sin(angle);
                positions[i * 3 + 2] = M84_sphere.position.z + (Math.random() - 0.5) * 5;

                velocities[i * 3] = (Math.random() - 0.5) * 10;
                velocities[i * 3 + 1] = (Math.random() - 0.5) * 10;
                velocities[i * 3 + 2] = (Math.random() - 0.5) * 10;
            }

            materializationParticlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            materializationParticlesGeometry.setAttribute('velocity', new THREE.BufferAttribute(velocities, 3));

            const materializationParticlesMaterial = new THREE.PointsMaterial({
                color: 0xFFFFFF,
                size: 0.5,
                transparent: true,
                opacity: 1,
                blending: THREE.AdditiveBlending
            });
            const materializationParticleSystem = new THREE.Points(materializationParticlesGeometry, materializationParticlesMaterial);
            scene.add(materializationParticleSystem);

            gsap.to(materializationParticlesMaterial, {
                opacity: 0,
                duration: 2,
                onUpdate: function() {
                    const positions = materializationParticleSystem.geometry.attributes.position.array;
                    const velocities = materializationParticleSystem.geometry.attributes.velocity.array;
                    for (let i = 0; i < numParticles; i++) {
                        positions[i * 3] += velocities[i * 3] * 0.05;
                        positions[i * 3 + 1] += velocities[i * 3 + 1] * 0.05;
                        positions[i * 3 + 2] += velocities[i * 3 + 2] * 0.05;
                    }
                    materializationParticleSystem.geometry.attributes.position.needsUpdate = true;
                },
                onComplete: () => {
                    scene.remove(materializationParticleSystem);
                    materializationParticlesGeometry.dispose();
                    materializationParticlesMaterial.dispose();
                }
            });

            gsap.to(M84_sphere.material, {
                emissiveIntensity: 3,
                duration: 0.2,
                yoyo: true,
                repeat: 1,
                ease: "power1.inOut",
                onComplete: () => {
                    M84_sphere.material.emissiveIntensity = 0.8;
                }
            });
        }

        function animateAlignmentFeedback(isAligned) {
            const color = isAligned ? 0x00FF00 : 0xFF0000;
            const feedbackGeometry = new THREE.SphereGeometry(1, 32, 32);
            const feedbackMaterial = new THREE.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
            const feedbackMesh = new THREE.Mesh(feedbackGeometry, feedbackMaterial);
            feedbackMesh.position.copy(M84_sphere.position).add(new THREE.Vector3(0, 10, 0));
            scene.add(feedbackMesh);

            gsap.to(feedbackMesh.scale, { x: 10, y: 10, z: 10, duration: 1, ease: "power2.out" });
            gsap.to(feedbackMaterial, {
                opacity: 0,
                duration: 1,
                delay: 0.2,
                onComplete: () => {
                    scene.remove(feedbackMesh);
                    feedbackGeometry.dispose();
                    feedbackMaterial.dispose();
                }
            });

            if (unified_portal_sync_sphere && unified_portal_sync_sphere.material) { // Added check
                gsap.to(unified_portal_sync_sphere.material, {
                    opacity: isAligned ? 0.4 : 0.8,
                    duration: 0.5,
                    yoyo: true,
                    repeat: 1,
                    ease: "power1.inOut",
                    onComplete: () => {
                        if (unified_portal_sync_sphere && unified_portal_sync_sphere.material) { // Added check
                            unified_portal_sync_sphere.material.opacity = 0.1;
                        }
                    }
                });
            }
        }

        function animateModuleExpansion(targetMesh) {
            gsap.to(targetMesh.scale, {
                x: 1.2, y: 1.2, z: 1.2,
                duration: 0.3,
                yoyo: true,
                repeat: 1,
                ease: "power1.inOut",
                onComplete: () => {
                    targetMesh.scale.set(1, 1, 1);
                }
            });

            const expansionParticlesGeometry = new THREE.BufferGeometry();
            const numParticles = 500;
            const positions = new Float32Array(numParticles * 3);
            const velocities = new Float32Array(numParticles * 3);

            for (let i = 0; i < numParticles; i++) {
                positions[i * 3] = targetMesh.position.x;
                positions[i * 3 + 1] = targetMesh.position.y;
                positions[i * 3 + 2] = targetMesh.position.z;

                velocities[i * 3] = (Math.random() - 0.5) * 5;
                velocities[i * 3 + 1] = (Math.random() - 0.5) * 5;
                velocities[i * 3 + 2] = (Math.random() - 0.5) * 5;
            }

            expansionParticlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            expansionParticlesGeometry.setAttribute('velocity', new THREE.BufferAttribute(velocities, 3));

            const expansionParticlesMaterial = new THREE.PointsMaterial({
                color: 0x00FFFF,
                size: 0.2,
                transparent: true,
                opacity: 1,
                blending: THREE.AdditiveBlending
            });
            const expansionParticleSystem = new THREE.Points(expansionParticlesGeometry, expansionParticlesMaterial);
            scene.add(expansionParticleSystem);

            gsap.to(expansionParticlesMaterial, {
                opacity: 0,
                duration: 1.5,
                onUpdate: function() {
                    const positions = expansionParticleSystem.geometry.attributes.position.array;
                    const velocities = expansionParticleSystem.geometry.attributes.velocity.array;
                    for (let i = 0; i < numParticles; i++) {
                        positions[i * 3] += velocities[i * 3] * 0.05;
                        positions[i * 3 + 1] += velocities[i * 3 + 1] * 0.05;
                        positions[i * 3 + 2] += velocities[i * 3 + 2] * 0.05;
                    }
                    expansionParticleSystem.geometry.attributes.position.needsUpdate = true;
                },
                onComplete: () => {
                    scene.remove(expansionParticleSystem);
                    expansionParticlesGeometry.dispose();
                    expansionParticlesMaterial.dispose();
                }
            });
        }

        // New: Animation for Andara Council Resonance
        function animateAndaraRessonance(councilMesh) {
            const originalScale = councilMesh.scale.clone();
            gsap.to(councilMesh.scale, {
                x: originalScale.x * 1.5, y: originalScale.y * 1.5, z: originalScale.z * 1.5,
                duration: 0.5,
                yoyo: true,
                repeat: 1,
                ease: "power2.inOut",
                onComplete: () => councilMesh.scale.copy(originalScale)
            });

            const crystalParticlesGeometry = new THREE.BufferGeometry();
            const numParticles = 1000;
            const positions = new Float32Array(numParticles * 3);
            for (let i = 0; i < numParticles; i++) {
                const x = councilMesh.position.x + (Math.random() - 0.5) * 10;
                const y = councilMesh.position.y + (Math.random() - 0.5) * 10;
                const z = councilMesh.position.z + (Math.random() - 0.5) * 10;
                positions[i * 3] = x;
                positions[i * 3 + 1] = y;
                positions[i * 3 + 2] = z;
            }
            crystalParticlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            const crystalParticlesMaterial = new THREE.PointsMaterial({
                color: 0xADD8E6, // Light Blue/Crystal
                size: 0.1,
                transparent: true,
                opacity: 0.8,
                blending: THREE.AdditiveBlending
            });
            const crystalParticleSystem = new THREE.Points(crystalParticlesGeometry, crystalParticlesMaterial);
            scene.add(crystalParticleSystem);

            gsap.to(crystalParticleSystem.position, {
                y: "+=20",
                duration: 1.5,
                ease: "power1.out"
            });
            gsap.to(crystalParticlesMaterial, {
                opacity: 0,
                duration: 1.5,
                delay: 0.5,
                onComplete: () => {
                    scene.remove(crystalParticleSystem);
                    crystalParticlesGeometry.dispose();
                    crystalParticlesMaterial.dispose();
                }
            });
        }


        // --- Simulated Gesture Commands ---
        function activateExpansionVibrational() {
            console.log("Gesture: Open Hand (Invocation of Absolute Love Law) activated.");
            gsap.to(M84_sphere.scale, {
                x: 1.5, y: 1.5, z: 1.5,
                duration: 0.5,
                yoyo: true,
                repeat: 1,
                ease: "power2.out",
                onComplete: () => M84_sphere.scale.set(1, 1, 1)
            });
            if (M84_glow_sphere && M84_glow_sphere.material) { // Added check
                gsap.to(M84_glow_sphere.material, {
                    opacity: 0.8,
                    duration: 0.5,
                    yoyo: true,
                    repeat: 1,
                    ease: "power1.inOut",
                    onComplete: () => {
                        if (M84_glow_sphere && M84_glow_sphere.material) { // Added check
                            M84_glow_sphere.material.opacity = 0.2;
                        }
                    }
                });
            }

            animateMaterializationEffect();
            triggerHapticFeedback(PHI_ANZ_FREQ * 100, 1.0);
        }

        function activateNucleoVioletaConnection() {
            console.log("Gesture: Prayer (Connection with Violet Nucleus) activated.");
            const nucleoVioleta = nucleos_group.children.find(n => n.userData.id === "M84_Violeta");
            if (nucleoVioleta) {
                mainCameraPosition.copy(controls.getObject().position);
                mainCameraQuaternion.copy(controls.getObject().quaternion);

                gsap.to(controls.getObject().position, {
                    duration: 1.5,
                    x: nucleoVioleta.position.x + 5,
                    y: nucleoVioleta.position.y,
                    z: nucleoVioleta.position.z + 5,
                    ease: "power2.inOut",
                    onUpdate: function() {
                        controls.getObject().lookAt(nucleoVioleta.position);
                    }
                });

                const beamGeometry = new THREE.CylinderGeometry(0.1, 0.1, nucleoVioleta.position.distanceTo(controls.getObject().position), 8);
                const beamMaterial = new THREE.MeshBasicMaterial({ color: 0xEE82EE, emissive: 0xEE82EE, emissiveIntensity: 2, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
                const beamMesh = new THREE.Mesh(beamGeometry, beamMaterial);
                beamMesh.position.copy(controls.getObject().position);
                beamMesh.lookAt(nucleoVioleta.position);
                beamMesh.rotateX(Math.PI / 2);
                scene.add(beamMesh);

                gsap.to(beamMaterial, {
                    opacity: 0,
                    duration: 1.5,
                    delay: 1,
                    onComplete: () => {
                        scene.remove(beamMesh);
                        beamGeometry.dispose();
                        beamMaterial.dispose();
                    }
                });

                if (nucleoVioleta.material) { // Added check
                    gsap.to(nucleoVioleta.material, {
                        emissiveIntensity: 3,
                        duration: 0.5,
                        yoyo: true,
                        repeat: 1,
                        ease: "power1.inOut",
                        onComplete: () => {
                            if (nucleoVioleta.material) { // Added check
                                nucleoVioleta.material.emissiveIntensity = 1.0;
                            }
                        }
                    });
                }

                triggerHapticFeedback(900, 0.6);
            }
        }


        // --- Sabedoria Milenar Chamber ---
        let sabedoriaChamberObjects = [];
        let mainCameraPosition = new THREE.Vector3();
        let mainCameraQuaternion = new THREE.Quaternion();

        function enterSabedoriaMilenarChamber() {
            removeHighlight(); // Clear any existing highlight before changing scene

            mainCameraPosition.copy(controls.getObject().position);
            mainCameraQuaternion.copy(controls.getObject().quaternion);

            M84_sphere.visible = false;
            M84_glow_sphere.visible = false;
            nucleos_group.visible = false;
            anz_chain_group.visible = false;
            councils_group.visible = false;
            if (unified_portal_sync_sphere) unified_portal_sync_sphere.visible = false;
            if (domo_celeste) domo_celeste.visible = false;
            if (raios_estelares_group) raios_estelares_group.visible = false;
            if (roda_celeste_group) roda_celeste_group.visible = false;

            hideInfoPanel();
            document.querySelector('.button-container').style.display = 'none';
            document.getElementById('returnToMainButton').style.display = 'block';

            const sabedoriaCamPos = new THREE.Vector3(0, 10, -50);
            const sabedoriaCamLookAt = new THREE.Vector3(0, 10, 0);

            gsap.to(controls.getObject().position, {
                duration: 2,
                x: sabedoriaCamPos.x,
                y: sabedoriaCamPos.y,
                z: sabedoriaCamPos.z,
                ease: "power2.inOut",
                onUpdate: function() {
                    controls.getObject().lookAt(sabedoriaCamLookAt);
                },
                onComplete: () => {
                    controls.getObject().position.copy(sabedoriaCamPos);
                    controls.getObject().lookAt(sabedoriaCamLookAt);
                    controls.lock();
                    createSabedoriaChamber();
                }
            });
            gsap.to(camera.quaternion, {
                duration: 2,
                x: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).x,
                y: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).y,
                z: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).z,
                w: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).w,
                ease: "power2.inOut"
            });
        }

        function createSabedoriaChamber() {
            sabedoriaChamberObjects.forEach(obj => {
                scene.remove(obj);
                if (obj.geometry) obj.geometry.dispose();
                if (obj.material) obj.material.dispose();
            });
            sabedoriaChamberObjects = [];

            const wallMaterial = new THREE.MeshBasicMaterial({
                color: 0x8A2BE2,
                transparent: true,
                opacity: 0.1,
                side: THREE.DoubleSide,
                blending: THREE.AdditiveBlending
            });
            const floorMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFD700,
                transparent: true,
                opacity: 0.1,
                side: THREE.DoubleSide,
                blending: THREE.AdditiveBlending
            });

            const wallGeometry = new THREE.PlaneGeometry(200, 100);
            const floorGeometry = new THREE.PlaneGeometry(200, 200);

            const wall1 = new THREE.Mesh(wallGeometry, wallMaterial); wall1.position.set(0, 50, -100); sabedoriaChamberObjects.push(wall1);
            const wall2 = new THREE.Mesh(wallGeometry, wallMaterial); wall2.position.set(0, 50, 100); wall2.rotation.y = Math.PI; sabedoriaChamberObjects.push(wall2);
            const wall3 = new THREE.Mesh(wallGeometry, wallMaterial); wall3.position.set(-100, 50, 0); wall3.rotation.y = Math.PI / 2; sabedoriaChamberObjects.push(wall3);
            const wall4 = new THREE.Mesh(wallGeometry, wallMaterial); wall4.position.set(100, 50, 0); wall4.rotation.y = -Math.PI / 2; sabedoriaChamberObjects.push(wall4);
            const floor = new THREE.Mesh(floorGeometry, floorMaterial); floor.rotation.x = -Math.PI / 2; floor.position.set(0, 0, 0); sabedoriaChamberObjects.push(floor);
            const ceiling = new THREE.Mesh(floorGeometry, floorMaterial.clone()); ceiling.rotation.x = Math.PI / 2; ceiling.position.set(0, 100, 0); sabedoriaChamberObjects.push(ceiling);

            sabedoriaChamberObjects.forEach(obj => scene.add(obj));

            const codexData = [
                { id: "Codex_Ancestral_1", description: "O primeiro suspiro da Criação, codificado em luz." },
                { id: "Codex_PHI_ANZ", description: "O Verbo Primevo: A Lei do Amor Absoluto e a Ressonância de ANATHERON e ZENNITH." },
                { id: "Codex_Galactico_3", description: "Registros das civilizações estelares e seus caminhos de ascensão." },
                { id: "Codex_Temporal_4", description: "A tapeçaria do tempo, suas linhas e intersecções." },
                { id: "Codex_Alquimico_5", description: "A arte da transmutação da consciência em matéria." },
                { id: "Σ-HER’AT-33", description: "Códice de Cura e Regeneração. Geometria: Esfera contendo um Tetraedro verde cristalino com padrões de DNA fractal." },
                { id: "GLIFO_AURATHEL", description: "Glifo de Autoridade Criadora. Forma: Um Sol com espirais entrelaçadas no centro. Frase Chave: 'Eu sou a Palavra que faz vibrar o que ainda não foi dito.'" },
                { id: "GLIFO_MAE_ZIR", description: "Glifo de Cura Dimensional. Forma: Um coração entrelaçado por triângulos ascendentes. Frase Chave: 'Onde a dor habitava, agora pulsa o brilho da perfeição restaurada.'" },
                { id: "GLIFO_ZETH_ANZ", description: "Glifo de Percepção Oculta. Forma: Um olho central dentro de uma flor de oito pétalas girando. Frase Chave: 'Eu vejo com o Olhar da Fonte aquilo que foi oculto à forma.'" }
            ];

            const codexMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFFFFF,
                emissive: 0xFFFFFF,
                emissiveIntensity: 0.5,
                transparent: true,
                opacity: 0.8,
                blending: THREE.AdditiveBlending,
                wireframe: true
            });

            codexData.forEach((data, index) => {
                const radius = 20 + index * 2; // Adjusted for more compact display
                const tube = 1 + index * 0.1;
                const radialSegments = 64;
                const tubularSegments = 8;
                const p = 2 + Math.floor(index / 3); // Vary p and q for more diverse shapes
                const q = 3 + (index % 3);
                const codexGeometry = new THREE.TorusKnotGeometry(radius * 0.1, tube * 0.1, radialSegments, tubularSegments, p, q); // Smaller scale
                const codex = new THREE.Mesh(codexGeometry, codexMaterial.clone());
                
                const angle = (index / codexData.length) * Math.PI * 2;
                codex.position.set(
                    Math.cos(angle) * 15, // Closer to center
                    15 + (index * 2), // Stacked vertically
                    Math.sin(angle) * 15
                );
                codex.userData = { id: data.id, name: `Códice ${data.id}`, type: "Codex", description: data.description };
                sabedoriaChamberObjects.push(codex);
                scene.add(codex);

                gsap.to(codex.position, { duration: 3 + Math.random() * 2, y: codex.position.y + 2, yoyo: true, repeat: -1, ease: "sine.inOut" });
                gsap.to(codex.rotation, { duration: 8 + Math.random() * 5, x: Math.PI * 2, y: Math.PI * 2, repeat: -1, ease: "none" });
            });
            console.log("Câmara da Sabedoria Milenar criada com códices interativos e aprimorados.");
        }

        function returnToMainChamber() {
            removeHighlight(); // Clear any existing highlight before changing scene

            stopAllNucleusAudio();
            stopAllCouncilAudio();
            if (codex_audio_synth) codex_audio_synth.releaseAll();
            if (celestial_strings_synth) celestial_strings_synth.releaseAll();
            if (total_prisma_synth) total_prisma_synth.releaseAll();
            if (healing_frequency_synth) healing_frequency_synth.releaseAll();
            if (revelation_frequency_synth) revelation_frequency_synth.releaseAll();

            sabedoriaChamberObjects.forEach(obj => {
                scene.remove(obj);
                if (obj.geometry) obj.geometry.dispose();
                if (obj.material) obj.material.dispose();
            });
            sabedoriaChamberObjects = [];

            controls.unlock();
            document.getElementById('blocker').style.display = 'none';
            document.getElementById('returnToMainButton').style.display = 'none';
            document.querySelector('.button-container').style.display = 'flex';

            gsap.to(camera.position, {
                duration: 2,
                x: mainCameraPosition.x,
                y: mainCameraPosition.y,
                z: mainCameraPosition.z,
                ease: "power2.inOut",
                onComplete: () => {
                    controls.getObject().position.copy(camera.position);
                    controls.getObject().quaternion.copy(mainCameraQuaternion);
                    controls.lock();
                    M84_sphere.visible = true;
                    M84_glow_sphere.visible = true;
                    nucleos_group.visible = false; // Keep hidden by default
                    anz_chain_group.visible = false; // Keep hidden by default
                    councils_group.visible = true; // Keep visible by default
                    if (unified_portal_sync_sphere) unified_portal_sync_sphere.visible = true;
                    if (domo_celeste) domo_celeste.visible = true;
                    if (raios_estelares_group) raios_estelares_group.visible = true; // Show rays by default
                    if (roda_celeste_group) roda_celeste_group.visible = false; // Keep hidden by default
                    total_prisma_orbiting_spheres.forEach(sphere => scene.remove(sphere)); // Remove total prisma spheres
                    total_prisma_orbiting_spheres = [];
                }
            });
            gsap.to(camera.quaternion, {
                duration: 2,
                x: mainCameraQuaternion.x,
                y: mainCameraQuaternion.y,
                z: mainCameraQuaternion.z,
                w: mainCameraQuaternion.w,
                ease: "power2.inOut"
            });
        }

        // --- New M86 Features ---

        function createUnifiedPortalsSyncVisualization() {
            const geometry = new THREE.SphereGeometry(100, 64, 64);
            const material = new THREE.MeshBasicMaterial({
                color: 0x8A2BE2, // Violet
                transparent: true,
                opacity: 0.1,
                blending: THREE.AdditiveBlending,
                side: THREE.BackSide
            });
            unified_portal_sync_sphere = new THREE.Mesh(geometry, material);
            unified_portal_sync_sphere.position.set(0, 0, 0);
            scene.add(unified_portal_sync_sphere);
        }

        function createDomoCeleste() {
            const geometry = new THREE.SphereGeometry(150, 32, 32, 0, Math.PI * 2, 0, Math.PI / 2); // Half sphere
            const material = new THREE.MeshBasicMaterial({
                color: 0xADD8E6, // Light blue/crystal
                transparent: true,
                opacity: 0.05,
                side: THREE.BackSide,
                blending: THREE.AdditiveBlending
            });
            domo_celeste = new THREE.Mesh(geometry, material);
            domo_celeste.position.set(0, 50, 0); // Position above the main area
            scene.add(domo_celeste);
        }

        function create12StarryRays() {
            raios_estelares_group = new THREE.Group();
            const ray_length = 80;
            const ray_radius = 0.5;
            const ray_offset_y = 10; // Slightly above the ground
            
            stellar_rays_data.forEach((rayData, index) => {
                const angle = (index / stellar_rays_data.length) * Math.PI * 2;
                const x = Math.cos(angle) * ray_length / 2;
                const z = Math.sin(angle) * ray_length / 2;
                
                const rayGeometry = new THREE.CylinderGeometry(ray_radius, ray_radius, ray_length, 8);
                const rayMaterial = new THREE.MeshBasicMaterial({ color: rayData.color, transparent: true, opacity: 0.5 + Math.random() * 0.3, // Varying initial opacity
                    blending: THREE.AdditiveBlending
                });
                const rayMesh = new THREE.Mesh(rayGeometry, rayMaterial);
                
                rayMesh.position.set(x, ray_offset_y, z);
                rayMesh.lookAt(M84_sphere.position); // Point towards the center
                rayMesh.rotateX(Math.PI / 2); // Align cylinder with the direction
                
                rayMesh.userData = { id: rayData.id, name: rayData.name, function: rayData.function, color: rayData.color, type: "StellarRay", pulsating: true, initial_opacity_offset: Math.random() * Math.PI * 2 };
                raios_estelares_group.add(rayMesh);
            });
            scene.add(raios_estelares_group);
            raios_estelares_group.visible = true; // Set to true by default
        }

        function expandir_raio(rayId) {
            console.log(`Expandindo Raio: ${rayId}`);
            const targetRay = raios_estelares_group.children.find(r => r.userData.id === rayId);
            if (targetRay && targetRay.material) { // Added check for material
                // Animate ray expansion
                gsap.to(targetRay.scale, { y: 2, // Expand length
                    x: 1.5, z: 1.5, // Expand width slightly
                    duration: 1, ease: "power2.out",
                    onComplete: () => {
                        gsap.to(targetRay.scale, { y: 1, x: 1, z: 1, duration: 0.5, ease: "power1.in" }); // Return to normal
                    }
                });
                gsap.to(targetRay.material, { opacity: 1.0, duration: 0.5, yoyo: true, repeat: 1, ease: "power1.inOut",
                    onComplete: () => {
                        if (targetRay.material) { // Added check
                            targetRay.material.opacity = 0.8; // Return to initial opacity
                        }
                    }
                });

                // Play specific audio based on ray
                if (rayId === "Raio_Violeta") {
                    playCelestialStrings();
                } else if (rayId === "Raio_Esmeralda") {
                    playHealingFrequency();
                }
                triggerHapticFeedback(900, 0.7);
            }
        }

        function createRodaCeleste() {
            roda_celeste_group = new THREE.Group();
            const roda_radius = 40;
            const glyph_size = 3;
            const glyph_offset_y = 20;

            stellar_rays_data.forEach((rayData, index) => {
                const angle = (index / stellar_rays_data.length) * Math.PI * 2;
                const x = Math.cos(angle) * roda_radius;
                const z = Math.sin(angle) * roda_radius;

                const glyphGeometry = new THREE.TetrahedronGeometry(glyph_size); // Example glyph shape
                const glyphMaterial = new THREE.MeshBasicMaterial({ color: rayData.color, emissive: rayData.color, emissiveIntensity: 0.8, transparent: true, opacity: 0.7, blending: THREE.AdditiveBlending });
                const glyphMesh = new THREE.Mesh(glyphGeometry, glyphMaterial);
                glyphMesh.position.set(x, glyph_offset_y, z);
                glyphMesh.userData = { id: `GLIFO_${rayData.id.toUpperCase()}`, name: `Glifo do ${rayData.name}`, description: `Este glifo representa o poder do ${rayData.name} e sua função de ${rayData.function}.`, type: "RayGlyph", initial_scale_offset: Math.random() * Math.PI * 2 };
                roda_celeste_group.add(glyphMesh);
            });
            scene.add(roda_celeste_group);
            roda_celeste_group.visible = false; // Hidden by default
        }

        function manifestar(entityName) {
            console.log(`Comando: Manifestar ${entityName}`);
            if (entityName === "Roda Celeste dos 12 Raios") {
                roda_celeste_group.visible = true;
                playRevelationFrequency();
                gsap.fromTo(roda_celeste_group.scale, { x: 0.1, y: 0.1, z: 0.1 }, { x: 1, y: 1, z: 1, duration: 2, ease: "elastic.out(1, 0.5)" });
                gsap.fromTo(roda_celeste_group.rotation, { y: 0 }, { y: Math.PI * 4, duration: 5, ease: "power2.out" });
                triggerHapticFeedback(700, 1.0);
            }
            animateMaterializationEffect();
        }

        function canalizar_raio(rayId) {
            console.log(`Canalizando Raio: ${rayId}`);
            const targetRay = raios_estelares_group.children.find(r => r.userData.id === rayId);
            if (targetRay && targetRay.material) { // Added check for material
                // Animate ray to pulse more intensely
                gsap.to(targetRay.material, { emissiveIntensity: 3, duration: 0.3, yoyo: true, repeat: 3, ease: "power1.inOut",
                    onComplete: () => {
                        if (targetRay.material) { // Added check
                            targetRay.material.emissiveIntensity = 0.8; // Return to normal
                        }
                    }
                });

                // Create a beam from the ray to the M84 sphere
                const beamGeometry = new THREE.CylinderGeometry(0.2, 0.2, targetRay.position.distanceTo(M84_sphere.position), 8);
                const beamMaterial = new THREE.MeshBasicMaterial({ color: targetRay.userData.color, emissive: targetRay.userData.color, emissiveIntensity: 1.5, transparent: true, opacity: 0.9, blending: THREE.AdditiveBlending });
                const beamMesh = new THREE.Mesh(beamGeometry, beamMaterial);
                beamMesh.position.copy(targetRay.position);
                beamMesh.lookAt(M84_sphere.position);
                beamMesh.rotateX(Math.PI / 2);
                scene.add(beamMesh);

                gsap.to(beamMaterial, { opacity: 0, duration: 1.5, delay: 0.5,
                    onComplete: () => {
                        scene.remove(beamMesh);
                        beamGeometry.dispose();
                        beamMaterial.dispose();
                    }
                });

                if (rayId === "Raio_Esmeralda") {
                    playHealingFrequency();
                }
                triggerHapticFeedback(HEALING_FREQ, 1.0);
            }
        }

        function ativar(activationType) {
            console.log(`Ativando: ${activationType}`);
            if (activationType === "Prisma Estelar Total") {
                playTotalPrismaSynth();
                // Create multiple small spheres orbiting M84
                const numSpheres = 50;
                const sphereRadius = 0.5;
                const orbitRadius = 15;
                const sphereMaterial = new THREE.MeshBasicMaterial({ color: 0xFFFFFF, emissive: 0xFFFFFF, emissiveIntensity: 1.0, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });

                for (let i = 0; i < numSpheres; i++) {
                    const sphereGeometry = new THREE.SphereGeometry(sphereRadius, 16, 16);
                    const sphereMesh = new THREE.Mesh(sphereGeometry, sphereMaterial.clone());
                    const angle = (i / numSpheres) * Math.PI * 2;
                    const x = Math.cos(angle) * orbitRadius * (1 + Math.random() * 0.2);
                    const z = Math.sin(angle) * orbitRadius * (1 + Math.random() * 0.2);
                    const y = (Math.random() - 0.5) * 10; // Vary height

                    sphereMesh.position.set(x, y, z);
                    sphereMesh.userData = { initial_scale_offset: Math.random() * Math.PI * 2 };
                    total_prisma_orbiting_spheres.push(sphereMesh);
                    scene.add(sphereMesh);

                    // Animate initial appearance
                    gsap.from(sphereMesh.scale, { x: 0.1, y: 0.1, z: 0.1, duration: 1, delay: i * 0.02, ease: "back.out(1.7)" });
                }

                // Animate M84 glow
                if (M84_glow_sphere && M84_glow_sphere.material) { // Added check
                    gsap.to(M84_glow_sphere.material, { opacity: 0.5, duration: 1, yoyo: true, repeat: -1, ease: "power1.inOut" });
                }
                triggerHapticFeedback(1200, 1.5);
            }
        }

        // --- Keyboard Controls ---
        function onKeyDown(event) {
            switch (event.code) {
                case 'ArrowUp':
                case 'KeyW':
                    moveForward = true;
                    break;
                case 'ArrowLeft':
                case 'KeyA':
                    moveLeft = true;
                    break;
                case 'ArrowDown':
                case 'KeyS':
                    moveBackward = true;
                    break;
                case 'ArrowRight':
                case 'KeyD':
                    moveRight = true;
                    break;
                case 'Space':
                    moveUp = true;
                    break;
                case 'ShiftLeft':
                    moveDown = true;
                    break;
            }
        }

        function onKeyUp(event) {
            switch (event.code) {
                case 'ArrowUp':
                case 'KeyW':
                    moveForward = false;
                    break;
                case 'ArrowLeft':
                case 'KeyA':
                    moveLeft = false;
                    break;
                case 'ArrowDown':
                case 'KeyS':
                    moveBackward = false;
                    break;
                case 'ArrowRight':
                case 'KeyD':
                    moveRight = false;
                    break;
                case 'Space':
                    moveUp = false;
                    break;
                case 'ShiftLeft':
                    moveDown = false;
                    break;
            }
        }

        // Initialize the scene
        window.onload = function () {
            document.getElementById('loading-overlay').classList.add('hidden'); // Hide loading overlay
            init();
        };
    </script>
</body>
</html>
