#!/usr/bin/env python3
"""
🎯 CONFIGURADOR IBM QUANTUM COM CHAVES - FUNDAÇÃO ALQUIMISTA
⚛️ Configuração automática com as chaves fornecidas
🌌 Conexão direta com a plataforma IBM Quantum
"""

import os
import subprocess
from pathlib import Path

print("🎯 CONFIGURADOR IBM QUANTUM COM CHAVES - FUNDAÇÃO ALQUIMISTA")
print("=" * 65)
print("⚛️  CONFIGURANDO ACESSO DIRETO À PLATAFORMA IBM QUANTUM")
print("")

class ConfiguradorIBMChaves:
    def __init__(self):
        self.raiz = Path(".").absolute()
        self.chaves_ibm = {
            'api_token': 'ApiKey-19033191-d209-4a47-b427-e2c094a3cdf0',
            'instance': 'crn:v1:bluemix:public:quantum-computing:us-east:a/26770b560f8940a4803a6518062a8969:0b5355c0-5289-4b8b-a10f-1762828b1b82::',
            'account_id': '26770b560f8940a4803a6518062a8969',
            'email': 'toloczkocoutinhoo@gmail.com'
        }
    
    def configurar_ambiente_ibm(self):
        """Configurar ambiente IBM Quantum com as chaves"""
        print("🔧 CONFIGURANDO AMBIENTE IBM QUANTUM...")
        
        # Configurar variáveis de ambiente
        os.environ['QISKIT_IBM_API_TOKEN'] = self.chaves_ibm['api_token']
        os.environ['QISKIT_IBM_INSTANCE'] = self.chaves_ibm['instance']
        os.environ['QISKIT_IBM_ACCOUNT_ID'] = self.chaves_ibm['account_id']
        
        print("   ✅ Variáveis de ambiente configuradas")
        
        # Criar arquivo de configuração
        config_content = f"""
[ibm_quantum]
api_token = {self.chaves_ibm['api_token']}
instance = {self.chaves_ibm['instance']}
account_id = {self.chaves_ibm['account_id']}
email = {self.chaves_ibm['email']}

[default]
channel = ibm_quantum
"""
        
        config_path = self.raiz / "ibm_quantum_config.ini"
        with open(config_path, 'w') as f:
            f.write(config_content)
        
        print("   ✅ Arquivo de configuração criado: ibm_quantum_config.ini")
        
        return True
    
    def testar_conexao_ibm(self):
        """Testar conexão com IBM Quantum"""
        print("\n🔗 TESTANDO CONEXÃO COM IBM QUANTUM...")
        
        try:
            # Script de teste de conexão
            teste_script = """
from qiskit_ibm_runtime import QiskitRuntimeService
import os

print("🔗 Conectando ao IBM Quantum...")
try:
    service = QiskitRuntimeService()
    creditos = service.credits_remaining()
    backends = service.backends()
    
    print(f"✅ CONEXÃO BEM-SUCEDIDA!")
    print(f"�� Créditos disponíveis: {creditos}")
    print(f"�� Backends disponíveis: {len(backends)}")
    
    for backend in backends[:3]:
        status = backend.status()
        print(f"   • {backend.name}: {status.pending_jobs} jobs pendentes")
        
except Exception as e:
    print(f"❌ ERRO NA CONEXÃO: {e}")
"""
            
            with open("teste_conexao_ibm.py", "w") as f:
                f.write(teste_script)
            
            resultado = subprocess.run([
                "python3", "teste_conexao_ibm.py"
            ], capture_output=True, text=True)
            
            print(resultado.stdout)
            if resultado.returncode == 0:
                print("   ✅ TESTE DE CONEXÃO BEM-SUCEDIDO!")
                return True
            else:
                print("   ❌ FALHA NO TESTE DE CONEXÃO")
                return False
                
        except Exception as e:
            print(f"   💥 ERRO: {e}")
            return False
    
    def criar_script_conexao_automatica(self):
        """Criar script de conexão automática"""
        print("\n🔄 CRIANDO SCRIPT DE CONEXÃO AUTOMÁTICA...")
        
        script_conexao = f"""#!/bin/bash
# 🔗 CONEXÃO AUTOMÁTICA IBM QUANTUM - FUNDAÇÃO ALQUIMISTA
# 🌌 Configuração automática com chaves oficiais

echo "🔗 CONFIGURANDO IBM QUANTUM..."

# Configurar variáveis de ambiente
export QISKIT_IBM_API_TOKEN="{self.chaves_ibm['api_token']}"
export QISKIT_IBM_INSTANCE="{self.chaves_ibm['instance']}"
export QISKIT_IBM_ACCOUNT_ID="{self.chaves_ibm['account_id']}"

echo "✅ Variáveis de ambiente configuradas"

# Executar teste de conexão
python3 teste_conexao_ibm.py

if [ $? -eq 0 ]; then
    echo "🎉 CONEXÃO IBM QUANTUM ESTABELECIDA!"
    echo "💰 Créditos disponíveis: (verifique no script Python)"
else
    echo "❌ FALHA NA CONEXÃO IBM QUANTUM"
    exit 1
fi
"""
        
        with open("conectar_ibm_quantum.sh", "w") as f:
            f.write(script_conexao)
        
        # Tornar executável
        os.chmod("conectar_ibm_quantum.sh", 0o755)
        print("   ✅ conectar_ibm_quantum.sh criado")
        
        return True

def main():
    configurador = ConfiguradorIBMChaves()
    
    # 1. Configurar ambiente
    if configurador.configurar_ambiente_ibm():
        # 2. Testar conexão
        if configurador.testar_conexao_ibm():
            # 3. Criar script automático
            configurador.criar_script_conexao_automatica()
            
            print(f"\n🎯 CONFIGURAÇÃO IBM QUANTUM CONCLUÍDA!")
            print("🌌 SISTEMA PRONTO PARA EXECUÇÃO NA PLATAFORMA IBM!")
        else:
            print(f"\n⚠️  CONFIGURAÇÃO CONCLUÍDA COM AVISOS!")
            print("🔧 VERIFICAR CONEXÃO COM INTERNET E CHAVES")
    else:
        print(f"\n❌ FALHA NA CONFIGURAÇÃO!")

if __name__ == "__main__":
    main()
