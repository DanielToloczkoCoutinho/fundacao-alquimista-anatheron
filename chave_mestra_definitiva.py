#!/usr/bin/env python3
"""
🔑 CHAVE MESTRA DEFINITIVA - FUNDAÇÃO ALQUIMISTA
⚛️ Configuração EXATA com todos os dados da transcrição
🌌 Usando TODAS as informações fornecidas
"""

from qiskit_ibm_runtime import QiskitRuntimeService
import json

print("🌌 CHAVE MESTRA DEFINITIVA - FUNDAÇÃO ALQUIMISTA")
print("=" * 60)

# DADOS EXATOS DA SUA TRANSCRIÇÃO - TODAS AS INFORMAÇÕES
CONFIGURACAO_DEFINITIVA = {
    # DADOS DA CONTA PRINCIPAL
    "nome_usuario": "Daniel Toloczko Coutinho",
    "email": "toloczkocoutinhoo@gmail.com", 
    "status": "Ativo",
    "nome_conta": "Fundação Alquimista",
    "id_conta": "26770b560f8940a4803a6518062a8969",
    "id_iam": "IBMid-692001639T",
    
    # CHAVES API EXATAS DA TRANSCRIÇÃO
    "chaves_api": [
        {
            "nome": "Fundação Alquimista",
            "id": "ApiKey-c965c4fe-e0e9-4d5c-ba65-dd061b4093e1",
            "status": "Desbloqueado",
            "data_criacao": "05-10-2025 00:38 GMT",
            "ultima_auth": "16-10-2025 07:10:13:114 GMT",
            "contagem_auth": 150
        },
        {
            "nome": "Fundação Alquimista nova", 
            "id": "ApiKey-19033191-d209-4a47-b427-e2c094a3cdf0",
            "status": "Desbloqueado",
            "data_criacao": "16-10-2025 13:02 GMT",
            "ultima_auth": "17-10-2025 21:50:43:019 GMT",
            "contagem_auth": 2
        }
    ],
    
    # INSTÂNCIA EXATA DO IBM QUANTUM
    "instancia": {
        "crn": "crn:v1:bluemix:public:quantum-computing:us-east:a/26770b560f8940a4803a6518062a8969:0b5355c0-5289-4b8b-a10f-1762828b1b82::",
        "plano": "Open",
        "regiao": "Washington DC (us-east)",
        "grupo_recursos": "Default",
        "criado_em": "4 de out. de 2025",
        "tempo_alocado": "10 min/dia",
        "ciclo_atual": "19 de set. de 2025 - 17 de out. de 2025"
    },
    
    # BACKENDS ESPECÍFICOS MENCIONADOS
    "backends_principais": [
        {"nome": "ibm_brisbane", "qubits": 127, "processador": "Eagle r3", "fila": 4368},
        {"nome": "ibm_torino", "qubits": 133, "processador": "Heron r1", "fila": 398}
    ]
}

