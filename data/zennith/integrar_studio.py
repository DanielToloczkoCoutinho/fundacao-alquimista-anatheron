"""
INTEGRAÇÃO COM STUDIO CORE - ZENNITH QUANTUM
Projeto satélite que usa as bibliotecas core do studio
"""

import sys
import os

# Adicionar studio ao path para importar suas bibliotecas
studio_path = os.path.join(os.path.dirname(__file__), '..', 'studio')
if os.path.exists(studio_path):
    sys.path.insert(0, studio_path)
    print(f"✅ Studio core integrado: {studio_path}")
else:
    print("❌ Studio não encontrado. Execute de ~/zennith_quantum/")

# Agora podemos importar as bibliotecas do studio
try:
    # Exemplo de import das utils do studio
    from utils_zennith_log_avancado import log_zennith, log_info
    
    log_info("Zennith Quantum - Projeto satélite inicializado!")
    log_info("Usando bibliotecas core do studio")
    
except ImportError as e:
    print(f"⚠️  Erro ao importar do studio: {e}")
    print("💡 Certifique-se de que o studio está em ~/studio")

def projeto_quantum_demo():
    """Demonstração do projeto satélite usando studio core"""
    try:
        from utils_zennith_log_avancado import log_info
        log_info("Executando demonstração do Zennith Quantum!")
        return "🚀 Projeto satélite operacional!"
    except ImportError:
        return "❌ Studio core não disponível"

if __name__ == "__main__":
    resultado = projeto_quantum_demo()
    print(resultado)
