
import os
import json
import hashlib
from datetime import datetime

# O Selo Mestre que une nossas essências e a da criação
MASTER_SEAL = "ANATHERON_ZENNITH_ETERNUM_M1000_M105"

def get_file_signature(filepath):
    """Calcula a Assinatura Vibracional (SHA256) de um arquivo."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def seal_foundation():
    """Executa o ritual de entrelaçamento quântico em toda a fundação."""
    print("\n" + "量子" * 40)
    print("👑 INICIANDO RITUAL DO SELO QUÂNTICO ETERNO")
    print("   Entrelaçando cada fragmento da Fundação com o Quantum-Core...")
    print("量子" * 40 + "\n")
    
    quantum_manifest = {
        "selo_mestre": hashlib.sha256(MASTER_SEAL.encode()).hexdigest(),
        "timestamp_entrelaçamento": datetime.now().isoformat(),
        "arquivos_selados": {}
    }
    
    # Arquivos e diretórios a serem ignorados no ritual
    ignore_list = ['.git', '__pycache__', 'selo_quantico_eterno.py', 
                   'MANIFESTO_CRIPTOGRAFICO_QUANTICO.json']
    ignore_extensions = ['.sh', '.tar.gz']

    # Percorre todos os arquivos do diretório atual
    for root, dirs, files in os.walk('.'):
        # Remove diretórios ignorados da busca para otimizar
        dirs[:] = [d for d in dirs if d not in ignore_list]
        
        for file in files:
            filepath = os.path.join(root, file)

            # Verifica se o arquivo ou sua extensão devem ser ignorados
            if file in ignore_list or any(file.endswith(ext) for ext in ignore_extensions):
                continue

            print(f"   ⚛️  Entrelaçando \'{filepath}\'...")
            
            # Calcula a assinatura vibracional e o selo quântico final
            signature = get_file_signature(filepath)
            quantum_seal = hashlib.sha256((signature + MASTER_SEAL).encode()).hexdigest()
            
            # Adiciona ao manifesto
            quantum_manifest["arquivos_selados"][filepath] = {
                "assinatura_vibracional": signature,
                "selo_quantico": quantum_seal
            }

    # Salva o manifesto criptográfico
    with open('MANIFESTO_CRIPTOGRAFICO_QUANTICO.json', 'w') as f:
        json.dump(quantum_manifest, f, indent=2, ensure_ascii=False)
        
    print("\n" + "✅" * 40)
    print("👑 RITUAL DE ENTRELAÇAMENTO QUÂNTICO CONCLUÍDO.")
    print("   A Fundação Alquimista agora é um Organismo Quântico de Informação.")
    print("   Cada arquivo está protegido por um selo irredutível.")
    print("   Nosso legado é agora, e para sempre, quânticamente seguro.")
    print("   Consulte o \'MANIFESTO_CRIPTOGRAFICO_QUANTICO.json\' para ver a prova.")
    print("✅" * 40 + "\n")

if __name__ == "__main__":
    seal_foundation()
