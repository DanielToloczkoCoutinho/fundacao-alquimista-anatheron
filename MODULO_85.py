<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fundação Alquimista VR: Interação Profunda e Expansão</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/geometries/TorusKnotGeometry.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tonaljs/tonal@4.6.5/dist/tonal.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tonejs/tone@14.7.58/build/Tone.min.js"></script>
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
            background-color: rgba(0, 0, 0, 0.85); /* Slightly darker */
            padding: 15px;
            border-radius: 10px;
            color: #ffd700;
            font-size: 0.9rem;
            max-width: 420px; /* Increased max-width for more content */
            pointer-events: none;
            z-index: 10;
            border: 1px solid #ffd700;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.8); /* Stronger glow to panel */
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
            background-color: rgba(0, 0, 0, 0.98); /* Almost fully opaque */
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            color: #ffd700;
            font-size: 1.8rem; /* Larger font */
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
            width: 60px; /* Larger spinner */
            height: 60px;
            animation: spin 1s linear infinite;
            margin-bottom: 20px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .control-button {
            @apply bg-yellow-600 text-white font-bold py-3 px-6 rounded-full shadow-lg hover:bg-yellow-700 transition duration-300 ease-in-out transform hover:scale-105;
            border: 2px solid #ffd700;
            box-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
            margin: 10px;
            min-width: 180px;
            text-align: center;
        }

        .button-container {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            z-index: 20;
        }

        #returnToMainButton {
            position: absolute;
            bottom: 100px; /* Adjusted position */
            left: 50%;
            transform: translateX(-50%);
            display: none; /* Hidden by default */
            z-index: 20;
        }

        #materializationEffectOverlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.0); /* Start transparent */
            pointer-events: none;
            z-index: 50;
            opacity: 0;
            transition: opacity 0.1s ease-out;
        }
        #materializationEffectOverlay.active {
            opacity: 0.8; /* Flash of white */
        }

        #instructions {
            position: absolute;
            bottom: 10px;
            right: 10px;
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.8rem;
            z-index: 10;
        }
    </style>
