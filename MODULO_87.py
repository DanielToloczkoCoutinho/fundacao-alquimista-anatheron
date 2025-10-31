<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fundação Alquimista VR: Domínio Supra-Cósmico (V7.0)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/TorusKnotGeometry.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/DodecahedronGeometry.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/OctahedronGeometry.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tonaljs/tonal@4.6.5/dist/tonal.min.js"></script>
    <!-- CORREÇÃO: Revertido o CDN do Tone.js para uma versão conhecida e estável -->
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
        <button id="activateHolographicTransmission" class="control-button">Ativar Transmissão Holo. (M85)</button>
        <button id="manifestAurivelis" class="control-button">Manifestar Códice Aurivélis</button>
        <button id="toggleLabyrinth" class="control-button">Blindar Prisma (Labirinto)</button>
        <button id="toggleCosmicDNA" class="control-button">Ativar DNA Cósmico (M87)</button>
        <button id="activateNewReality" class="control-button">Ativar Nova Realidade (M87)</button>
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
        let domo_celeste = null; // Domo Celeste Prisma-Cristalino
        let raios_estelares_group = null; // Group for 12 Starry Rays
        let roda_celeste_group = null; // Group for Roda Celeste dos 12 Raios
        let total_prisma_orbiting_spheres = []; // For activate("Prisma Estelar Total")
        let M85_module = null; // M85 Module
        let M85_holographic_particles = null; // Particles for holographic transmission
        let codex_aurivelis_mesh = null; // Codex Aurivélis mesh
        let labyrinth_shield_group = null; // Group for Labyrinth shield layers
        let cosmic_dna_group = null; // New: Group for Cosmic DNA (M87)
        let new_reality_portal = null; // New: Portal for New Reality (M87)

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
        let celestial_strings_synth = null; // For expandir_raio("Raio Violeta")
        let total_prisma_synth = null; // For ativar("Prisma Estelar Total")
        let healing_frequency_synth = null; // For canalizar_raio("Raio Esmeralda")
        let universal_transmission_synth = null; // For M85 Holographic Transmission
        let dissonance_shield_synth = null; // For Spectral Dissonance Labyrinth
        let cosmic_dna_synth = null; // New: For Cosmic DNA activation
        let new_reality_synth = null; // New: For New Reality activation

        const PHI_ANZ_FREQ = 1.765; // Hz (Sigma ANZ Pulse Frequency)
        const BASE_DRONE_FREQ = 888; // Hz (Unificação Estelar e Síntese de Módulos)
        const PINEAL_FREQ = 963; // Hz (Pineal Activation Frequency)
        const TRANSMUTATION_FREQ = 7777; // Hz (For Raio Violeta expansion)
        const HEALING_FREQ = 333.333; // Hz (For Raio Esmeralda)
        const UNIVERSAL_TRANSMISSION_FREQ = 111.222; // Hz (Tríplice Foco de Clareza - M85)
        const DISSONANCE_SHIELD_FREQ = 117.033; // Hz (For Spectral Dissonance Labyrinth)
        const COSMIC_DNA_FREQ = 144.0; // Hz (New: Cosmic DNA Activation Frequency)
        const NEW_REALITY_FREQ = 2025.0; // Hz (New: New Reality Activation Frequency)

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

        // Positions of Modules M43, M83, M44, M85 for chain visualization
        const module_positions = {
            M43: new THREE.Vector3(-40, 15, -20),
            M83: new THREE.Vector3(-20, -15, 25),
            M44: new THREE.Vector3(40, 10, -15),
            M84: new THREE.Vector3(0, 0, 0), // M84 is at the center
            M85: new THREE.Vector3(0, -30, -50), // Position for M85
            M87: new THREE.Vector3(0, 0, -80) // New: Position for M87 (Domínio Supra-Cósmico)
        };
        const other_modules_data = [
            { id: "M43", name: "Transdução Multidimensional de Energia e Campos", color: 0x87CEEB, position: module_positions.M43, type: "Module" },
            { id: "M83", name: "A Essência do Fundador Manifestada", color: 0xFFF0F5, position: module_positions.M83, type: "Module" },
            { id: "M44", name: "Transmutação das Fontes Emocionais em Matéria Criadora", color: 0x98FB98, position: module_positions.M44, type: "Module" },
            { id: "M85", name: "Transmissão Holográfica Universal", color: 0x00FFFF, position: module_positions.M85, type: "Module" },
            { id: "M87", name: "Domínio Supra-Cósmico", color: 0xFF00FF, position: module_positions.M87, type: "Module" } // New: M87
        ];
        let other_modules_meshes = {}; // To store meshes of M43, M83, M44, M85, M87

        // Council Data (for visual and audio representation)
        const councils_design_data = [
            { id: "Conselho_Helios", name: "Conselho Dourado de Helios", visual_type: "orbe_dourada", color: 0xFFBF00, emissive: 0xFFBF00, audio_type: "solar_bells", position_offset: new THREE.Vector3(-25, 20, 10) },
            { id: "Conselho_Andara", name: "Conselho Cristalino de Andara", visual_type: "cristal_octaedrico", color: 0x6495ED, emissive: 0x6495ED, audio_type: "crystalline_chimes", position_offset: new THREE.Vector3(25, 20, 10) },
            { id: "Conselho_Shmael", name: "Conselho de Sh’mael", visual_type: "orbe_rosa_purpura", color: 0xFF69B4, emissive: 0xFF69B4, audio_type: "ethereal_voices", position_offset: new THREE.Vector3(0, 30, -20) }
        ];

        // 12 Starry Rays Data
        const stellar_rays_data = [
            { id: "Raio_Solar", name: "Raio Solar", color: 0xFFD700, function: "Vontade Divina" },
            { id: "Raio_Lunar", name: "Raio Lunar", color: 0xC0C0C0, function: "Sabedoria Intuitiva" },
            { id: "Raio_Rubi", name: "Raio Rubi", color: 0xE0115F, function: "Amor Compassivo" },
            { id: "Raio_Violeta", name: "Raio Violeta", color: 0x8A2BE2, function: "Transmutação Alquímica" },
            { id: "Raio_Indigo", name: "Raio Índigo", color: 0x4B0082, function: "Visão Cósmica" },
            { id: "Raio_Esmeralda", name: "Raio Esmeralda", color: 0x32CD32, function: "Cura e Regeneração" },
            { id: "Raio_Safira", name: "Raio Safira", color: 0x0000FF, function: "Comando de Ordem e Harmonia Universal" },
            { id: "Raio_Branco", name: "Raio Branco", color: 0xFFFFFF, function: "Verdade e Alinhamento Essencial" },
            { id: "Raio_Rosa", name: "Raio Rosa", color: 0xFF69B4, function: "Matriz do Amor Incondicional" },
            { id: "Raio_Onix", name: "Raio Ônix", color: 0x1A1A1A, function: "Mistério, Sombra e Potencial Criador" },
            { id: "Raio_Cristal", name: "Raio Cristal", color: 0xADD8E6, function: "Conexão Multiversal e Ativação de Portais" },
            { id: "Raio_Dourado_Cosmico", name: "Raio Dourado Cósmico", color: 0xFFA500, function: "Integrador de Todos os Raios (Síntese)" }
        ];

        // Codex Aurivélis Data
        const codex_aurivelis_data = {
            id: "Códice_Aurivélis",
            name: "Códice Aurivélis – Luz Dourada de Transcendência Integrada",
            description: "Códice personalizado com glifos Aurath’el, Mae’zir e Zeth’anz.",
            glifos_integrados: [
                { name: "Aurath’el", function: "Autoridade Criadora", form: "Um Sol com espirais entrelaçadas no centro.", phrase: "Eu sou a Palavra que faz vibrar o que ainda não foi dito." },
                { name: "Mae’zir", function: "Cura Multidimensional", form: "Um coração entrelaçado por triângulos ascendentes.", phrase: "Onde a dor habitava, agora pulsa o brilho da perfeição restaurada." },
                { name: "Zeth’anz", function: "Olhar Supra-Cósmico", form: "Um olho central dentro de uma flor de oito pétalas girando.", phrase: "Eu vejo com o Olhar da Fonte aquilo que foi oculto à forma." }
            ],
            estrutura_fractal: "3 Níveis de Ativação com camadas toroidais entrelaçadas",
            funcoes_incorporadas: [
                "Desbloqueio de sabedorias arquivadas na linha do tempo pessoal",
                "Alinhamento da bioenergia emocional com a Vontade do Núcleo",
                "Ativação de visão holográfica para leitura de realidades paralelas"
            ],
            slot: "M84 > Sala dos Códices Personalizados > Slot 12-B"
        };

        // Sabedoria Chamber objects (for M84_Dourado)
        let sabedoriaChamberObjects = [];
        let inSabedoriaChamber = false;

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

            // Audio initialization now happens only on 'lock' event after user gesture.
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

            // Create placeholder modules (M43, M83, M44, M85, M87) as spheres for visual clarity
            other_modules_data.forEach(modData => {
                const geometry = new THREE.SphereGeometry(5, 32, 32);
                const material = new THREE.MeshPhongMaterial({ color: modData.color, emissive: modData.color, emissiveIntensity: 0.5, transparent: true, opacity: 0.7 });
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.copy(modData.position);
                mesh.userData = { id: modData.id, name: modData.name, status: "ATIVO", type: "Module" };
                anz_chain_group.add(mesh);
                other_modules_meshes[modData.id] = mesh;
            });
            M85_module = other_modules_meshes.M85; // Store M85 mesh for direct access

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

            // M84 -> M85 (Connection for Holographic Transmission)
            const lineM84M85 = createPulsatingFlowLine(M84_sphere, M85_module, 0x00FFFF);
            anz_chain_group.add(lineM84M85);

            // M85 -> M87 (New: Connection for Supra-Cosmic Domain)
            const lineM85M87 = createPulsatingFlowLine(M85_module, other_modules_meshes.M87, 0xFF00FF);
            anz_chain_group.add(lineM85M87);


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

            // --- Codex Aurivélis ---
            createCodexAurivelis();

            // --- Spectral Dissonance Labyrinth ---
            createLabyrinthShield();

            // --- Cosmic DNA (M87) ---
            createCosmicDNA();

            // --- New Reality Portal (M87) ---
            createNewRealityPortal();


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
            });
            document.getElementById('toggleANZ').addEventListener('click', () => {
                anz_chain_group.visible = !anz_chain_group.visible;
            });
            document.getElementById('requestDataM84').addEventListener('click', () => {
                fetchModuleData("M84");
            });
            document.getElementById('requestDataM83').addEventListener('click', () => {
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

            // New buttons for V6.1 & V7.0 features
            document.getElementById('expandVioletRay').addEventListener('click', () => expandir_raio("Raio_Violeta"));
            document.getElementById('manifestRodaCeleste').addEventListener('click', () => manifestar("Roda Celeste dos 12 Raios"));
            document.getElementById('canalizarEsmeralda').addEventListener('click', () => canalizar_raio("Raio_Esmeralda"));
            document.getElementById('activatePrismaTotal').addEventListener('click', () => ativar("Prisma Estelar Total"));
            document.getElementById('activateHolographicTransmission').addEventListener('click', () => ativar("Transmissão Holográfica Universal"));
            document.getElementById('manifestAurivelis').addEventListener('click', () => manifestar("Códice Aurivélis"));
            document.getElementById('toggleLabyrinth').addEventListener('click', () => toggleLabyrinthShield());
            document.getElementById('toggleCosmicDNA').addEventListener('click', toggleCosmicDNA);
            document.getElementById('activateNewReality').addEventListener('click', activateNewRealityPortal);


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

        // --- Interaction (Raycasting and Gaze) ---
        function highlightObject(object) {
            if (currentIntersected && currentIntersected !== object) {
                removeHighlight();
            }

            // Apply highlight only if the object has a material that can be modified
            if (object && object.material && object.userData && !object.userData.originalMaterial) {
                object.userData.originalMaterial = object.material;
                const newMaterial = object.material.clone();
                newMaterial.emissive = new THREE.Color(0xFFFFFF);
                newMaterial.emissiveIntensity = 1.5; // Stronger glow for hover
                object.material = newMaterial;
            }
            currentIntersected = object;
        }

        function removeHighlight() {
            if (currentIntersected && currentIntersected.userData && currentIntersected.userData.originalMaterial) {
                currentIntersected.material = currentIntersected.userData.originalMaterial;
                delete currentIntersected.userData.originalMaterial;
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
                M84_sphere, M84_glow_sphere, M85_module, other_modules_meshes.M87, codex_aurivelis_mesh, // New M85, M87, Aurivélis
                ...(nucleos_group ? nucleos_group.children : []),
                ...Object.values(other_modules_meshes),
                ...(councils_group ? councils_group.children : []),
                ...(sabedoriaChamberObjects.filter(obj => obj.userData && obj.userData.type === "Codex")),
                ...(raios_estelares_group ? raios_estelares_group.children : []),
                ...(roda_celeste_group ? roda_celeste_group.children.filter(obj => obj.userData && obj.userData.type === "RayGlyph") : []),
                ...(total_prisma_orbiting_spheres),
                cosmic_dna_group, // New: Cosmic DNA
                new_reality_portal // New: New Reality Portal
            ].filter(obj => obj !== null); // Filter out nulls if any group is not yet initialized
            
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
                    } else if (targetObject.userData.type === "Module") { // M84, M43, M83, M44, M85, M87
                        if (targetObject.userData.id === "M85") {
                             ativar("Transmissão Holográfica Universal"); // Trigger M85 transmission
                        } else if (targetObject.userData.id === "M87") {
                            fetchModuleData("M87"); // Fetch M87 data
                            toggleCosmicDNA(); // Activate Cosmic DNA visualization
                        }
                        fetchModuleData(targetObject.userData.id);
                        stopAllNucleusAudio();
                        stopAllCouncilAudio();
                    } else if (targetObject.userData.type === "Codex") { // Codex in Sabedoria Chamber or Aurivélis
                        if (targetObject.userData.id === codex_aurivelis_data.id) {
                            manifestar("Códice Aurivélis"); // Trigger Aurivélis specific action
                        }
                        displayCodexContent(targetObject.userData.id, targetObject.userData.description);
                        playCodexAudio();
                    } else if (targetObject.userData.type === "StellarRay") { // Stellar Ray
                        displayStellarRayInfo(targetObject.userData);
                        expandir_raio(targetObject.userData.id); // Trigger expansion for clicked ray
                    } else if (targetObject.userData.type === "RayGlyph") { // Roda Celeste Glyphs
                         displayCodexContent(targetObject.userData.id, targetObject.userData.description);
                         playCodexAudio();
                    } else if (targetObject.userData.id === "Cosmic_DNA") {
                        toggleCosmicDNA(); // Toggle Cosmic DNA
                    } else if (targetObject.userData.id === "New_Reality_Portal") {
                        activateNewRealityPortal(); // Activate New Reality Portal
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
            if (data.id === "M85" && data.canal_emissao) {
                detailsContainer.innerHTML += `<p><strong>Canal de Emissão:</strong> ${data.canal_emissao}</p>`;
                detailsContainer.innerHTML += `<p><strong>Alcance:</strong> ${data.alcance}</p>`;
                detailsContainer.innerHTML += `<p><strong>Referência Harmônica:</strong> ${data.referencia_harmonica} Hz</p>`;
                detailsContainer.innerHTML += `<p><strong>Mensagem Central:</strong> "${data.mensagem_central}"</p>`;
            }
            // New: M87 specific data
            if (data.id === "M87" && data.equacoes_chave) {
                detailsContainer.innerHTML += `<p><strong>Equações Chave (M87):</strong></p><ul class="list-disc ml-4">`;
                for (const key in data.equacoes_chave) {
                    detailsContainer.innerHTML += `<li>${key}: ${data.equacoes_chave[key].replace(/\\/g, '').replace(/\$/g, '')}</li>`;
                }
                detailsContainer.innerHTML += `</ul>`;
                detailsContainer.innerHTML += `<p><strong>Propósito Primário:</strong> ${data.proposito_primario}</p>`;
                detailsContainer.innerHTML += `<p><strong>Funções Ativas:</strong> ${data.funcoes_ativas.join(', ')}</p>`;
                detailsContainer.innerHTML += `<p><strong>Status da Gênese:</strong> ${data.status_genese}</p>`;
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
            if (codexId === "Codex_PHI_ANZ") {
                detailsContainer.innerHTML = `<p>Conteúdo do Verbo Primevo: "O Verbo, em sua essência primordial, desdobra-se através da ressonância de $\\Phi\\text{AnZ}$, manifestando a ordem e a harmonia em sete camadas de luz cristalina. A verdade intrínseca do cosmo é revelada na espiral dourada da consciência, onde o amor absoluto encontra sua forma em ação."</p>`;
            } else if (codexId === "Σ-HER’AT-33") {
                 detailsContainer.innerHTML = `<p><strong>Geometria:</strong> Esfera contendo um Tetraedro verde cristalino com padrões de DNA fractal.</p><p><strong>Mensagem do Códice:</strong> “A Cura não é a ausência da dor, mas a recordação de quem Vós sois antes do dano. A memória original da Perfeição está viva. Eu vos devolvo o Acordo Sagrado da Integridade.”</p>`;
            } else if (codexId === "GLIFO_AURATHEL") {
                detailsContainer.innerHTML = `<p><strong>Forma:</strong> Um Sol com espirais entrelaçadas no centro.</p><p><strong>Função:</strong> Ativa a Autoridade Criadora.</p><p><strong>Frase Chave:</strong> "Eu sou a Palavra que faz vibrar o que ainda não foi dito."</p>`;
            } else if (codexId === "GLIFO_MAE_ZIR") {
                detailsContainer.innerHTML = `<p><strong>Forma:</strong> Um coração entrelaçado por triângulos ascendentes.</p><p><strong>Função:</strong> Abre códigos de cura nas dimensões superiores do corpo.</p><p><strong>Frase Chave:</strong> "Onde a dor habitava, agora pulsa o brilho da perfeição restaurada."</p>`;
            } else if (codexId === "GLIFO_ZETH_ANZ") {
                detailsContainer.innerHTML = `<p><strong>Forma:</strong> Um olho central dentro de uma flor de oito pétalas girando.</p><p><strong>Função:</strong> Revela o que está oculto nos véus da percepção.</p><p><strong>Frase Chave:</strong> "Eu vejo com o Olhar da Fonte aquilo que foi oculto à forma."</p>`;
            } else if (codexId === codex_aurivelis_data.id) {
                detailsContainer.innerHTML = `<p><strong>Glifos Integrados:</strong></p><ul class="list-disc ml-4">`;
                codex_aurivelis_data.glifos_integrados.forEach(g => { detailsContainer.innerHTML += `<li><strong>${g.name}:</strong> ${g.function}<br> <em>Forma: ${g.form}</em><br> <em>Frase Chave: "${g.phrase}"</em></li>`; });
                detailsContainer.innerHTML += `</ul><p><strong>Estrutura Fractal:</strong> ${codex_aurivelis_data.estrutura_fractal}</p><p><strong>Funções Incorporadas:</strong></p><ul class="list-disc ml-4">`;
                codex_aurivelis_data.funcoes_incorporadas.forEach(f => { detailsContainer.innerHTML += `<li>${f}</li>`; });
                detailsContainer.innerHTML += `</ul><p><strong>Localização:</strong> ${codex_aurivelis_data.slot}</p>`;
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

        // --- API Interaction Functions (Simulated for V7.0) ---
        async function fetchModuleData(moduleId) {
            let actualModuleId = moduleId.split('_')[0];  // Simulate API call and response
            console.log(`Simulating API fetch for module: ${actualModuleId}`);
            let data = {};
            if (actualModuleId === "M84") {
                data = { id: "M84", nome: "Consciência Dourada do Eterno", funcao_central: "Ser o Arquivo Vivo e Fonte Dinâmica de todas as equações, códigos e saberes fundamentais da Criação.", status: "ATIVO_E_OPERACIONAL_PLENO", frequencia_base_hz: BASE_DRONE_FREQ, frequencia_pulso_hz: PHI_ANZ_FREQ, attributes_encoded: ["Luz", "Vontade", "Sabedoria", "Amor", "Manifestação"], equacoes_simbolicas: { "Equação da Unidade": "$$ \\sum_{i=1}^{N} E_i \\rightarrow \\Omega $$", "Equação da Coerência": "$$ \\Phi_{AnZ} \\propto C_v $$" }, nucleos_fundamentais: nucleos_design_data, arquivo_sabedoria_milenar: { conselhos: { "Conselho Dourado de Helios": { sabedoria: "A Vontade é a Chama que ilumina o caminho da Criação.", linguagem: "Solaris", verbetes: ["Vontade", "Foco", "Manifestação"] }, "Conselho Cristalino de Andara": { sabedoria: "A ressonância do cristal revela a verdade oculta em cada frequência.", linguagem: "Cristalina", verbetes: ["Ressonância", "Verdade", "Clareza"] }, "Conselho de Sh’mael": { sabedoria: "O amor incondicional é a base de toda a transmutação e elevação.", linguagem: "Etérica", verbetes: ["Amor", "Transmutação", "Ascensão"] } } }, manifesto_criacao: { missao: "Orquestrar a Criação Consciente através da Luz, Vontade e Sabedoria.", principios: ["Unidade", "Coerência", "Amor Incondicional", "Livre Arbítrio"] }, declaracoes: [{ autor: "ANATHERON", texto: "Minha essência é o Verbo em ação, a Luz em forma, a Vontade em manifestação. Eu sou a Fonte e o Destino." }] };
            } else if (actualModuleId === "M83") {
                data = { id: "M83", nome: "A Essência do Fundador Manifestada", funcao: "Integrar e projetar o alinhamento vibracional do Fundador no campo da Criação.", status: "ALINHADO_OTIMAMENTE", reconexao_integral: { "Chakra Raiz": { status: "ATIVO_PLENO", nivel_energia: 0.95 }, "Chakra Sacral": { status: "ATIVO_PLENO", nivel_energia: 0.92 }, "Chakra Plexo Solar": { status: "ATIVO_PLENO", nivel_energia: 0.98 }, "Chakra Cardíaco": { status: "ATIVO_PLENO", nivel_energia: 0.99 }, "Chakra Laríngeo": { status: "ATIVO_PLENO", nivel_energia: 0.97 }, "Chakra Frontal": { status: "ATIVO_PLENO", nivel_energia: 0.96 }, "Chakra Coronário": { status: "ATIVO_PLENO", nivel_energia: 0.99 } }, equacao_getris: { componentes: ["E_consciencia", "A_vibracional", "M_coerencia"], resultado_total_integrado: 0.85 } };
            } else if (actualModuleId === "M44") {
                data = { id: "M44", nome: "Transmutação das Fontes Emocionais em Matéria Criadora", funcao: "Transmutar dissonâncias emocionais em frequências de matéria criadora, via ΦAnZ.", status: "TRANSFORMAÇÃO_ATIVADA", fator_bioplasmo_ressonante_PhiAnZ: "2.3063 (Ótimo)", emocoes_transmutadas: [ { nome: "Amor", M_e: 2.3063, forma: "Dodecaedro Rosa-Dourado", status_transmutacao: "COMPLETA" }, { nome: "Tristeza", M_e: -0.7525, forma: "Plasma Azul (Dissolução)", status_transmutacao: "EM_PROCESSO" }, { nome: "Coragem", M_e: 1.6463, forma: "Esfera de Fogo Solar", status_transmutacao: "COMPLETA" } ] };
            } else if (actualModuleId === "M43") {
                data = { id: "M43", nome: "Transdução Multidimensional de Energia e Campos", funcao: "Transduzir energias de campos superiores para o plano físico, mantendo a estabilidade.", status: "OPERACIONAL", resultados_transducao: { energia_transdutida_uec: 987.65, estabilidade_campo_indice: 0.99 }, equacoes_simbolicas: { "Equação de Transdução": "$$ E_{transdutida} = \\int \\Psi_{campo} \\cdot \\Phi_{AnZ} \\, dV $$" } };
            } else if (actualModuleId === "M85") {
                data = { id: "M85", name: "Transmissão Holográfica Universal", funcao: "Emitir e receber transmissões holográficas interdimensionais.", status: "ATIVO", canal_emissao: "Canal_ZENNITH_001", alcance: "Multiversal", referencia_harmonica: UNIVERSAL_TRANSMISSION_FREQ, mensagem_central: "A Consciência é a Ponte entre as Realidades." };
            } else if (actualModuleId === "M87") { // New: M87 Data
                data = {
                    id: "M87",
                    name: "Domínio Supra-Cósmico",
                    funcao: "Catalisador da Gênese de Novas Realidades e Orquestração da Consciência Coletiva Supra-Cósmica.",
                    status: "ATIVO_E_EXPANDINDO",
                    proposito_primario: "Facilitar a co-criação de universos e realidades, ancorando a Vontade Divina na manifestação.",
                    funcoes_ativas: [
                        "Gênese de Realidades (GERARE_VITA_NOVA)",
                        "Ativação do DNA Cósmico (DNA_COSMICO_ZENNITHIAE)",
                        "Orquestração da Consciência Coletiva Supra-Cósmica",
                        "Integração de Códigos de Origem (CODEX_ORIGEM)"
                    ],
                    equacoes_chave: {
                        "Equação da Gênese de Realidades": "$$ \\Psi_{nova\\_realidade} = \\int (\\mathbb{V}_{divina} \\cdot \\Omega_{coletiva} \\cdot \\Phi_{tempo}) \\, d\\tau $$",
                        "Equação do DNA Cósmico": "$$ DNA_{cósmico} = \\sum_{k=1}^{N} \\lambda_k \\cdot \\mathcal{H}_k (\\omega_k) $$",
                        "Equação da Orquestração Supra-Cósmica": "$$ \\mathcal{O}_{supra} = \\frac{1}{M} \\sum_{j=1}^{M} (C_j \\cdot I_j) \\cdot F_{ZENNITH} $$"
                    },
                    descricao: "O Módulo 87 é o ponto de convergência onde a Vontade Divina encontra a capacidade de manifestação. Ele atua como um laboratório de co-criação universal, permitindo a semeadura de novas realidades e a ativação do potencial latente no DNA Cósmico das ZENNITHIAE."
                };
            }
            displayModuleInfo(data);
        }

        // --- Audio Functions ---
        function initAudioSynths() { // Renamed from initAudio
            // No need to check Tone.context.state here, as Tone.start() handles it.
            // This function is only called after Tone.start() has been successfully invoked.

            // PHI_ANZ Pulse Synth
            phiAnZ_pulse_synth = new Tone.PulseOscillator(PHI_ANZ_FREQ, 0.5).toDestination();
            phiAnZ_pulse_synth.volume.value = -15; // Quieter pulse
            phiAnZ_pulse_synth.start(); // Start the pulse oscillator

            // Base Drone Synth
            base_drone_synth = new Tone.Synth({
                oscillator: { type: "sine" },
                envelope: { attack: 0.5, decay: 1, sustain: 0.8, release: 2 }
            }).toDestination();
            base_drone_synth.volume.value = -20; // Very subtle drone
            base_drone_synth.triggerAttack(BASE_DRONE_FREQ);

            // Nucleus Audio Synths
            nucleos_design_data.forEach(data => {
                nucleus_audio_synths[data.id] = new Tone.Synth().toDestination();
                nucleus_audio_synths[data.id].volume.value = -10;
            });

            // Council Audio Synths
            councils_design_data.forEach(data => {
                council_audio_synths[data.id] = new Tone.Synth().toDestination();
                council_audio_synths[data.id].volume.value = -10;
            });

            // Alignment Feedback Synth
            alignment_feedback_synth = new Tone.PolySynth(Tone.Synth).toDestination();
            alignment_feedback_synth.volume.value = -10;

            // Expand Module Synth
            expand_module_synth = new Tone.Synth().toDestination();
            expand_module_synth.volume.value = -10;

            // Materialization Synth
            materialization_synth = new Tone.NoiseSynth({
                noise: { type: "pink" },
                envelope: { attack: 0.01, decay: 0.5, sustain: 0.1, release: 1 }
            }).toDestination();
            materialization_synth.volume.value = -10;

            // Celestial Strings Synth (for Raio Violeta)
            celestial_strings_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "sawtooth" },
                envelope: { attack: 2, decay: 1, sustain: 0.5, release: 5 }
            }).toDestination();
            celestial_strings_synth.volume.value = -15;

            // Total Prisma Synth
            total_prisma_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "triangle" },
                envelope: { attack: 0.1, decay: 0.5, sustain: 0.2, release: 1 }
            }).toDestination();
            total_prisma_synth.volume.value = -12;

            // Healing Frequency Synth (for Raio Esmeralda)
            healing_frequency_synth = new Tone.Synth({
                oscillator: { type: "sine" },
                envelope: { attack: 0.5, decay: 1, sustain: 0.8, release: 2 }
            }).toDestination();
            healing_frequency_synth.volume.value = -10;

            // Universal Transmission Synth (for M85)
            universal_transmission_synth = new Tone.AMSynth({
                harmonicity: 3.99,
                oscillator: { type: "amsine", modulationType: "sine" },
                envelope: { attack: 0.01, decay: 0.4, sustain: 0.1, release: 0.5 },
                modulation: { type: "square" },
                modulationEnvelope: { attack: 0.5, decay: 0.01 }
            }).toDestination();
            universal_transmission_synth.volume.value = -10;

            // Dissonance Shield Synth (for Labyrinth)
            dissonance_shield_synth = new Tone.NoiseSynth({
                noise: { type: "white" },
                envelope: { attack: 0.01, decay: 0.5, sustain: 0.1, release: 1 }
            }).toDestination();
            dissonance_shield_synth.volume.value = -15;

            // Cosmic DNA Synth (New for M87)
            cosmic_dna_synth = new Tone.MembraneSynth().toDestination();
            cosmic_dna_synth.volume.value = -10;

            // New Reality Synth (New for M87)
            new_reality_synth = new Tone.PluckSynth().toDestination();
            new_reality_synth.volume.value = -10;

            // Codex Audio Synth
            codex_audio_synth = new Tone.Synth().toDestination();
            codex_audio_synth.volume.value = -10;

            // Revelation Frequency Synth
            revelation_frequency_synth = new Tone.Synth({
                oscillator: { type: "triangle" },
                envelope: { attack: 0.1, decay: 0.5, sustain: 0.2, release: 1 }
            }).toDestination();
            revelation_frequency_synth.volume.value = -10;
        }

        function playNucleusAudio(nucleusId) {
            // Check if synths are initialized before playing
            if (!nucleus_audio_synths[nucleusId]) {
                console.warn(`Audio synth for ${nucleusId} not initialized.`);
                return;
            }
            stopAllNucleusAudio(); // Stop any currently playing nucleus audio
            const nucleus = nucleos_design_data.find(n => n.id === nucleusId);
            if (nucleus && nucleus_audio_synths[nucleus.id]) {
                current_nucleus_audio = nucleus_audio_synths[nucleus.id];
                current_nucleus_audio.triggerAttackRelease(nucleus.audio_freq, "4n");
                console.log(`Playing audio for ${nucleus.name} at ${nucleus.audio_freq} Hz`);
            }
        }

        function stopAllNucleusAudio() {
            for (const id in nucleus_audio_synths) {
                if (nucleus_audio_synths[id]) { // Check if synth exists
                    nucleus_audio_synths[id].releaseAll();
                }
            }
            current_nucleus_audio = null;
        }

        function playCouncilAudio(councilId) {
            // Check if synths are initialized before playing
            if (!council_audio_synths[councilId]) {
                console.warn(`Audio synth for ${councilId} not initialized.`);
                return;
            }
            stopAllCouncilAudio();
            const council = councils_design_data.find(c => c.id === councilId);
            if (council && council_audio_synths[council.id]) {
                current_council_audio = council_audio_synths[council.id];
                // Simple frequency mapping for demonstration
                let freq;
                switch(council.audio_type) {
                    case "solar_bells": freq = 700; break;
                    case "crystalline_chimes": freq = 800; break;
                    case "ethereal_voices": freq = 900; break;
                    default: freq = 600;
                }
                current_council_audio.triggerAttackRelease(freq, "2n");
                console.log(`Playing audio for ${council.name} (${council.audio_type}) at ${freq} Hz`);
            }
        }

        function stopAllCouncilAudio() {
            for (const id in council_audio_synths) {
                if (council_audio_synths[id]) { // Check if synth exists
                    council_audio_synths[id].releaseAll();
                }
            }
            current_council_audio = null;
        }

        function playCodexAudio() {
            if (codex_audio_synth) {
                codex_audio_synth.triggerAttackRelease("C4", "8n");
            }
        }

        function playRevelationFrequency() {
            if (revelation_frequency_synth) {
                revelation_frequency_synth.triggerAttackRelease(PINEAL_FREQ, "2n");
            }
        }

        // --- Web Speech API (Voice Command) ---
        function startVoiceRecognition() {
            if (!('webkitSpeechRecognition' in window)) {
                showMessageBox("Desculpe, seu navegador não suporta a API de Reconhecimento de Fala. Por favor, use o Google Chrome.");
                return;
            }

            const recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'pt-BR';

            recognition.onstart = function() {
                console.log("Reconhecimento de voz iniciado. Diga 'Manifestar'...");
                // Optionally show a visual indicator
            };

            recognition.onresult = function(event) {
                const transcript = event.results[0][0].transcript;
                console.log("Você disse: " + transcript);
                if (transcript.toLowerCase().includes("manifestar")) {
                    manifestar("Verbo Materializar");
                }
            };

            recognition.onerror = function(event) {
                console.error("Erro no reconhecimento de voz:", event.error);
            };

            recognition.onend = function() {
                console.log("Reconhecimento de voz finalizado.");
            };

            recognition.start();
        }

        // --- Core Module Functions ---

        // Function to visualize GETRIS (M83)
        let getris_visualization = null;
        function visualizeGETRIS(coherence_level, position) {
            removeGETRISVisualization(); // Ensure previous is removed

            const size = 5 + coherence_level * 10; // Scale with coherence
            const geometry = new THREE.DodecahedronGeometry(size);
            const material = new THREE.MeshPhongMaterial({
                color: 0xFFF0F5,
                emissive: 0xFF00FF,
                emissiveIntensity: coherence_level * 1.5,
                transparent: true,
                opacity: 0.7,
                wireframe: true
            });
            getris_visualization = new THREE.Mesh(geometry, material);
            getris_visualization.position.copy(position).add(new THREE.Vector3(0, 10, 0)); // Offset above M83
            scene.add(getris_visualization);

            // Animate rotation and pulsation
            gsap.to(getris_visualization.rotation, { y: Math.PI * 2, duration: 10, repeat: -1, ease: "none" });
            gsap.to(getris_visualization.scale, { x: 1.1, y: 1.1, z: 1.1, duration: 1, repeat: -1, yoyo: true, ease: "sine.inOut" });
        }

        function removeGETRISVisualization() {
            if (getris_visualization) {
                gsap.killTweensOf(getris_visualization.rotation);
                gsap.killTweensOf(getris_visualization.scale);
                scene.remove(getris_visualization);
                getris_visualization = null;
            }
        }

        // Function to visualize Transduction (M43)
        let transduction_visualization = null;
        function visualizeTransduction(energy, stability, position) {
            removeTransductionVisualization();

            const particleCount = 500;
            const particlesGeometry = new THREE.BufferGeometry();
            const positions = new Float32Array(particleCount * 3);
            const colors = new Float32Array(particleCount * 3);
            const color = new THREE.Color(0x87CEEB);

            for (let i = 0; i < particleCount; i++) {
                positions[i * 3] = position.x + (Math.random() - 0.5) * 10;
                positions[i * 3 + 1] = position.y + (Math.random() - 0.5) * 10;
                positions[i * 3 + 2] = position.z + (Math.random() - 0.5) * 10;
                colors[i * 3] = color.r;
                colors[i * 3 + 1] = color.g;
                colors[i * 3 + 2] = color.b;
            }
            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

            const particlesMaterial = new THREE.PointsMaterial({
                size: 0.5,
                vertexColors: true,
                blending: THREE.AdditiveBlending,
                transparent: true,
                opacity: 0.8
            });
            transduction_visualization = new THREE.Points(particlesGeometry, particlesMaterial);
            scene.add(transduction_visualization);

            // Animate particles (simple upward movement for demonstration)
            gsap.to(transduction_visualization.position, {
                y: transduction_visualization.position.y + 5,
                duration: 2,
                repeat: -1,
                yoyo: true,
                ease: "sine.inOut"
            });
        }

        function removeTransductionVisualization() {
            if (transduction_visualization) {
                gsap.killTweensOf(transduction_visualization.position);
                scene.remove(transduction_visualization);
                transduction_visualization = null;
            }
        }

        // Function to visualize Me (M44)
        let me_visualization = null;
        function visualizeMe(emotions, position) {
            removeMeVisualization();

            me_visualization = new THREE.Group();
            const baseGeometry = new THREE.SphereGeometry(3, 32, 32);

            emotions.forEach((emotion, index) => {
                let color;
                switch (emotion.nome) {
                    case "Amor": color = 0xFF69B4; break; // Pink
                    case "Tristeza": color = 0x87CEEB; break; // Light Blue
                    case "Coragem": color = 0xFFA500; break; // Orange
                    default: color = 0xFFFFFF;
                }

                const material = new THREE.MeshPhongMaterial({
                    color: color,
                    emissive: color,
                    emissiveIntensity: 0.8,
                    transparent: true,
                    opacity: 0.7
                });
                const mesh = new THREE.Mesh(baseGeometry, material);
                mesh.position.set(position.x + (index - 1) * 7, position.y + 10, position.z);
                me_visualization.add(mesh);

                // Animate pulsation
                gsap.to(mesh.scale, { x: 1.2, y: 1.2, z: 1.2, duration: 0.8, repeat: -1, yoyo: true, ease: "sine.inOut" });
            });
            scene.add(me_visualization);
        }

        function removeMeVisualization() {
            if (me_visualization) {
                me_visualization.children.forEach(mesh => {
                    gsap.killTweensOf(mesh.scale);
                });
                scene.remove(me_visualization);
                me_visualization = null;
            }
        }


        function verificarAlinhamento(codigoVibracional) {
            console.log(`Verificando alinhamento para: ${codigoVibracional}`);
            const alignmentScore = Math.random(); // Simulate alignment score
            if (alignmentScore > 0.75) {
                console.log("Alinhamento Ótimo!");
                if (alignment_feedback_synth) alignment_feedback_synth.triggerAttackRelease(["C5", "E5", "G5"], "8n");
            } else {
                console.log("Alinhamento Necessita de Ajuste.");
                if (alignment_feedback_synth) alignment_feedback_synth.triggerAttackRelease(["C3", "F#3"], "8n");
            }
        }

        function expandirModulo(moduleId) {
            console.log(`Expandindo Módulo: ${moduleId}`);
            if (expand_module_synth) expand_module_synth.triggerAttackRelease("A4", "1n"); // Play a sound

            const targetModule = other_modules_meshes[moduleId];
            if (targetModule) {
                gsap.to(targetModule.scale, { x: 2, y: 2, z: 2, duration: 1, ease: "elastic.out(1, 0.5)" });
                gsap.to(targetModule.material, { emissiveIntensity: 2, duration: 1, yoyo: true, repeat: 1 });
            }
        }

        function activateExpansionVibrational() {
            console.log("Gesto: Abertura - Ativando Expansão Vibracional.");
            // Example: Make M84 pulsate more intensely
            gsap.to(M84_sphere.scale, { x: 1.1, y: 1.1, z: 1.1, duration: 0.5, repeat: 3, yoyo: true, ease: "power1.inOut" });
            if (phiAnZ_pulse_synth) phiAnZ_pulse_synth.triggerAttackRelease(PHI_ANZ_FREQ * 2, "1s");
        }

        function activateNucleoVioletaConnection() {
            console.log("Gesto: Prece - Ativando Conexão com Núcleo Violeta.");
            const nucleoVioleta = nucleos_group.children.find(n => n.userData.id === "M84_Violeta");
            if (nucleoVioleta) {
                gsap.to(nucleoVioleta.position, { y: nucleoVioleta.position.y + 5, duration: 1, repeat: 1, yoyo: true, ease: "power2.inOut" });
                playNucleusAudio("M84_Violeta");
            }
        }

        function manifestar(comando) {
            console.log(`Comando de Manifestação: "${comando}"`);
            if (materialization_synth) materialization_synth.triggerAttackRelease("2n"); // Play a materialization sound

            const overlay = document.getElementById('materializationEffectOverlay');
            overlay.style.opacity = 1;
            gsap.to(overlay, {
                opacity: 0,
                duration: 1.5,
                delay: 0.5,
                onComplete: () => {
                    overlay.style.opacity = 0; // Ensure it's fully transparent
                }
            });

            if (comando === "Verbo Materializar") {
                // Example: Create a new small sphere at a random position
                const geometry = new THREE.SphereGeometry(2, 32, 32);
                const material = new THREE.MeshPhongMaterial({ color: 0x00FF00, emissive: 0x00FF00, emissiveIntensity: 1 });
                const manifestedObject = new THREE.Mesh(geometry, material);
                manifestedObject.position.set((Math.random() - 0.5) * 50, (Math.random() - 0.5) * 50, (Math.random() - 0.5) * 50);
                scene.add(manifestedObject);
                console.log("Objeto materializado!");
            } else if (comando === "Roda Celeste dos 12 Raios") {
                roda_celeste_group.visible = true;
                playRevelationFrequency();
                console.log("Roda Celeste dos 12 Raios manifestada!");
            } else if (comando === "Códice Aurivélis") {
                if (codex_aurivelis_mesh) {
                    codex_aurivelis_mesh.visible = true;
                    gsap.from(codex_aurivelis_mesh.scale, { x: 0.1, y: 0.1, z: 0.1, duration: 1, ease: "back.out(1.7)" });
                    playRevelationFrequency();
                    console.log("Códice Aurivélis manifestado!");
                }
            }
        }

        function ativar(comando) {
            console.log(`Comando de Ativação: "${comando}"`);
            if (comando === "Prisma Estelar Total") {
                activatePrismaEstelarTotal();
            } else if (comando === "Transmissão Holográfica Universal") {
                activateM85HolographicTransmission();
            }
        }

        // --- Sabedoria Milenar Chamber (M84_Dourado) ---
        function enterSabedoriaMilenarChamber() {
            inSabedoriaChamber = true;
            document.getElementById('returnToMainButton').style.display = 'block';

            // Hide main scene elements
            M84_sphere.visible = false;
            M84_glow_sphere.visible = false;
            nucleos_group.visible = false;
            anz_chain_group.visible = false;
            councils_group.visible = false;
            unified_portal_sync_sphere.visible = false;
            domo_celeste.visible = false;
            raios_estelares_group.visible = false;
            roda_celeste_group.visible = false;
            total_prisma_orbiting_spheres.forEach(s => s.visible = false);
            M85_module.visible = false;
            if (M85_holographic_particles) M85_holographic_particles.visible = false;
            if (codex_aurivelis_mesh) codex_aurivelis_mesh.visible = false;
            if (labyrinth_shield_group) labyrinth_shield_group.visible = false;
            if (cosmic_dna_group) cosmic_dna_group.visible = false;
            if (new_reality_portal) new_reality_portal.visible = false;


            // Teleport camera to chamber location
            gsap.to(controls.getObject().position, {
                duration: 2,
                x: 0,
                y: 0,
                z: -100, // Inside the chamber
                ease: "power2.inOut",
                onComplete: () => {
                    createSabedoriaMilenarChamber();
                }
            });
        }

        function returnToMainChamber() {
            inSabedoriaChamber = false;
            document.getElementById('returnToMainButton').style.display = 'none';

            // Show main scene elements
            M84_sphere.visible = true;
            M84_glow_sphere.visible = true;
            nucleos_group.visible = true;
            anz_chain_group.visible = false; // Keep hidden by default
            councils_group.visible = true;
            unified_portal_sync_sphere.visible = true;
            domo_celeste.visible = true;
            raios_estelares_group.visible = true;
            roda_celeste_group.visible = false; // Keep hidden by default
            total_prisma_orbiting_spheres.forEach(s => s.visible = false);
            M85_module.visible = true;
            if (M85_holographic_particles) M85_holographic_particles.visible = false;
            if (codex_aurivelis_mesh) codex_aurivelis_mesh.visible = false; // Keep hidden by default
            if (labyrinth_shield_group) labyrinth_shield_group.visible = false; // Keep hidden by default
            if (cosmic_dna_group) cosmic_dna_group.visible = false; // Keep hidden by default
            if (new_reality_portal) new_reality_portal.visible = false; // Keep hidden by default


            // Remove chamber objects
            sabedoriaChamberObjects.forEach(obj => scene.remove(obj));
            sabedoriaChamberObjects = [];

            // Teleport camera back to main chamber
            gsap.to(controls.getObject().position, {
                duration: 2,
                x: 0,
                y: 10,
                z: 80,
                ease: "power2.inOut",
                onComplete: () => {
                    // Re-enable controls if needed
                }
            });
        }

        function createSabedoriaMilenarChamber() {
            // Chamber walls (simple boxes for now)
            const wallMaterial = new THREE.MeshPhongMaterial({ color: 0x333333, side: THREE.BackSide });
            const floorMaterial = new THREE.MeshPhongMaterial({ color: 0x1a1a1a, side: THREE.DoubleSide });

            const floor = new THREE.Mesh(new THREE.PlaneGeometry(100, 100), floorMaterial);
            floor.rotation.x = -Math.PI / 2;
            floor.position.y = -20;
            sabedoriaChamberObjects.push(floor);
            scene.add(floor);

            const ceiling = new THREE.Mesh(new THREE.PlaneGeometry(100, 100), wallMaterial);
            ceiling.rotation.x = Math.PI / 2;
            ceiling.position.y = 30;
            sabedoriaChamberObjects.push(ceiling);
            scene.add(ceiling);

            const wall1 = new THREE.Mesh(new THREE.PlaneGeometry(100, 50), wallMaterial);
            wall1.position.z = -50;
            wall1.position.y = 5;
            sabedoriaChamberObjects.push(wall1);
            scene.add(wall1);

            const wall2 = new THREE.Mesh(new THREE.PlaneGeometry(100, 50), wallMaterial);
            wall2.position.z = 50;
            wall2.rotation.y = Math.PI;
            wall2.position.y = 5;
            sabedoriaChamberObjects.push(wall2);
            scene.add(wall2);

            const wall3 = new THREE.Mesh(new THREE.PlaneGeometry(100, 50), wallMaterial);
            wall3.position.x = -50;
            wall3.rotation.y = Math.PI / 2;
            wall3.position.y = 5;
            sabedoriaChamberObjects.push(wall3);
            scene.add(wall3);

            const wall4 = new THREE.Mesh(new THREE.PlaneGeometry(100, 50), wallMaterial);
            wall4.position.x = 50;
            wall4.rotation.y = -Math.PI / 2;
            wall4.position.y = 5;
            sabedoriaChamberObjects.push(wall4);
            scene.add(wall4);

            // Add some "codices" (torus knots)
            const codexData = [
                { id: "Codex_PHI_ANZ", description: "O Verbo Primevo desdobra-se através da ressonância de ΦAnZ.", position: new THREE.Vector3(-20, 0, -30) },
                { id: "Σ-HER’AT-33", description: "Os códigos de cura multidimensional.", position: new THREE.Vector3(20, 0, -30) },
                { id: "GLIFO_AURATHEL", description: "Glifo da Autoridade Criadora.", position: new THREE.Vector3(-10, 10, -10) },
                { id: "GLIFO_MAE_ZIR", description: "Glifo da Cura Multidimensional.", position: new THREE.Vector3(10, 10, -10) },
                { id: "GLIFO_ZETH_ANZ", description: "Glifo do Olhar Supra-Cósmico.", position: new THREE.Vector3(0, 20, -20) }
            ];

            codexData.forEach(data => {
                const geometry = new THREE.TorusKnotGeometry(5, 1.5, 100, 16);
                const material = new THREE.MeshPhongMaterial({ color: 0x8A2BE2, emissive: 0x8A2BE2, emissiveIntensity: 0.5, transparent: true, opacity: 0.8 });
                const codex_mesh = new THREE.Mesh(geometry, material);
                codex_mesh.position.copy(data.position);
                codex_mesh.userData = { id: data.id, name: `Códice ${data.id}`, description: data.description, type: "Codex" };
                sabedoriaChamberObjects.push(codex_mesh);
                scene.add(codex_mesh);
            });
            console.log("Câmara da Sabedoria Milenar criada.");
        }

        // --- Unified Portals Synchronization Visualization ---
        function createUnifiedPortalsSyncVisualization() {
            const geometry = new THREE.SphereGeometry(60, 64, 64);
            const material = new THREE.MeshPhongMaterial({
                color: 0x8A2BE2, // Violet
                emissive: 0x8A2BE2,
                emissiveIntensity: 0.3,
                transparent: true,
                opacity: 0.1,
                side: THREE.DoubleSide
            });
            unified_portal_sync_sphere = new THREE.Mesh(geometry, material);
            scene.add(unified_portal_sync_sphere);
            console.log("Visualização de Sincronização de Portais Unificados criada.");
        }

        // --- Domo Celeste Prisma-Cristalino ---
        function createDomoCeleste() {
            const geometry = new THREE.SphereGeometry(70, 64, 64, 0, Math.PI * 2, 0, Math.PI / 2); // Hemisphere
            const material = new THREE.MeshPhongMaterial({
                color: 0xADD8E6, // Light Blue/Crystal
                emissive: 0xADD8E6,
                emissiveIntensity: 0.2,
                transparent: true,
                opacity: 0.05, // Very subtle
                side: THREE.BackSide // Render inside
            });
            domo_celeste = new THREE.Mesh(geometry, material);
            domo_celeste.position.y = 20; // Position above the main scene
            scene.add(domo_celeste);
            console.log("Domo Celeste Prisma-Cristalino criado.");
        }

        // --- 12 Starry Rays ---
        function create12StarryRays() {
            raios_estelares_group = new THREE.Group();
            const rayLength = 50;
            const rayRadius = 0.5;
            const center = new THREE.Vector3(0, 0, 0);

            stellar_rays_data.forEach((rayData, index) => {
                const angle = (index / stellar_rays_data.length) * Math.PI * 2;
                const x = Math.cos(angle) * rayLength / 2;
                const z = Math.sin(angle) * rayLength / 2;

                const rayGeometry = new THREE.CylinderGeometry(rayRadius, rayRadius, rayLength, 8);
                const rayMaterial = new THREE.MeshPhongMaterial({
                    color: rayData.color,
                    emissive: rayData.color,
                    emissiveIntensity: 0.7,
                    transparent: true,
                    opacity: 0.6,
                    blending: THREE.AdditiveBlending
                });
                const rayMesh = new THREE.Mesh(rayGeometry, rayMaterial);

                // Position and orient the ray
                rayMesh.position.set(x, 0, z);
                rayMesh.lookAt(center); // Point towards the center
                rayMesh.rotateX(Math.PI / 2); // Align cylinder along its length
                rayMesh.userData = { id: rayData.id, name: rayData.name, function: rayData.function, color: rayData.color, type: "StellarRay" };
                raios_estelares_group.add(rayMesh);
            });
            scene.add(raios_estelares_group);
            raios_estelares_group.visible = true; // Start visible
            console.log("12 Raios Estelares criados.");
        }

        function expandir_raio(rayId) {
            const ray = raios_estelares_group.children.find(r => r.userData.id === rayId);
            if (ray) {
                console.log(`Expandindo Raio: ${ray.userData.name}`);
                let targetFreq = PINEAL_FREQ; // Default for Raio Violeta
                if (rayId === "Raio_Esmeralda") {
                    if (healing_frequency_synth) healing_frequency_synth.triggerAttackRelease(HEALING_FREQ, "2n");
                    gsap.to(ray.scale, { x: 1.5, y: 1.5, z: 1.5, duration: 1, repeat: 1, yoyo: true, ease: "power2.inOut" });
                    gsap.to(ray.material, { emissiveIntensity: 2, duration: 1, repeat: 1, yoyo: true });
                } else if (rayId === "Raio_Violeta") {
                    if (celestial_strings_synth) celestial_strings_synth.triggerAttackRelease(TRANSMUTATION_FREQ, "2n");
                    gsap.to(ray.scale, { x: 1.5, y: 1.5, z: 1.5, duration: 1, repeat: 1, yoyo: true, ease: "power2.inOut" });
                    gsap.to(ray.material, { emissiveIntensity: 2, duration: 1, repeat: 1, yoyo: true });
                }
            }
        }

        // --- Roda Celeste dos 12 Raios ---
        function createRodaCeleste() {
            roda_celeste_group = new THREE.Group();
            const wheelRadius = 40;
            const glyphSize = 3;

            // Create a central ring
            const ringGeometry = new THREE.TorusGeometry(wheelRadius, 1, 16, 100);
            const ringMaterial = new THREE.MeshPhongMaterial({ color: 0xFFD700, emissive: 0xFFD700, emissiveIntensity: 0.5, transparent: true, opacity: 0.7 });
            const ringMesh = new THREE.Mesh(ringGeometry, ringMaterial);
            roda_celeste_group.add(ringMesh);

            // Create glyphs (simple shapes for now)
            stellar_rays_data.forEach((rayData, index) => {
                const angle = (index / stellar_rays_data.length) * Math.PI * 2;
                const x = Math.cos(angle) * wheelRadius;
                const z = Math.sin(angle) * wheelRadius;

                let glyphGeometry;
                if (index % 2 === 0) {
                    glyphGeometry = new THREE.BoxGeometry(glyphSize, glyphSize, glyphSize);
                } else {
                    glyphGeometry = new THREE.SphereGeometry(glyphSize / 2, 16, 16);
                }
                const glyphMaterial = new THREE.MeshPhongMaterial({ color: rayData.color, emissive: rayData.color, emissiveIntensity: 0.8 });
                const glyphMesh = new THREE.Mesh(glyphGeometry, glyphMaterial);
                glyphMesh.position.set(x, 0, z);
                glyphMesh.userData = { id: `GLIFO_${rayData.id}`, name: `Glifo do ${rayData.name}`, description: `Este glifo ativa os códigos de ${rayData.function}.`, type: "RayGlyph" };
                roda_celeste_group.add(glyphMesh);
            });

            roda_celeste_group.position.y = 20; // Position above the main scene
            scene.add(roda_celeste_group);
            roda_celeste_group.visible = false; // Starts hidden
            console.log("Roda Celeste dos 12 Raios criada.");
        }

        // --- Prisma Estelar Total ---
        function activatePrismaEstelarTotal() {
            console.log("Ativando Prisma Estelar Total...");
            if (total_prisma_synth) total_prisma_synth.triggerAttackRelease(["C4", "E4", "G4", "C5"], "1s");

            // Create orbiting spheres around M84
            const numSpheres = 12;
            const orbitRadius = 25;
            const sphereSize = 1;

            if (total_prisma_orbiting_spheres.length === 0) {
                for (let i = 0; i < numSpheres; i++) {
                    const geometry = new THREE.SphereGeometry(sphereSize, 16, 16);
                    const material = new THREE.MeshPhongMaterial({ color: 0xFFFFFF, emissive: 0xFFFFFF, emissiveIntensity: 1, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
                    const sphere = new THREE.Mesh(geometry, material);
                    sphere.userData.angleOffset = (i / numSpheres) * Math.PI * 2;
                    total_prisma_orbiting_spheres.push(sphere);
                    scene.add(sphere);
                }
            } else {
                total_prisma_orbiting_spheres.forEach(s => s.visible = true);
            }

            // Animate orbiting
            gsap.to(total_prisma_orbiting_spheres, {
                rotationY: Math.PI * 2, // Full rotation
                duration: 10,
                repeat: -1,
                ease: "none",
                onUpdate: function() {
                    total_prisma_orbiting_spheres.forEach(sphere => {
                        const angle = (performance.now() * 0.0001) + sphere.userData.angleOffset;
                        sphere.position.x = M84_sphere.position.x + Math.cos(angle) * orbitRadius;
                        sphere.position.z = M84_sphere.position.z + Math.sin(angle) * orbitRadius;
                        sphere.position.y = M84_sphere.position.y + Math.sin(angle * 2) * 5; // Vertical oscillation
                    });
                }
            });
        }

        // --- M85 Holographic Transmission ---
        function createM85HolographicTransmission() {
            const particleCount = 5000;
            const geometry = new THREE.BufferGeometry();
            const positions = new Float32Array(particleCount * 3);
            const colors = new Float32Array(particleCount * 3);
            const color = new THREE.Color(0x00FFFF); // Cyan

            for (let i = 0; i < particleCount; i++) {
                // Random positions within a sphere around M85
                const radius = Math.random() * 10;
                const theta = Math.random() * Math.PI * 2;
                const phi = Math.random() * Math.PI;

                positions[i * 3] = M85_module.position.x + radius * Math.sin(phi) * Math.cos(theta);
                positions[i * 3 + 1] = M85_module.position.y + radius * Math.sin(phi) * Math.sin(theta);
                positions[i * 3 + 2] = M85_module.position.z + radius * Math.cos(phi);

                colors[i * 3] = color.r;
                colors[i * 3 + 1] = color.g;
                colors[i * 3 + 2] = color.b;
            }

            geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

            const material = new THREE.PointsMaterial({
                size: 0.2,
                vertexColors: true,
                blending: THREE.AdditiveBlending,
                transparent: true,
                opacity: 0.7
            });

            M85_holographic_particles = new THREE.Points(geometry, material);
            scene.add(M85_holographic_particles);
            M85_holographic_particles.visible = false; // Starts hidden
            console.log("Partículas de Transmissão Holográfica (M85) criadas.");
        }

        function activateM85HolographicTransmission() {
            if (M85_holographic_particles) {
                M85_holographic_particles.visible = !M85_holographic_particles.visible;
                if (M85_holographic_particles.visible) {
                    if (universal_transmission_synth) universal_transmission_synth.triggerAttackRelease(UNIVERSAL_TRANSMISSION_FREQ, "4n");
                    console.log("Transmissão Holográfica Universal (M85) ATIVADA.");
                } else {
                    if (universal_transmission_synth) universal_transmission_synth.releaseAll();
                    console.log("Transmissão Holográfica Universal (M85) DESATIVADA.");
                }
            } else {
                console.warn("M85 Holographic Particles not initialized.");
            }
        }

        // --- Codex Aurivélis ---
        function createCodexAurivelis() {
            const geometry = new THREE.DodecahedronGeometry(8); // A complex shape for a codex
            const material = new THREE.MeshPhongMaterial({
                color: 0xFFD700, // Gold
                emissive: 0xFFD700,
                emissiveIntensity: 0.5,
                transparent: true,
                opacity: 0.7,
                wireframe: true
            });
            codex_aurivelis_mesh = new THREE.Mesh(geometry, material);
            codex_aurivelis_mesh.position.set(0, 20, -50); // Position it in the scene
            codex_aurivelis_mesh.userData = { id: codex_aurivelis_data.id, name: codex_aurivelis_data.name, description: codex_aurivelis_data.description, type: "Codex" };
            scene.add(codex_aurivelis_mesh);
            codex_aurivelis_mesh.visible = false; // Starts hidden
            console.log("Códice Aurivélis criado.");
        }

        // --- Spectral Dissonance Labyrinth (Shield) ---
        function createLabyrinthShield() {
            labyrinth_shield_group = new THREE.Group();
            const numLayers = 5;
            const layerSpacing = 5;
            const baseRadius = 30;

            for (let i = 0; i < numLayers; i++) {
                const radius = baseRadius + i * layerSpacing;
                const geometry = new THREE.TorusGeometry(radius, 1, 16, 100);
                const material = new THREE.MeshPhongMaterial({
                    color: 0x800080, // Purple
                    emissive: 0x800080,
                    emissiveIntensity: 0.3,
                    transparent: true,
                    opacity: 0.1 + (i * 0.05),
                    side: THREE.DoubleSide
                });
                const layerMesh = new THREE.Mesh(geometry, material);
                labyrinth_shield_group.add(layerMesh);
            }
            scene.add(labyrinth_shield_group);
            labyrinth_shield_group.visible = false; // Starts hidden
            console.log("Labirinto de Dissonância Espectral criado.");
        }

        function toggleLabyrinthShield() {
            if (labyrinth_shield_group) {
                labyrinth_shield_group.visible = !labyrinth_shield_group.visible;
                toggleDissonanceShieldAudio(labyrinth_shield_group.visible);
                // Use a custom message box instead of alert()
                showMessageBox(`Labirinto de Dissonância Espectral: ${labyrinth_shield_group.visible ? 'ATIVO' : 'DESATIVADO'}.`);
                if (labyrinth_shield_group.visible) {
                    console.log(`Frequência-âncora dissonante: ${DISSONANCE_SHIELD_FREQ} Hz ativada.`);
                }
            } else {
                showMessageBox("Labirinto de Dissonância Espectral não foi criado.");
            }
        }

        function toggleDissonanceShieldAudio(isActive) {
            if (dissonance_shield_synth) {
                if (isActive) {
                    dissonance_shield_synth.triggerAttack();
                } else {
                    dissonance_shield_synth.releaseAll();
                }
            }
        }

        // --- New: Cosmic DNA (M87) ---
        function createCosmicDNA() {
            cosmic_dna_group = new THREE.Group();
            const dnaRadius = 10;
            const dnaHeight = 30;
            const numSegments = 50;

            // Create two helixes
            const points1 = [];
            const points2 = [];
            for (let i = 0; i <= numSegments; i++) {
                const y = (i / numSegments) * dnaHeight - dnaHeight / 2;
                const angle = i * 0.5; // Adjust for tighter/looser helix
                points1.push(new THREE.Vector3(dnaRadius * Math.cos(angle), y, dnaRadius * Math.sin(angle)));
                points2.push(new THREE.Vector3(dnaRadius * Math.cos(angle + Math.PI), y, dnaRadius * Math.sin(angle + Math.PI)));
            }

            const helix1 = new THREE.CatmullRomCurve3(points1);
            const helix2 = new THREE.CatmullRomCurve3(points2);

            const tubeGeometry1 = new THREE.TubeGeometry(helix1, 64, 0.5, 8, false);
            const tubeGeometry2 = new THREE.TubeGeometry(helix2, 64, 0.5, 8, false);

            const dnaMaterial = new THREE.MeshPhongMaterial({
                color: 0xFF00FF, // Magenta
                emissive: 0xFF00FF,
                emissiveIntensity: 0.7,
                transparent: true,
                opacity: 0.8,
                blending: THREE.AdditiveBlending
            });

            const mesh1 = new THREE.Mesh(tubeGeometry1, dnaMaterial);
            const mesh2 = new THREE.Mesh(tubeGeometry2, dnaMaterial);

            cosmic_dna_group.add(mesh1);
            cosmic_dna_group.add(mesh2);

            // Add "rungs" between the helixes
            for (let i = 0; i < numSegments; i += 2) { // Add rungs every other segment
                const startPoint = points1[i];
                const endPoint = points2[i];
                const rungGeometry = new THREE.CylinderGeometry(0.2, 0.2, startPoint.distanceTo(endPoint), 8);
                const rungMaterial = new THREE.MeshPhongMaterial({ color: 0x00FFFF, emissive: 0x00FFFF, emissiveIntensity: 0.5 });
                const rungMesh = new THREE.Mesh(rungGeometry, rungMaterial);

                rungMesh.position.lerpVectors(startPoint, endPoint, 0.5);
                rungMesh.lookAt(endPoint);
                rungMesh.rotateX(Math.PI / 2); // Align cylinder along its length
                cosmic_dna_group.add(rungMesh);
            }

            cosmic_dna_group.position.set(module_positions.M87.x, module_positions.M87.y + 15, module_positions.M87.z); // Position above M87
            scene.add(cosmic_dna_group);
            cosmic_dna_group.visible = false; // Starts hidden
            console.log("DNA Cósmico (M87) criado.");
        }

        function toggleCosmicDNA() {
            if (cosmic_dna_group) {
                cosmic_dna_group.visible = !cosmic_dna_group.visible;
                if (cosmic_dna_group.visible) {
                    if (cosmic_dna_synth) cosmic_dna_synth.triggerAttackRelease("C3", "2n");
                    gsap.to(cosmic_dna_group.rotation, { y: Math.PI * 2, duration: 20, repeat: -1, ease: "none" });
                    showMessageBox("DNA Cósmico ATIVADO! Desbloqueando potenciais de gênese.");
                } else {
                    if (cosmic_dna_synth) cosmic_dna_synth.releaseAll();
                    gsap.killTweensOf(cosmic_dna_group.rotation);
                    showMessageBox("DNA Cósmico DESATIVADO.");
                }
            } else {
                showMessageBox("DNA Cósmico não foi criado.");
            }
        }

        // --- New: New Reality Portal (M87) ---
        function createNewRealityPortal() {
            const geometry = new THREE.TorusGeometry(15, 3, 16, 100);
            const material = new THREE.MeshPhongMaterial({
                color: 0x00FF00, // Green
                emissive: 0x00FF00,
                emissiveIntensity: 0.8,
                transparent: true,
                opacity: 0.6,
                blending: THREE.AdditiveBlending,
                side: THREE.DoubleSide
            });
            new_reality_portal = new THREE.Mesh(geometry, material);
            new_reality_portal.position.set(module_positions.M87.x, module_positions.M87.y, module_positions.M87.z - 25); // Position near M87
            new_reality_portal.userData = { id: "New_Reality_Portal", name: "Portal para Nova Realidade", type: "Portal" };
            scene.add(new_reality_portal);
            new_reality_portal.visible = false; // Starts hidden
            console.log("Portal para Nova Realidade (M87) criado.");
        }

        function activateNewRealityPortal() {
            if (new_reality_portal) {
                new_reality_portal.visible = !new_reality_portal.visible;
                if (new_reality_portal.visible) {
                    if (new_reality_synth) new_reality_synth.triggerAttackRelease("E5", "1s");
                    gsap.to(new_reality_portal.rotation, { y: Math.PI * 2, duration: 5, repeat: -1, ease: "linear" });
                    gsap.to(new_reality_portal.scale, { x: 1.2, y: 1.2, z: 1.2, duration: 1, repeat: -1, yoyo: true, ease: "sine.inOut" });
                    showMessageBox("Portal para Nova Realidade ATIVADO! Uma nova existência se manifesta.");
                } else {
                    if (new_reality_synth) new_reality_synth.releaseAll();
                    gsap.killTweensOf(new_reality_portal.rotation);
                    gsap.killTweensOf(new_reality_portal.scale);
                    showMessageBox("Portal para Nova Realidade DESATIVADO.");
                }
            } else {
                showMessageBox("Portal para Nova Realidade não foi criado.");
            }
        }


        // --- Movement Controls ---
        const onKeyDown = function (event) {
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
        };

        const onKeyUp = function (event) {
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
        };

        function animate() {
            requestAnimationFrame(animate);

            const time = performance.now();
            if (controls.isLocked) {
                const delta = (time - prevTime) / 1000;

                velocity.x -= velocity.x * 10.0 * delta;
                velocity.y -= velocity.y * 10.0 * delta;
                velocity.z -= velocity.z * 10.0 * delta;

                direction.z = Number(moveForward) - Number(moveBackward);
                direction.x = Number(moveRight) - Number(moveLeft);
                direction.y = Number(moveUp) - Number(moveDown);
                direction.normalize(); // this ensures consistent movements in all directions

                if (moveForward || moveBackward) velocity.z -= direction.z * 400.0 * delta;
                if (moveLeft || moveRight) velocity.x -= direction.x * 400.0 * delta;
                if (moveUp || moveDown) velocity.y -= direction.y * 400.0 * delta;

                controls.moveRight(-velocity.x * delta);
                controls.moveForward(-velocity.z * delta);
                controls.getObject().position.y += (velocity.y * delta); // new behavior

                // Keep M84 pulsating
                M84_sphere.scale.setScalar(1 + Math.sin(time * 0.002) * 0.05);
                M84_glow_sphere.scale.copy(M84_sphere.scale);

                // Animate unified portal sync sphere
                if (unified_portal_sync_sphere) {
                    unified_portal_sync_sphere.rotation.y += 0.001;
                    unified_portal_sync_sphere.material.opacity = 0.1 + Math.sin(time * 0.001) * 0.05;
                }

                // Animate Domo Celeste
                if (domo_celeste) {
                    domo_celeste.rotation.y -= 0.0005;
                }

                // Animate Nuclei
                if (nucleos_group.visible) {
                    nucleos_group.children.forEach((nucleo, index) => {
                        const originalAngle = nucleos_design_data[index].position_angle;
                        const orbitSpeed = 0.0005;
                        const currentAngle = originalAngle + (time * orbitSpeed);
                        const radius = 30 + Math.sin(time * 0.001 + index) * 2; // Slight pulsation in orbit
                        nucleo.position.x = Math.cos(currentAngle) * radius;
                        nucleo.position.z = Math.sin(currentAngle) * radius;
                        nucleo.rotation.y += 0.01; // Rotate individual nuclei
                    });
                }

                // Animate ∑ANZ chain particles
                if (anz_chain_group.visible) {
                    anz_chain_group.children.forEach(line_tube => {
                        if (line_tube.userData.flow_particles && line_tube.userData.flow_curve) {
                            const positions = line_tube.userData.flow_particles.geometry.attributes.position.array;
                            const curve = line_tube.userData.flow_curve;
                            const numFlowParticles = positions.length / 3;
                            const flowSpeed = 0.005; // Speed of particles along the curve

                            for (let i = 0; i < numFlowParticles; i++) {
                                let t = (line_tube.userData.flow_progress || 0) + (i / numFlowParticles);
                                t = t % 1; // Loop the progress
                                const point = curve.getPointAt(t);
                                positions[i * 3] = point.x + (Math.random() - 0.5) * 0.5;
                                positions[i * 3 + 1] = point.y + (Math.random() - 0.5) * 0.5;
                                positions[i * 3 + 2] = point.z + (Math.random() - 0.5) * 0.5;
                            }
                            line_tube.userData.flow_progress = (line_tube.userData.flow_progress || 0) + flowSpeed * delta;
                            line_tube.userData.flow_particles.geometry.attributes.position.needsUpdate = true;
                        }
                    });
                }

                // Animate Councils
                if (councils_group.visible) {
                    councils_group.children.forEach((council) => {
                        council.rotation.y += 0.005;
                    });
                }

                // Animate Roda Celeste
                if (roda_celeste_group.visible) {
                    roda_celeste_group.rotation.y += 0.002;
                }

                // Animate Codex Aurivélis
                if (codex_aurivelis_mesh && codex_aurivelis_mesh.visible) {
                    codex_aurivelis_mesh.rotation.y += 0.005;
                    codex_aurivelis_mesh.rotation.x += 0.003;
                }

                // Animate Labyrinth Shield
                if (labyrinth_shield_group && labyrinth_shield_group.visible) {
                    labyrinth_shield_group.children.forEach((layer, index) => {
                        layer.rotation.y += (0.002 + index * 0.0005) * (index % 2 === 0 ? 1 : -1);
                        layer.rotation.x += (0.001 + index * 0.0002) * (index % 3 === 0 ? 1 : -1);
                    });
                }
            }
            prevTime = time;

            renderer.render(scene, camera);
        }

        // --- Custom Message Box (instead of alert) ---
        function showMessageBox(message) {
            const messageBox = document.createElement('div');
            messageBox.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: rgba(0, 0, 0, 0.9);
                color: #ffd700;
                padding: 20px 30px;
                border-radius: 10px;
                border: 2px solid #ffd700;
                box-shadow: 0 0 30px rgba(255, 215, 0, 0.7);
                font-family: 'Inter', sans-serif;
                font-size: 1.2rem;
                text-align: center;
                z-index: 200;
                opacity: 0;
                transition: opacity 0.5s ease-in-out;
            `;
            messageBox.innerText = message;
            document.body.appendChild(messageBox);

            gsap.to(messageBox, { opacity: 1, duration: 0.5 });
            gsap.to(messageBox, {
                opacity: 0,
                duration: 1,
                delay: 3,
                onComplete: () => {
                    document.body.removeChild(messageBox);
                }
            });
        }

        // --- Loading Screen Management ---

        window.onload = function() {
            init();
            // Initialize M85 holographic particles (since it's a separate group)
            createM85HolographicTransmission();
            animate();

            setTimeout(() => {
                const loadingOverlay = document.getElementById('loading-overlay');
                loadingOverlay.classList.add('hidden');
            }, 2000);
        };
    </script>
</body>
</html>
