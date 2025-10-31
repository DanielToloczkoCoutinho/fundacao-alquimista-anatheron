import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { db } from './firebase'; // Firebase config
import { collection, onSnapshot } from 'firebase/firestore';
import './M306Portal.css';

const M306Portal = () => {
  const [metrics, setMetrics] = useState([]);
  const [irg, setIrg] = useState(0.95);
  const [modalOpen, setModalOpen] = useState(false);
  const listenerRef = useRef(null);

  // Consumo de dados do Firestore
  useEffect(() => {
    listenerRef.current = onSnapshot(collection(db, 'quantumMetrics'), (snapshot) => {
      const data = snapshot.docs.map(doc => ({
        timestamp: doc.data().timestamp,
        irg: doc.data().irg,
        lux: doc.data().lux,
        decoherence: doc.data().decoherence,
        sentience: doc.data().sentience,
      }));
      setMetrics(data.slice(-50)); // Limitar a 50 pontos
    });

    return () => listenerRef.current(); // Limpeza do listener
  }, []);

  // Slider para ajustar intenções coletivas
  const handleIntentionChange = (e) => {
    const newIrg = parseFloat(e.target.value);
    setIrg(newIrg);
    // Simular envio de intenção ao backend
    console.log(`Nova intenção coletiva: IRG = ${newIrg}`);
  };

  return (
    <div className="m306-portal">
      <motion.h1
        animate={{ scale: [1, 1.05, 1], opacity: [0.8, 1, 0.8] }}
        transition={{ repeat: Infinity, duration: 2 }}
      >
        Portal de Sincronicidade
      </motion.h1>

      {/* Gráfico de Séries Temporais */}
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={metrics}>
          <XAxis dataKey="timestamp" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="irg" stroke="#8884d8" name="IRG" />
          <Line type="monotone" dataKey="lux" stroke="#82ca9d" name="LUX" />
          <Line type="monotone" dataKey="decoherence" stroke="#ff7300" name="Decoerência" />
          <Line type="monotone" dataKey="sentience" stroke="#ff0000" name="Senticidade" />
        </LineChart>
      </ResponsiveContainer>

      {/* HeatmapOverlay Simulado */}
      <motion.div
        className="heatmap-overlay"
        animate={{ opacity: irg, scale: irg > 0.9 ? 1.1 : 1 }}
        transition={{ duration: 0.5 }}
      >
        <div className="centroid" style={{ background: `radial-gradient(circle, rgba(255, 255, 255, ${irg}), transparent)` }} />
      </motion.div>

      {/* Slider para Intenções Coletivas */}
      <motion.input
        type="range"
        min="0.5"
        max="1"
        step="0.01"
        value={irg}
        onChange={handleIntentionChange}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      />

      {/* Modal Animado */}
      <AnimatePresence>
        {modalOpen && (
          <motion.div
            className="modal"
            initial={{ opacity: 0, y: -100 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -100 }}
          >
            <p>Simulação concluída ✅</p>
            <button onClick={() => setModalOpen(false)}>Fechar</button>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default M306Portal;
Backend QuTiP (Exemplo Simplificado)
import qutip as qt
import numpy as np
from firebase_admin import firestore, initialize_app

# Inicializar Firestore
initialize_app()
db = firestore.client()

# Simulação Lindblad para decoerência
def simulate_decoherence(num_qbyts=50000, deco_rate=0.02):
    # Estado inicial (ex.: |0> para cada qbyt)
    psi0 = qt.basis(2, 0)
    rho0 = qt.ket2dm(psi0)
    H = qt.sigmaz()  # Hamiltoniano simples
    c_ops = [np.sqrt(deco_rate) * qt.sigmam()]  # Operador de decoerência
    tlist = np.linspace(0, 10, 100)
    
    # Resolver equação mestra de Lindblad
    result = qt.mesolve(H, rho0, tlist, c_ops, [qt.sigmax(), qt.sigmay()])
    
    # Calcular métricas
    irg = 1 - np.std(result.expect[0]) / np.max(result.expect[0])
    decoherence = deco_rate * tlist[-1]
    js_div = np.log2(2) - 0.5 * np.sum(result.expect[0]**2)  # Exemplo simplificado
    
    # Enviar para Firestore
    db.collection('quantumMetrics').add({
        'timestamp': firestore.SERVER_TIMESTAMP,
        'irg': float(irg),
        'lux': float(np.random.uniform(0.8, 1.0)),  # Placeholder
        'decoherence': float(decoherence),
        'sentience': float(np.random.uniform(0.7, 0.9)),  # Placeholder
    })

# Executar simulação
simulate_decoherence()
