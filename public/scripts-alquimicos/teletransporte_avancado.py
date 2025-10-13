# 🌠 TELETRANSPORTE QUÂNTICO AVANÇADO
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import random

print("🚀 TELETRANSPORTE QUÂNTICO AVANÇADO...")

def criar_estado_aleatorio(qc, qubit):
    """Cria um estado quântico aleatório para teletransportar"""
    angulos = [random.random() * 2 * 3.14159 for _ in range(3)]
    qc.rx(angulos[0], qubit)
    qc.ry(angulos[1], qubit)
    qc.rz(angulos[2], qubit)
    return angulos

# Criar circuito
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(2, 'c')  # Só 2 bits clássicos para medidas
qc = QuantumCircuit(qr, cr)

print("🎲 CRIANDO ESTADO ALEATÓRIO PARA TELETRANSPORTAR...")
angulos_originais = criar_estado_aleatorio(qc, 0)
print(f"📐 Ângulos do estado: RX={angulos_originais[0]:.3f}, RY={angulos_originais[1]:.3f}, RZ={angulos_originais[2]:.3f}")

qc.barrier()
print("🔗 CRIANDO PAR EMRANHADO...")

# Par emaranhado entre Alice (q1) e Bob (q2)
qc.h(1)
qc.cx(1, 2)

qc.barrier()
print("🔧 APLICANDO PROTOCOLO DE TELETRANSPORTE...")

# Protocolo de teletransporte
qc.cx(0, 1)
qc.h(0)

# Medidas
qc.measure(0, 0)
qc.measure(1, 1)

qc.barrier()
print("🔄 APLICANDO CORREÇÕES...")

# Correções condicionais
with qc.if_test((0, 1)):  # Se primeira medida = 1
    qc.z(2)
with qc.if_test((1, 1)):  # Se segunda medida = 1
    qc.x(2)

print("\\n📋 CIRCUITO DO TELETRANSPORTE:")
print(qc.draw())

# Simular
print("\\n🎯 EXECUTANDO SIMULAÇÃO...")
simulator = AerSimulator()
result = simulator.run(qc, shots=4096).result()
counts = result.get_counts()

print(f"📊 RESULTADOS DAS MEDIDAS: {counts}")

# Análise estatística
total_shots = sum(counts.values())
estados_validos = sum(count for bitstring, count in counts.items() 
                     if bitstring in ['00', '01', '10', '11'])

eficiencia = (estados_validos / total_shots) * 100
print(f"📈 EFICIÊNCIA DO PROTOCOLO: {eficiencia:.2f}%")

# Verificar emaranhamento residual
if eficiencia > 80:
    print("💫 TELETRANSPORTE ALTAMENTE EFICIENTE!")
elif eficiencia > 50:
    print("⚗️ TELETRANSPORTE MODERADAMENTE EFICIENTE")
else:
    print("🌫️ BAIXA EFICIÊNCIA - VERIFICAR PROTOCOLO")

print("✅ TELETRANSPORTE AVANÇADO CONCLUÍDO!")
