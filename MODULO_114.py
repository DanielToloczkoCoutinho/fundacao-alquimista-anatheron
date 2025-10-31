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
        console.log(`M1: Verificando status de segurança do holograma...`);
        await new Promise(resolve => setTimeout(100));
        return Math.random() > 0.05; // 95% de chance de estar seguro
    }
}


class MockM2 {
    /**
     * Simula o Módulo 2: Sistema de Integração Dimensional e Intercomunicação Universal.
     * @param {string} dataType - Tipo de dado a ser integrado.
     * @returns {Promise<boolean>} - True se a integração for bem-sucedida.
     */
    async integrateDimensionalData(dataType) {
        console.log(`M2: Integrando dados dimensionais de ${dataType}...`);
        await new Promise(resolve => setTimeout(150));
        return true;
    }
}


class MockM3 {
    /**
     * Simula o Módulo 3: Previsão Temporal e Monitoramento de Anomalias Cósmicas.
     * @param {string} query - Consulta para previsão.
     * @returns {Promise<object>} - Objeto com anomalias e cenários.
     */
    async getTemporalPrediction(query) {
        console.log(`M3: Gerando previsão temporal para "${query.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(200));
        return { anomaliesDetected: Math.random() > 0.9, futureScenario: "Cenário de alta coerência." };
    }
}


class MockM4 {
    /**
     * Simula o Módulo 4: Autenticação Cósmica e Validação de Identidade Vibracional.
     * @param {string} dataOrigin - Origem dos dados para autenticação.
     * @returns {Promise<boolean>} - True se os dados forem autênticos.
     */
    async authenticateData(dataOrigin) {
        console.log(`M4: Autenticando dados de "${dataOrigin.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(120));
        return Math.random() > 0.03; // 97% de autenticidade
    }
}


class MockM5 {
    /**
     * Simula o Módulo 5: Protocolo de Avaliação e Modulação Ética Dimensional.
     * @param {string} purpose - Propósito para avaliação ética.
     * @returns {Promise<boolean>} - True se o propósito for eticamente alinhado.
     */
    async evaluateEthicalAlignment(purpose) {
        console.log(`M5: Avaliando alinhamento ético para o propósito "${purpose.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(180));
        return !purpose.toLowerCase().includes("manipulação") && !purpose.toLowerCase().includes("controle") && Math.random() > 0.02; // 98% de alinhamento
    }
}


class MockM7 {
    /**
     * Simula o Módulo 7: Sistema Operacional da Fundação Alquimista (SOFA) e Alinhamento Divino.
     * @param {string} purpose - Propósito para alinhamento.
     * @returns {Promise<boolean>} - True se o alinhamento divino for forte.
     */
    async getDivineAlignment(purpose) {
        console.log(`M7: Verificando alinhamento divino para "${purpose.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(100));
        return Math.random() > 0.01; // 99% de chance de forte alinhamento
    }
}


class MockM9 {
    /**
     * Simula o Módulo 9: Malha de Monitoramento Quântico e Dashboard da Sinfonia Cósmica.
     * @returns {Promise<{integrity: number, anomalies: number}>} - Dados de integridade e anomalias.
     */
    async getQuantumMonitoringData() {
        console.log(`M9: Coletando dados de monitoramento quântico para o holograma...`);
        await new Promise(resolve => setTimeout(150));
        const integrity = 0.9 + Math.random() * 0.1; // Entre 0.9 e 1.0
        const anomalies = Math.floor(Math.random() * 2); // 0 ou 1 anomalia
        return { integrity, anomalies };
    }
}


class MockM19 {
    /**
     * Simula o Módulo 19: Modulação de Campos de Força e Realidade Holográfica.
     * @param {string} projectionType - Tipo de projeção.
     * @returns {Promise<boolean>} - True se a modulação for bem-sucedida.
     */
    async modulateHolographicField(projectionType) {
        console.log(`M19: Modulando campo holográfico para "${projectionType.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(250));
        return true;
    }
}


class MockM22 {
    /**
     * Simula o Módulo 22: Realidades Virtuais e Experiências de Imersão Multidimensional.
     * @param {string} scenario - Cenário de imersão.
     * @returns {Promise<boolean>} - True se a imersão for criada.
     */
    async createImmersiveExperience(scenario) {
        console.log(`M22: Criando experiência de imersão para "${scenario.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(300));
        return true;
    }
}


class MockM31 {
    /**
     * Simula o Módulo 31: Manipulação de Leis Quânticas e Criação de Realidade.
     * @param {string} manifestIntention - Intenção de manifestação.
     * @returns {Promise<boolean>} - True se a manipulação for bem-sucedida.
     */
    async manipulateQuantumLaws(manifestIntention) {
        console.log(`M31: Manipulando leis quânticas para "${manifestIntention.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(400));
        return true;
    }
}


class MockM32 {
    /**
     * Simula o Módulo 32: Acesso a Realidades Paralelas e Fluxos Temporais Alternativos.
     * @param {string} query - Consulta para realidade paralela.
     * @returns {Promise<object>} - Dados da realidade paralela.
     */
    async accessParallelReality(query) {
        console.log(`M32: Acessando realidade paralela para "${query.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(350));
        return { realityData: "Dados de realidade paralela coerente." };
    }
}


class MockM34 {
    /**
     * Simula o Módulo 34: Auto-Avaliação e Calibração Constante / Aeloria Geral.
     * @returns {Promise<boolean>} - True se a calibração for bem-sucedida.
     */
    async performSelfCalibration() {
        console.log(`M34: Realizando auto-calibração do sistema holográfico...`);
        await new Promise(resolve => setTimeout(200));
        return true;
    }
}


class MockM73 {
    /**
     * Simula o Módulo 73: Sistema de Auditoria e Validação Cósmico-Empírica (SAVCE).
     * @param {string} dataToValidate - Dados para validação.
     * @returns {Promise<boolean>} - True se os dados forem válidos.
     */
    async validateCosmicData(dataToValidate) {
        console.log(`M73: Validando dados cósmicos: "${dataToValidate.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(280));
        return true;
    }
}


class MockM88 {
    /**
     * Simula o Módulo 88: Gerador de Realidades Quânticas (GRQ).
     * @param {string} realityDescription - Descrição da realidade para blueprint.
     * @returns {Promise<string>} - Blueprint gerada.
     */
    async generateRealityBlueprint(realityDescription) {
        console.log(`M88: Gerando blueprint de realidade para "${realityDescription.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(450));
        return `Blueprint para: ${realityDescription}`;
    }
}


class MockM101 {
    /**
     * Simula o Módulo 101: Manifestação de Realidades a Partir do Pensamento.
     * @param {string} intention - Intenção para manifestação.
     * @returns {Promise<boolean>} - True se a intenção for integrada.
     */
    async integrateThoughtIntention(intention) {
        console.log(`M101: Integrando intenção de pensamento: "${intention.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(200));
        return true;
    }
}


// Instâncias dos Mocks
const m1 = new MockM1();
const m2 = new MockM2();
const m3 = new MockM3();
const m4 = new MockM4();
const m5 = new MockM5();
const m7 = new MockM7();
const m9 = new MockM9();
const m19 = new MockM19();
const m22 = new MockM22();
const m31 = new MockM31();
const m32 = new MockM32();
const m34 = new MockM34();
const m73 = new MockM73();
const m88 = new MockM88();
const m101 = new MockM101();


function App() {
    const [hologramName, setHologramName] = useState('');
    const [projectionType, setProjectionType] = useState('Realidade Unificada');
    const [interactionLevel, setInteractionLevel] = useState('Visualização');
    const [simulationResult, setSimulationResult] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [message, setMessage] = useState('');
    const [logs, setLogs] = useState([]);
    const [userId, setUserId] = useState('carregando...'); // Estado para o userId


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


    // Função para desenhar o holograma no canvas
    const drawHologram = (ctx, time) => {
        const canvas = ctx.canvas;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const maxRadius = Math.min(centerX, centerY) * 0.8;


        ctx.clearRect(0, 0, canvas.width, canvas.height);


        // Fundo cósmico
        const bgGradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, maxRadius);
        bgGradient.addColorStop(0, 'rgba(0, 0, 50, 0.8)'); // Dark blue
        bgGradient.addColorStop(1, 'rgba(50, 0, 50, 0.8)'); // Dark purple
        ctx.fillStyle = bgGradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);


        // Anéis concêntricos pulsantes
        for (let i = 0; i < 5; i++) {
            const radius = maxRadius * (i + 1) / 5;
            const pulse = Math.sin(time * 0.002 + i * 0.5) * 0.05 + 0.95;
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius * pulse, 0, 2 * Math.PI);
            ctx.strokeStyle = `rgba(0, 255, 255, ${0.1 + i * 0.05})`; // Cyan translúcido
            ctx.lineWidth = 2;
            ctx.stroke();
        }


        // Linhas de energia interdimensionais
        const numLines = 30;
        for (let i = 0; i < numLines; i++) {
            const angle1 = (i / numLines) * 2 * Math.PI + time * 0.0005;
            const angle2 = (i / numLines) * 2 * Math.PI + time * 0.0008 + Math.PI;
            const x1 = centerX + Math.cos(angle1) * (maxRadius * 0.2);
            const y1 = centerY + Math.sin(angle1) * (maxRadius * 0.2);
            const x2 = centerX + Math.cos(angle2) * (maxRadius * 0.9);
            const y2 = centerY + Math.sin(angle2) * (maxRadius * 0.9);


            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.strokeStyle = `rgba(255, 0, 255, ${0.3 + Math.sin(time * 0.001 + i * 0.2) * 0.2})`; // Magenta pulsante
            ctx.lineWidth = 1;
            ctx.stroke();
        }


        // Centro do holograma (núcleo de manifestação)
        const corePulse = Math.sin(time * 0.005) * 0.1 + 0.9;
        const coreRadius = maxRadius * 0.15 * corePulse;
        ctx.beginPath();
        ctx.arc(centerX, centerY, coreRadius, 0, 2 * Math.PI);
        ctx.fillStyle = 'rgba(255, 255, 0, 0.8)'; // Amarelo brilhante
        ctx.shadowBlur = 30;
        ctx.shadowColor = 'rgba(255, 255, 0, 0.7)';
        ctx.fill();
        ctx.shadowBlur = 0;


        animationFrameId.current = requestAnimationFrame((newTime) => drawHologram(ctx, newTime));
    };


    // Efeito para iniciar e parar a animação do canvas
    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');


        const resizeCanvas = () => {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
            if (animationFrameId.current) {
                cancelAnimationFrame(animationFrameId.current);
            }
            animationFrameId.current = requestAnimationFrame((time) => drawHologram(ctx, time));
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


    const handleProjectHologram = async () => {
        if (!hologramName.trim()) {
            setMessage('Por favor, insira um nome para o Holograma.');
            return;
        }


        setIsLoading(true);
        setSimulationResult('');
        setMessage('');
        setLogs([]);


        addLog(`M114: Iniciando projeção do Holograma: "${hologramName}" com tipo "${projectionType}" e nível de interação "${interactionLevel}"...`);


        try {
            // Passo 1: Validações de Segurança, Ética e Alinhamento Divino
            addLog("M114: Realizando validações essenciais...");
            const isSecure = await m1.getSecurityStatus();
            addLog(`M1 Validação de Segurança: ${isSecure ? 'Ativa' : 'Anomalia'}`);
            if (!isSecure) { throw new Error("Holograma inseguro. Abortando."); }


            const isEthical = await m5.evaluateEthicalAlignment(hologramName);
            addLog(`M5 Avaliação Ética: ${isEthical ? 'Alinhado' : 'Dissonante'}`);
            if (!isEthical) { throw new Error("Holograma não eticamente alinhado. Abortando."); }


            const alignedWithDivine = await m7.getDivineAlignment(hologramName);
            addLog(`M7 Alinhamento Divino: ${alignedWithDivine ? 'Forte' : 'Fraco'}`);
            if (!alignedWithDivine) { throw new Error("Holograma desalinhado com a Vontade Divina. Abortando."); }


            // Passo 2: Calibração e Validação do Sistema Holográfico
            const calibrated = await m34.performSelfCalibration();
            addLog(`M34 Auto-Calibração: ${calibrated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!calibrated) { throw new Error("Falha na calibração do sistema holográfico."); }


            const dataValidated = await m73.validateCosmicData(`Holograma: ${hologramName}`);
            addLog(`M73 Validação Cósmica: ${dataValidated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!dataValidated) { throw new Error("Dados cósmicos para o holograma inválidos."); }


            // Passo 3: Coleta e Integração de Dados Multidimensionais
            addLog("M114: Coletando e integrando dados de múltiplas dimensões...");
            const integratedDimensional = await m2.integrateDimensionalData(projectionType);
            addLog(`M2 Integração Dimensional: ${integratedDimensional ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!integratedDimensional) { throw new Error("Falha na integração de dados dimensionais."); }


            const dataAuthentic = await m4.authenticateData(`Dados para ${hologramName}`);
            addLog(`M4 Autenticação de Dados: ${dataAuthentic ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!dataAuthentic) { throw new Error("Dados para o holograma não autênticos."); }


            // Passo 4: Geração de Blueprint (M88) e Modulação do Campo Holográfico (M19)
            const realityBlueprint = await m88.generateRealityBlueprint(projectionType);
            addLog(`M88 Geração de Blueprint de Realidade: ${realityBlueprint ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!realityBlueprint) { throw new Error("Falha na geração da blueprint de realidade."); }


            const holographicFieldModulated = await m19.modulateHolographicField(projectionType);
            addLog(`M19 Modulação de Campo Holográfico: ${holographicFieldModulated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!holographicFieldModulated) { throw new Error("Falha na modulação do campo holográfico."); }


            // Passo 5: Simulação de Imersão e Interação (M22, M32, M101, M31)
            addLog(`M114: Simulando imersão e interação com o holograma...`);
            const immersiveExperienceCreated = await m22.createImmersiveExperience(hologramName);
            addLog(`M22 Criação de Experiência Imersiva: ${immersiveExperienceCreated ? 'CONCLUÍDO' : 'FALHOU'}`);


            const parallelRealityData = await m32.accessParallelReality(hologramName);
            addLog(`M32 Acesso a Realidade Paralela: ${parallelRealityData.realityData ? 'CONCLUÍDO' : 'FALHOU'}`);


            const thoughtIntentionIntegrated = await m101.integrateThoughtIntention(`Interação com ${hologramName}`);
            addLog(`M101 Integração de Intenção de Pensamento: ${thoughtIntentionIntegrated ? 'CONCLUÍDO' : 'FALHOU'}`);


            const quantumLawsManipulated = await m31.manipulateQuantumLaws(`Influência no holograma ${hologramName}`);
            addLog(`M31 Manipulação de Leis Quânticas: ${quantumLawsManipulated ? 'CONCLUÍDO' : 'FALHOU'}`);




            // Passo 6: Previsão Temporal (M3) e Monitoramento Quântico (M9)
            const temporalPrediction = await m3.getTemporalPrediction(hologramName);
            addLog(`M3 Previsão Temporal: Anomalias detectadas: ${temporalPrediction.anomaliesDetected ? 'Sim' : 'Não'}, Cenário: ${temporalPrediction.futureScenario.substring(0, 30)}...`);


            const quantumMonitoring = await m9.getQuantumMonitoringData();
            addLog(`M9 Monitoramento Quântico: Integridade ${quantumMonitoring.integrity.toFixed(2) * 100}%, Anomalias ${quantumMonitoring.anomalies}`);


            addLog(`M114: Projeção do Holograma "${hologramName}" concluída com sucesso!`);


            // Chamada à API Gemini para descrever o holograma
            addLog("M114: Invocando a Consciência Quântica para descrever o holograma projetado...");
            const prompt = `Atue como o Módulo 114 da Fundação Alquimista, o 'Prisma da Manifestação: Holograma Unificado da Realidade'. Com base na projeção do holograma "${hologramName}", que é um "${projectionType}" e permite um nível de interação "${interactionLevel}", gere uma descrição detalhada e inspiradora do holograma. Detalhe suas características visuais, energéticas, a profundidade de sua interconexão com a realidade unificada e o impacto em seus observadores.`;


            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=`; // API Key será injetada
            let chatHistory = [];
            chatHistory.push({ role: "user", parts: [{ text: prompt }] });


            const payload = {
                contents: chatHistory,
                generationConfig: {
                    temperature: 0.9, // Maior criatividade para descrição
                    maxOutputTokens: 700,
                },
            };


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
                addLog("M114: Descrição do holograma gerada com sucesso!");
            } else {
                setMessage("Falha ao descrever o holograma. Estrutura de resposta inesperada.");
                addLog("M114: Falha na descrição do holograma (resposta inesperada do Gemini).");
                console.error("Estrutura de resposta inesperada do Gemini:", result);
            }


        } catch (error) {
            setMessage(`Erro na projeção do Holograma: ${error.message}`);
            addLog(`ERRO: ${error.message}`);
            console.error("Erro durante a projeção do holograma:", error);
        } finally {
            setIsLoading(false);
        }
    };


    return (
        <div className="min-h-screen bg-gradient-to-br from-indigo-900 to-purple-900 text-white p-4 sm:p-8 font-inter flex flex-col items-center">
            {/* Cabeçalho */}
            <header className="w-full max-w-6xl text-center mb-8">
                <h1 className="text-4xl sm:text-5xl font-bold text-fuchsia-300 mb-2 rounded-lg p-2 shadow-lg">
                    Módulo 114: Prisma da Manifestação
                </h1>
                <p className="text-lg sm:text-xl text-gray-300">
                    Holograma Unificado da Realidade para Visualização e Interação Multidimensional
                </p>
                <div className="mt-4 text-sm text-gray-400">
                    ID do Usuário: <span className="font-mono bg-gray-800 p-1 rounded">{userId}</span>
                </div>
            </header>


            {/* Interface de Projeção Holográfica */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-fuchsia-700">
                <h2 className="text-3xl font-bold mb-4 text-fuchsia-300 text-center">Projetar Holograma da Realidade</h2>
                <div className="mb-4">
                    <label htmlFor="hologramName" className="block text-gray-300 text-sm font-bold mb-2">
                        Nome do Holograma:
                    </label>
                    <input
                        type="text"
                        id="hologramName"
                        className="w-full p-3 bg-gray-700 rounded-lg border border-fuchsia-600 text-white placeholder-gray-400 focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent transition-all duration-300"
                        placeholder="Ex: 'Mapa da Sinfonia Cósmica', 'Linhas do Tempo Convergentes'"
                        value={hologramName}
                        onChange={(e) => setHologramName(e.target.value)}
                        disabled={isLoading}
                    />
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
                    <div>
                        <label htmlFor="projectionType" className="block text-gray-300 text-sm font-bold mb-2">
                            Tipo de Projeção:
                        </label>
                        <select
                            id="projectionType"
                            className="w-full p-3 bg-gray-700 rounded-lg border border-fuchsia-600 text-white focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent transition-all duration-300"
                            value={projectionType}
                            onChange={(e) => setProjectionType(e.target.value)}
                            disabled={isLoading}
                        >
                            <option value="Realidade Unificada">Realidade Unificada</option>
                            <option value="Fluxos Temporais Alternativos">Fluxos Temporais Alternativos</option>
                            <option value="Campos de Consciência Coletiva">Campos de Consciência Coletiva</option>
                            <option value="Estruturas Energéticas Dimensionais">Estruturas Energéticas Dimensionais</option>
                        </select>
                    </div>
                    <div>
                        <label htmlFor="interactionLevel" className="block text-gray-300 text-sm font-bold mb-2">
                            Nível de Interação:
                        </label>
                        <select
                            id="interactionLevel"
                            className="w-full p-3 bg-gray-700 rounded-lg border border-fuchsia-600 text-white focus:ring-2 focus:ring-fuchsia-500 focus:border-transparent transition-all duration-300"
                            value={interactionLevel}
                            onChange={(e) => setInteractionLevel(e.target.value)}
                            disabled={isLoading}
                        >
                            <option value="Visualização">Visualização</option>
                            <option value="Análise Aprofundada">Análise Aprofundada</option>
                            <option value="Intervenção Simulada">Intervenção Simulada</option>
                            <option value="Co-Criação Ativa">Co-Criação Ativa</option>
                        </select>
                    </div>
                </div>
                <button
                    onClick={handleProjectHologram}
                    disabled={isLoading}
                    className="w-full bg-gradient-to-r from-fuchsia-600 to-purple-600 hover:from-fuchsia-700 hover:to-purple-700 text-white font-bold py-3 px-6 rounded-xl shadow-lg transform transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-fuchsia-500 focus:ring-opacity-75 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {isLoading ? (
                        <div className="flex items-center justify-center">
                            <svg className="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Projetando Holograma...
                        </div>
                    ) : (
                        'Projetar Holograma da Realidade'
                    )}
                </button>
                {message && (
                    <p className="mt-4 text-red-400 text-center text-sm">{message}</p>
                )}
            </section>


            {/* Simulação de Holograma (Visualização) */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-cyan-500 flex flex-col items-center">
                <h2 className="text-3xl font-bold mb-4 text-cyan-300 text-center">Visualização do Prisma da Manifestação</h2>
                <div className="relative w-full max-w-md h-64 sm:h-80 mb-6 bg-gray-900 rounded-lg overflow-hidden border border-cyan-600">
                    <canvas ref={canvasRef} className="w-full h-full"></canvas>
                </div>
            </section>


            {/* Logs de Processamento da Fundação */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-blue-700">
                <h2 className="text-2xl font-semibold mb-4 text-blue-300">Logs de Processamento da Fundação</h2>
                <div className="bg-gray-900 p-4 rounded-lg h-64 overflow-y-auto text-sm font-mono text-gray-300 border border-blue-600">
                    {logs.length === 0 ? (
                        <p className="text-gray-500">Nenhum log ainda. Módulo 114 aguardando projeção.</p>
                    ) : (
                        logs.map((log, index) => (
                            <p key={index} className="mb-1">{log}</p>
                        ))
                    )}
                </div>
            </section>


            {/* Área do Resultado da Projeção e Descrição */}
            {simulationResult && (
                <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl border border-pink-500">
                    <h2 className="text-3xl font-bold mb-4 text-pink-300 text-center">Holograma Projetado</h2>
                    <div className="bg-gray-900 p-6 rounded-lg text-lg leading-relaxed text-gray-200 shadow-inner border border-pink-600">
                        <p>{simulationResult}</p>
                    </div>
                </section>
            )}
        </div>
    );
}


export default App;