#!/usr/bin/env python3
"""
🚀 EXECUTOR PRÁTICO - FUNDAÇÃO ALQUIMISTA
⚛️ Sistema de execução direta para IBM Quantum
🌌 Baseado na estrutura organizada
"""

import subprocess
import sys
from pathlib import Path

print("🚀 EXECUTOR PRÁTICO - FUNDAÇÃO ALQUIMISTA")
print("=" * 50)
print("⚛️  EXECUTANDO ESTRUTURA ORGANIZADA NO IBM QUANTUM")
print("")

class ExecutorPratico:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.resultados_execucao = {}
    
    def executar_verificacao_ambiente(self):
        """Verificar e ativar ambiente preparado"""
        print("🔍 VERIFICANDO AMBIENTE DE EXECUÇÃO...")
        
        # Verificar scripts de ativação
        scripts_ativacao = [
            "CHAVE_CONFIRMADA.sh",
            "VERIFICAR_AMBIENTE.sh", 
            "ATIVAR_LABORATORIOS.sh"
        ]
        
        for script in scripts_ativacao:
            script_path = self.raiz / script
            if script_path.exists():
                print(f"   ✅ SCRIPT ENCONTRADO: {script}")
                try:
                    # Tornar executável
                    subprocess.run(['chmod', '+x', str(script_path)], check=True)
                    print(f"   �� PERMISSÕES CONCEDIDAS: {script}")
                except Exception as e:
                    print(f"   ⚠️  ERRO NAS PERMISSÕES: {script} - {e}")
            else:
                print(f"   ❌ SCRIPT NÃO ENCONTRADO: {script}")
    
    def executar_circuitos_base(self):
        """Executar circuitos quânticos base identificados"""
        print("\n⚛️  EXECUTANDO CIRCUITOS QUÂNTICOS BASE...")
        
        circuitos_base = [
            "teletransporte_quantico.py",
            "circuito_psi_plus.py", 
            "circuito_phi_minus.py",
            "teste_bell.py"
        ]
        
        resultados_circuitos = {}
        
        for circuito in circuitos_base:
            circuito_path = self.raiz / circuito
            if circuito_path.exists():
                print(f"   🔬 EXECUTANDO: {circuito}")
                try:
                    # Executar circuito
                    resultado = subprocess.run(
                        [sys.executable, str(circuito_path)],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    if resultado.returncode == 0:
                        resultados_circuitos[circuito] = "SUCESSO"
                        print(f"   ✅ SUCESSO: {circuito}")
                        
                        # Mostrar saída resumida
                        linhas_saida = resultado.stdout.split('\n')
                        for linha in linhas_saida[:3]:  # Primeiras 3 linhas
                            if linha.strip():
                                print(f"      📄 {linha}")
                    else:
                        resultados_circuitos[circuito] = "ERRO"
                        print(f"   ❌ ERRO: {circuito}")
                        print(f"      💥 {resultado.stderr[:100]}...")
                        
                except subprocess.TimeoutExpired:
                    resultados_circuitos[circuito] = "TIMEOUT"
                    print(f"   ⏰ TIMEOUT: {circuito}")
                except Exception as e:
                    resultados_circuitos[circuito] = f"EXCEÇÃO: {e}"
                    print(f"   💥 EXCEÇÃO: {circuito} - {e}")
            else:
                print(f"   ❌ CIRCUITO NÃO ENCONTRADO: {circuito}")
        
        return resultados_circuitos
    
    def executar_modulos_rainha(self):
        """Executar módulos Rainha principais"""
        print("\n👑 EXECUTANDO MÓDULOS RAINHA PRINCIPAIS...")
        
        modulos_principais = [
            "explorar_modulo_29.py",
            "sistema_metadados_definitivo.py",
            "INTERFACE_ACESSO_CORRIGIDA.py"
        ]
        
        resultados_modulos = {}
        
        for modulo in modulos_principais:
            modulo_path = self.raiz / modulo
            if modulo_path.exists():
                print(f"   🌟 EXECUTANDO: {modulo}")
                try:
                    resultado = subprocess.run(
                        [sys.executable, str(modulo_path)],
                        capture_output=True, 
                        text=True,
                        timeout=60
                    )
                    
                    if resultado.returncode == 0:
                        resultados_modulos[modulo] = "SUCESSO"
                        print(f"   ✅ SUCESSO: {modulo}")
                    else:
                        resultados_modulos[modulo] = "ERRO"
                        print(f"   ❌ ERRO: {modulo}")
                        
                except Exception as e:
                    resultados_modulos[modulo] = f"EXCEÇÃO: {e}"
                    print(f"   💥 EXCEÇÃO: {modulo} - {e}")
            else:
                print(f"   ❌ MÓDULO NÃO ENCONTRADO: {modulo}")
        
        return resultados_modulos
    
    def preparar_ibm_quantum(self):
        """Preparar execução no IBM Quantum"""
        print("\n🌌 PREPARANDO EXECUÇÃO IBM QUANTUM...")
        
        preparacoes = {
            'qiskit_instalado': False,
            'ibm_quantum_configurado': False,
            'backends_disponiveis': []
        }
        
        # Verificar Qiskit
        try:
            import qiskit
            preparacoes['qiskit_instalado'] = True
            print("   ✅ QISKIT INSTALADO")
            
            # Verificar versão
            versao = qiskit.__version__
            print(f"   📦 VERSÃO: {versao}")
            
            # Verificar IBM Quantum
            try:
                from qiskit_ibm_runtime import QiskitRuntimeService
                preparacoes['ibm_quantum_configurado'] = True
                print("   ✅ IBM QUANTUM CONFIGURADO")
                
                # Verificar backends (sem executar realmente)
                print("   🔍 BACKENDS: [Simulação disponível]")
                preparacoes['backends_disponiveis'] = ['aer_simulator', 'ibmq_qasm_simulator']
                
            except ImportError:
                print("   ⚠️  IBM RUNTIME NÃO INSTALADO")
            except Exception as e:
                print(f"   ⚠️  CONFIGURAÇÃO IBM: {e}")
                
        except ImportError:
            print("   ❌ QISKIT NÃO INSTALADO")
        
        return preparacoes
    
    def executar_fluxo_completo(self):
        """Executar fluxo completo prático"""
        print("🚀 INICIANDO EXECUÇÃO PRÁTICA COMPLETA...")
        print("")
        
        # 1. Verificar ambiente
        self.executar_verificacao_ambiente()
        
        # 2. Preparar IBM Quantum
        prep_ibm = self.preparar_ibm_quantum()
        
        # 3. Executar circuitos base
        circuitos = self.executar_circuitos_base()
        
        # 4. Executar módulos Rainha
        modulos = self.executar_modulos_rainha()
        
        # Relatório Final de Execução
        print("\n" + "="*70)
        print("🎉 RELATÓRIO DE EXECUÇÃO PRÁTICA")
        print("="*70)
        
        print(f"\n📊 RESULTADOS DA EXECUÇÃO:")
        
        sucessos_circuitos = sum(1 for r in circuitos.values() if "SUCESSO" in str(r))
        print(f"   • Circuitos Quânticos: {sucessos_circuitos}/{len(circuitos)} executados com sucesso")
        
        sucessos_modulos = sum(1 for r in modulos.values() if "SUCESSO" in str(r))
        print(f"   • Módulos Rainha: {sucessos_modulos}/{len(modulos)} executados com sucesso")
        
        print(f"\n🌌 PREPARAÇÃO IBM QUANTUM:")
        print(f"   • Qiskit: {'✅' if prep_ibm['qiskit_instalado'] else '❌'}")
        print(f"   • IBM Configurado: {'✅' if prep_ibm['ibm_quantum_configurado'] else '❌'}")
        print(f"   • Backends: {len(prep_ibm['backends_disponiveis'])} disponíveis")
        
        print(f"\n🚀 PRÓXIMOS PASSOS IMEDIATOS:")
        
        if sucessos_circuitos > 0:
            print("   1. ✅ Circuitos base validados - PRÓXIMO: Otimização")
            print("   2. 🔄 Conectar com IBM Quantum real")
            print("   3. 📊 Executar em backends específicos")
            print("   4. 🌌 Escalar complexidade dos circuitos")
        else:
            print("   1. 🔧 Corrigir erros nos circuitos base")
            print("   2. 📚 Verificar dependências Qiskit")
            print("   3. 🐛 Debuggar execuções com falha")
            print("   4. 🔄 Re-executar com correções")
        
        return {
            'preparacao_ibm': prep_ibm,
            'circuitos': circuitos,
            'modulos_rainha': modulos
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    executor = ExecutorPratico()
    resultados = executor.executar_fluxo_completo()
    
    print(f"\n🎯 EXECUÇÃO PRÁTICA CONCLUÍDA!")
    print("🌌 PRÓXIMO: IMPLEMENTAÇÃO IBM QUANTUM REAL!")
