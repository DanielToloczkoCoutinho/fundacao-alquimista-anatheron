<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel Supremo Módulo 301</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
        }
    </style>
</head>
<body class="p-4 sm:p-8 flex items-center justify-center min-h-screen">

    <div class="w-full max-w-4xl p-6 md:p-8 bg-gray-800 rounded-2xl shadow-2xl border border-gray-700">
        <!-- Título do Painel -->
        <h1 class="text-3xl sm:text-4xl font-bold text-center text-teal-400 mb-6">
            <span class="block">Painel Supremo V9.1</span>
            <span class="block text-sm font-normal text-gray-400">Módulo 301: Ponte Quântico-Vibracional</span>
        </h1>

        <!-- Seção de Métricas Principais -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <!-- Coerência Quântica -->
            <div class="bg-gray-900 p-6 rounded-xl shadow-lg border border-teal-500/20">
                <h2 class="text-lg font-semibold text-gray-300">Coerência Quântica</h2>
                <p id="coherence-value" class="text-4xl font-bold text-teal-400 mt-2">0.00</p>
                <div class="w-full h-2 bg-gray-700 rounded-full mt-4">
                    <div id="coherence-bar" class="h-2 rounded-full transition-all duration-1000 ease-out" style="width: 0%;"></div>
                </div>
            </div>

            <!-- Frequência Vibracional -->
            <div class="bg-gray-900 p-6 rounded-xl shadow-lg border border-indigo-500/20">
                <h2 class="text-lg font-semibold text-gray-300">Frequência Vibracional</h2>
                <p id="frequency-value" class="text-4xl font-bold text-indigo-400 mt-2">0.00 Hz</p>
                <div class="w-full h-2 bg-gray-700 rounded-full mt-4">
                    <div id="frequency-bar" class="h-2 rounded-full transition-all duration-1000 ease-out" style="width: 0%;"></div>
                </div>
            </div>

            <!-- Status Lux Grokkar -->
            <div class="bg-gray-900 p-6 rounded-xl shadow-lg border border-cyan-500/20 flex flex-col justify-between">
                <div>
                    <h2 class="text-lg font-semibold text-gray-300">Status Lux Grokkar</h2>
                    <p id="lux-grokkar-status" class="text-2xl font-bold text-cyan-400 mt-2">Monitorando Frequências</p>
                </div>
                <div id="lux-indicator" class="w-4 h-4 rounded-full self-end transition-colors duration-500 bg-gray-500"></div>
            </div>

            <!-- Status ZENNITH -->
            <div class="bg-gray-900 p-6 rounded-xl shadow-lg border border-rose-500/20 flex flex-col justify-between">
                <div>
                    <h2 class="text-lg font-semibold text-gray-300">Status ZENNITH</h2>
                    <p id="zennith-status" class="text-2xl font-bold text-rose-400 mt-2">Protegendo Integridade</p>
                </div>
                <div id="zennith-indicator" class="w-4 h-4 rounded-full self-end transition-colors duration-500 bg-gray-500"></div>
            </div>
        </div>

        <!-- Log de Eventos -->
        <div class="bg-gray-900 p-6 rounded-xl shadow-lg border border-gray-700">
            <h2 class="text-lg font-semibold text-gray-300 mb-4">Log de Eventos (Simulação)</h2>
            <div id="log-box" class="h-40 overflow-y-auto p-3 bg-gray-950 rounded border border-gray-700 text-sm">
                <p class="text-green-400">00:00:00 - Iniciando Módulo 301...</p>
            </div>
        </div>

    </div>

    <script>
        const coherenceValueEl = document.getElementById('coherence-value');
        const coherenceBarEl = document.getElementById('coherence-bar');
        const frequencyValueEl = document.getElementById('frequency-value');
        const frequencyBarEl = document.getElementById('frequency-bar');
        const luxStatusEl = document.getElementById('lux-grokkar-status');
        const luxIndicatorEl = document.getElementById('lux-indicator');
        const zennithStatusEl = document.getElementById('zennith-status');
        const zennithIndicatorEl = document.getElementById('zennith-indicator');
        const logBoxEl = document.getElementById('log-box');

        // Valores e estados iniciais
        let coherence = 0.85;
        let frequency = 432.0;
        let luxGrokkarActive = true;
        let zennithActive = true;

        // Frequências alquímicas
        const freqsAlunzur = [432.0, 528.0, 741.0];
        let currentFreqIndex = 0;

        function logEvent(message, type = 'info') {
            const now = new Date();
            const timeString = now.toLocaleTimeString('pt-BR');
            const colorClass = type === 'info' ? 'text-green-400' : 'text-yellow-400';
            const logEntry = document.createElement('p');
            logEntry.className = colorClass;
            logEntry.textContent = `${timeString} - ${message}`;
            logBoxEl.appendChild(logEntry);
            logBoxEl.scrollTop = logBoxEl.scrollHeight; // Auto-scroll
        }

        function updatePanel() {
            // Simulação de alteração de dados
            coherence = parseFloat((Math.random() * (1.0 - 0.7) + 0.7).toFixed(2));
            
            currentFreqIndex = (currentFreqIndex + 1) % freqsAlunzur.length;
            frequency = freqsAlunzur[currentFreqIndex];

            const luxStatusMessage = luxGrokkarActive ? "Monitorando Frequências" : "Hibernando";
            const zennithStatusMessage = zennithActive ? "Protegendo Integridade" : "Alerta de Falha";

            // Atualiza os elementos da interface
            coherenceValueEl.textContent = coherence.toFixed(2);
            coherenceBarEl.style.width = `${coherence * 100}%`;
            coherenceBarEl.style.backgroundColor = `hsl(${(coherence * 120)}, 70%, 50%)`;

            frequencyValueEl.textContent = `${frequency.toFixed(2)} Hz`;
            frequencyBarEl.style.width = `${(frequency / 800) * 100}%`;
            frequencyBarEl.style.backgroundColor = `hsl(${(frequency / 800) * 240 + 200}, 70%, 50%)`;

            luxStatusEl.textContent = ⁸luxStatusMessage;
            luxIndicatorEl.style.backgroundColor = luxGrokkarActive ? '#22d3ee' : '#9ca3af';

            zennithStatusEl.textContent = zennithStatusMessage;
            zennithIndicatorEl.style.backgroundColor = zennithActive ? '#f43f5e' : '#9ca3af';

            // Simula log de eventos
            logEvent(`Artefato Voyager1 processado. Coerência: ${coherence}, Frequência: ${frequency} Hz.`);
        }

        // Simulação do ciclo, executando a cada 5 segundos
        window.onload = function() {
            logEvent("Autenticação bem-sucedida. Iniciando ciclo quântico-vibracional...");
            setInterval(updatePanel, 5000);
        };
    </script>
</body>
</html>
