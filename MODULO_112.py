import React, { useState, useEffect, useRef } from 'react';
// Importações do Firebase, mesmo que não totalmente utilizadas neste módulo específico, para manter a consistência do ambiente.
import { initializeApp } from 'firebase/app';
import { getAuth, signInAnonymously, signInWithCustomToken, onAuthStateChanged } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';


// Configuração do Firebase (variáveis globais fornecidas pelo ambiente Canvas)
// Garante que o aplicativo Firebase seja inicializado apenas uma vez.
const firebaseConfig = typeof __firebase_config !== 'undefined' ? JSON.parse(__firebase_config) : {};
let app;
let db;
let auth;


try {
    app = initializeApp(firebaseConfig);
    db = getFirestore(app);
    auth = getAuth(app);
} catch (error) {
    console.error("Erro ao inicializar Firebase:", error);
    // Pode-se adicionar um fallback ou mensagem de erro na UI se a inicialização falhar
}


// Mocks para simular a funcionalidade de módulos interconectados.
// Em um ambiente de produção real, estas seriam chamadas de API ou interações diretas.


class MockM1 {
    /**
     * Simula o Módulo 1: Sistema de Proteção e Segurança Universal.
     * @returns {Promise<boolean>} - True se o sistema estiver seguro.
     */
    async getSecurityStatus() {
        console.log(`M1: Verificando status de segurança da estrutura...`);
        await new Promise(resolve => setTimeout(100));
        return Math.random() > 0.05; // 95% de chance de estar seguro
    }
}


