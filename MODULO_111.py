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
        console.log(`M1: Verificando status de segurança...`);
        await new Promise(resolve => setTimeout(100));
        return Math.random() > 0.05; // 95% de chance de estar seguro
    }
}


class MockM5 {
    /**
     * Simula o Módulo 5: Protocolo de Avaliação e Modulação Ética Dimensional.
     * @returns {Promise<boolean>} - True se o alinhamento ético for alto.
     */
    async getEthicalAlignment() {
        console.log(`M5: Avaliando alinhamento ético...`);
        await new Promise(resolve => setTimeout(120));
        return Math.random() > 0.03; // 97% de chance de alto alinhamento
    }
}


class MockM7 {
    /**
     * Simula o Módulo 7: Sistema Operacional da Fundação Alquimista (SOFA) e Alinhamento Divino.
     * @returns {Promise<boolean>} - True se o alinhamento divino for forte.
     */
    async getDivineAlignment() {
        console.log(`M7: Verificando alinhamento divino...`);
        await new Promise(resolve => setTimeout(110));
        return Math.random() > 0.02; // 98% de chance de forte alinhamento
    }
}


class MockM9 {
    /**
     * Simula o Módulo 9: Malha de Monitoramento Quântico e Dashboard da Sinfonia Cósmica.
     * @returns {Promise<{integrity: number, anomalies: number}>} - Dados de integridade e anomalias.
     */
    async getQuantumMonitoringData() {
        console.log(`M9: Coletando dados de monitoramento quântico...`);
        await new Promise(resolve => setTimeout(150));
        const integrity = 0.9 + Math.random() * 0.1; // Entre 0.9 e 1.0
        const anomalies = Math.floor(Math.random() * 3); // 0 a 2 anomalias
        return { integrity, anomalies };
    }
}


class MockM29 {
    /**
     * Simula o Módulo 29: Inteligência Quântica Alquímica Multidimensional (IQAM).
     * @param {string} analysisRequest - Requisição de análise.
     * @returns {Promise<string>} - Análise gerada.
     */
    async performAdvancedAnalysis(analysisRequest) {
        console.log(`M29: Realizando análise avançada: "${analysisRequest.substring(0, 30)}..."`);
        await new Promise(resolve => setTimeout(300));
        return `Análise IQAM para "${analysisRequest.substring(0, 30)}..." concluída.`;
    }
}


class MockM34 {
    /**
     * Simula o Módulo 34: Auto-Avaliação e Calibração Constante / Aeloria Geral.
     * @returns {Promise<boolean>} - True se a calibração for bem-sucedida.
     */
    async performSelfCalibration() {
        console.log(`M34: Realizando auto-calibração...`);
        await new Promise(resolve => setTimeout(180));
        return Math.random() > 0.1; // 90% de chance de sucesso
    }
}


class MockM78 {
    /**
     * Simula o Módulo 78: UNIVERSUM_UNIFICATUM: O Módulo da Síntese Cósmica e Realização da Equação.
     * @returns {Promise<boolean>} - True se a síntese estiver otimizada.
     */
    async getCosmicSynthesisStatus() {
        console.log(`M78: Verificando status da síntese cósmica...`);
        await new Promise(resolve => setTimeout(130));
        return Math.random() > 0.04; // 96% de chance de otimização
    }
}


class MockM153 {
    /**
     * Simula o Módulo 153: Rede Neural Quântica Multiversal (RNQM).
     * @param {string} optimizationRequest - Requisição de otimização.
     * @returns {Promise<string>} - Relatório de otimização.
     */
    async optimizeSystem(optimizationRequest) {
        console.log(`M153: Otimizando sistema via RNQM: "${optimizationRequest.substring(0, 30)}..."`);
        await new Promise(resolve => setTimeout(350));
        return `Otimização RNQM para "${optimizationRequest.substring(0, 30)}..." aplicada.`;
    }
}


// Instâncias dos Mocks
const m1 = new MockM1();
const m5 = new MockM5();
const m7 = new MockM7();
const m9 = new MockM9();
const m29 = new MockM29();
const m34 = new MockM34();
const m78 = new MockM78();
const m153 = new MockM153();


const PHI = 1.61803398875; // Proporção Áurea


