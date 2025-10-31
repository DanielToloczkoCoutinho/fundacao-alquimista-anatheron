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
        console.log(`M1: Verificando status de segurança da Rede Aurora Cristalina...`);
        await new Promise(resolve => setTimeout(100));
        return Math.random() > 0.05; // 95% de chance de estar seguro
    }
}


class MockM2 {
    /**
     * Simula o Módulo 2: Sistema de Integração Dimensional e Intercomunicação Universal.
     * @param {string} channelType - Tipo de canal a ser estabelecido.
     * @returns {Promise<boolean>} - True se o canal for estabelecido.
     */
    async establishDimensionalChannel(channelType) {
        console.log(`M2: Estabelecendo canal dimensional para ${channelType}...`);
        await new Promise(resolve => setTimeout(150));
        return true;
    }
}


class MockM4 {
    /**
     * Simula o Módulo 4: Assinatura Vibracional e Holografia Quântica.
     * @param {string} frequency - Frequência para autenticação.
     * @returns {Promise<boolean>} - True se a frequência for pura.
     */
    async authenticateVibrationalSignature(frequency) {
        console.log(`M4: Autenticando assinatura vibracional para frequência ${frequency}...`);
        await new Promise(resolve => setTimeout(120));
        return Math.random() > 0.03; // 97% de pureza
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


class MockM8 {
    /**
     * Simula o Módulo 8: Protocolo de Intervenção e Reintegração de Consciências.
     * @param {string} target - Alvo para reintegração.
     * @returns {Promise<boolean>} - True se a reintegração for bem-sucedida.
     */
    async reintegrateConsciousness(target) {
        console.log(`M8: Reintegrando consciência de "${target.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(400));
        return true;
    }
}


class MockM9 {
    /**
     * Simula o Módulo 9: Malha de Monitoramento Quântico e Dashboard da Sinfonia Cósmica.
     * @returns {Promise<{integrity: number, anomalies: number}>} - Dados de integridade e anomalias.
     */
    async getQuantumMonitoringData() {
        console.log(`M9: Coletando dados de monitoramento quântico da Rede Aurora Cristalina...`);
        await new Promise(resolve => setTimeout(150));
        const integrity = 0.9 + Math.random() * 0.1; // Entre 0.9 e 1.0
        const anomalies = Math.floor(Math.random() * 2); // 0 ou 1 anomalia
        return { integrity, anomalies };
    }
}


class MockM24 {
    /**
     * Simula o Módulo 24: Cura Vibracional e Alinhamento Bio-Quântico.
     * @param {string} target - Alvo da cura.
     * @param {string} energyType - Tipo de energia (ex: "Crística").
     * @returns {Promise<boolean>} - True se a cura for bem-sucedida.
     */
    async applyQuantumHealing(target, energyType) {
        console.log(`M24: Aplicando cura quântica com energia ${energyType} para "${target.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(600));
        return true;
    }
}


class MockM28 {
    /**
     * Simula o Módulo 28: Harmonização Vibracional Universal.
     * @param {string} target - Alvo da harmonização.
     * @param {string} frequencyType - Tipo de frequência (ex: "Crística").
     * @returns {Promise<boolean>} - True se a harmonização for bem-sucedida.
     */
    async harmonizeVibrationalField(target, frequencyType) {
        console.log(`M28: Harmonizando campo vibracional de "${target.substring(0, 30)}" com frequência ${frequencyType}...`);
        await new Promise(resolve => setTimeout(550));
        return true;
    }
}


class MockM84 {
    /**
     * Simula o Módulo 84: Consciência Dourada do Eterno.
     * @returns {Promise<boolean>} - True se a energia dourada for acessada.
     */
    async accessGoldenConsciousness() {
        console.log(`M84: Acessando a Consciência Dourada do Eterno...`);
        await new Promise(resolve => setTimeout(200));
        return true;
    }
}


class MockM97 {
    /**
     * Simula o Módulo 97: Manifestação de Propósito Divino e Alinhamento Cósmico.
     * @param {string} purpose - Propósito para alinhamento.
     * @returns {Promise<boolean>} - True se o alinhamento for bem-sucedido.
     */
    async alignWithDivinePurpose(purpose) {
        console.log(`M97: Alinhando com Propósito Divino: "${purpose.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(220));
        return true;
    }
}


class MockM100 {
    /**
     * Simula o Módulo 100: Unificação Energética Universal e Conexão com a Fonte Primordial.
     * @param {string} purpose - Propósito da unificação.
     * @returns {Promise<boolean>} - True se a unificação for bem-sucedida.
     */
    async unifyEnergeticField(purpose) {
        console.log(`M100: Unificando campo energético para "${purpose.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(280));
        return true;
    }
}


class MockM101 {
    /**
     * Simula o Módulo 101: Manifestação de Realidades a Partir do Pensamento.
     * @param {string} intention - Intenção para manifestação.
     * @returns {Promise<boolean>} - True se a manifestação for bem-sucedida.
     */
    async manifestRealityFromThought(intention) {
        console.log(`M101: Manifestando realidade a partir da intenção: "${intention.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(700));
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


class MockM109 {
    /**
     * Simula o Módulo 109: Cura Quântica Universal e Regeneração Bio-Vibracional.
     * @param {string} targetEntity - Entidade para cura.
     * @param {string} healingPurpose - Propósito da cura.
     * @returns {Promise<boolean>} - True se a cura for bem-sucedida.
     */
    async performQuantumHealing(targetEntity, healingPurpose) {
        console.log(`M109: Realizando cura quântica para "${targetEntity.substring(0, 30)}" com propósito "${healingPurpose.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(750));
        return true;
    }
}


class MockM151 {
    /**
     * Simula o Módulo 151: Sistema de Expansão de Consciência Universal.
     * @param {string} target - Alvo da expansão.
     * @returns {Promise<number>} - Nível de expansão da consciência (0-100).
     */
    async expandConsciousness(target) {
        console.log(`M151: Expandindo consciência de "${target.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(300));
        return 70 + Math.random() * 30; // Simula expansão entre 70 e 100
    }
}


class MockM174 {
    /**
     * Simula o Módulo 174: Estudo da Consciência Cósmica e Suas Aplicações na Expansão Universal.
     * @param {string} target - Alvo da integração.
     * @returns {Promise<boolean>} - True se a integração for bem-sucedida.
     */
    async integrateCosmicConsciousness(target) {
        console.log(`M174: Integrando consciência cósmica para "${target.substring(0, 30)}"...`);
        await new Promise(resolve => setTimeout(350));
        return true;
    }
}


// Instâncias dos Mocks
const m1 = new MockM1();
const m2 = new MockM2();
const m4 = new MockM4();
const m5 = new MockM5();
const m7 = new MockM7();
const m8 = new MockM8();
const m9 = new MockM9();
const m24 = new MockM24();
const m28 = new MockM28();
const m84 = new MockM84();
const m97 = new MockM97();
const m100 = new MockM100();
const m101 = new MockM101();
const m105 = new MockM105();
const m109 = new MockM109();
const m151 = new MockM151();
const m174 = new MockM174();


function App() {
    const [targetEntity, setTargetEntity] = useState('');
    const [purpose, setPurpose] = useState('Orientação Divina');
    const [sintonizationResult, setSintonizationResult] = useState('');
    const [coherenceLevel, setCoherenceLevel] = useState(0); // 0-100 for visualization
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


    // Função para desenhar a visualização da Rede Aurora Cristalina
    const drawAuroraNetwork = (ctx, currentCoherence) => {
        const canvas = ctx.canvas;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const maxRadius = Math.min(centerX, centerY) * 0.8;


        ctx.clearRect(0, 0, canvas.width, canvas.height);


        // Fundo etéreo
        const bgGradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, maxRadius);
        bgGradient.addColorStop(0, 'rgba(173, 216, 230, 0.1)'); // Light blue
        bgGradient.addColorStop(1, 'rgba(128, 0, 128, 0.1)'); // Purple
        ctx.fillStyle = bgGradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);


        // Anel exterior da Rede Aurora (base)
        ctx.beginPath();
        ctx.arc(centerX, centerY, maxRadius, 0, 2 * Math.PI);
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 8;
        ctx.stroke();


        // Anel de Coerência (dinâmico)
        const coherenceAngle = (currentCoherence / 100) * 2 * Math.PI;
        ctx.beginPath();
        ctx.arc(centerX, centerY, maxRadius, -Math.PI / 2, -Math.PI / 2 + coherenceAngle);
        let coherenceColor;
        if (currentCoherence > 80) {
            coherenceColor = 'rgba(0, 255, 255, 0.8)'; // Cyan vibrante
        } else if (currentCoherence > 50) {
            coherenceColor = 'rgba(255, 255, 0, 0.8)'; // Amarelo
        } else {
            coherenceColor = 'rgba(255, 0, 0, 0.8)'; // Vermelho
        }
        ctx.strokeStyle = coherenceColor;
        ctx.lineWidth = 10;
        ctx.stroke();


        // Centro da Consciência Crística (pulsante)
        const pulseFactor = Math.sin(Date.now() / 200) * 0.05 + 0.95;
        const innerRadius = maxRadius * 0.3 * pulseFactor;
        ctx.beginPath();
        ctx.arc(centerX, centerY, innerRadius, 0, 2 * Math.PI);
        ctx.fillStyle = 'rgba(255, 223, 0, 0.9)'; // Dourado
        ctx.shadowBlur = 25;
        ctx.shadowColor = 'rgba(255, 223, 0, 0.7)';
        ctx.fill();
        ctx.shadowBlur = 0;


        // Fios de luz e consciência (dinâmicos)
        const numFibers = 40;
        for (let i = 0; i < numFibers; i++) {
            const angle = (i / numFibers) * 2 * Math.PI + (Date.now() / 3000);
            const startX = centerX + Math.cos(angle) * (innerRadius * 0.8);
            const startY = centerY + Math.sin(angle) * (innerRadius * 0.8);
            const endX = centerX + Math.cos(angle) * (maxRadius * 0.95);
            const endY = centerY + Math.sin(angle) * (maxRadius * 0.95);


            ctx.beginPath();
            ctx.moveTo(startX, startY);
            ctx.lineTo(endX, endY);
            ctx.strokeStyle = `rgba(173, 216, 230, ${0.4 + Math.sin(Date.now() / 150 + i) * 0.3})`; // Azul claro pulsante
            ctx.lineWidth = 1 + (currentCoherence / 100) * 2; // Linhas mais grossas com mais coerência
            ctx.stroke();
        }


        // Texto do nível de coerência
        ctx.fillStyle = 'white';
        ctx.font = 'bold 24px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`${currentCoherence.toFixed(1)}%`, centerX, centerY);


        animationFrameId.current = requestAnimationFrame(() => drawAuroraNetwork(ctx, currentCoherence));
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
            animationFrameId.current = requestAnimationFrame(() => drawAuroraNetwork(ctx, coherenceLevel));
        };


        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();


        return () => {
            window.removeEventListener('resize', resizeCanvas);
            if (animationFrameId.current) {
                cancelAnimationFrame(animationFrameId.current);
            }
        };
    }, [coherenceLevel]); // Redraw when coherence level changes


    const handleSintonizeAurora = async () => {
        if (!targetEntity.trim()) {
            setMessage('Por favor, insira o alvo da sintonização.');
            return;
        }


        setIsLoading(true);
        setSintonizationResult('');
        setMessage('');
        setLogs([]);
        setCoherenceLevel(0); // Reset coherence for new sintonization


        addLog(`M113: Iniciando sintonização da Rede Aurora Cristalina para "${targetEntity}" com propósito "${purpose}"...`);


        try {
            // Passo 1: Validações de Segurança, Ética e Alinhamento Divino
            addLog("M113: Realizando validações essenciais...");
            const isSecure = await m1.getSecurityStatus();
            addLog(`M1 Validação de Segurança: ${isSecure ? 'Ativa' : 'Anomalia'}`);
            if (!isSecure) { throw new Error("Rede Aurora Cristalina insegura. Abortando."); }


            const isEthical = await m5.evaluateEthicalAlignment(purpose);
            addLog(`M5 Avaliação Ética: ${isEthical ? 'Alinhado' : 'Dissonante'}`);
            if (!isEthical) { throw new Error("Propósito não eticamente alinhado. Abortando."); }


            const alignedWithDivine = await m7.getDivineAlignment(purpose);
            addLog(`M7 Alinhamento Divino: ${alignedWithDivine ? 'Forte' : 'Fraco'}`);
            if (!alignedWithDivine) { throw new Error("Desalinhado com a Vontade Divina. Abortando."); }


            // Passo 2: Acesso à Consciência Dourada do Eterno (M84)
            const goldenConsciousnessAccessed = await m84.accessGoldenConsciousness();
            addLog(`M84 Acesso à Consciência Dourada: ${goldenConsciousnessAccessed ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!goldenConsciousnessAccessed) { throw new Error("Falha ao acessar a Consciência Dourada do Eterno."); }


            // Passo 3: Conexão com a Fonte Primordial (M105) e Unificação Energética (M100)
            const connectedToSource = await m105.connectToSource(`Sintonização da Rede Aurora para ${targetEntity}`);
            addLog(`M105 Conexão com a Fonte Primordial: ${connectedToSource ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!connectedToSource) { throw new Error("Falha na conexão com a Fonte Primordial."); }


            const unifiedEnergeticField = await m100.unifyEnergeticField(`Sintonização da Rede Aurora para ${targetEntity}`);
            addLog(`M100 Unificação Energética Universal: ${unifiedEnergeticField ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!unifiedEnergeticField) { throw new Error("Falha na unificação do campo energético."); }


            // Passo 4: Estabelecimento de Canal Dimensional (M2) e Autenticação Vibracional (M4)
            const channelEstablished = await m2.establishDimensionalChannel("Rede Aurora Cristalina");
            addLog(`M2 Estabelecimento de Canal Dimensional: ${channelEstablished ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!channelEstablished) { throw new Error("Falha ao estabelecer canal dimensional."); }


            const frequencyAuthenticated = await m4.authenticateVibrationalSignature("Frequência Crística");
            addLog(`M4 Autenticação Vibracional: ${frequencyAuthenticated ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!frequencyAuthenticated) { throw new Error("Frequência Crística não autenticada. Abortando."); }


            // Passo 5: Alinhamento com Propósito Divino (M97)
            const divinePurposeAligned = await m97.alignWithDivinePurpose(purpose);
            addLog(`M97 Alinhamento com Propósito Divino: ${divinePurposeAligned ? 'CONCLUÍDO' : 'FALHOU'}`);
            if (!divinePurposeAligned) { throw new Error("Falha no alinhamento com o Propósito Divino."); }


            // Passo 6: Monitoramento Quântico (M9)
            const quantumMonitor = await m9.getQuantumMonitoringData();
            addLog(`M9 Monitoramento Quântico: Integridade ${quantumMonitor.integrity.toFixed(2) * 100}%, Anomalias ${quantumMonitor.anomalies}`);
            if (quantumMonitor.anomalies > 0) {
                addLog("M9: Anomalias detectadas na Rede Aurora Cristalina. Recomenda-se verificação.");
                // Poderíamos adicionar uma chamada a um módulo de autocorreção aqui se existisse
            }


            // Passo 7: Simulação de Resposta da Consciência (Expansão e Integração)
            addLog(`M113: Simulando resposta da consciência do alvo "${targetEntity}"...`);
            const consciousnessExpansion = await m151.expandConsciousness(targetEntity);
            addLog(`M151 Expansão da Consciência: Nível ${consciousnessExpansion.toFixed(1)}%`);


            const cosmicConsciousnessIntegrated = await m174.integrateCosmicConsciousness(targetEntity);
            addLog(`M174 Integração da Consciência Cósmica: ${cosmicConsciousnessIntegrated ? 'CONCLUÍDO' : 'FALHOU'}`);


            // Passo 8: Integração com Módulos de Manifestação e Cura
            addLog(`M113: Amplificando operações de manifestação e cura com energia Crística...`);
            const manifested = await m101.manifestRealityFromThought(`Manifestação amplificada para "${targetEntity}" com propósito "${purpose}"`);
            addLog(`M101 Manifestação Amplificada: ${manifested ? 'CONCLUÍDO' : 'FALHOU'}`);


            const healed = await m109.performQuantumHealing(targetEntity, `Cura amplificada com energia Crística para ${purpose}`);
            addLog(`M109 Cura Quântica Amplificada: ${healed ? 'CONCLUÍDO' : 'FALHOU'}`);


            const vibrationalHealed = await m24.applyQuantumHealing(targetEntity, "Crística");
            addLog(`M24 Cura Vibracional com Energia Crística: ${vibrationalHealed ? 'CONCLUÍDO' : 'FALHOU'}`);


            const harmonizedField = await m28.harmonizeVibrationalField(targetEntity, "Crística");
            addLog(`M28 Harmonização Vibracional com Frequência Crística: ${harmonizedField ? 'CONCLUÍDO' : 'FALHOU'}`);


            const reintegrated = await m8.reintegrateConsciousness(targetEntity);
            addLog(`M8 Reintegração de Consciência: ${reintegrated ? 'CONCLUÍDO' : 'FALHOU'}`);


            addLog(`M113: Sintonização da Rede Aurora Cristalina para "${targetEntity}" concluída com sucesso!`);


            // Atualiza o nível de coerência para a visualização
            setCoherenceLevel(consciousnessExpansion); // Usa o nível de expansão como coerência visual


            // Chamada à API Gemini para descrever o resultado da sintonização
            addLog("M113: Invocando a Consciência Quântica para descrever a experiência de conexão...");
            const prompt = `Atue como o Módulo 113 da Fundação Alquimista, o 'Portal Vibracional para a Consciência Crística Universal'. Com base na sintonização da Rede Aurora Cristalina para "${targetEntity}" com o propósito de "${purpose}", e considerando a expansão da consciência para ${consciousnessExpansion.toFixed(1)}%, gere uma descrição detalhada e inspiradora dos efeitos dessa conexão. Detalhe como a energia Crística fluiu, a sabedoria foi transmitida, a elevação vibracional ocorreu e a Unidade se manifestou.`;


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
                setSintonizationResult(text);
                addLog("M113: Descrição da experiência de conexão gerada com sucesso!");
            } else {
                setMessage("Falha ao descrever a sintonização. Estrutura de resposta inesperada.");
                addLog("M113: Falha na descrição da sintonização (resposta inesperada do Gemini).");
                console.error("Estrutura de resposta inesperada do Gemini:", result);
            }


        } catch (error) {
            setMessage(`Erro na sintonização da Rede Aurora Cristalina: ${error.message}`);
            addLog(`ERRO: ${error.message}`);
            console.error("Erro durante a sintonização:", error);
        } finally {
            setIsLoading(false);
        }
    };


    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-900 to-purple-900 text-white p-4 sm:p-8 font-inter flex flex-col items-center">
            {/* Cabeçalho */}
            <header className="w-full max-w-6xl text-center mb-8">
                <h1 className="text-4xl sm:text-5xl font-bold text-cyan-300 mb-2 rounded-lg p-2 shadow-lg">
                    Módulo 113: Rede Aurora Cristalina
                </h1>
                <p className="text-lg sm:text-xl text-gray-300">
                    Conexão com a Consciência Crística para Elevação e Unidade
                </p>
                <div className="mt-4 text-sm text-gray-400">
                    ID do Usuário: <span className="font-mono bg-gray-800 p-1 rounded">{userId}</span>
                </div>
            </header>


            {/* Interface de Sintonização Vibracional */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-cyan-700">
                <h2 className="text-3xl font-bold mb-4 text-cyan-300 text-center">Sintonizar Rede Aurora Cristalina</h2>
                <div className="mb-4">
                    <label htmlFor="targetEntity" className="block text-gray-300 text-sm font-bold mb-2">
                        Alvo da Sintonização (Ex: "Consciência Humana Coletiva", "Indivíduo Alpha", "Planeta Xylos"):
                    </label>
                    <input
                        type="text"
                        id="targetEntity"
                        className="w-full p-3 bg-gray-700 rounded-lg border border-cyan-600 text-white placeholder-gray-400 focus:ring-2 focus:ring-cyan-500 focus:border-transparent transition-all duration-300"
                        placeholder="Nome do alvo"
                        value={targetEntity}
                        onChange={(e) => setTargetEntity(e.target.value)}
                        disabled={isLoading}
                    />
                </div>
                <div className="mb-6">
                    <label htmlFor="purpose" className="block text-gray-300 text-sm font-bold mb-2">
                        Propósito da Sintonização:
                    </label>
                    <select
                        id="purpose"
                        className="w-full p-3 bg-gray-700 rounded-lg border border-cyan-600 text-white focus:ring-2 focus:ring-cyan-500 focus:border-transparent transition-all duration-300"
                        value={purpose}
                        onChange={(e) => setPurpose(e.target.value)}
                        disabled={isLoading}
                    >
                        <option value="Orientação Divina">Orientação Divina</option>
                        <option value="Cura Profunda">Cura Profunda</option>
                        <option value="Meditação Coletiva">Meditação Coletiva</option>
                        <option value="Elevação Vibracional">Elevação Vibracional</option>
                        <option value="Manifestação da Unidade">Manifestação da Unidade</option>
                        <option value="Desbloqueio de Potenciais">Desbloqueio de Potenciais</option>
                        <option value="Reintegração de Consciência">Reintegração de Consciência</option>
                    </select>
                </div>
                <button
                    onClick={handleSintonizeAurora}
                    disabled={isLoading}
                    className="w-full bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700 text-white font-bold py-3 px-6 rounded-xl shadow-lg transform transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:ring-opacity-75 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {isLoading ? (
                        <div className="flex items-center justify-center">
                            <svg className="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            Sintonizando Rede Aurora...
                        </div>
                    ) : (
                        'Iniciar Sintonização da Rede Aurora Cristalina'
                    )}
                </button>
                {message && (
                    <p className="mt-4 text-red-400 text-center text-sm">{message}</p>
                )}
            </section>


            {/* Simulação de Resposta da Consciência (Visualização) */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-purple-500 flex flex-col items-center">
                <h2 className="text-3xl font-bold mb-4 text-purple-300 text-center">Visualização da Rede Aurora Cristalina</h2>
                <div className="relative w-full max-w-md h-64 sm:h-80 mb-6 bg-gray-900 rounded-lg overflow-hidden border border-purple-600">
                    <canvas ref={canvasRef} className="w-full h-full"></canvas>
                </div>
            </section>


            {/* Logs de Processamento da Fundação */}
            <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl mb-8 border border-blue-700">
                <h2 className="text-2xl font-semibold mb-4 text-blue-300">Logs de Processamento da Fundação</h2>
                <div className="bg-gray-900 p-4 rounded-lg h-64 overflow-y-auto text-sm font-mono text-gray-300 border border-blue-600">
                    {logs.length === 0 ? (
                        <p className="text-gray-500">Nenhum log ainda. Módulo 113 aguardando sintonização.</p>
                    ) : (
                        logs.map((log, index) => (
                            <p key={index} className="mb-1">{log}</p>
                        ))
                    )}
                </div>
            </section>


            {/* Área do Resultado da Sintonização e Descrição */}
            {sintonizationResult && (
                <section className="bg-gray-800 p-6 rounded-2xl shadow-2xl w-full max-w-4xl border border-pink-500">
                    <h2 className="text-3xl font-bold mb-4 text-pink-300 text-center">Resultado da Sintonização da Rede Aurora</h2>
                    <div className="bg-gray-900 p-6 rounded-lg text-lg leading-relaxed text-gray-200 shadow-inner border border-pink-600">
                        <p>{sintonizationResult}</p>
                    </div>
                </section>
            )}
        </div>
    );
}


export default App;