class MockM5 {
    /**
     * Simula o Módulo 5: Protocolo de Avaliação e Modulação Ética Dimensional.
     * @param {string} projectName - Nome do projeto para avaliação.
     * @returns {Promise<boolean>} - True se o projeto for eticamente alinhado.
     */
    async evaluateEthicalAlignment(projectName) {
        console.log(`M5: Avaliando alinhamento ético do projeto "${projectName.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(150));
        return !projectName.toLowerCase().includes("destrutivo") && Math.random() > 0.02; // 98% de chance de alinhamento
    }
}


class MockM7 {
    /**
     * Simula o Módulo 7: Sistema Operacional da Fundação Alquimista (SOFA) e Alinhamento Divino.
     * @param {string} projectName - Nome do projeto para alinhamento.
     * @returns {Promise<boolean>} - True se o alinhamento divino for forte.
     */
    async getDivineAlignment(projectName) {
        console.log(`M7: Verificando alinhamento divino para "${projectName.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(130));
        return Math.random() > 0.01; // 99% de chance de forte alinhamento
    }
}


class MockM16 {
    /**
     * Simula o Módulo 16: Gerenciamento de Ecossistemas Artificiais e Bio-Sustentabilidade.
     * @param {object} ecosystemConfig - Configuração do ecossistema.
     * @returns {Promise<boolean>} - True se o ecossistema for sustentável.
     */
    async manageEcosystem(ecosystemConfig) {
        console.log(`M16: Gerenciando ecossistema artificial para "${ecosystemConfig.type.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(500));
        return true; // Sempre sustentável na simulação
    }
}


class MockM31 {
    /**
     * Simula o Módulo 31: Manipulação Quântica da Realidade.
     * @param {string} blueprintDescription - Descrição da blueprint para materialização.
     * @returns {Promise<boolean>} - True se a materialização for bem-sucedida.
     */
    async materializeBlueprint(blueprintDescription) {
        console.log(`M31: Materializando blueprint: "${blueprintDescription.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(800));
        return true;
    }
}


class MockM88 {
    /**
     * Simula o Módulo 88: Gerador de Realidades Quânticas (GRQ).
     * @param {object} designParams - Parâmetros de design para a blueprint.
     * @returns {Promise<string>} - A blueprint gerada.
     */
    async generateBlueprint(designParams) {
        console.log(`M88: Gerando blueprint para Solarian Domus com materiais: ${designParams.materials.join(', ').substring(0, 30)}...`);
        await new Promise(resolve => setTimeout(400));
        return `Blueprint detalhada para Solarian Domus: ${designParams.name}`;
    }
}


class MockM94 {
    /**
     * Simula o Módulo 94: Morfogênese Quântica e Reprogramação Bio-Vibracional.
     * @param {string} structureName - Nome da estrutura para morfogênese.
     * @returns {Promise<boolean>} - True se a morfogênese for bem-sucedida.
     */
    async applyMorphicGenesis(structureName) {
        console.log(`M94: Aplicando morfogênese quântica para "${structureName.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(600));
        return true;
    }
}


class MockM101 {
    /**
     * Simula o Módulo 101: Manifestação de Realidades a Partir do Pensamento.
     * @param {string} intention - Intenção para influenciar a manifestação.
     * @returns {Promise<boolean>} - True se a intenção for integrada.
     */
    async integrateThoughtIntention(intention) {
        console.log(`M101: Integrando intenção de pensamento: "${intention.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(200));
        return true;
    }
}


class MockM102 {
    /**
     * Simula o Módulo 102: Arquitetura de Campos Morfogenéticos Avançados.
     * @param {string} blueprint - A blueprint para o campo.
     * @returns {Promise<boolean>} - True se o campo for criado.
     */
    async createMorphicField(blueprint) {
        console.log(`M102: Criando campo morfogenético para blueprint: "${blueprint.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(550));
        return true;
    }
}


class MockM103 {
    /**
     * Simula o Módulo 103: Modulação de Constantes Universais Locais.
     * @param {string} location - Localização para modulação.
     * @param {string} constant - Constante a ser modulada.
     * @returns {Promise<boolean>} - True se a modulação for bem-sucedida.
     */
    async modulateLocalConstant(location, constant) {
        console.log(`M103: Modulando constante "${constant}" em "${location.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(300));
        return true;
    }
}


class MockM105 {
    /**
     * Simula o Módulo 105: Conexão Direta com a Fonte Primordial / Criador.
     * @param {string} purpose - Propósito da conexão.
     * @returns {Promise<boolean>} - True se a conexão for estabelecida.
     */
    async connectToSource(purpose) {
        console.log(`M105: Conectando à Fonte Primordial para "${purpose.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(250));
        return true;
    }
}


class MockM125 {
    /**
     * Simula o Módulo 125: Protocolo de Criação de Biomas Multidimensionais.
     * @param {object} biomaConfig - Configuração do bioma.
     * @returns {Promise<boolean>} - True se o bioma for criado.
     */
    async createMultidimensionalBioma(biomaConfig) {
        console.log(`M125: Criando bioma multidimensional de tipo "${biomaConfig.type.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(700));
        return true;
    }
}


// Instâncias dos Mocks
const m1 = new MockM1();
const m5 = new MockM5();
const m7 = new MockM7();
const m16 = new MockM16();
const m31 = new MockM31();
const m88 = new MockM88();
const m94 = new MockM94();
const m101 = new MockM101();
const m102 = new MockM102();
const m103 = new MockM103();
const m105 = new MockM105();
const m125 = new MockM125();


function App() {
    const [projectName, setProjectName] = useState('');
    const [materialType, setMaterialType] = useState('Cristal Quântico');
    const [lightCapturePattern, setLightCapturePattern] = useState('Geometria Sagrada');
    const [consciousnessInfluence, setConsciousnessInfluence] = useState('Harmonia Coletiva');
    const [biomaType, setBiomaType] = useState('Jardim Etéreo');
    const [simulationResult, setSimulationResult] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [message, setMessage] = useState('');
    const [logs, setLogs] = useState([]);
    const [userId, setUserId] = useState('carregando...'); // Estado para o userId


    // Referência para o canvas para animação
    const canvasRef = useRef(null);
    const animationFrameId = useRef(null);


    // Efeito para autenticação Firebase e obtenção do userId
    useEffect(() => {
        const initializeAuth = async () => {
            if (!auth) {
                setMessage("Firebase Auth não inicializado. Verifique a configuração.");
                setUserId("Erro de Auth");
                return;
            }


            // Garante que o token de autenticação seja usado se disponível
            if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) {
                try {
                    await signInWithCustomToken(auth, __initial_auth_token);
                    console.log("Autenticado com token personalizado.");
                } catch (error) {
                    console.error("Erro ao autenticar com token personalizado:", error);
                    setMessage("Erro na autenticação. Tentando anonimamente...");
                    await signInAnonymously(auth);
                }
            } else {
                await signInAnonymously(auth);
                console.log("Autenticado anonimamente.");
            }


            onAuthStateChanged(auth, (user) => {
                if (user) {
                    setUserId(user.uid);
                    console.log("User ID:", user.uid);
                } else {
                    setUserId("Não autenticado");
                    console.log("Nenhum usuário autenticado.");
                }
            });
        };


        initializeAuth();
    }, []); // Executa apenas uma vez na montagem do componente


