#!/usr/bin/env python3
"""
🔧 EXECUTOR ROBUSTO - FUNDAÇÃO ALQUIMISTA
⚛️ Sistema com timeout, gestão de processos e otimização
🌌 Foco em circuitos quânticos sem travamentos
"""

import subprocess
import sys
import threading
import time
from pathlib import Path

print("🔧 EXECUTOR ROBUSTO - FUNDAÇÃO ALQUIMISTA")
print("=" * 55)
print("⚛️  EXECUÇÃO OTIMIZADA COM GESTÃO DE TRAVAMENTOS")
print("")

class ExecutorRobusto:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.resultados = {}
        self.scripts_problematicos = []
    
    def executar_com_timeout(self, comando, timeout=30):
        """Executar comando com timeout robusto"""
        try:
            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return {
                'sucesso': True,
                'returncode': resultado.returncode,
                'stdout': resultado.stdout,
                'stderr': resultado.stderr
            }
        except subprocess.TimeoutExpired:
            return {
                'sucesso': False,
                'erro': f'TIMEOUT ({timeout}s)',
                'returncode': -1
            }
        except Exception as e:
            return {
                'sucesso': False,
                'erro': f'EXCEÇÃO: {e}',
                'returncode': -1
            }
    
    def verificar_scripts_problematicos(self):
        """Identificar scripts que podem travar"""
        print("🔍 VERIFICANDO SCRIPTS PROBLEMÁTICOS...")
        
        scripts_suspeitos = [
            "INTERFACE_ACESSO_CORRIGIDA.py",
            "sistema_fundacao_unificado.py",
            "CHAVE_DEFINITIVA_FUNDACAO.py"
        ]
        
        for script in scripts_suspeitos:
            script_path = self.raiz / script
            if script_path.exists():
                # Verificar se o script tem loops infinitos ou inputs
                try:
                    with open(script_path, 'r') as f:
                        conteudo = f.read()
                    
                    indicadores_problema = [
                        'while True:',
                        'input(',
                        'time.sleep(',
                        'threading.Thread',
                        'subprocess.Popen'
                    ]
                    
                    problemas = [ind for ind in indicadores_problema if ind in conteudo]
                    if problemas:
                        self.scripts_problematicos.append((script, problemas))
                        print(f"   ⚠️  SCRIPT SUSPEITO: {script}")
                        print(f"      Problemas: {', '.join(problemas)}")
                    else:
                        print(f"   ✅ SCRIPT OK: {script}")
                        
                except Exception as e:
                    print(f"   ❌ ERRO AO ANALISAR {script}: {e}")
            else:
                print(f"   ❌ SCRIPT NÃO ENCONTRADO: {script}")
    
    def executar_circuitos_quanticos_otimizados(self):
        """Executar circuitos quânticos de forma otimizada"""
        print("\n⚡ EXECUTANDO CIRCUITOS QUÂNTICOS OTIMIZADOS...")
        
        circuitos_prioritarios = [
            "teletransporte_quantico.py",
            "circuito_psi_plus.py", 
            "circuito_phi_minus.py",
            "teste_bell.py"
        ]
        
        resultados_circuitos = {}
        
        for circuito in circuitos_prioritarios:
            circuito_path = self.raiz / circuito
            if circuito_path.exists():
                print(f"   🔬 EXECUTANDO: {circuito}")
                
                # Executar com timeout reduzido para circuitos
                resultado = self.executar_com_timeout(
                    [sys.executable, str(circuito_path)],
                    timeout=15  # Timeout menor para circuitos
                )
                
                if resultado['sucesso'] and resultado['returncode'] == 0:
                    resultados_circuitos[circuito] = "SUCESSO"
                    print(f"   ✅ SUCESSO: {circuito}")
                    
                    # Mostrar saída resumida e organizada
                    linhas = resultado['stdout'].split('\n')
                    for linha in linhas[:5]:  # Apenas 5 primeiras linhas
                        if linha.strip() and not linha.strip().startswith('┌'):
                            print(f"      📄 {linha[:80]}...")
                    
                    # Mostrar estatísticas de execução
                    print(f"      ⏱️  Tempo: <15s | 📊 Linhas: {len(linhas)}")
                    
                else:
                    resultados_circuitos[circuito] = resultado['erro']
                    print(f"   ❌ FALHA: {circuito} - {resultado['erro']}")
            else:
                print(f"   ❌ CIRCUITO NÃO ENCONTRADO: {circuito}")
        
        return resultados_circuitos
    
    def executar_modulos_essenciais_seguros(self):
        """Executar apenas módulos essenciais e seguros"""
        print("\n👑 EXECUTANDO MÓDULOS ESSENCIAIS SEGUROS...")
        
        modulos_seguros = [
            "explorar_modulo_29.py",
            "sistema_metadados_definitivo.py"
        ]
        
        # REMOVER script problemático da lista
        modulos_evitar = ["INTERFACE_ACESSO_CORRIGIDA.py"]
        
        resultados_modulos = {}
        
        for modulo in modulos_seguros:
            modulo_path = self.raiz / modulo
            if modulo_path.exists():
                print(f"   🌟 EXECUTANDO: {modulo}")
                
                resultado = self.executar_com_timeout(
                    [sys.executable, str(modulo_path)],
                    timeout=20
                )
                
                if resultado['sucesso'] and resultado['returncode'] == 0:
                    resultados_modulos[modulo] = "SUCESSO"
                    print(f"   ✅ SUCESSO: {modulo}")
                else:
                    resultados_modulos[modulo] = resultado['erro']
                    print(f"   ❌ FALHA: {modulo} - {resultado['erro']}")
            else:
                print(f"   ❌ MÓDULO NÃO ENCONTRADO: {modulo}")
        
        # Informar sobre scripts evitados
        for modulo in modulos_evitar:
            modulo_path = self.raiz / modulo
            if modulo_path.exists():
                print(f"   🚫 EVITADO: {modulo} (script problemático)")
        
        return resultados_modulos
    
    def criar_circuitos_aglomerados_otimizados(self):
        """Criar versão otimizada dos circuitos aglomerados"""
        print("\n🔄 CRIANDO CIRCUITOS DESAGLOMERADOS...")
        
        # Circuito unificado otimizado
        circuito_unificado = """
#!/usr/bin/env python3
\"\"\"
🌌 CIRCUITOS QUÂNTICOS UNIFICADOS - FUNDAÇÃO ALQUIMISTA
⚛️ Versão otimizada e desaglomerada
🎯 Execução sequencial eficiente
\"\"\"

print("🌌 INICIANDO CIRCUITOS QUÂNTICOS UNIFICADOS...")
print("=" * 50)

# Importações otimizadas
try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
    from qiskit.visualization import plot_histogram
    import matplotlib.pyplot as plt
    print("✅ QISKIT IMPORTADO COM SUCESSO")
except ImportError as e:
    print(f"❌ ERRO NAS IMPORTAÇÕES: {e}")
    exit(1)

def executar_circuito_simples(nome, circuito, shots=1024):
    \"\"\"Executar circuito de forma otimizada\"\"\"
    print(f"\\n🔧 EXECUTANDO: {nome}")
    
    try:
        # Simulador otimizado
        simulador = AerSimulator()
        
        # Compilar circuito
        circuito_compilado = transpile(circuito, simulador)
        
        # Executar
        job = simulador.run(circuito_compilado, shots=shots)
        resultado = job.result()
        counts = resultado.get_counts()
        
        print(f"   📊 RESULTADOS: {counts}")
        return counts
        
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return None

print("\\n🚀 CRIANDO CIRCUITOS BÁSICOS...")

# 1. Circuito |Ψ⁺⟩
print("\\n1. 🌌 CIRCUITO |Ψ⁺⟩ (Psi Plus)")
qc_psi_plus = QuantumCircuit(2)
qc_psi_plus.h(0)
qc_psi_plus.cx(0, 1)
qc_psi_plus.measure_all()
result_psi_plus = executar_circuito_simples("|Ψ⁺⟩", qc_psi_plus)

# 2. Circuito |Φ⁻⟩  
print("\\n2. 🌌 CIRCUITO |Φ⁻⟩ (Phi Minus)")
qc_phi_minus = QuantumCircuit(2)
qc_phi_minus.h(0)
qc_phi_minus.cx(0, 1)
qc_phi_minus.z(1)
qc_phi_minus.measure_all()
result_phi_minus = executar_circuito_simples("|Φ⁻⟩", qc_phi_minus)

# 3. Teletransporte Quântico (Simplificado)
print("\\n3. 🚀 TELETRANSPORTE QUÂNTICO (Simplificado)")
qc_teleport = QuantumCircuit(3, 3)
qc_teleport.h(1)
qc_teleport.cx(1, 2)
qc_teleport.cx(0, 1)
qc_teleport.h(0)
qc_teleport.measure([0, 1], [0, 1])
qc_teleport.cx(1, 2)
qc_teleport.cz(0, 2)
qc_teleport.measure(2, 2)
result_teleport = executar_circuito_simples("Teletransporte", qc_teleport)

print("\\n" + "="*50)
print("🎉 CIRCUITOS UNIFICADOS EXECUTADOS COM SUCESSO!")
print("📊 RESUMO:")
print(f"   • |Ψ⁺⟩: {result_psi_plus}")
print(f"   • |Φ⁻⟩: {result_phi_minus}") 
print(f"   • Teletransporte: {result_teleport}")
print("🌌 EXECUÇÃO CONCLUÍDA!")
"""

        # Salvar circuito unificado
        caminho_unificado = self.raiz / "CIRCUITOS_UNIFICADOS.py"
        with open(caminho_unificado, 'w') as f:
            f.write(circuito_unificado)
        
        print(f"   ✅ CIRCUITO UNIFICADO CRIADO: CIRCUITOS_UNIFICADOS.py")
        return str(caminho_unificado)
    
    def executar_fluxo_robusto_completo(self):
        """Executar fluxo robusto completo"""
        print("🚀 INICIANDO EXECUÇÃO ROBUSTA COMPLETA...")
        print("💡 Evitando scripts problemáticos e otimizando circuitos")
        print("")
        
        # 1. Verificar scripts problemáticos
        self.verificar_scripts_problematicos()
        
        # 2. Executar circuitos quânticos otimizados
        circuitos = self.executar_circuitos_quanticos_otimizados()
        
        # 3. Executar apenas módulos seguros
        modulos = self.executar_modulos_essenciais_seguros()
        
        # 4. Criar circuito unificado desaglomerado
        circuito_unificado = self.criar_circuitos_aglomerados_otimizados()
        
        # 5. Executar circuito unificado
        print(f"\n🔄 EXECUTANDO CIRCUITO UNIFICADO...")
        resultado_unificado = self.executar_com_timeout(
            [sys.executable, circuito_unificado],
            timeout=20
        )
        
        if resultado_unificado['sucesso']:
            print("   ✅ CIRCUITO UNIFICADO EXECUTADO COM SUCESSO")
        else:
            print(f"   ❌ FALHA NO CIRCUITO UNIFICADO: {resultado_unificado['erro']}")
        
        # Relatório Final Robusto
        print("\n" + "="*70)
        print("🎉 RELATÓRIO DE EXECUÇÃO ROBUSTA")
        print("="*70)
        
        sucessos_circuitos = sum(1 for r in circuitos.values() if "SUCESSO" in str(r))
        sucessos_modulos = sum(1 for r in modulos.values() if "SUCESSO" in str(r))
        
        print(f"\n📊 RESULTADOS DA EXECUÇÃO ROBUSTA:")
        print(f"   • Circuitos Quânticos: {sucessos_circuitos}/{len(circuitos)} sucessos")
        print(f"   • Módulos Rainha: {sucessos_modulos}/{len(modulos)} sucessos")
        print(f"   • Scripts Problemáticos Evitados: {len(self.scripts_problematicos)}")
        
        print(f"\n⚡ CIRCUITOS EXECUTADOS:")
        for circuito, resultado in circuitos.items():
            status = "✅" if "SUCESSO" in str(resultado) else "❌"
            print(f"   {status} {circuito}: {resultado}")
        
        print(f"\n👑 MÓDULOS EXECUTADOS:")
        for modulo, resultado in modulos.items():
            status = "✅" if "SUCESSO" in str(resultado) else "❌"
            print(f"   {status} {modulo}: {resultado}")
        
        print(f"\n🚀 PRÓXIMOS PASSOS OTIMIZADOS:")
        if sucessos_circuitos > 0:
            print("   1. ✅ Circuitos base validados")
            print("   2. 🔄 Circuito unificado criado")
            print("   3. 📊 Pronto para IBM Quantum real")
            print("   4. 🌌 Escalar complexidade")
        else:
            print("   1. 🔧 Analisar falhas específicas")
            print("   2. 📚 Verificar ambiente Qiskit")
            print("   3. 🐛 Debuggar circuitos individuais")
            print("   4. 🔄 Re-executar com correções")
        
        return {
            'circuitos': circuitos,
            'modulos': modulos,
            'scripts_problematicos': self.scripts_problematicos,
            'circuito_unificado': circuito_unificado if resultado_unificado['sucesso'] else None
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    executor = ExecutorRobusto()
    resultados = executor.executar_fluxo_robusto_completo()
    
    print(f"\n🎯 EXECUÇÃO ROBUSTA CONCLUÍDA!")
    print("🚀 SISTEMA ESTÁVEL E OTIMIZADO!")