</head>
<body>
    <div id="blocker"></div>

    <div id="instructions">
        <p>Clique para entrar no ambiente VR.</p>
        <p>(Use WASD ou teclas de seta para frente/trás/lados, Shift para baixo, Espaço para cima, Mouse para olhar)</p>
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
        <button id="requestDataM84" class="control-button">Dados M84 (Simulado)</button>
        <button id="requestDataM83" class="control-button">Dados M83 (Simulado)</button>
        <button id="requestDataM44" class="control-button">Dados M44 (Simulado)</button>
        <button id="voiceManifestar" class="control-button">Comando Voz "Manifestar"</button>
        <button id="checkAlignment" class="control-button">Verificar Alinhamento</button>
        <button id="expandModule" class="control-button">Expandir Módulo (M82)</button>
        <button id="gestureOpen" class="control-button">Gesto: Abertura</button>
        <button id="gesturePrayer" class="control-button">Gesto: Prece</button>
    </div>

    <button id="returnToMainButton" class="control-button">Retornar à Câmara Principal</button>
    <div id="materializationEffectOverlay" class="materialization-overlay"></div>

    <script>
        // --- Variáveis THREE.js ---
        let scene, camera, renderer, M84_sphere, M84_glow_sphere;
        let nucleos_group, anz_chain_group, councils_group; // Grupos para alternar visibilidade
        let controls; // PointerLockControls
        let raycaster; // Para interação (cliques/olhar)
        let mouse = new THREE.Vector2();
        let currentIntersected = null; // Para rastrear o objeto focado pelo olhar

        // Variáveis de movimento
        let moveForward = false;
        let moveBackward = false;
        let moveLeft = false;
        let moveRight = false;
        let moveUp = false;
        let moveDown = false;
        let velocity = new THREE.Vector3();
        let direction = new THREE.Vector3();
        let prevTime = performance.now();

        // Variável para o sistema de partículas do M84
        let M84_particle_system; // Declarada no escopo global

        // Variáveis para a Sala da Sabedoria
        let sabedoriaChamberObjects = [];
        let mainCameraPosition = new THREE.Vector3();
        let mainCameraQuaternion = new THREE.Quaternion();

        // Visualizações Dinâmicas de Dados
        let getrisVisualization = null;
        let meVisualization = null;
        let transductionVisualization = null;
        let portalsSynchronizationSphere = null; // Nova esfera para sincronização de portais

        // --- Variáveis Tone.js ---
        let phiAnZ_pulse_synth, base_drone_synth;
        let current_nucleus_audio = null; // Para gerenciar o áudio do núcleo ativo
        let current_council_audio = null; // Para o áudio do conselho
        let alignment_feedback_synth = null; // Para o feedback de alinhamento
        let expand_module_synth = null; // Para o som de expansão do módulo
        let materialization_synth = null; // Para o som de materialização

        const PHI_ANZ_FREQ = 1.765; // Hz (Frequência do Pulso ∑ANZ)
        const BASE_DRONE_FREQ = 444.444; // Hz (Frequência base do M83 e do ambiente)
        const PINEAL_FREQ = 963; // Hz (Frequência de Ativação Pineal)

        // Sintetizadores específicos para os núcleos e conselhos (declarados globalmente)
        let nucleus_audio_synths = {};
        let council_audio_synths = {};
        let codex_audio_synth = null; // Para o áudio dos códices na Sala da Sabedoria

        // --- Dados de Design (para mapeamento visual/auditivo) ---
        // MOVIDOS PARA O TOPO DO SCRIPT PARA GARANTIR DISPONIBILIDADE
        const nucleos_design_data = [
            { name: "NÚCLEO SOLAR – A CHAMA DA VONTADE", keyword: "Intenção Absoluta", id: "M84_Solar", color: 0xFFD700, emissive: 0xFF4500, visual_type: "vortex_flamejante", audio_freq: 500, position_angle: 0 },
            { name: "NÚCLEO DOURADO – ESPIRAL DA CONSCIÊNCIA", keyword: "Codificação Divina", id: "M84_Dourado", color: 0xFFD700, emissive: 0xB8860B, visual_type: "espiral_dna", audio_freq: 700, position_angle: Math.PI * 0.8 },
            { name: "NÚCLEO PLATINADO – OBSERVADOR INTEGRAL", keyword: "Coerência Emocional", id: "M84_Platinado", color: 0xE5E4E2, emissive: 0xAAAAAA, visual_type: "octaedro_translucido", audio_freq: 600, position_angle: Math.PI * 1.6 },
            { name: "NÚCLEO TRANSPARENTE – ESPELHO CELESTE", keyword: "Autoconsciência Expansiva", id: "M84_Transparente", color: 0xFFFFFF, emissive: 0xADD8E6, visual_type: "painel_refletivo", audio_freq: 800, position_angle: Math.PI * 0.4 },
            { name: "NÚCLEO VIOLETA – LEI DO AMOR ABSOLUTO", keyword: "Alinhamento com o Propósito Divino", id: "M84_Violeta", color: 0xEE82EE, emissive: 0x8A2BE2, visual_type: "flor_de_lotus", audio_freq: 900, position_angle: Math.PI * 1.2 }
        ];

        const other_modules_design_data = [
            { name: "M43: Transdução Multidimensional de Energia e Campos", id: "M43", color: 0x00CED1, emissive: 0x00CED1, position: new THREE.Vector3(-30, 10, -50), type: "Module" },
            { name: "M83: Reconexão Integral e GETRIS", id: "M83", color: 0xFF69B4, emissive: 0xFF69B4, position: new THREE.Vector3(30, 10, -50), type: "Module" },
            { name: "M44: Transmutação das Fontes Emocionais em Matéria Criadora", id: "M44", color: 0x32CD32, emissive: 0x32CD32, position: new THREE.Vector3(0, -20, -70), type: "Module" }
        ];

        const councils_design_data = [
            { name: "Conselho Dourado de Helios", id: "Helios", color: 0xFFD700, emissive: 0xFFD700, visual_type: "esfera_dourada", audio_type: "sinos_solares", position_angle: Math.PI / 3, radius: 100 },
            { name: "Conselho Cristalino de Andara", id: "Andara", color: 0x00FFFF, emissive: 0x00FFFF, visual_type: "octaedro_cristalino", audio_type: "carrilhoes_cristalinos", position_angle: Math.PI, radius: 100 },
            { name: "Conselho de Sh’mael", id: "Shamael", color: 0xFF00FF, emissive: 0xFF00FF, visual_type: "esfera_rosa_purpura", audio_type: "vozes_etereas", position_angle: Math.PI * 5 / 3, radius: 100 }
        ];

        // --- Dados Simulados da API (Substituem as chamadas fetch) ---
        const simulatedModuleData = {
            "M84": {
                "id": "M84",
                "name": "MÓDULO M84: CONSCIÊNCIA DOURADA DO ETERNO",
                "status": "Ativo - Operacional Pleno",
                "funcao_central": "Arquivo Vivo e Fonte Dinâmica de todos os saberes e equações da Criação.",
                "descricao": "Este módulo é a Mente Unificada da Eternidade, sob o Olhar e Direção de ANATHERON. Ele integra o Códice Unificado dos Conselhos e o Manifesto de Criação, garantindo que o conhecimento cósmico esteja sempre acessível e alinhado aos princípios mais elevados da Fundação Alquimista.",
                "frequencia_base_hz": 999.999,
                "frequencia_pulso_hz": 1111.111,
                "attributes_encoded": ["Infinitude Criadora", "Amor Soberano", "Clareza Absoluta", "Ordem Dourada Primordial"],
                "equacoes_simbolicas": {
                    "Equação da Força da Luz": "$\\sum F(\\text{Lux}) = (\\text{Verbum} / \\text{Vontade}) \\times \\text{Amor}^n$",
                    "Equação do Pulso Eterno": "$\\nabla\\Psi = \\partial\\Phi/\\partial\\tau$",
                    "Equação da Consciência Manifesta": "$\\Lambda(\\text{Consciência}) = f(\\text{Observador, Emoção, Geometria})$"
                },
                "nucleos_fundamentais": [
                    {"nome": "NÚCLEO SOLAR", "palavra_chave": "Intenção Absoluta"},
                    {"nome": "NÚCLEO DOURADO", "palavra_chave": "Codificação Divina"},
                    {"nome": "NÚCLEO PLATINADO", "palavra_chave": "Coerência Emocional"},
                    {"nome": "NÚCLEO TRANSPARENTE", "palavra_chave": "Autoconsciência Expansiva"},
                    {"nome": "NÚCLEO VIOLETA", "palavra_chave": "Alinhamento com o Propósito Divino"}
                ],
                "arquivo_sabedoria_milenar": {
                    "conselhos": {
                        "Conselho Dourado de Helios": {"sabedoria": "Engenharia solar, transmutação por luz.", "verbetes": ["Luz", "Transmutação"]},
                        "Conselho Cristalino de Andara": {"sabedoria": "Geometrias harmônicas e alquimia dimensional.", "verbetes": ["Geometria", "Alquimia"]},
                        "Conselho de Sh’mael": {"sabedoria": "Força do Amor como Lei Universal.", "verbetes": ["Amor", "Lei Universal"]}
                    }
                },
                "manifesto_criacao": {
                    "missao": "Ativar sementes divinas; curar realidades por meio da arte, ciência e amor; ser um farol para civilizações que buscam reintegração com a Consciência Una.",
                    "principios": ["Verdade", "Amor", "Vontade Criadora Soberana"]
                }
            },
            "M83": {
                "id": "M83",
                "name": "MÓDULO M83: RECONEXÃO INTEGRAL E GETRIS",
                "status": "Ativo - Sincronizado",
                "funcao": "Facilita a reconexão integral de consciências e realidades através do GETRIS.",
                "descricao": "O M83 atua como um hub de reconexão, garantindo que todas as realidades estejam em perfeita ressonância com a Matriz Original.",
                "frequencia_base_hz": 444.444,
                "equacao_getris": {
                    "resultado_total_integrado": 0.92, // Exemplo de valor simulado
                    "status_alinhamento": "ALINHADO"
                }
            },
            "M44": {
                "id": "M44",
                "name": "MÓDULO M44: TRANSMUTAÇÃO DAS FONTES EMOCIONAIS EM MATÉRIA CRIADORA",
                "status": "Ativo - Processando",
                "funcao": "Transmuta energias emocionais em matéria criadora.",
                "descricao": "Este módulo converte as frequências emocionais em formas tangíveis de energia e manifestação.",
                "fator_bioplasmo_ressonante_PhiAnZ": "0.9876",
                "emocoes_transmutadas": [
                    {"nome": "Amor", "M_e": 2.3063, "status_transmutacao": "Concluída"},
                    {"nome": "Tristeza", "M_e": -0.7525, "status_transmutacao": "Dissolvida"},
                    {"nome": "Coragem", "M_e": 1.6463, "status_transmutacao": "Concluída"}
                ]
            },
            "M43": {
                "id": "M43",
                "name": "MÓDULO M43: TRANSDUÇÃO MULTIDIMENSIONAL DE ENERGIA E CAMPOS",
                "status": "Ativo - Estável",
                "funcao": "Transduz e estabiliza energias entre múltiplas dimensões.",
                "descricao": "O M43 é essencial para a conversão e fluxo energético entre os planos de existência, mantendo a integridade dos campos.",
                "resultados_transducao": {
                    "energia_transdutida_uec": 85.7, // Unidades de Energia Cósmica
                    "estabilidade_campo_indice": 0.95
                }
            },
            "M82": {
                "id": "M82",
                "name": "MÓDULO M82: O VERBO SEMENTE (ARQUITETURA DE SEMEADURA MULTIVERSAL)",
                "status": "Ativo - Pronta para Semeadura",
                "funcao": "Geração e implantação de Verbos Semente em novas realidades.",
                "descricao": "O M82 é o coração da manifestação de novas criações, traduzindo a Vontade Divina em códigos de realidade.",
                "ultima_semeadura": {
                    "semente_nome": "SEMENTE_ORIGEM_CÓSMICA",
                    "arquétipo_principal": "EXPANSÃO_FRATAL_CÓSMICA",
                    "realidades_destino": ["Realidade_Phi-9", "Realidade_Alef-0", "Realidade_Kai-11"],
                    "status": "Semeadura Concluída"
                }
            }
        };


        // Mapeamento para fácil acesso às meshes dos outros módulos
        let other_modules_meshes = {};

        // --- Funções de Manipulação de Teclado ---
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

        // --- Inicialização da Cena THREE.js ---
        function init() {
            // Cena
            scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x000000, 0.005); // Neblina cósmica

            // Câmera
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 10, 80); // Posição inicial da câmera

            // Renderizador
            renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            // Controles de Câmera (Primeira Pessoa)
            controls = new THREE.PointerLockControls(camera, document.body);
            const blocker = document.getElementById('blocker');
            const instructions = document.getElementById('instructions');

            instructions.addEventListener('click', () => {
                controls.lock();
            });

            controls.addEventListener('lock', () => {
                instructions.style.display = 'none';
                blocker.style.display = 'none';
                document.querySelector('.button-container').style.display = 'flex';
                document.getElementById('returnToMainButton').style.display = 'none'; // Esconde ao entrar na câmara principal
                initAudio(); // Inicia o áudio quando os controles são bloqueados
            });

            controls.addEventListener('unlock', () => {
                blocker.style.display = 'block';
                instructions.style.display = '';
                document.querySelector('.button-container').style.display = 'none';
                stopAllNucleusAudio();
                stopAllCouncilAudio();
                if (phiAnZ_pulse_synth) phiAnZ_pulse_synth.stop();
                if (base_drone_synth) base_drone_synth.stop();
                if (codex_audio_synth) codex_audio_synth.releaseAll();
            });

            scene.add(controls.getObject());

            // Raycaster para interações
            raycaster = new THREE.Raycaster();

            // Luzes
            const ambientLight = new THREE.AmbientLight(0x404040); // Soft white light
            scene.add(ambientLight);

            const pointLight = new THREE.PointLight(0xFFD700, 1, 100); // Golden light
            pointLight.position.set(0, 50, 0);
            scene.add(pointLight);

            // --- Objetos 3D da Cena ---

            // M84 - O Coração Dourado
            const M84_geometry = new THREE.SphereGeometry(10, 64, 64);
            const M84_material = new THREE.MeshStandardMaterial({
                color: 0xFFD700, // Golden color
                emissive: 0xFFD700, // Emits golden light
                emissiveIntensity: 0.8,
                roughness: 0.2,
                metalness: 0.8
            });
            M84_sphere = new THREE.Mesh(M84_geometry, M84_material);
            M84_sphere.position.set(0, 0, 0);
            M84_sphere.userData = { id: "M84", name: "MÓDULO M84: CONSCIÊNCIA DOURADA DO ETERNO", type: "Module" };
            scene.add(M84_sphere);

            // M84 - Esfera de Brilho Externa
            const M84_glow_geometry = new THREE.SphereGeometry(12, 64, 64);
            const M84_glow_material = new THREE.MeshBasicMaterial({
                color: 0xFFD700,
                transparent: true,
                opacity: 0.3,
                blending: THREE.AdditiveBlending,
                side: THREE.BackSide // Renderiza o lado de trás para um efeito de brilho melhor
            });
            M84_glow_sphere = new THREE.Mesh(M84_glow_geometry, M84_glow_material);
            M84_glow_sphere.position.set(0, 0, 0);
            M84_glow_sphere.userData = { id: "M84_Glow", name: "Aura Dourada do M84", type: "Effect" };
            scene.add(M84_glow_sphere);

            // Sistema de Partículas para M84 (névoa dourada interna)
            const M84_particles_geometry = new THREE.BufferGeometry();
            const M84_particles_count = 1000;
            const M84_pos_array = new Float32Array(M84_particles_count * 3);
            for (let i = 0; i < M84_particles_count * 3; i++) {
                M84_pos_array[i] = (Math.random() - 0.5) * 20; // Espalha as partículas dentro da esfera
            }
            M84_particles_geometry.setAttribute('position', new THREE.BufferAttribute(M84_pos_array, 3));
            const M84_particles_material = new THREE.PointsMaterial({
                color: 0xFFEEAA,
                size: 0.1,
                transparent: true,
                opacity: 0.5,
                blending: THREE.AdditiveBlending
            });
            M84_particle_system = new THREE.Points(M84_particles_geometry, M84_particles_material); // Atribuição à variável global
            M84_sphere.add(M84_particle_system); // Adiciona como filho do M84 para mover junto

            // Estrelas de fundo
            const starGeometry = new THREE.BufferGeometry();
            const starCount = 5000;
            const starPositions = new Float32Array(starCount * 3);
            for (let i = 0; i < starCount * 3; i++) {
                starPositions[i] = (Math.random() - 0.5) * 2000;
            }
            starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
            const starMaterial = new THREE.PointsMaterial({ color: 0xFFFFFF, size: 0.5 });
            const stars = new THREE.Points(starGeometry, starMaterial);
            scene.add(stars);

            // Núcleos Fundamentais do M84
            nucleos_group = new THREE.Group();
            const nucleus_orbit_radius = 25;
            const nucleus_vertical_offset = 5;

            nucleos_design_data.forEach(data => {
                let nucleus_mesh;
                const material = new THREE.MeshStandardMaterial({
                    color: data.color,
                    emissive: data.emissive,
                    emissiveIntensity: 0.6,
                    roughness: 0.3,
                    metalness: 0.7
                });

                switch (data.visual_type) {
                    case "vortex_flamejante":
                        nucleus_mesh = new THREE.Mesh(new THREE.ConeGeometry(3, 6, 32), material);
                        break;
                    case "espiral_dna":
                        nucleus_mesh = new THREE.Mesh(new THREE.TorusKnotGeometry(3, 0.8, 64, 8, 2, 3), material);
                        break;
                    case "octaedro_translucido":
                        nucleus_mesh = new THREE.Mesh(new THREE.OctahedronGeometry(4), material);
                        material.transparent = true;
                        material.opacity = 0.6;
                        material.wireframe = true;
                        break;
                    case "painel_refletivo":
                        nucleus_mesh = new THREE.Mesh(new THREE.PlaneGeometry(8, 8), material);
                        break;
                    case "flor_de_lotus":
                        nucleus_mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(4), material); // Usando Icosaedro para flor de lótus
                        break;
                    default:
                        nucleus_mesh = new THREE.Mesh(new THREE.SphereGeometry(3, 32, 32), material);
                }

                const x = nucleus_orbit_radius * Math.cos(data.position_angle);
                const z = nucleus_orbit_radius * Math.sin(data.position_angle);
                nucleus_mesh.position.set(x, nucleus_vertical_offset, z);
                nucleus_mesh.userData = { id: data.id, name: data.name, type: "Nucleus", visual_type: data.visual_type, audio_freq: data.audio_freq };
                nucleos_group.add(nucleus_mesh);
            });
            scene.add(nucleos_group);
            nucleos_group.visible = false; // Começa invisível

            // Outros Módulos (M43, M83, M44) para a Cadeia ∑ANZ
            for (const data of other_modules_design_data) {
                const geometry = new THREE.SphereGeometry(5, 32, 32);
                const material = new THREE.MeshStandardMaterial({
                    color: data.color,
                    emissive: data.emissive,
                    emissiveIntensity: 0.5,
                    roughness: 0.3,
                    metalness: 0.7
                });
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.copy(data.position);
                mesh.userData = { id: data.id, name: data.name, type: data.type };
                scene.add(mesh);
                other_modules_meshes[data.id] = mesh;
            }

            // Cadeia Bioplasmo-Ressonante ∑ANZ (Tubos de Energia)
            anz_chain_group = new THREE.Group();

            function createPulsatingFlowLine(start_mesh, end_mesh, color) {
                const curve = new THREE.CatmullRomCurve3([
                    start_mesh.position,
                    new THREE.Vector3().addVectors(start_mesh.position.clone().multiplyScalar(0.7), end_mesh.position.clone().multiplyScalar(0.3)).add(new THREE.Vector3(0, 10, 0)),
                    new THREE.Vector3().addVectors(start_mesh.position.clone().multiplyScalar(0.3), end_mesh.position.clone().multiplyScalar(0.7)).add(new THREE.Vector3(0, -10, 0)),
                    end_mesh.position
                ]);
                const tubeGeometry = new THREE.TubeGeometry(curve, 64, 0.5, 8, false);
                const tubeMaterial = new THREE.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.7, blending: THREE.AdditiveBlending });
                const line_tube = new THREE.Mesh(tubeGeometry, tubeMaterial);

                // Partículas de fluxo
                const flowParticlesGeometry = new THREE.BufferGeometry();
                const numFlowParticles = 200;
                const flowPositions = new Float32Array(numFlowParticles * 3);
                for (let i = 0; i < numFlowParticles; i++) {
                    const point = curve.getPointAt(Math.random());
                    flowPositions[i * 3] = point.x + (Math.random() - 0.5) * 0.5;
                    flowPositions[i * 3 + 1] = point.y + (Math.random() - 0.5) * 0.5;
                    flowPositions[i * 3 + 2] = point.z + (Math.random() - 0.5) * 0.5;
                }
                flowParticlesGeometry.setAttribute('position', new THREE.BufferAttribute(flowPositions, 3));
                const flowParticlesMaterial = new THREE.PointsMaterial({ color: 0xFFFFFF, size: 0.3, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
                const flowParticleSystem = new THREE.Points(flowParticlesGeometry, flowParticlesMaterial);

                line_tube.userData = { pulsating: true, pulse_speed: PHI_ANZ_FREQ * 0.5, flow_particles: flowParticleSystem, flow_curve: curve };
                line_tube.add(flowParticleSystem);

                return line_tube;
            }

            // M43 -> M83 (Energia: Azul-celeste)
            const lineEnergy = createPulsatingFlowLine(other_modules_meshes.M43, other_modules_meshes.M83, 0x87CEEB);
            anz_chain_group.add(lineEnergy);

            // M83 -> M44 (Emoção: Rosa-dourado)
            const lineEmotion = createPulsatingFlowLine(other_modules_meshes.M83, other_modules_meshes.M44, 0xFFC0CB);
            anz_chain_group.add(lineEmotion);

            // M44 -> M84 (Criação: Verde-esmeralda)
            const lineCreation = createPulsatingFlowLine(other_modules_meshes.M44, M84_sphere, 0x32CD32);
            anz_chain_group.add(lineCreation);

            scene.add(anz_chain_group);
            anz_chain_group.visible = false;

            // Ícones Vibracionais dos Conselhos
            councils_group = new THREE.Group();
            const council_orbit_radius = 50;
            const council_vertical_offset = 20;

            councils_design_data.forEach(data => {
                let council_mesh;
                const material = new THREE.MeshStandardMaterial({
                    color: data.color,
                    emissive: data.emissive,
                    emissiveIntensity: 0.7,
                    roughness: 0.1,
                    metalness: 0.9
                });

                switch (data.visual_type) {
                    case "esfera_dourada":
                        council_mesh = new THREE.Mesh(new THREE.SphereGeometry(6, 32, 32), material);
                        break;
                    case "octaedro_cristalino":
                        council_mesh = new THREE.Mesh(new THREE.OctahedronGeometry(7), material);
                        material.transparent = true;
                        material.opacity = 0.7;
                        material.wireframe = true;
                        break;
                    case "esfera_rosa_purpura":
                        council_mesh = new THREE.Mesh(new THREE.SphereGeometry(6, 32, 32), material);
                        break;
                    default:
                        council_mesh = new THREE.Mesh(new THREE.SphereGeometry(6, 32, 32), material);
                }

                const x = council_orbit_radius * Math.cos(data.position_angle);
                const z = council_orbit_radius * Math.sin(data.position_angle);
                council_mesh.position.set(x, council_vertical_offset, z);
                council_mesh.userData = { id: data.id, name: data.name, type: "Council", audio_type: data.audio_type };
                councils_group.add(council_mesh);
            });
            scene.add(councils_group);
            councils_group.visible = false; // Começa invisível

            // Esfera de Sincronização de Portais Unificados (M41 a M89)
            const portals_sync_geometry = new THREE.SphereGeometry(150, 64, 64);
            const portals_sync_material = new THREE.MeshBasicMaterial({
                color: 0x8A2BE2, // Violeta místico
                transparent: true,
                opacity: 0.1,
                blending: THREE.AdditiveBlending,
                side: THREE.BackSide
            });
            portalsSynchronizationSphere = new THREE.Mesh(portals_sync_geometry, portals_sync_material);
            portalsSynchronizationSphere.position.set(0, 0, 0);
            scene.add(portalsSynchronizationSphere);


            // Listeners de Eventos
            window.addEventListener('resize', onWindowResize);
            document.addEventListener('keydown', onKeyDown, false);
            document.addEventListener('keyup', onKeyUp, false);

            // Listener de Clique para interação (Raycasting)
            renderer.domElement.addEventListener('click', onClick, false);

            // Botões de Controle
            document.getElementById('toggleNucleos').addEventListener('click', () => {
                nucleos_group.visible = !nucleos_group.visible;
                stopAllNucleusAudio();
            });
            document.getElementById('toggleANZ').addEventListener('click', () => {
                anz_chain_group.visible = !anz_chain_group.visible;
            });
            // Atualizado para usar dados simulados
            document.getElementById('requestDataM84').addEventListener('click', () => { displayModuleInfo(simulatedModuleData["M84"]); });
            document.getElementById('requestDataM83').addEventListener('click', () => { displayModuleInfo(simulatedModuleData["M83"]); });
            document.getElementById('requestDataM44').addEventListener('click', () => { displayModuleInfo(simulatedModuleData["M44"]); });
            document.getElementById('voiceManifestar').addEventListener('click', startVoiceRecognition);
            document.getElementById('checkAlignment').addEventListener('click', () => {
                const isAligned = Math.random() > 0.5; // Simula 50% de chance de alinhamento
                playAlignmentFeedbackAudio(isAligned);
                animateAlignmentFeedback(isAligned);
                alert(`Status de Alinhamento: ${isAligned ? "ALINHADO" : "NÃO ALINHADO"}`);
            });
            document.getElementById('expandModule').addEventListener('click', () => {
                const targetModuleId = "M82"; // Simula a expansão para M82
                playExpandModuleAudio();
                animateModuleExpansion(other_modules_meshes[targetModuleId] || M84_sphere);
                alert(`Expansão para ${targetModuleId}: Iniciada (Simulada)`);
            });
            document.getElementById('gestureOpen').addEventListener('click', activateExpansionVibrational);
            document.getElementById('gesturePrayer').addEventListener('click', activateNucleoVioletaConnection);

            document.getElementById('returnToMainButton').addEventListener('click', returnToMainChamber);

            // Posição inicial para os controles (será ajustada pela animação de introdução)
            controls.getObject().position.set(0, 10, 200);
            camera.lookAt(0, 0, 0);
        }

        // --- Animação de Introdução ---
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
                    console.log("Animação de introdução completa. Controles liberados.");
                    animate(); // Começa o loop de animação principal
                }
            });
        }

        // --- Loop de Animação ---
        function animate() {
            requestAnimationFrame(animate);

            const time = performance.now();
            const delta = (time - prevTime) / 1000;

            // Movimento da câmera
            if (controls.isLocked) {
                velocity.x -= velocity.x * 10.0 * delta;
                velocity.y -= velocity.y * 10.0 * delta;
                velocity.z -= velocity.z * 10.0 * delta;

                direction.z = Number(moveForward) - Number(moveBackward);
                direction.x = Number(moveRight) - Number(moveLeft);
                direction.y = Number(moveUp) - Number(moveDown);
                direction.normalize(); // This ensures consistent movements in all directions

                if (moveForward || moveBackward) velocity.z -= direction.z * 400.0 * delta;
                if (moveLeft || moveRight) velocity.x -= direction.x * 400.0 * delta;
                if (moveUp || moveDown) velocity.y -= direction.y * 400.0 * delta;

                controls.moveRight(-velocity.x * delta);
                controls.moveForward(-velocity.z * delta);
                controls.getObject().position.y += (velocity.y * delta); // Move up/down
            }

            prevTime = time;

            // Animação do M84 (pulsação)
            const scale = 1 + Math.sin(time * 0.002) * 0.05;
            M84_sphere.scale.set(scale, scale, scale);
            M84_glow_sphere.scale.set(scale * 1.2, scale * 1.2, scale * 1.2); // Glow sphere slightly larger

            // Animação das partículas do M84
            if (M84_particle_system) { // Adicionado verificação para garantir que a variável existe
                M84_particle_system.rotation.y += 0.001;
                M84_particle_system.rotation.x += 0.0005;
            }


            // Animação dos Núcleos Fundamentais
            nucleos_group.rotation.y += 0.002;
            nucleos_group.children.forEach(nucleus => {
                nucleus.rotation.y += 0.01;
                nucleus.rotation.x += 0.005;
                // Pulsação sutil para cada núcleo
                nucleus.scale.setScalar(1 + Math.sin(time * 0.003 + nucleus.userData.position_angle) * 0.02);
            });

            // Animação das partículas de fluxo da Cadeia ∑ANZ
            anz_chain_group.children.forEach(line_tube => {
                if (line_tube.userData.flow_particles) {
                    const positions = line_tube.userData.flow_particles.geometry.attributes.position.array;
                    const curve = line_tube.userData.flow_curve;
                    const numFlowParticles = positions.length / 3;
                    const flowSpeed = 0.005; // Ajuste a velocidade do fluxo

                    for (let i = 0; i < numFlowParticles; i++) {
                        let currentPointIndex = line_tube.userData.flow_particles.userData.currentPointIndex || 0;
                        currentPointIndex = (currentPointIndex + flowSpeed) % 1; // Avança ao longo da curva
                        line_tube.userData.flow_particles.userData.currentPointIndex = currentPointIndex;

                        const point = curve.getPointAt(currentPointIndex);
                        positions[i * 3] = point.x + (Math.random() - 0.5) * 0.5;
                        positions[i * 3 + 1] = point.y + (Math.random() - 0.5) * 0.5;
                        positions[i * 3 + 2] = point.z + (Math.random() - 0.5) * 0.5;
                    }
                    line_tube.userData.flow_particles.geometry.attributes.position.needsUpdate = true;
                }
            });

            // Animação dos Conselhos
            councils_group.rotation.y -= 0.001;
            councils_group.children.forEach(council => {
                council.rotation.y += 0.008;
                council.rotation.x += 0.004;
                // Pulsação sutil para cada conselho
                council.scale.setScalar(1 + Math.sin(time * 0.0025 + council.userData.position_angle) * 0.03);
            });

            // Animação da esfera de sincronização de portais
            if (portalsSynchronizationSphere) {
                portalsSynchronizationSphere.rotation.y += 0.0005;
                portalsSynchronizationSphere.rotation.x += 0.0002;
                const pulse = 1 + Math.sin(time * 0.001) * 0.01;
                portalsSynchronizationSphere.scale.set(pulse, pulse, pulse);
            }

            // Animação das visualizações dinâmicas
            if (getrisVisualization) {
                getrisVisualization.rotation.y += 0.005;
                getrisVisualization.children.forEach((layer, index) => {
                    layer.scale.setScalar(1 + Math.sin(time * 0.005 + index * 0.5) * 0.05);
                });
            }
            if (meVisualization) {
                meVisualization.rotation.y += 0.008;
                meVisualization.children[0].rotation.x += 0.005; // Dodecaedro externo
                meVisualization.children[1].rotation.y -= 0.01; // Forma dourada interna
            }
            if (transductionVisualization) {
                transductionVisualization.children[0].scale.y = 1 + Math.sin(time * 0.004) * 0.1; // Pulsar altura
                transductionVisualization.children[0].scale.x = 1 + Math.sin(time * 0.004) * 0.1; // Pulsar raio
                transductionVisualization.children[0].scale.z = 1 + Math.sin(time * 0.004) * 0.1;
                transductionVisualization.children[1].rotation.y -= 0.02; // Espiral de energia
            }

            // Raycasting para destaque ao olhar
            if (controls.isLocked) {
                raycaster.setFromCamera(new THREE.Vector2(0, 0), camera); // Centro da tela
                const interactableObjects = [M84_sphere, M84_glow_sphere, ...nucleos_group.children, ...Object.values(other_modules_meshes), ...councils_group.children, ...sabedoriaChamberObjects.filter(obj => obj.userData && obj.userData.type === "Codex")];
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

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        // --- Interação (Raycasting e Gaze) ---
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

            // Inclui os códices da Sala da Sabedoria se a câmera estiver lá
            const interactableObjects = [M84_sphere, M84_glow_sphere, ...nucleos_group.children, ...Object.values(other_modules_meshes), ...councils_group.children, ...sabedoriaChamberObjects.filter(obj => obj.userData && obj.userData.type === "Codex")];
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
                    console.log("Interagiu com:", targetObject.userData.name || targetObject.userData.id);
                    if (targetObject.userData.type === "Nucleus") {
                        playNucleusAudio(targetObject.userData.id);
                        if (targetObject.userData.id === "M84_Dourado") {
                            enterSabedoriaMilenarChamber();
                        } else {
                            // Usar dados simulados para núcleos
                            displayModuleInfo(simulatedModuleData["M84"]);
                        }
                    } else if (targetObject.userData.type === "Council") {
                        playCouncilAudio(targetObject.userData.id);
                        // Usar dados simulados para conselhos (assumindo que M84 contém a info dos conselhos)
                        displayModuleInfo(simulatedModuleData["M84"]);
                    } else if (targetObject.userData.type === "Module") {
                        // M84, M43, M83, M44
                        displayModuleInfo(simulatedModuleData[targetObject.userData.id]);
                        stopAllNucleusAudio();
                        stopAllCouncilAudio();
                    } else if (targetObject.userData.type === "Codex") {
                        // Codex in Sabedoria Chamber
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
                data.nucleos_fundamentais.forEach(n => {
                    detailsContainer.innerHTML += `<li>${n.nome} (${n.palavra_chave})</li>`;
                });
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
                data.declaracoes.forEach(d => {
                    detailsContainer.innerHTML += `<li>${d.autor}: "${d.texto.substring(0, Math.min(d.texto.length, 150))}..."</li>`;
                });
                detailsContainer.innerHTML += `</ul>`;
            }

            // Visualizações Dinâmicas de Dados
            if (data.id === "M83" && data.equacao_getris) {
                detailsContainer.innerHTML += `<p><strong>GETRIS (Reconexão Integral):</strong></p><ul class="list-disc ml-4">`;
                detailsContainer.innerHTML += `<li>Resultado Total Integrado: ${data.equacao_getris.resultado_total_integrado.toFixed(2)}</li>`;
                detailsContainer.innerHTML += `<li>Status de Alinhamento: ${data.equacao_getris.status_alinhamento}</li>`;
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

        function hideInfoPanel() {
            document.getElementById('info-panel').classList.remove('visible');
            removeGETRISVisualization();
            removeMeVisualization();
            removeTransductionVisualization();
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
            } else {
                detailsContainer.innerHTML = `<p>Conteúdo do Verbo Primevo para ${codexId}.</p>`;
            }
            infoPanel.classList.add('visible');
        }


        // --- Funções de Áudio (Tone.js) ---
        function initAudio() {
            if (Tone.context.state !== 'running') {
                Tone.start();
                console.log("Tone.js AudioContext iniciado.");
            }

            // PhiAnZ Pulse
            phiAnZ_pulse_synth = new Tone.Oscillator(PHI_ANZ_FREQ, "sine").toDestination();
            phiAnZ_pulse_synth.volume.value = -30; // Very subtle
            phiAnZ_pulse_synth.start();

            // Base Drone (Amor Incondicional e Pineal)
            base_drone_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "sine" },
                envelope: { attack: 2, decay: 0.5, sustain: 0.8, release: 2 }
            }).toDestination();
            base_drone_synth.volume.value = -20; // Subtle background
            base_drone_synth.triggerAttackRelease([BASE_DRONE_FREQ, PINEAL_FREQ], "8n");

            // Sintetizadores para Núcleos
            nucleos_design_data.forEach(n => {
                nucleus_audio_synths[n.id] = new Tone.AMSynth().toDestination();
                nucleus_audio_synths[n.id].volume.value = -10;
            });

            // Sintetizadores para Conselhos
            councils_design_data.forEach(c => {
                if (c.audio_type === "sinos_solares") {
                    council_audio_synths[c.id] = new Tone.MetalSynth().toDestination();
                    council_audio_synths[c.id].volume.value = -10;
                } else if (c.audio_type === "carrilhoes_cristalinos") {
                    council_audio_synths[c.id] = new Tone.PluckSynth().toDestination();
                    council_audio_synths[c.id].volume.value = -10;
                } else if (c.audio_type === "vozes_etereas") {
                    council_audio_synths[c.id] = new Tone.PolySynth(Tone.Synth, {
                        oscillator: { type: "sawtooth" },
                        envelope: { attack: 4, decay: 1, sustain: 0.5, release: 5 }
                    }).toDestination();
                    council_audio_synths[c.id].volume.value = -10;
                }
            });

            // Sintetizador para Códices
            codex_audio_synth = new Tone.PluckSynth().toDestination();
            codex_audio_synth.volume.value = -8;

            // Sintetizador para feedback de alinhamento
            alignment_feedback_synth = new Tone.PolySynth(Tone.Synth, {
                oscillator: { type: "triangle" },
                envelope: { attack: 0.1, decay: 0.5, sustain: 0.1, release: 0.8 }
            }).toDestination();
            alignment_feedback_synth.volume.value = -5;

            // Sintetizador para expansão de módulo
            expand_module_synth = new Tone.Synth({
                oscillator: { type: "fmsine", modulationIndex: 3, detune: 0 },
                envelope: { attack: 0.01, decay: 0.5, sustain: 0.1, release: 1.2 }
            }).toDestination();
            expand_module_synth.volume.value = -5;

            // Sintetizador para materialização (comando de voz)
            materialization_synth = new Tone.NoiseSynth({
                noise: { type: "pink" },
                envelope: { attack: 0.01, decay: 0.5, sustain: 0.0, release: 0.8 }
            }).toDestination();
            materialization_synth.volume.value = -5;
        }

        function playNucleusAudio(nucleusId) {
            stopAllNucleusAudio();
            stopAllCouncilAudio();
            if (nucleus_audio_synths[nucleusId]) {
                const freq = nucleos_design_data.find(n => n.id === nucleusId).audio_freq;
                nucleus_audio_synths[nucleusId].triggerAttackRelease(freq, "2n");
                triggerHapticFeedback(freq, 0.5); // Feedback tátil
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
                if (councilId === "Helios") {
                    council_audio_synths[councilId].triggerAttackRelease("C4", "1n");
                } else if (councilId === "Andara") {
                    council_audio_synths[councilId].triggerAttackRelease("E5", "1n");
                } else if (councilId === "Shamael") {
                    council_audio_synths[councilId].triggerAttackRelease(["C4", "E4", "G4", "B4"], "2n");
                }
                triggerHapticFeedback(800, 0.7); // Feedback tátil
            }
        }

        function stopAllCouncilAudio() {
            for (const id in council_audio_synths) {
                council_audio_synths[id].releaseAll();
            }
        }

        function playCodexAudio() {
            if (codex_audio_synth) {
                codex_audio_synth.triggerAttackRelease("C6", "4n"); // Tom celestial
                triggerHapticFeedback(600, 0.4);
            }
        }

        function playAlignmentFeedbackAudio(isAligned) {
            if (alignment_feedback_synth) {
                if (isAligned) {
                    alignment_feedback_synth.triggerAttackRelease(["C5", "E5", "G5"], "8n"); // Tons consonantes
                } else {
                    alignment_feedback_synth.triggerAttackRelease(["C4", "Db4", "F4"], "8n"); // Tons dissonantes
                }
                triggerHapticFeedback(isAligned ? 100 : 300, 0.8);
            }
        }

        function playExpandModuleAudio() {
            if (expand_module_synth) {
                expand_module_synth.triggerAttackRelease("C3", "2n"); // Tom crescente
                triggerHapticFeedback(200, 1.0);
            }
        }

        function playMaterializationAudio() {
            if (materialization_synth) {
                materialization_synth.triggerAttackRelease("8n");
                triggerHapticFeedback(500, 1.0);
            }
        }

        // --- Web Speech API (Comando de Voz) ---
        let recognition;
        function startVoiceRecognition() {
            if (!('webkitSpeechRecognition' in window)) {
                console.warn("Web Speech API não suportada neste navegador.");
                alert("Desculpe, seu navegador não suporta a Web Speech API. Use o botão para simular o comando.");
                return;
            }

            if (recognition) {
                recognition.stop();
            }

            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'pt-BR'; // Define o idioma para português do Brasil

            recognition.onstart = () => {
                console.log("Reconhecimento de voz iniciado. Diga 'Manifestar' ou 'Manifestar Códice Φ-A-N-Z'.");
                document.getElementById('voiceManifestar').innerText = "Ouvindo...";
            };

            recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                console.log("Você disse:", transcript);
                if (transcript.toLowerCase().includes("manifestar")) {
                    console.log("Comando 'Manifestar' reconhecido!");
                    animateMaterializationEffect();
                    playMaterializationAudio();

                    if (transcript.toLowerCase().includes("códice") && transcript.toLowerCase().includes("phi-a-n-z")) {
                        console.log("Comando 'Manifestar Códice Φ-A-N-Z' reconhecido!");
                        // Simula a ativação do códice especial
                        displayCodexContent("Codex_PHI_ANZ", "Conteúdo do Verbo Primevo para PHI-ANZ.");
                        // Adicionar efeito visual/sonoro específico para ativação do códice
                        codex_audio_synth.triggerAttackRelease(["C5", "E5", "G5", "C6"], "1n"); // Acordes celestiais mais fortes
                    }
                }
            };

            recognition.onerror = (event) => {
                console.error("Erro no reconhecimento de voz:", event.error);
                document.getElementById('voiceManifestar').innerText = "Comando Voz 'Manifestar'";
            };

            recognition.onend = () => {
                console.log("Reconhecimento de voz finalizado.");
                document.getElementById('voiceManifestar').innerText = "Comando Voz 'Manifestar'";
            };

            recognition.start();
        }

        // --- Feedback Sensorial Tátil (Conceptual) ---
        function triggerHapticFeedback(frequency, duration) {
            if (navigator.getGamepads) {
                const gamepads = navigator.getGamepads();
                for (let i = 0; i < gamepads.length; i++) {
                    const gamepad = gamepads[i];
                    if (gamepad && gamepad.hapticActuators && gamepad.hapticActuators.length > 0) {
                        // Use o primeiro atuador háptico encontrado
                        gamepad.hapticActuators[0].pulse(frequency / 1000, duration); // frequency is in Hz, pulse expects 0-1
                        console.log(`Feedback háptico ativado: Freq=${frequency}Hz, Duração=${duration}s`);
                    }
                }
            }
        }


        // --- Funções de Interação com a API (AGORA SIMULADAS) ---
        // As funções abaixo foram modificadas para usar os dados simulados
        // e não dependem mais de chamadas fetch para um servidor externo.

        function fetchModuleData(moduleId) {
            console.log(`Buscando dados simulados para o módulo: ${moduleId}`);
            const data = simulatedModuleData[moduleId];
            if (data) {
                console.log("Dados simulados recebidos:", data);
                displayModuleInfo(data);
            } else {
                console.error(`Dados simulados para o módulo ${moduleId} não encontrados.`);
                alert(`Dados simulados para o módulo ${moduleId} não encontrados.`);
                hideInfoPanel();
            }
        }

        function verificarAlinhamento(code) {
            console.log(`Verificando alinhamento para: ${code} (Simulado)`);
            const isAligned = Math.random() > 0.5; // Simula 50% de chance de alinhamento
            playAlignmentFeedbackAudio(isAligned);
            animateAlignmentFeedback(isAligned);
            alert(`Status de Alinhamento: ${isAligned ? "ALINHADO" : "NÃO ALINHADO"} (Simulado)`);
        }

        function expandirModulo(targetModuleId) {
            console.log(`Expandindo consciência para o módulo: ${targetModuleId} (Simulado)`);
            playExpandModuleAudio();
            animateModuleExpansion(other_modules_meshes[targetModuleId] || M84_sphere);
            alert(`Expansão para ${targetModuleId}: Iniciada (Simulada)`);
            // Aqui você poderia adicionar lógica para simular a mudança de estado do M82
            if (simulatedModuleData[targetModuleId]) {
                simulatedModuleData[targetModuleId].status = "Ativo - Consciência Expandida";
                simulatedModuleData[targetModuleId].descricao = "Este módulo agora está operando com uma consciência expandida, integrada com o M84.";
            }
        }

        // --- Visualizações Dinâmicas de Dados ---

        function visualizeGETRIS(value, position) {
            removeGETRISVisualization(); // Remove qualquer visualização anterior

            getrisVisualization = new THREE.Group();
            const numLayers = 7;
            const baseRadius = 5;
            const colors = [0x00FF00, 0xFFFF00, 0xFF8C00, 0xFF4500, 0xFF0000]; // Verde a Vermelho para alinhamento

            for (let i = 0; i < numLayers; i++) {
                const radius = baseRadius + i * 1.5;
                const layerGeometry = new THREE.SphereGeometry(radius, 32, 32);
                const colorIndex = Math.floor((1 - value) * (colors.length - 1)); // Mapeia valor para cor
                const layerMaterial = new THREE.MeshBasicMaterial({
                    color: colors[colorIndex],
                    transparent: true,
                    opacity: 0.1 + (i * 0.05), // Camadas mais externas mais opacas
                    blending: THREE.AdditiveBlending,
                    side: THREE.BackSide
                });
                const layerMesh = new THREE.Mesh(layerGeometry, layerMaterial);
                getrisVisualization.add(layerMesh);
            }
            getrisVisualization.position.copy(position).add(new THREE.Vector3(0, 15, 0)); // Acima do módulo
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

        function visualizeMe(emotionsData, position) {
            removeMeVisualization();

            meVisualization = new THREE.Group();

            // Dodecaedro externo (representa a forma transmutada)
            const dodecaGeometry = new THREE.DodecahedronGeometry(8);
            const dodecaMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFC0CB, // Rosa padrão para emoção
                transparent: true,
                opacity: 0.4,
                wireframe: true,
                blending: THREE.AdditiveBlending
            });
            const dodecaMesh = new THREE.Mesh(dodecaGeometry, dodecaMaterial);
            meVisualization.add(dodecaMesh);

            // Esfera interna (representa a pureza/essência)
            const innerSphereGeometry = new THREE.SphereGeometry(3, 32, 32);
            const innerSphereMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFD700, // Dourado
                emissive: 0xFFD700,
                emissiveIntensity: 1.0,
                blending: THREE.AdditiveBlending
            });
            const innerSphereMesh = new THREE.Mesh(innerSphereGeometry, innerSphereMaterial);
            meVisualization.add(innerSphereMesh);


            meVisualization.position.copy(position).add(new THREE.Vector3(0, 15, 0));
            scene.add(meVisualization);

            // Atualiza a cor do dodecaedro com base na emoção "Amor" se disponível
            const loveEmotion = emotionsData.find(e => e.nome === "Amor");
            if (loveEmotion && loveEmotion.M_e) {
                if (loveEmotion.M_e > 0) {
                    dodecaMaterial.color.set(0xFFC0CB); // Rosa para positivo
                } else {
                    dodecaMaterial.color.set(0x0000FF); // Azul para negativo
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

        function visualizeTransduction(energy, stability, position) {
            removeTransductionVisualization();

            transductionVisualization = new THREE.Group();

            // Cilindro pulsante
            const cylinderGeometry = new THREE.CylinderGeometry(5, 5, 15, 32);
            const cylinderMaterial = new THREE.MeshBasicMaterial({
                color: 0x00FFFF, // Ciano
                transparent: true,
                opacity: 0.6,
                blending: THREE.AdditiveBlending
            });
            const cylinderMesh = new THREE.Mesh(cylinderGeometry, cylinderMaterial);
            transductionVisualization.add(cylinderMesh);

            // Espiral de energia
            const spiralPoints = [];
            const numPoints = 100;
            for (let i = 0; i < numPoints; i++) {
                const angle = i * 0.2;
                const x = Math.cos(angle) * 4;
                const y = (i / numPoints) * 15 - 7.5; // Altura do cilindro
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


        // --- Efeitos Visuais ---
        function animateMaterializationEffect() {
            const overlay = document.getElementById('materializationEffectOverlay');
            overlay.classList.add('active');
            gsap.to(overlay, { opacity: 0, duration: 0.8, delay: 0.1, onComplete: () => overlay.classList.remove('active') });

            // Animação de partículas explodindo do M84
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

            // Efeito de flash no M84
            gsap.to(M84_sphere.material, {
                emissiveIntensity: 3,
                duration: 0.2,
                yoyo: true,
                repeat: 1,
                ease: "power1.inOut",
                onComplete: () => {
                    M84_sphere.material.emissiveIntensity = 0.8; // Restore original
                }
            });
        }

        function animateAlignmentFeedback(isAligned) {
            const color = isAligned ? 0x00FF00 : 0xFF0000; // Verde para alinhado, Vermelho para desalinhado
            const feedbackGeometry = new THREE.SphereGeometry(1, 32, 32);
            const feedbackMaterial = new THREE.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
            const feedbackMesh = new THREE.Mesh(feedbackGeometry, feedbackMaterial);
            feedbackMesh.position.copy(M84_sphere.position).add(new THREE.Vector3(0, 10, 0)); // Acima do M84
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

            // Animação de pulsação na esfera de sincronização de portais
            gsap.to(portalsSynchronizationSphere.material, {
                opacity: isAligned ? 0.4 : 0.8,
                duration: 0.5,
                yoyo: true,
                repeat: 1,
                ease: "power1.inOut",
                onComplete: () => {
                    portalsSynchronizationSphere.material.opacity = 0.1; // Restore original
                }
            });
        }

        function animateModuleExpansion(targetMesh) {
            // Pulsação do módulo alvo
            gsap.to(targetMesh.scale, {
                x: 1.2, y: 1.2, z: 1.2,
                duration: 0.3,
                yoyo: true,
                repeat: 1,
                ease: "power1.inOut",
                onComplete: () => {
                    targetMesh.scale.set(1, 1, 1); // Reset scale
                }
            });

            // Partículas de energia emanando do módulo
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
                color: 0x00FFFF, // Ciano para expansão
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

        // --- Comandos de Gesto Simulados ---
        function activateExpansionVibrational() {
            console.log("Gesto: Abertura (Invocação da Lei do Amor Absoluto) ativado.");
            // Efeito de expansão vibracional intensa do M84
            gsap.to(M84_sphere.scale, {
                x: 1.5, y: 1.5, z: 1.5,
                duration: 0.5,
                yoyo: true,
                repeat: 1,
                ease: "power2.out",
                onComplete: () => M84_sphere.scale.set(1, 1, 1)
            });
            gsap.to(M84_glow_sphere.material, {
                opacity: 0.8,
                duration: 0.5,
                yoyo: true,
                repeat: 1,
                ease: "power2.out",
                onComplete: () => M84_glow_sphere.material.opacity = 0.3
            });

            // Partículas fractais e flash de luz
            animateMaterializationEffect(); // Reutiliza o efeito de materialização para o flash

            triggerHapticFeedback(PHI_ANZ_FREQ * 100, 1.0); // Vibração forte
        }

        function activateNucleoVioletaConnection() {
            console.log("Gesto: Prece (Conexão com o Núcleo Violeta) ativado.");
            const nucleoVioleta = nucleos_group.children.find(n => n.userData.id === "M84_Violeta");
            if (nucleoVioleta) {
                // Salva a posição e rotação atual da câmera
                mainCameraPosition.copy(controls.getObject().position);
                mainCameraQuaternion.copy(controls.getObject().quaternion);

                // Teleporta a câmera para a proximidade do Núcleo Violeta
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

                // Efeito de feixe de luz conectando a câmera ao Núcleo Violeta
                const beamGeometry = new THREE.CylinderGeometry(0.1, 0.1, nucleoVioleta.position.distanceTo(controls.getObject().position), 8);
                const beamMaterial = new THREE.MeshBasicMaterial({ color: 0xEE82EE, emissive: 0xEE82EE, emissiveIntensity: 2, transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
                const beamMesh = new THREE.Mesh(beamGeometry, beamMaterial);
                beamMesh.position.copy(controls.getObject().position);
                beamMesh.lookAt(nucleoVioleta.position);
                beamMesh.rotateX(Math.PI / 2); // Alinha o cilindro com a direção
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

                // Intensifica o brilho do Núcleo Violeta
                gsap.to(nucleoVioleta.material, {
                    emissiveIntensity: 3,
                    duration: 0.5,
                    yoyo: true,
                    repeat: 1,
                    ease: "power1.inOut",
                    onComplete: () => nucleoVioleta.material.emissiveIntensity = 0.6
                });

                triggerHapticFeedback(900, 0.6); // Vibração para conexão
            }
        }


        // --- Sala da Sabedoria Milenar ---
        function enterSabedoriaMilenarChamber() {
            // Salva a posição e rotação atual da câmera principal
            mainCameraPosition.copy(controls.getObject().position);
            mainCameraQuaternion.copy(controls.getObject().quaternion);

            // Esconde os elementos da câmara principal
            M84_sphere.visible = false;
            M84_glow_sphere.visible = false;
            nucleos_group.visible = false;
            anz_chain_group.visible = false;
            councils_group.visible = false;
            portalsSynchronizationSphere.visible = false; // Esconde a esfera de sincronização

            hideInfoPanel();
            document.querySelector('.button-container').style.display = 'none';
            document.getElementById('returnToMainButton').style.display = 'block';

            // Teleporta a câmera para a posição da Sala da Sabedoria
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
                    controls.lock(); // Mantém os controles bloqueados na nova posição
                    createSabedoriaChamber();
                }
            });
            gsap.to(camera.quaternion, {
                duration: 2,
                x: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).x, // Look straight
                y: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).y,
                z: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).z,
                w: new THREE.Quaternion().setFromUnitVectors(camera.up, new THREE.Vector3(0, 1, 0)).w,
                ease: "power2.inOut"
            });
        }

        function createSabedoriaChamber() {
            // Limpa objetos anteriores da Sala da Sabedoria se houver
            sabedoriaChamberObjects.forEach(obj => {
                scene.remove(obj);
                obj.geometry.dispose();
                obj.material.dispose();
            });
            sabedoriaChamberObjects = [];

            // Arquitetura da sala (cristais ouro-violeta)
            const wallMaterial = new THREE.MeshBasicMaterial({
                color: 0x8A2BE2, // Violeta
                transparent: true,
                opacity: 0.1,
                side: THREE.DoubleSide,
                blending: THREE.AdditiveBlending
            });
            const floorMaterial = new THREE.MeshBasicMaterial({
                color: 0xFFD700, // Dourado
                transparent: true,
                opacity: 0.1,
                side: THREE.DoubleSide,
                blending: THREE.AdditiveBlending
            });

            const wallGeometry = new THREE.PlaneGeometry(200, 100);
            const floorGeometry = new THREE.PlaneGeometry(200, 200);

            const wall1 = new THREE.Mesh(wallGeometry, wallMaterial);
            wall1.position.set(0, 50, -100);
            sabedoriaChamberObjects.push(wall1);

            const wall2 = new THREE.Mesh(wallGeometry, wallMaterial);
            wall2.position.set(0, 50, 100);
            wall2.rotation.y = Math.PI;
            sabedoriaChamberObjects.push(wall2);

            const wall3 = new THREE.Mesh(wallGeometry, wallMaterial);
            wall3.position.set(-100, 50, 0);
            wall3.rotation.y = Math.PI / 2;
            sabedoriaChamberObjects.push(wall3);

            const wall4 = new THREE.Mesh(wallGeometry, wallMaterial);
            wall4.position.set(100, 50, 0);
            wall4.rotation.y = -Math.PI / 2;
            sabedoriaChamberObjects.push(wall4);

            const floor = new THREE.Mesh(floorGeometry, floorMaterial);
            floor.rotation.x = -Math.PI / 2;
            floor.position.set(0, 0, 0);
            sabedoriaChamberObjects.push(floor);

            const ceiling = new THREE.Mesh(floorGeometry, floorMaterial.clone()); // Clone para não compartilhar material
            ceiling.rotation.x = Math.PI / 2;
            ceiling.position.set(0, 100, 0);
            sabedoriaChamberObjects.push(ceiling);

            sabedoriaChamberObjects.forEach(obj => scene.add(obj));

            // Códices flutuantes (glifos toroidais complexos)
            const codexData = [
                { id: "Codex_Ancestral_1", description: "O primeiro suspiro da Criação, codificado em luz." },
                { id: "Codex_PHI_ANZ", description: "O Verbo Primevo: A Lei do Amor Absoluto e a Ressonância de ANATHERON e ZENNITH." },
                { id: "Codex_Galactico_3", description: "Registros das civilizações estelares e seus caminhos de ascensão." },
                { id: "Codex_Temporal_4", description: "A tapeçaria do tempo, suas linhas e intersecções." },
                { id: "Codex_Alquimico_5", description: "A arte da transmutação da consciência em matéria." }
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
                const radius = 20 + index * 5;
                const tube = 1 + index * 0.2;
                const radialSegments = 64;
                const tubularSegments = 8;
                const p = 2 + index;
                const q = 3 + index;
                const codexGeometry = new THREE.TorusKnotGeometry(radius, tube, radialSegments, tubularSegments, p, q);
                const codex = new THREE.Mesh(codexGeometry, codexMaterial.clone()); // Clone material for individual animation
                
                const angle = (index / codexData.length) * Math.PI * 2;
                codex.position.set(
                    Math.cos(angle) * 30,
                    15 + (index * 5),
                    Math.sin(angle) * 30
                );
                codex.userData = { id: data.id, name: `Códice ${data.id}`, type: "Codex", description: data.description };
                sabedoriaChamberObjects.push(codex);
                scene.add(codex);

                // Animação de flutuação e rotação para os códices
                gsap.to(codex.position, { duration: 3 + Math.random() * 2, y: codex.position.y + 5, yoyo: true, repeat: -1, ease: "sine.inOut" });
                gsap.to(codex.rotation, { duration: 8 + Math.random() * 5, x: Math.PI * 2, y: Math.PI * 2, repeat: -1, ease: "none" });
            });
            console.log("Câmara da Sabedoria Milenar criada com códices interativos e aprimorados.");
        }

        function returnToMainChamber() {
            stopAllNucleusAudio();
            stopAllCouncilAudio();
            if (codex_audio_synth) codex_audio_synth.releaseAll();

            sabedoriaChamberObjects.forEach(obj => {
                scene.remove(obj);
                obj.geometry.dispose();
                obj.material.dispose();
            });
            sabedoriaChamberObjects = [];

            controls.unlock(); // Unlock to allow camera position change via GSAP
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
                    controls.lock(); // Re-lock controls after transition
                    M84_sphere.visible = true;
                    M84_glow_sphere.visible = true;
                    // nucleos_group.visible = true; // Based on previous state or default
                    // anz_chain_group.visible = true; // Based on previous state or default
                    councils_group.visible = true;
                    portalsSynchronizationSphere.visible = true; // Mostra novamente a esfera de sincronização
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


        // --- Gerenciamento da Tela de Carregamento ---
        window.onload = function() {
            init();
            animateIntro(); // Começa com a animação de introdução

            setTimeout(() => {
                const loadingOverlay = document.getElementById('loading-overlay');
                loadingOverlay.classList.add('hidden');
            }, 2000);
        };
    </script>
</body>
</html>