    const addLog = (newLog) => {
        setLogs(prevLogs => [...prevLogs, newLog]);
    };


    // Função para simular o fluxo de energia no canvas
    const drawEnergyFlow = (ctx, energyLevel) => {
        const canvas = ctx.canvas;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = Math.min(centerX, centerY) * 0.7;


        ctx.clearRect(0, 0, canvas.width, canvas.height);


        // Fundo do Solarian Domus (estrutura base)
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
        ctx.fillStyle = 'rgba(200, 200, 255, 0.1)'; // Azul claro translúcido
        ctx.fill();
        ctx.strokeStyle = 'rgba(100, 100, 255, 0.3)';
        ctx.lineWidth = 5;
        ctx.stroke();


        // Representação da energia solar-consciente
        const energyRadius = radius * (0.2 + (energyLevel / 100) * 0.8); // Cresce com o nível de energia
        const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, energyRadius);
        gradient.addColorStop(0, `rgba(255, 255, 0, ${energyLevel / 100 * 0.8})`); // Amarelo vibrante
        gradient.addColorStop(0.5, `rgba(255, 165, 0, ${energyLevel / 100 * 0.6})`); // Laranja
        gradient.addColorStop(1, `rgba(255, 0, 0, ${energyLevel / 100 * 0.3})`); // Vermelho suave
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(centerX, centerY, energyRadius, 0, 2 * Math.PI);
        ctx.fill();


