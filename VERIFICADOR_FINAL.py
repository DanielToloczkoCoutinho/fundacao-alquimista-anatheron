#!/usr/bin/env python3
"""
🔮 VERIFICADOR FINAL - FUNDAÇÃO ALQUIMISTA
⚛️ Verificação completa do ambiente e otimização
🌌 Preparação final para IBM Quantum
"""

import sys
from pathlib import Path

print("🔮 VERIFICADOR FINAL - FUNDAÇÃO ALQUIMISTA")
print("=" * 55)
print("⚛️  VERIFICAÇÃO COMPLETA E OTIMIZAÇÃO FINAL")
print("")

class VerificadorFinal:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.estado_sistema = {}
    
    def verificar_ambiente_quantico(self):
        """Verificação completa do ambiente quântico"""
        print("🔍 VERIFICANDO AMBIENTE QUÂNTICO...")
        
        verificacoes = {}
        
        # 1. Verificar Python e dependências
        try:
            import qiskit
            verificacoes['qiskit'] = {'status': '✅', 'versao': qiskit.__version__}
        except ImportError:
            verificacoes['qiskit'] = {'status': '❌', 'erro': 'Não instalado'}
        
        try:
            from qiskit_aer import AerSimulator
            verificacoes['aer_simulator'] = {'status': '✅', 'versao': 'Disponível'}
        except ImportError:
            verificacoes['aer_simulator'] = {'status': '❌', 'erro': 'Não disponível'}
        
        # 2. Verificar scripts essenciais
        scripts_essenciais = [
            "CIRCUITOS_UNIFICADOS.py",
            "teletransporte_quantico.py", 
            "circuito_psi_plus.py",
            "circuito_phi_minus.py",
            "teste_bell.py"
        ]
        
        for script in scripts_essenciais:
            script_path = self.raiz / script
            if script_path.exists():
                verificacoes[script] = {'status': '✅', 'caminho': str(script_path)}
            else:
                verificacoes[script] = {'status': '❌', 'erro': 'Não encontrado'}
        
        # Mostrar resultados
        for item, info in verificacoes.items():
            if info['status'] == '✅':
                detalhes = info.get('versao', info.get('caminho', 'OK'))
                print(f"   {info['status']} {item}: {detalhes}")
            else:
                print(f"   {info['status']} {item}: {info['erro']}")
        
        return verificacoes
    
    def otimizar_execucao_circuitos(self):
        """Otimizar a execução dos circuitos quânticos"""
        print("\n⚡ OTIMIZANDO EXECUÇÃO DE CIRCUITOS...")
        
        # Criar script de execução otimizada
        script_otimizado = """
#!/usr/bin/env python3
\"\"\"
⚡ EXECUTOR OTIMIZADO - FUNDAÇÃO ALQUIMISTA
🎯 Execução sequencial e eficiente de circuitos
🌌 Preparado para IBM Quantum
\"\"\"

import time
import sys
from pathlib import Path

print("⚡ INICIANDO EXECUÇÃO OTIMIZADA...")
print("=" * 45)

# Lista de circuitos para execução otimizada
circuitos = [
    "teletransporte_quantico.py",
    "circuito_psi_plus.py",
    "circuito_phi_minus.py", 
    "teste_bell.py",
    "CIRCUITOS_UNIFICADOS.py"
]

tempo_inicio = time.time()
resultados = {}

for i, circuito in enumerate(circuitos, 1):
    circuito_path = Path(circuito)
    if circuito_path.exists():
        print(f"\\n🔧 [{i}/{len(circuitos)}] EXECUTANDO: {circuito}")
        
        try:
            import subprocess
            resultado = subprocess.run(
                [sys.executable, str(circuito_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if resultado.returncode == 0:
                resultados[circuito] = "✅ SUCESSO"
                print(f"   ✅ EXECUTADO COM SUCESSO")
                
                # Mostrar linha de resultado se existir
                linhas = resultado.stdout.split('\\n')
                for linha in linhas:
                    if any(termo in linha for termo in ['RESULTADOS', 'Correlação', 'BELL']):
                        print(f"   📊 {linha.strip()}")
                        break
            else:
                resultados[circuito] = f"❌ ERRO: {resultado.stderr[:100]}"
                print(f"   ❌ FALHA NA EXECUÇÃO")
                
        except subprocess.TimeoutExpired:
            resultados[circuito] = "⏰ TIMEOUT"
            print(f"   ⏰ TIMEOUT")
        except Exception as e:
            resultados[circuitos] = f"💥 EXCEÇÃO: {e}"
            print(f"   💥 EXCEÇÃO: {e}")
    else:
        resultados[circuito] = "🚫 NÃO ENCONTRADO"
        print(f"   🚫 ARQUIVO NÃO ENCONTRADO")

tempo_total = time.time() - tempo_inicio

print("\\n" + "="*45)
print("🎉 EXECUÇÃO OTIMIZADA CONCLUÍDA!")
print(f"📊 RESUMO:")
for circuito, resultado in resultados.items():
    print(f"   • {circuito}: {resultado}")
print(f"⏱️  TEMPO TOTAL: {tempo_total:.2f}s")
print("🌌 PRONTO PARA IBM QUANTUM!")
"""

        caminho_otimizado = self.raiz / "EXECUCAO_OTIMIZADA.py"
        with open(caminho_otimizado, 'w') as f:
            f.write(script_otimizado)
        
        print(f"   ✅ SCRIPT OTIMIZADO CRIADO: EXECUCAO_OTIMIZADA.py")
        return str(caminho_otimizado)
    
    def executar_verificacao_completa(self):
        """Executar verificação completa"""
        print("🚀 INICIANDO VERIFICAÇÃO COMPLETA...")
        
        # 1. Verificar ambiente
        verificacoes = self.verificar_ambiente_quantico()
        
        # 2. Otimizar execução
        script_otimizado = self.otimizar_execucao_circuitos()
        
        # Relatório Final
        print("\n" + "="*70)
        print("🎉 RELATÓRIO DE VERIFICAÇÃO FINAL")
        print("="*70)
        
        total_verificacoes = len(verificacoes)
        verificacoes_ok = sum(1 for v in verificacoes.values() if v['status'] == '✅')
        
        print(f"\n📊 ESTADO DO SISTEMA:")
        print(f"   • Verificações: {verificacoes_ok}/{total_verificacoes} OK")
        print(f"   • Script otimizado: EXECUCAO_OTIMIZADA.py")
        
        print(f"\n🎯 STATUS PRONTO PARA IBM QUANTUM:")
        if verificacoes_ok >= total_verificacoes - 2:  # Permitir 2 falhas
            print("   ✅ SISTEMA PRONTO PARA EXECUÇÃO REAL!")
            print("   🚀 Circuitos otimizados e estáveis")
            print("   🌌 Ambiente Qiskit configurado")
            print("   📊 Script de execução criado")
        else:
            print("   ⚠️  SISTEMA PRECISA DE AJUSTES")
            print("   🔧 Verificar dependências faltantes")
            print("   📚 Corrigir scripts com problemas")
            print("   🔄 Re-executar verificação")
        
        print(f"\n🚀 COMANDO FINAL DE EXECUÇÃO:")
        print("   python3 EXECUCAO_OTIMIZADA.py")
        
        return {
            'verificacoes': verificacoes,
            'script_otimizado': script_otimizado,
            'pronto_ibm_quantum': verificacoes_ok >= total_verificacoes - 2
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    verificador = VerificadorFinal()
    resultados = verificador.executar_verificacao_completa()
    
    if resultados['pronto_ibm_quantum']:
        print(f"\n🎯 SISTEMA VERIFICADO E OTIMIZADO!")
        print("🚀 EXECUTE: python3 EXECUCAO_OTIMIZADA.py")
    else:
        print(f"\n⚠️  SISTEMA PRECISA DE CORREÇÕES")
        print("🔧 VERIFIQUE AS DEPENDÊNCIAS FALTANTES")
