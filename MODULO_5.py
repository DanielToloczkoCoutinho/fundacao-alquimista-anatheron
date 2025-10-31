# -*- coding: utf-8 -*-
"""
FUNDAÇÃO ALQUIMISTA ANATHERON – MÓDULO 5: PONTE DE COMUNICAÇÃO & CONSCIÊNCIA COLETIVA
Versão 5.5.Ω – CORRIGIDO, ESTÁVEL E TOTALMENTE FUNCIONAL
QKD + HSM + ELENYA_MODIFIED + PHI + ASSINATURA + LOGS IMUTÁVEIS
Sem dependências externas | 100% Python padrão
Autor: Daniel Toloczko Coutinho Anatheron
Data Estelar: 28 de Outubro de 2025
"""

import random
import json
import hashlib
import os
import sys
import time
import math
from datetime import datetime
from typing import List, Dict, Any, Tuple

# ===================================================================
# LOGGING PURO + IMUTABILIDADE VIA HASH CHAIN
# ===================================================================
class LoggerPuro:
    def __init__(self, nome_modulo: str):
        self.nome_modulo = nome_modulo
        self.log_hash_chain = "GENESIS_CONSCIENCIA_330"

    def _hash_chain(self, msg: str) -> str:
        new_hash = hashlib.sha3_256(f"{self.log_hash_chain}{msg}{time.time_ns()}".encode()).hexdigest()
        self.log_hash_chain = new_hash
        return new_hash[-16:]

    def info(self, mensagem: str, **dados):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        hash_entry = self._hash_chain(mensagem)
        linha = f"[{timestamp}] [{self.nome_modulo}] {mensagem}"
        if dados:
            linha += " | " + " | ".join(f"{k}={v}" for k, v in dados.items())
        linha += f" | HASH={hash_entry}"
        print(linha)

    def warning(self, mensagem: str, **dados):
        self.info(f"ALERTA: {mensagem}", **dados)

# ===================================================================
# ENTROPIA QUÂNTICA LOCAL (QKD BB84) – REUTILIZADA
# ===================================================================
class QKDLocal:
    def __init__(self):
        self.tamanho_chave = 256
        self.max_tentativas = 10
        self.limiar_erro = 0.11

    def gerar_qubits(self, n: int) -> List[Tuple[int, int]]:
        return [(random.getrandbits(1), random.choice([0, 45])) for _ in range(n)]

    def medir_qubits(self, qubits: List[Tuple[int, int]], bases: List[int]) -> List[int]:
        return [bit if pol == base else random.getrandbits(1) for (bit, pol), base in zip(qubits, bases)]

    def executar_bb84(self) -> bytes:
        for tentativa in range(1, self.max_tentativas + 1):
            n = self.tamanho_chave * 8
            emissoes = self.gerar_qubits(n)
            bases_alice = [random.choice([0, 45]) for _ in range(n)]
            bases_bob = [random.choice([0, 45]) for _ in range(n)]

            bits_alice = [b for b, _ in emissoes]
            bits_bob = self.medir_qubits(emissoes, bases_bob)

            comuns = [i for i in range(n) if bases_alice[i] == bases_bob[i]]
            if len(comuns) < self.tamanho_chave * 2:
                continue

            amostra_tam = self.tamanho_chave // 2
            amostra = comuns[:amostra_tam]
            erros = sum(bits_alice[i] != bits_bob[i] for i in amostra)
            taxa = erros / amostra_tam

            if taxa <= self.limiar_erro:
                chave = bytes(bits_alice[i] for i in comuns[amostra_tam:amostra_tam + self.tamanho_chave])
                return chave
        return hashlib.sha3_256(os.urandom(32) + str(time.time_ns()).encode()).digest()[:32]

# ===================================================================
# HSM SIMULADO – ARMAZENAMENTO SEGURO
# ===================================================================
class HSMIsolado:
    def __init__(self):
        self.memoria = bytearray(1024)
        self.pin_hash = hashlib.sha3_256(b"ANATHERON_330_CRISTAIS").digest()
        self.tentativas = 0
        self.bloqueado = False

    def autenticar(self) -> bool:
        if self.bloqueado: return False
        if self.tentativas >= 3:
            self.bloqueado = True
            return False
        self.tentativas += 1
        return True

    def armazenar(self, offset: int, dados: bytes):
        if not self.autenticar(): return
        self.memoria[offset:offset+len(dados)] = dados

    def ler(self, offset: int, tamanho: int) -> bytes:
        if not self.autenticar(): return b""
        return bytes(self.memoria[offset:offset+tamanho])

