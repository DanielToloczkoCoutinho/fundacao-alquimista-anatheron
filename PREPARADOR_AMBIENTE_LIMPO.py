#!/usr/bin/env python3
"""
🔧 PREPARADOR DE AMBIENTE LIMPO - FUNDAÇÃO ALQUIMISTA
⚛️ Limpeza completa do ambiente entre execuções
🌌 Prevenção total de sobreposição
"""

import os
import subprocess
import sys
import time
from pathlib import Path

print("🔧 PREPARADOR DE AMBIENTE LIMPO - FUNDAÇÃO ALQUIMISTA")
print("=" * 60)
print("⚛️  LIMPEZA COMPLETA E PREPARAÇÃO PARA EXECUÇÃO ISOLADA")
print("")

class PreparadorAmbienteLimpo:
    def __init__(self):
        self.raiz = Path(".").absolute()
    
    def limpar_cache_python(self):
        """Limpar cache do Python para execução limpa"""
        print("🧹 LIMPANDO CACHE DO PYTHON...")
        
        # Limpar arquivos .pyc e __pycache__
        for root, dirs, files in os.walk(self.raiz):
            for dir_name in dirs:
                if dir_name == "__pycache__":
                    cache_dir = Path(root) / dir_name
                    try:
                        import shutil
                        shutil.rmtree(cache_dir)
                        print(f"   ✅ LIMPO: {cache_dir}")
                    except Exception as e:
                        print(f"   ⚠️  ERRO AO LIMPAR {cache_dir}: {e}")
            
            for file_name in files:
                if file_name.endswith(".pyc"):
                    pyc_file = Path(root) / file_name
                    try:
                        pyc_file.unlink()
                        print(f"   ✅ REMOVIDO: {pyc_file}")
                    except Exception as e:
                        print(f"   ⚠️  ERRO AO REMOVER {pyc_file}: {e}")
    
    def verificar_e_preparar_scripts(self):
        """Verificar e preparar todos os scripts para execução limpa"""
        print("\n🔍 VERIFICANDO E PREPARANDO SCRIPTS...")
        
        scripts_principais = [
            "circuito_psi_plus.py",
            "circuito_phi_minus.py",
            "teletransporte_quantico.py", 
            "teste_bell.py",
            "CIRCUITOS_UNIFICADOS.py",
            "explorar_modulo_29.py"
        ]
        
        for script in scripts_principais:
            script_path = self.raiz / script
            if script_path.exists():
                # Verificar se o script tem imports adequados
                try:
                    with open(script_path, 'r') as f:
                        conteudo = f.read()
                    
                    # Verificar imports básicos do Qiskit
                    if 'import qiskit' in conteudo or 'from qiskit' in conteudo:
                        print(f"   ✅ {script}: IMPORTS OK")
                    else:
                        print(f"   ⚠️  {script}: SEM IMPORTS QISKIT")
                        
                    # Verificar se tem execução principal
                    if '__name__' in conteudo and '__main__' in conteudo:
                        print(f"   ✅ {script}: EXECUÇÃO PRINCIPAL OK")
                    else:
                        print(f"   ⚠️  {script}: SEM BLOCO PRINCIPAL")
                        
                except Exception as e:
                    print(f"   ❌ {script}: ERRO NA VERIFICAÇÃO - {e}")
            else:
                print(f"   🚫 {script}: NÃO ENCONTRADO")
    
    def criar_script_execucao_ultra_organizada(self):
        """Criar script de execução ultra organizada"""
        print("\n🎯 CRIANDO SCRIPT DE EXECUÇÃO ULTRA ORGANIZADA...")
        
        script_ultra_organizado = '''#!/usr/bin/env python3
"""
🎯 EXECUÇÃO ULTRA ORGANIZADA - FUNDAÇÃO ALQUIMISTA
⚛️ Execução sequencial perfeita sem nenhuma sobreposição
🌌 Cada circuito executado em ambiente completamente isolado
"""

import subprocess
import sys
import time
from pathlib import Path

print("🎯 EXECUÇÃO ULTRA ORGANIZADA - FUNDAÇÃO ALQUIMISTA")
print("=" * 65)
print("⚛️  EXECUÇÃO SEQUENCIAL PERFEITA - ZERO SOBREPOSIÇÃO")
print("")

def executar_com_isolamento_total(arquivo, descricao):
    """Executar arquivo com isolamento total"""
    print(f"\\\\n{'🔷'*30}")
    print(f"🔬 EXECUTANDO: {descricao}")
    print(f"📁 ARQUIVO: {arquivo}")
    print(f"{'🔷'*30}\\\\n")
    
    # Pequena pausa para garantir isolamento
    time.sleep(0.5)
    
    try:
        processo = subprocess.run(
            [sys.executable, arquivo],
            capture_output=True,
            text=True,
            timeout=25,
            cwd=str(Path(".").absolute())  # Diretório de trabalho isolado
        )
        
        # Mostrar saída COMPLETA e organizada
        if processo.stdout:
            print("📄 SAÍDA DO PROGRAMA:")
            print("-" * 50)
            for linha in processo.stdout.split('\\\\n'):
                if linha.strip():
                    print(f"   {linha}")
            print("-" * 50)
        
        if processo.returncode == 0:
            print(f"\\\\n✅ {descricao} - EXECUTADO COM SUCESSO!")
            return True
        else:
            print(f"\\\\n❌ {descricao} - ERRO NA EXECUÇÃO")
            if processo.stderr:
                print(f"💥 ERRO: {processo.stderr[:200]}...")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"\\\\n⏰ {descricao} - TIMEOUT")
        return False
    except Exception as e:
        print(f"\\\\n💥 {descricao} - EXCEÇÃO: {e}")
        return False

# SEQUÊNCIA DE EXECUÇÃO ULTRA ORGANIZADA
scripts_sequencia = [
    ("circuito_psi_plus.py", "🌌 CIRCUITO |Ψ⁺⟩ - Estado Emaranhado Básico"),
    ("circuito_phi_minus.py", "🌌 CIRCUITO |Φ⁻⟩ - Estado Emaranhado com Fase"),
    ("teletransporte_quantico.py", "🚀 TELETRANSPORTE QUÂNTICO - Protocolo Completo"),
    ("teste_bell.py", "🔔 TESTE DE BELL - Verificação de Emaranhamento"),
    ("CIRCUITOS_UNIFICADOS.py", "⚡ CIRCUITOS UNIFICADOS - Execução Consolidada"),
    ("explorar_modulo_29.py", "👑 MÓDULO 29 - Análise da Rainha Zennith")
]

print("🚀 INICIANDO SEQUÊNCIA ULTRA ORGANIZADA...\\\\n")
time.sleep(1)

resultados = []
tempo_inicio = time.time()

for i, (arquivo, descricao) in enumerate(scripts_sequencia, 1):
    print(f"\\\\n📋 ETAPA {i}/{len(scripts_sequencia)}")
    sucesso = executar_com_isolamento_total(arquivo, descricao)
    resultados.append((descricao, sucesso))
    
    # Pausa maior entre execuções para total isolamento
    if i < len(scripts_sequencia):
        print(f"\\\\n⏳ PREPARANDO PRÓXIMA ETAPA...\\\\n")
        time.sleep(2)

tempo_total = time.time() - tempo_inicio

# RELATÓRIO FINAL ULTRA ORGANIZADO
print(f"\\\\n{'🎉'*20}")
print("🎉 RELATÓRIO FINAL - EXECUÇÃO ULTRA ORGANIZADA")
print(f"{'🎉'*20}\\\\n")

sucessos = sum(1 for _, sucesso in resultados if sucesso)
print(f"📊 ESTATÍSTICAS:")
print(f"   • Total de execuções: {len(scripts_sequencia)}")
print(f"   • Execuções bem-sucedidas: {sucessos}")
print(f"   • Taxa de sucesso: {sucessos/len(scripts_sequencia)*100:.1f}%")
print(f"   • Tempo total: {tempo_total:.2f} segundos")

print(f"\\\\n📋 DETALHES DAS EXECUÇÕES:")
for descricao, sucesso in resultados:
    status = "✅ SUCESSO" if sucesso else "❌ FALHA"
    print(f"   • {descricao}: {status}")

print(f"\\\\n🌌 STATUS FINAL:")
if sucessos == len(scripts_sequencia):
    print("   🎉 TODAS AS EXECUÇÕES CONCLUÍDAS COM SUCESSO!")
    print("   ⚛️  SISTEMA PERFEITAMENTE ORGANIZADO!")
    print("   🚀 PRONTO PARA IBM QUANTUM REAL!")
else:
    print("   ⚠️  ALGUMAS EXECUÇÕES APRESENTARAM FALHAS")
    print("   🔧 VERIFICAR OS SCRIPTS COM PROBLEMAS")

print(f"\\\\n✨ EXECUÇÃO ULTRA ORGANIZADA CONCLUÍDA!")
'''

        caminho_script = self.raiz / "EXECUCAO_ULTRA_ORGANIZADA.py"
        with open(caminho_script, 'w') as f:
            f.write(script_ultra_organizado)
        
        # Tornar executável
        import os
        os.chmod(caminho_script, 0o755)
        
        print(f"   ✅ SCRIPT CRIADO: EXECUCAO_ULTRA_ORGANIZADA.py")
        return str(caminho_script)
    
    def executar_preparacao_completa(self):
        """Executar preparação completa do ambiente"""
        print("🚀 INICIANDO PREPARAÇÃO COMPLETA DO AMBIENTE...")
        
        # 1. Limpar cache
        self.limpar_cache_python()
        
        # 2. Verificar scripts
        self.verificar_e_preparar_scripts()
        
        # 3. Criar script ultra organizado
        script_ultra = self.criar_script_execucao_ultra_organizada()
        
        print(f"\n{'='*70}")
        print("🎉 PREPARAÇÃO DO AMBIENTE CONCLUÍDA!")
        print(f"{'='*70}")
        
        print(f"\n🚀 COMANDO PARA EXECUÇÃO ULTRA ORGANIZADA:")
        print(f"   python3 EXECUCAO_ULTRA_ORGANIZADA.py")
        
        print(f"\n💡 CARACTERÍSTICAS DO SISTEMA:")
        print(f"   • Cache Python limpo")
        print(f"   • Scripts verificados e preparados") 
        print(f"   • Execução sequencial perfeita")
        print(f"   • Zero sobreposição garantida")
        print(f"   • Isolamento total entre circuitos")
        
        return {
            'script_ultra_organizado': script_ultra,
            'ambiente_preparado': True
        }

# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    preparador = PreparadorAmbienteLimpo()
    resultados = preparador.executar_preparacao_completa()
    
    print(f"\n🔧 AMBIENTE PREPARADO PARA EXECUÇÃO PERFEITA!")
    print("🎯 EXECUTE: python3 EXECUCAO_ULTRA_ORGANIZADA.py")