def configurar_chave_mestra():
    """Configuração DEFINITIVA com todas as informações exatas"""
    print("🔑 CONFIGURANDO CHAVE MESTRA DEFINITIVA...")
    print(f"👤 Usuário: {CONFIGURACAO_DEFINITIVA['nome_usuario']}")
    print(f"📧 E-mail: {CONFIGURACAO_DEFINITIVA['email']}")
    print(f"🏢 Conta: {CONFIGURACAO_DEFINITIVA['nome_conta']}")
    
    # USAR AMBAS AS CHAVES PARA TESTE
    chaves = CONFIGURACAO_DEFINITIVA['chaves_api']
    
    for i, chave in enumerate(chaves, 1):
        print(f"\n🔑 TENTANDO CHAVE {i}: {chave['nome']}")
        print(f"   ID: {chave['id']}")
        print(f"   Status: {chave['status']}")
        print(f"   Último uso: {chave['ultima_auth']}")
        
        try:
            # CONFIGURAR COM CHAVE EXATA
            QiskitRuntimeService.save_account(
                channel="ibm_quantum_platform",
                token=chave['id'],
                instance=CONFIGURACAO_DEFINITIVA['instancia']['crn'],
                overwrite=True
            )
            
            # TESTAR CONEXÃO
            service = QiskitRuntimeService()
            backends = service.backends()
            
            print(f"   ✅ CONEXÃO BEM-SUCEDIDA!")
            print(f"   🌌 Backends disponíveis: {len(backends)}")
            
            # MOSTRAR BACKENDS PRINCIPAIS
            print(f"\n   🔧 BACKENDS DA TRANSCRIÇÃO:")
            for backend_info in CONFIGURACAO_DEFINITIVA['backends_principais']:
                try:
                    backend = service.backend(backend_info['nome'])
                    status = backend.status()
                    print(f"      🖥️  {backend_info['nome']}: {backend_info['qubits']} qubits")
                    print(f"         📊 Fila atual: {status.pending_jobs} jobs")
                    print(f"         🟢 Status: {status.status}")
                except:
                    print(f"      ⚠️  {backend_info['nome']}: Não disponível")
            
            # INFORMACOES DA INSTÂNCIA
            instancia = CONFIGURACAO_DEFINITIVA['instancia']
            print(f"\n   💼 INFORMAÇÕES DA INSTÂNCIA:")
            print(f"      📍 Região: {instancia['regiao']}")
            print(f"      ⏰ Tempo: {instancia['tempo_alocado']}")
            print(f"      📅 Ciclo: {instancia['ciclo_atual']}")
            
            return service, chave['id']  # Retorna serviço e chave bem-sucedida
            
        except Exception as e:
            print(f"   ❌ Falha com esta chave: {e}")
            continue
    
    return None, None

def executar_teste_quantico(service):
    """Executa teste quântico simples"""
    print(f"\n⚛️ EXECUTANDO TESTE QUÂNTICO...")
    
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    
    # Circuito simples de teste
    qc = QuantumCircuit(2, 2, name="Teste_Fundacao")
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    print("   ✅ Circuito criado:")
    print(f"   {qc.draw(text=True)}")
    
    # Executar no simulador
    backend = AerSimulator()
    result = backend.run(qc, shots=100).result()
    counts = result.get_counts()
    
    print(f"   📊 Resultado teste: {counts}")
    return counts

# EXECUÇÃO PRINCIPAL
print("🚀 INICIANDO CONFIGURAÇÃO DEFINITIVA...")
print(f"📋 Total de chaves: {len(CONFIGURACAO_DEFINITIVA['chaves_api'])}")
print(f"🔧 Backends conhecidos: {len(CONFIGURACAO_DEFINITIVA['backends_principais'])}")

service, chave_ativa = configurar_chave_mestra()

if service:
    print(f"\n🎉 CONFIGURAÇÃO DEFINITIVA BEM-SUCEDIDA!")
    print(f"🔑 Chave ativa: {chave_ativa}")
    
    # Executar teste
    resultados = executar_teste_quantico(service)
    
    print(f"\n🌌 FUNDAÇÃO ALQUIMISTA CONFIGURADA!")
    print("⚛️ SISTEMA QUÂNTICO OPERACIONAL!")
    print("🔑 CHAVE MESTRA ATIVADA COM SUCESSO!")
    
else:
    print(f"\n❌ Nenhuma chave funcionou.")
    print("💡 Verifique:")
    print("   - As chaves estão ativas no portal IBM?")
    print("   - A instância CRN está correta?")
    print("   - Há conexão com internet?")

# SALVAR CONFIGURAÇÃO PARA USO FUTURO
print(f"\n💾 SALVANDO CONFIGURAÇÃO...")
with open('configuracao_fundacao.json', 'w') as f:
    json.dump(CONFIGURACAO_DEFINITIVA, f, indent=2, ensure_ascii=False)

print("✅ Configuração salva em 'configuracao_fundacao.json'")
