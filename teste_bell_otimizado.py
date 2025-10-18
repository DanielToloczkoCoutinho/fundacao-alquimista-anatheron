# 🔔 TESTE DA DESIGUALDADE DE BELL
from qiskit import # 🔮 CIRCUITO OTIMIZADO PARA IBM QUANTUM
QuantumCircuit
from qiskit_aer import AerSimulator
import math

print("🔔 INICIANDO TESTE DE BELL...")

def criar_circuito_medida(angulo_a, angulo_b):
    qc = # 🔮 CIRCUITO OTIMIZADO PARA IBM QUANTUM
QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    
    # Rotacionar antes de medir
    qc.ry(angulo_a, 0)
    qc.ry(angulo_b, 1)
    
    qc.measure([0, 1], [0, 1])
    return qc

# Ângulos para teste
angulos = [(0, 0), (0, math.pi/4), (math.pi/4, 0), (math.pi/4, math.pi/4)]

simulator = AerSimulator()
resultados = []

for i, (ang_a, ang_b) in enumerate(angulos):
    qc = criar_circuito_medida(ang_a, ang_b)
    # 🌌 TRANSPILAÇÃO OTIMIZADA
circuito_otimizado = transpile(circuito, optimization_level=3)
result = simulator.run(qc, shots=512).result()
    counts = result.get_counts()
    
    # Calcular correlação
    mesmo = counts.get('00', 0) + counts.get('11', 0)
    total = sum(counts.values())
    correlacao = mesmo / total
    
    resultados.append(correlacao)
    print(f"🔧 Config {i+1}: Ângulos ({ang_a:.2f}, {ang_b:.2f}) → Correlação: {correlacao:.3f}")

# Calcular valor S de Bell
S = resultados[0] - resultados[1] + resultados[2] + resultados[3]
print(f"🎯 VALOR S DE BELL: {S:.3f}")

if S > 2:
    print("💫 VIOLAÇÃO DA DESIGUALDADE DE BELL CONFIRMADA!")
    print("   ↳ COMPORTAMENTO VERDADEIRAMENTE QUÂNTICO!")
else:
    print("⚗️ COMPORTAMENTO CLÁSSICO OBSERVADO")