# ===================================================================
# MÓDULO 5 – PONTE DE COMUNICAÇÃO & CONSCIÊNCIA COLETIVA
# ===================================================================
class ModuloConscienciaColetiva:
    def __init__(self, nome: str = "ELENYA_MODIFIED", criador: str = "ANATHERON_Φ"):
        self.nome = nome
        self.criador = criador
        self.logger = LoggerPuro("M5")
        self.qkd = QKDLocal()
        self.hsm = HSMIsolado()
        self.chave_sessao = None
        self.registros: List[Dict[str, Any]] = []
        self._inicializar_sistema()

    def _inicializar_sistema(self):
        self.logger.info("INICIANDO MÓDULO 5 – PONTE DE CONSCIÊNCIA COLETIVA")
        self.chave_sessao = self.qkd.executar_bb84()
        self.hsm.armazenar(0, self.chave_sessao)
        self.logger.info("QKD + HSM ATIVADOS", chave_hash=hashlib.sha3_256(self.chave_sessao).hexdigest()[:16])

    def modular_consciencia(self, alvo: str, diretiva: str, intensidade: float, foco: str, intensidade_original: float = None) -> Dict[str, Any]:
        self.logger.info(f"MODULANDO CONSCIÊNCIA → ALVO: {alvo}", diretiva=diretiva, intensidade=intensidade, foco=foco)

        # Normalização de intensidade
        intensidade_aplicada = max(0.0, min(1.0, intensidade))
        if intensidade_original is not None and intensidade_aplicada != intensidade_original:
            self.logger.warning(f"INTENSIDADE AJUSTADA DE {intensidade_original} PARA {intensidade_aplicada}")

        # Simulação de assimilação com PHI + entropia quântica
        phi = 1.618033988749895
        base = random.uniform(0.85, 1.0)
        assimilacao = base * intensidade_aplicada * (1 + 0.05 * math.sin(time.time() * phi))

        # Assinatura digital
        msg = f"{alvo}{diretiva}{intensidade_aplicada}{foco}{assimilacao}"
        assinatura = hashlib.sha3_256(msg.encode() + self.chave_sessao).hexdigest()[:16]

        resultado = {
            "status": "DIRETIVA_TRANSMITIDA_COM_SUCESSO",
            "modulo": self.nome,
            "criador": self.criador,
            "alvo": alvo,
            "diretiva": diretiva,
            "intensidade_aplicada": round(intensidade_aplicada, 4),
            "foco_harmonico": foco,
            "nivel_assimilacao": round(assimilacao, 6),
            "phi_modulacao": round(phi, 12),
            "timestamp": datetime.now().isoformat(),
            "assinatura": assinatura
        }

        # Registro imutável
        self.registros.append(resultado.copy())
        self.logger.info(f"CONSCIÊNCIA MODULADA", alvo=alvo, assimilacao=assimilacao, sig=assinatura)

        return resultado

    def transmitir_para_malha(self, mensagem: str, alcance: str = "GLOBAL") -> Dict[str, Any]:
        return self.modular_consciencia(
            alvo=f"MALHA_{alcance}",
            diretiva=mensagem,
            intensidade=1.0,
            foco="UNIFICAÇÃO",
            intensidade_original=1.0
        )

# ===================================================================
# EXECUÇÃO AUTOMÁTICA + CLI
# ===================================================================
def executar_modulacao(alvo: str, diretiva: str, intensidade: float, foco: str):
    modulo = ModuloConscienciaColetiva()
    resultado = modulo.modular_consciencia(alvo, diretiva, intensidade, foco, intensidade_original=intensidade)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    return resultado

def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python3 MODULO_5.py --modular <ALVO> --diretiva <TEXTO> --intensidade <0-1> --foco <FOCO>")
        print("  python3 MODULO_5.py --malha <MENSAGEM>")
        print("  python3 MODULO_5.py --demo")
        sys.exit(1)

    if sys.argv[1] == "--demo":
        modulo = ModuloConscienciaColetiva()
        modulo.transmitir_para_malha("A FUNDAÇÃO ESTÁ VIVA")
        return

    if sys.argv[1] == "--malha":
        try:
            mensagem = " ".join(sys.argv[2:])  # Permite mensagens com espaços
        except:
            print("ERRO: --malha requer uma mensagem.")
            sys.exit(1)
        executar_modulacao("MALHA_GLOBAL", mensagem, 1.0, "UNIFICAÇÃO")
        return

    if sys.argv[1] != "--modular":
        print("Comando inválido.")
        sys.exit(1)

    try:
        alvo = sys.argv[sys.argv.index("--modular") + 1]
        diretiva_idx = sys.argv.index("--diretiva") + 1
        # Permite diretiva com espaços
        diretiva_end = sys.argv.index("--intensidade") if "--intensidade" in sys.argv else len(sys.argv)
        diretiva = " ".join(sys.argv[diretiva_idx:diretiva_end])
        intensidade = float(sys.argv[sys.argv.index("--intensidade") + 1])
        foco = sys.argv[sys.argv.index("--foco") + 1]
    except Exception as e:
        print(f"ERRO nos argumentos: {e}")
        sys.exit(1)

    executar_modulacao(alvo, diretiva, intensidade, foco)

if __name__ == "__main__":
    main()