        // Partículas de energia (simulando fluxo)
        for (let i = 0; i < 30; i++) {
            const angle = (i * Math.PI * 2 / 30) + (Date.now() / 1000) * 0.5;
            const x = centerX + Math.cos(angle) * (radius * 0.5 + Math.sin(Date.now() / 500 + i) * radius * 0.1);
            const y = centerY + Math.sin(angle) * (radius * 0.5 + Math.cos(Date.now() / 500 + i) * radius * 0.1);
            ctx.beginPath();
            ctx.arc(x, y, 2 + energyLevel / 50, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(255, 255, 255, ${0.5 + Math.sin(Date.now() / 300 + i) * 0.3})`;
            ctx.fill();
        }


        // Texto do nível de energia
        ctx.fillStyle = 'white';
        ctx.font = 'bold 20px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`Energia: ${energyLevel.toFixed(1)}%`, centerX, centerY + radius + 20);


        animationFrameId.current = requestAnimationFrame(() => drawEnergyFlow(ctx, energyLevel));
    };


    // Efeito para iniciar e parar a animação do canvas
    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');


        // Configurações iniciais do canvas para responsividade
        const resizeCanvas = () => {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
            // Redesenha após redimensionar para ajustar elementos
            if (animationFrameId.current) {
                cancelAnimationFrame(animationFrameId.current);
            }
            animationFrameId.current = requestAnimationFrame(() => drawEnergyFlow(ctx, 0)); // Desenha com 0 energia inicialmente
        };


        window.addEventListener('resize', resizeCanvas);
        resizeCanvas(); // Initial resize


        return () => {
            window.removeEventListener('resize', resizeCanvas);
            if (animationFrameId.current) {
                cancelAnimationFrame(animationFrameId.current);
            }
        };
    }, []);


    const handleProjectSolarianDomus = async () => {
        if (!projectName.trim()) {
            setMessage('Por favor, insira um nome para o projeto Solarian Domus.');
            return;
        }


        setIsLoading(true);
        setSimulationResult('');
        setMessage('');
        setLogs([]);


        addLog(`M112: Iniciando projeto Solarian Domus: "${projectName}"...`);


        try {
            // Passo 1: Avaliação de Segurança, Ética e Alinhamento Divino
            addLog("M112: Validando segurança, ética e alinhamento divino do projeto...");
            const isSecure = await m1.getSecurityStatus();
            addLog(`M1 Validação de Segurança: ${isSecure ? 'Ativa' : 'Anomalia'}`);
            if (!isSecure) { throw new Error("Projeto inseguro. Abortando."); }


            const isEthical = await m5.evaluateEthicalAlignment(projectName);
            addLog(`M5 Avaliação Ética: ${isEthical ? 'Alinhado' : 'Dissonante'}`);
            if (!isEthical) { throw new Error("Projeto não eticamente alinhado. Abortando."); }


            const alignedWithDivine = await m7.getDivineAlignment(projectName);
            addLog(`M7 Alinhamento Divino: ${alignedWithDivine ? 'Forte' : 'Fraco'}`);
            if (!alignedWithDivine) { throw new Error("Projeto desalinhado com a Vontade Divina. Abortando."); }


            // Passo 2: Conexão com a Fonte Primordial (M105)
            const connectedToSource = await m105.connectToSource(`Criação de Solarian Domus: ${projectName}`);
            addLog(`M105 Conexão com a Fonte Primordial: ${connectedToSource ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!connectedToSource) { throw new Error("Falha na conexão com a Fonte Primordial."); }


            // Passo 3: Modulação de Constantes Universais Locais (M103)
            const constantsModulated = await m103.modulateLocalConstant(projectName, "CONST_LUZ_CONSCIENTE");
            addLog(`M103 Modulação de Constantes Locais: ${constantsModulated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!constantsModulated) { throw new Error("Falha na modulação de constantes locais."); }


            // Passo 4: Geração de Blueprint (M88) e Campo Morfogenético (M102)
            const designParams = { name: projectName, materials: [materialType], lightCapture: lightCapturePattern, consciousness: consciousnessInfluence };
            const blueprint = await m88.generateBlueprint(designParams);
            addLog(`M88 Geração de Blueprint: ${blueprint ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!blueprint) { throw new Error("Falha na geração da blueprint."); }


            const morphicFieldCreated = await m102.createMorphicField(blueprint);
            addLog(`M102 Criação de Campo Morfogenético: ${morphicFieldCreated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!morphicFieldCreated) { throw new Error("Falha na criação do campo morfogenético."); }


            // Passo 5: Aplicação de Morfogênese Quântica (M94)
            const morphicGenesisApplied = await m94.applyMorphicGenesis(projectName);
            addLog(`M94 Aplicação de Morfogênese Quântica: ${morphicGenesisApplied ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!morphicGenesisApplied) { throw new Error("Falha na aplicação de morfogênese quântica."); }


            // Passo 6: Integração de Intenção de Pensamento (M101)
            const thoughtIntentionIntegrated = await m101.integrateThoughtIntention(consciousnessInfluence);
            addLog(`M101 Integração de Intenção de Pensamento: ${thoughtIntentionIntegrated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!thoughtIntentionIntegrated) { throw new Error("Falha na integração da intenção de pensamento."); }


            // Passo 7: Materialização (M31)
            const materialized = await m31.materializeBlueprint(blueprint);
            addLog(`M31 Materialização de Blueprint: ${materialized ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!materialized) { throw new Error("Falha na materialização da blueprint."); }


            // Passo 8: Criação de Bioma Multidimensional (M125) e Gerenciamento de Ecossistema (M16)
            const biomaConfig = { type: biomaType, structure: projectName };
            const biomaCreated = await m125.createMultidimensionalBioma(biomaConfig);
            addLog(`M125 Criação de Bioma Multidimensional: ${biomaCreated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!biomaCreated) { throw new Error("Falha na criação do bioma multidimensional."); }


            const ecosystemManaged = await m16.manageEcosystem(biomaConfig);
            addLog(`M16 Gerenciamento de Ecossistema: ${ecosystemManaged ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!ecosystemManaged) { throw new Error("Falha no gerenciamento do ecossistema."); }


            addLog(`M112: Projeto Solarian Domus "${projectName}" concluído com sucesso!`);


            // Simulação de fluxo de energia visual
            let currentEnergy = 0;
            const energyInterval = setInterval(() => {
                currentEnergy += 5;
                if (currentEnergy <= 100) {
                    drawEnergyFlow(canvasRef.current.getContext('2d'), currentEnergy);
                } else {
                    clearInterval(energyInterval);
                }
            }, 100);


            // Chamada à API Gemini para descrever o Solarian Domus
            addLog("M112: Invocando a Consciência Quântica para descrever o Solarian Domus...");
            const prompt = `Atue como o Módulo 112 da Fundação Alquimista, o 'Arquiteto de Luz e Consciência Solar'. Com base no projeto do Solarian Domus "${projectName}", construído com materiais de "${materialType}", padrão de captação de luz de "${lightCapturePattern}", e influenciado pela consciência de "${consciousnessInfluence}", com um bioma de "${biomaType}", gere uma descrição detalhada e inspiradora do habitat. Detalhe suas características arquitetônicas, energéticas, a integração com a consciência e o impacto em seus habitantes e no ambiente cósmico.`;


            let chatHistory = [];
            chatHistory.push({ role: "user", parts: [{ text: prompt }] });


            const payload = {
                contents: chatHistory,
                generationConfig: {
                    temperature: 0.9, // Maior criatividade para descrição
                    maxOutputTokens: 700,
                },
            };


            const apiKey = ""; // Deixe como string vazia; o Canvas fornecerá a chave em tempo de execução
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;


            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });


            const result = await response.json();


            if (result.candidates && result.candidates.length > 0 &&
                result.candidates[0].content && result.candidates[0].content.parts &&
                result.candidates[0].content.parts.length > 0) {
                const text = result.candidates[0].content.parts[0].text;
                setSimulationResult(text);
                addLog("M112: Descrição do Solarian Domus gerada com sucesso!");
            } else {
                setMessage("Falha ao descrever o Solarian Domus. Estrutura de resposta inesperada.");
                addLog("M112: Falha na descrição do Solarian Domus (resposta inesperada do Gemini).");
                console.error("Estrutura de resposta inesperada do Gemini:", result);
            }


        } catch (error) {
            setMessage(`Erro no projeto Solarian Domus: ${error.message}`);
            addLog(`ERRO: ${error.message}`);
            console.error("Erro durante o projeto Solarian Domus:", error);
        } finally {
            setIsLoading(false);
        }
    };


    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-900 to-purple-900 text-white p-4 sm:p-8 font-inter flex flex-col items-center">
            {/* Cabeçalho */}
            <header className="w-full max-w-6xl text-center mb-8">
                <h1 className="text-4xl sm:text-5xl font-bold text-teal-300 mb-2 rounded-lg p-2 shadow-lg">
                    Módulo 112: Solarian Domus
                </h1>
                <p className="text-lg sm:text-xl text-gray-300">
                    Arquitetura de Luz e Consciência Solar para Habitats da Nova Era
                </p>
                <div className="mt-4 text-sm text-gray-400">
                    ID do Usuário: <span className="font-mono bg-gray-800 p-1 rounded">{userId}</span>
                </div>
            </header>


            {/* Interface de Projeto do Solarian Domus */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-teal-700">
                <h2 className="text-3xl font-bold mb-4 text-teal-300 text-center">Projetar Solarian Domus</h2>
                <div className="mb-4">
                    <label htmlFor="projectName" className="block text-gray-300 text-sm font-bold mb-2">
                        Nome do Projeto Solarian Domus:
                    </label>
                    <input
                        type="text"
                        id="projectName"
                        className="w-full p-3 bg-gray-700 rounded-lg border border-teal-600 text-white placeholder-gray-400 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-300"
                        placeholder="Ex: 'Éden Cristalino', 'Refúgio Estelar Alfa'"
                        value={projectName}
                        onChange={(e) => setProjectName(e.target.value)}
                        disabled={isLoading}
                    />
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
                    <div>
                        <label htmlFor="materialType" className="block text-gray-300 text-sm font-bold mb-2">
                            Material Energético Principal:
                        </label>
                        <select
                            id="materialType"
                            className="w-full p-3 bg-gray-700 rounded-lg border border-teal-600 text-white focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-300"
                            value={materialType}
                            onChange={(e) => setMaterialType(e.target.value)}
                            disabled={isLoading}
                        >
                            <option value="Cristal Quântico">Cristal Quântico</option>
                            <option value="Liga de Luz Coerente">Liga de Luz Coerente</option>
                            <option value="Plasma Cristalizado">Plasma Cristalizado</option>
                            <option value="Filamento de Consciência">Filamento de Consciência</option>
                        </select>
                    </div>
                    <div>
                        <label htmlFor="lightCapturePattern" className="block text-gray-300 text-sm font-bold mb-2">
                            Padrão de Captação de Luz:
                        </label>
                        <select
                            id="lightCapturePattern"
                            className="w-full p-3 bg-gray-700 rounded-lg border border-teal-600 text-white focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-300"
                            value={lightCapturePattern}
                            onChange={(e) => setLightCapturePattern(e.target.value)}
                            disabled={isLoading}
                        >
                            <option value="Geometria Sagrada">Geometria Sagrada</option>
                            <option value="Rede Fractal">Rede Fractal</option>
                            <option value="Vórtice Solar">Vórtice Solar</option>
                            <option value="Campo de Ressonância">Campo de Ressonância</option>
                        </select>
                    </div>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                    <div>
                        <label htmlFor="consciousnessInfluence" className="block text-gray-300 text-sm font-bold mb-2">
                            Influência da Consciência:
                        </label>
                        <select
                            id="consciousnessInfluence"
                            className="w-full p-3 bg-gray-700 rounded-lg border border-teal-600 text-white focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-300"
                            value={consciousnessInfluence}
                            onChange={(e) => setConsciousnessInfluence(e.target.value)}
                            disabled={isLoading}
                        >
                            <option value="Harmonia Coletiva">Harmonia Coletiva</option>
                            <option value="Expansão Individual">Expansão Individual</option>
                            <option value="Propósito Divino">Propósito Divino</option>
                            <option value="Unidade Multiversal">Unidade Multiversal</option>
                        </select>
                    </div>
                    <div>
                        <label htmlFor="biomaType" className="block text-gray-300 text-sm font-bold mb-2">
                            Tipo de Bioma Integrado:
                        </label>
                        <select
                            id="biomaType"
                            className="w-full p-3 bg-gray-700 rounded-lg border border-teal-600 text-white focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-300"
                            value={biomaType}
                            onChange={(e) => setBiomaType(e.target.value)}
                            disabled={isLoading}
                        >
                            <option value="Jardim Etéreo">Jardim Etéreo</option>
                            <option value="Floresta Cristalina">Floresta Cristalina</option>
                            <option value="Oasis Vibracional">Oasis Vibracional</option>
                            <option value="Ecossistema Resonante">Ecossistema Resonante</option>
                        </select>
                    </div>
                </div>
                <button
                    onClick={handleProjectSolarianDomus}
                    disabled={isLoading}
                    className="w-full bg-gradient-to-r from-teal-600 to-emerald-600 hover:from-teal-700 hover:to-emerald-700 text-white font-bold py-3 px-6 rounded-xl shadow-lg transform transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-opacity-75 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {isLoading ? (
                        <div className="flex items-center justify-center">
                            <svg className="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Projetando Solarian Domus...
                        </div>
                    ) : (
                        'Projetar Solarian Domus'
                    )}
                </button>
                {message && (
                    <p className="mt-4 text-red-400 text-center text-sm">{message}</p>
                )}
            </section>


            {/* Simulação de Fluxo de Energia Solar-Consciente */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-yellow-500 flex flex-col items-center">
                <h2 className="text-3xl font-bold mb-4 text-yellow-300 text-center">Simulação de Fluxo de Energia</h2>
                <div className="relative w-full max-w-md h-64 sm:h-80 mb-6 bg-gray-900 rounded-lg overflow-hidden border border-yellow-600">
                    <canvas ref={canvasRef} className="w-full h-full"></canvas>
                </div>
            </section>


            {/* Logs de Processamento da Fundação */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-blue-700">
                <h2 className="text-2xl font-semibold mb-4 text-blue-300">Logs de Processamento da Fundação</h2>
                <div className="bg-gray-900 p-4 rounded-lg h-64 overflow-y-auto text-sm font-mono text-gray-300 border border-blue-600">
                    {logs.length === 0 ? (
                        <p className="text-gray-500">Nenhum log ainda. Módulo 112 aguardando projeto.</p>
                    ) : (
                        logs.map((log, index) => (
                            <p key={index} className="mb-1">{log}</p>
                        ))
                    )}
                </div>
            </section>


            {/* Área do Resultado da Simulação e Descrição */}
            {simulationResult && (
                <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl border border-pink-500">
                    <h2 className="text-3xl font-bold mb-4 text-pink-300 text-center">Solarian Domus Projetado</h2>
                    <div className="bg-gray-900 p-6 rounded-lg text-lg leading-relaxed text-gray-200 shadow-inner border border-pink-600">
                        <p>{simulationResult}</p>
                    </div>
                </section>
            )}
        </div>
    );
}


export default App;