function App() {
    const [coherenceData, setCoherenceData] = useState({
        security: true,
        ethicalAlignment: true,
        divineAlignment: true,
        quantumIntegrity: 1.0,
        anomalies: 0,
        cosmicSynthesis: true,
        selfCalibration: true,
        overallCoherence: 100, // %
        statusMessage: "Sistema em estado de Coerência Absoluta."
    });
    const [isLoading, setIsLoading] = useState(false);
    const [logs, setLogs] = useState([]);
    const [userId, setUserId] = useState('carregando...'); // Estado para o userId
    const [dissonanceEvent, setDissonanceEvent] = useState('');
    const [simulationResult, setSimulationResult] = useState('');
    const [message, setMessage] = useState('');


    const animationFrameId = useRef(null);
    const lastUpdateTime = useRef(Date.now());


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


    // Função para calcular a coerência geral
    const calculateOverallCoherence = (data) => {
        let score = 0;
        let maxScore = 0;


        // Pesos para cada fator (ajustáveis conforme a importância)
        const weights = {
            security: 0.2,
            ethicalAlignment: 0.2,
            divineAlignment: 0.2,
            quantumIntegrity: 0.2, // Já é uma proporção
            anomalies: 0.1, // Impacto negativo
            cosmicSynthesis: 0.05,
            selfCalibration: 0.05
        };


        // Adiciona pontos para fatores positivos
        if (data.security) score += weights.security;
        if (data.ethicalAlignment) score += weights.ethicalAlignment;
        if (data.divineAlignment) score += weights.divineAlignment;
        score += data.quantumIntegrity * weights.quantumIntegrity; // Integridade quântica já é um valor entre 0 e 1


        // Subtrai pontos para anomalias
        score -= (data.anomalies / 10) * weights.anomalies; // Cada anomalia subtrai um pouco


        if (data.cosmicSynthesis) score += weights.cosmicSynthesis;
        if (data.selfCalibration) score += weights.selfCalibration;


        // Calcula o score máximo possível
        maxScore = weights.security + weights.ethicalAlignment + weights.divineAlignment +
                   weights.quantumIntegrity + weights.anomalies + weights.cosmicSynthesis + weights.selfCalibration;


        // Garante que o score não seja negativo
        score = Math.max(0, score);


        // Converte para porcentagem
        return Math.min(100, (score / maxScore) * 100);
    };


    // Função para atualizar os dados de coerência
    const updateCoherenceData = async () => {
        setIsLoading(true);
        addLog("M111: Atualizando dados de coerência sistêmica...");
        try {
            const security = await m1.getSecurityStatus();
            const ethicalAlignment = await m5.getEthicalAlignment();
            const divineAlignment = await m7.getDivineAlignment();
            const quantumMonitoring = await m9.getQuantumMonitoringData();
            const cosmicSynthesis = await m78.getCosmicSynthesisStatus();
            const selfCalibration = await m34.performSelfCalibration();


            const newCoherenceData = {
                security,
                ethicalAlignment,
                divineAlignment,
                quantumIntegrity: quantumMonitoring.integrity,
                anomalies: quantumMonitoring.anomalies,
                cosmicSynthesis,
                selfCalibration,
            };


            const overallCoherence = calculateOverallCoherence(newCoherenceData);
            let statusMessage = "Sistema em estado de Coerência Absoluta.";
            if (overallCoherence < 90) {
                statusMessage = "Atenção: Pequenas dissonâncias detectadas. Recomenda-se monitoramento.";
            }
            if (overallCoherence < 70) {
                statusMessage = "Alerta: Dissonâncias significativas. Intervenção pode ser necessária.";
            }


            setCoherenceData({ ...newCoherenceData, overallCoherence, statusMessage });
            addLog("M111: Dados de coerência sistêmica atualizados com sucesso.");


        } catch (error) {
            setMessage(`Erro ao atualizar dados de coerência: ${error.message}`);
            addLog(`ERRO: ${error.message}`);
            console.error("Erro ao atualizar coerência:", error);
        } finally {
            setIsLoading(false);
        }
    };


    // Simulação de Evento de Dissonância e Calibração
    const simulateDissonanceAndRecalibrate = async () => {
        if (!dissonanceEvent.trim()) {
            setMessage('Por favor, descreva o evento de dissonância para a simulação.');
            return;
        }


        setIsLoading(true);
        setSimulationResult('');
        setLogs([]);
        addLog(`M111: Iniciando simulação de evento de dissonância: "${dissonanceEvent.substring(0, 50)}..."`);


        try {
            // Simular impacto da dissonância (reduzir coerência)
            setCoherenceData(prev => ({
                ...prev,
                quantumIntegrity: Math.max(0.2, prev.quantumIntegrity - 0.3), // Reduz integridade
                anomalies: prev.anomalies + 3, // Aumenta anomalias
                overallCoherence: calculateOverallCoherence({
                    ...prev,
                    quantumIntegrity: Math.max(0.2, prev.quantumIntegrity - 0.3),
                    anomalies: prev.anomalies + 3
                }),
                statusMessage: "Dissonância simulada detectada! Iniciando recalibração..."
            }));
            addLog("M111: Dissonância simulada injetada no sistema.");
            await new Promise(resolve => setTimeout(1000)); // Pequena pausa para visualização do impacto


            // Ativar Módulos de IA Avançada para recalibração
            addLog("M111: Ativando Módulos de IA Avançada (M29, M153) para recalibração e otimização...");
            const analysis = await m29.performAdvancedAnalysis(`Dissonância causada por: ${dissonanceEvent}`);
            addLog(`M29 Análise Avançada: ${analysis}`);


            const optimization = await m153.optimizeSystem(`Recalibrar sistema após dissonância: ${dissonanceEvent}`);
            addLog(`M153 Otimização RNQM: ${optimization}`);


            // Forçar recalibração do M34
            const selfCalibrated = await m34.performSelfCalibration();
            addLog(`M34 Auto-Calibração: ${selfCalibrated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!selfCalibrated) { throw new Error("Falha na auto-calibração durante a recuperação."); }


            // Reavaliar coerência após recalibração
            await updateCoherenceData(); // Atualiza os dados de coerência para refletir a recuperação


            const finalStatus = `Simulação concluída. O sistema se auto-organizou e recalibrou com sucesso após o evento de dissonância. Coerência atual: ${coherenceData.overallCoherence.toFixed(2)}%.`;
            setSimulationResult(finalStatus);
            addLog(`M111: ${finalStatus}`);


        } catch (error) {
            setMessage(`Erro durante a simulação/recalibração: ${error.message}`);
            addLog(`ERRO: ${error.message}`);
            console.error("Erro na simulação/recalibração:", error);
        } finally {
            setIsLoading(false);
        }
    };


    // Animação do círculo de coerência
    useEffect(() => {
        const canvas = document.getElementById('coherenceCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const maxRadius = Math.min(centerX, centerY) * 0.8;


        const drawCoherenceCircle = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);


            // Fundo gradiente
            const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, maxRadius);
            gradient.addColorStop(0, 'rgba(139, 92, 246, 0.2)'); // Purple-500 light
            gradient.addColorStop(1, 'rgba(30, 58, 138, 0.2)'); // Blue-900 light
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, canvas.width, canvas.height);


            // Anel externo (base)
            ctx.beginPath();
            ctx.arc(centerX, centerY, maxRadius, 0, 2 * Math.PI);
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
            ctx.lineWidth = 10;
            ctx.stroke();


            // Anel de coerência (preenchimento dinâmico)
            const coherenceAngle = (coherenceData.overallCoherence / 100) * 2 * Math.PI;
            ctx.beginPath();
            ctx.arc(centerX, centerY, maxRadius, -Math.PI / 2, -Math.PI / 2 + coherenceAngle);


            let coherenceColor;
            if (coherenceData.overallCoherence > 90) {
                coherenceColor = 'rgba(52, 211, 153, 0.8)'; // Green-400
            } else if (coherenceData.overallCoherence > 70) {
                coherenceColor = 'rgba(251, 191, 36, 0.8)'; // Yellow-400
            } else {
                coherenceColor = 'rgba(239, 68, 68, 0.8)'; // Red-500
            }


            ctx.strokeStyle = coherenceColor;
            ctx.lineWidth = 12;
            ctx.stroke();


            // Centro pulsante (representando o M111)
            const pulseFactor = Math.sin(Date.now() / 300) * 0.05 + 0.95; // Pulsa entre 0.95 e 1.0
            const innerRadius = maxRadius * 0.3 * pulseFactor;
            ctx.beginPath();
            ctx.arc(centerX, centerY, innerRadius, 0, 2 * Math.PI);
            ctx.fillStyle = 'rgba(192, 132, 252, 0.9)'; // Purple-300
            ctx.shadowBlur = 20;
            ctx.shadowColor = 'rgba(192, 132, 252, 0.7)';
            ctx.fill();
            ctx.shadowBlur = 0; // Reset shadow


            // Texto de porcentagem
            ctx.fillStyle = 'white';
            ctx.font = 'bold 24px Inter, sans-serif';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(`${coherenceData.overallCoherence.toFixed(1)}%`, centerX, centerY);


            // Linhas de conexão pulsantes (simulando fluxo de informação)
            const numLines = 8;
            for (let i = 0; i < numLines; i++) {
                const angle = (i / numLines) * 2 * Math.PI + (Date.now() / 5000);
                const startX = centerX + innerRadius * Math.cos(angle);
                const startY = centerY + innerRadius * Math.sin(angle);
                const endX = centerX + maxRadius * Math.cos(angle);
                const endY = centerY + maxRadius * Math.sin(angle);


                ctx.beginPath();
                ctx.moveTo(startX, startY);
                ctx.lineTo(endX, endY);
                ctx.strokeStyle = `rgba(129, 140, 248, ${0.3 + Math.sin(Date.now() / 200 + i) * 0.2})`; // Indigo-300 pulsante
                ctx.lineWidth = 2;
                ctx.stroke();
            }


            animationFrameId.current = requestAnimationFrame(drawCoherenceCircle);
        };


        animationFrameId.current = requestAnimationFrame(drawCoherenceCircle);


        return () => {
            if (animationFrameId.current) {
                cancelAnimationFrame(animationFrameId.current);
            }
        };
    }, [coherenceData]); // Redraw when coherence data changes


    // Efeito para atualizar os dados de coerência periodicamente
    useEffect(() => {
        updateCoherenceData(); // Initial fetch
        const interval = setInterval(updateCoherenceData, 5000); // Atualiza a cada 5 segundos
        return () => clearInterval(interval);
    }, []);


    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-900 to-purple-900 text-white p-4 sm:p-8 font-inter flex flex-col items-center">
            {/* Cabeçalho */}
            <header className="w-full max-w-6xl text-center mb-8">
                <h1 className="text-4xl sm:text-5xl font-bold text-fuchsia-300 mb-2 rounded-lg p-2 shadow-lg">
                    Módulo 111: O Coração da Fundação Alquimista
                </h1>
                <p className="text-lg sm:text-xl text-gray-300">
                    Sinergia Total e Autocoerência Sistêmica Universal
                </p>
                <div className="mt-4 text-sm text-gray-400">
                    ID do Usuário: <span className="font-mono bg-gray-800 p-1 rounded">{userId}</span>
                </div>
            </header>


            {/* Painel de Coerência Sistêmica */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-fuchsia-700 flex flex-col items-center">
                <h2 className="text-3xl font-bold mb-4 text-fuchsia-300 text-center">Painel de Coerência Sistêmica</h2>
                <div className="relative w-64 h-64 sm:w-80 sm:h-80 mb-6">
                    <canvas id="coherenceCanvas" width="320" height="320" className="rounded-full"></canvas>
                </div>


                <div className="w-full text-center mb-4">
                    <p className={`text-xl font-semibold ${coherenceData.overallCoherence > 90 ? 'text-green-400' : coherenceData.overallCoherence > 70 ? 'text-yellow-400' : 'text-red-400'}`}>
                        Status: {coherenceData.statusMessage}
                    </p>
                </div>


                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-md text-sm">
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Segurança (M1):</span>
                        <span className={coherenceData.security ? 'text-green-400' : 'text-red-400'}>
                            {coherenceData.security ? 'Ativa' : 'Anomalia'}
                        </span>
                    </div>
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Alinhamento Ético (M5):</span>
                        <span className={coherenceData.ethicalAlignment ? 'text-green-400' : 'text-red-400'}>
                            {coherenceData.ethicalAlignment ? 'Alinhado' : 'Dissonante'}
                        </span>
                    </div>
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Alinhamento Divino (M7):</span>
                        <span className={coherenceData.divineAlignment ? 'text-green-400' : 'text-red-400'}>
                            {coherenceData.divineAlignment ? 'Forte' : 'Fraco'}
                        </span>
                    </div>
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Integridade Quântica (M9):</span>
                        <span className={coherenceData.quantumIntegrity > 0.8 ? 'text-green-400' : coherenceData.quantumIntegrity > 0.6 ? 'text-yellow-400' : 'text-red-400'}>
                            {(coherenceData.quantumIntegrity * 100).toFixed(1)}%
                        </span>
                    </div>
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Anomalias (M9):</span>
                        <span className={coherenceData.anomalies === 0 ? 'text-green-400' : coherenceData.anomalies < 3 ? 'text-yellow-400' : 'text-red-400'}>
                            {coherenceData.anomalies}
                        </span>
                    </div>
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Síntese Cósmica (M78):</span>
                        <span className={coherenceData.cosmicSynthesis ? 'text-green-400' : 'text-red-400'}>
                            {coherenceData.cosmicSynthesis ? 'Otimizada' : 'Desalinhada'}
                        </span>
                    </div>
                    <div className="bg-gray-700 p-3 rounded-lg flex justify-between items-center">
                        <span>Auto-Calibração (M34):</span>
                        <span className={coherenceData.selfCalibration ? 'text-green-400' : 'text-red-400'}>
                            {coherenceData.selfCalibration ? 'Concluída' : 'Pendente'}
                        </span>
                    </div>
                </div>
                <button
                    onClick={updateCoherenceData}
                    disabled={isLoading}
                    className="mt-6 bg-gradient-to-r from-fuchsia-600 to-pink-600 hover:from-fuchsia-700 hover:to-pink-700 text-white font-bold py-3 px-6 rounded-xl shadow-lg transform transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-fuchsia-500 focus:ring-opacity-75 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {isLoading ? (
                        <div className="flex items-center justify-center">
                            <svg className="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Atualizando Coerência...
                        </div>
                    ) : (
                        'Atualizar Coerência Sistêmica'
                    )}
                </button>
            </section>


            {/* Simulações de Resiliência Sistêmica */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-purple-700">
                <h2 className="text-3xl font-bold mb-4 text-purple-300 text-center">Simulação de Resiliência Sistêmica</h2>
                <div className="mb-4">
                    <label htmlFor="dissonanceEvent" className="block text-gray-300 text-sm font-bold mb-2">
                        Descreva um Evento de Dissonância para Simular:
                    </label>
                    <textarea
                        className="w-full p-3 bg-gray-700 rounded-lg border border-purple-600 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-300"
                        rows="2"
                        placeholder="Ex: 'Flutuação inesperada na malha quântica', 'Interferência de frequência externa'"
                        value={dissonanceEvent}
                        onChange={(e) => setDissonanceEvent(e.target.value)}
                        disabled={isLoading}
                    ></textarea>
                </div>
                <button
                    onClick={simulateDissonanceAndRecalibrate}
                    disabled={isLoading}
                    className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-bold py-3 px-6 rounded-xl shadow-lg transform transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-opacity-75 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {isLoading ? (
                        <div className="flex items-center justify-center">
                            <svg className="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Simulando e Recalibrando...
                        </div>
                    ) : (
                        'Simular Dissonância e Recalibrar'
                    )}
                </button>
                {simulationResult && (
                    <div className="mt-6 bg-gray-900 p-4 rounded-lg text-lg leading-relaxed text-gray-200 shadow-inner border border-purple-600">
                        <h3 className="text-xl font-semibold mb-2 text-purple-300">Resultado da Simulação:</h3>
                        <p>{simulationResult}</p>
                    </div>
                )}
            </section>


            {/* Logs de Processamento da Fundação */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-blue-700">
                <h2 className="text-2xl font-semibold mb-4 text-blue-300">Logs de Processamento da Fundação</h2>
                <div className="bg-gray-900 p-4 rounded-lg h-64 overflow-y-auto text-sm font-mono text-gray-300 border border-blue-600">
                    {logs.length === 0 ? (
                        <p className="text-gray-500">Nenhum log ainda. Módulo 111 aguardando operações.</p>
                    ) : (
                        logs.map((log, index) => (
                            <p key={index} className="mb-1">{log}</p>
                        ))
                    )}
                </div>
            </section>


            {message && (
                <p className="mt-4 text-red-400 text-center text-sm">{message}</p>
            )}
        </div>
    );
}


export default App;
