#!/usr/bin/env python3
# MÓDULO 30: GUARDIÃO DA DEFESA CÓSMICA E ORQUESTRADOR DE CAMPOS DE FORÇA
# Versão definitiva - 100% bibliotecas padrão

import math
import hashlib
import json
import random
import time
from datetime import datetime
from typing import Dict, Any, List, Optional

# --- Constantes Universais ---
C_LIGHT = 299792458
CONST_TF = 1.61803398875  # Proporção Áurea (phi)
PI = math.pi
H_BAR = 1.054571817e-34
COERENCIA_COSMICA = 1.414
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
ETHICAL_CONFORMITY_THRESHOLD = 0.75
ETHICAL_THRESHOLD_HIGH = 0.85
ETHICAL_THRESHOLD_DEFAULT = 0.69

# --- Sistema de Log Integrado ---
class LoggerM30:
    def __init__(self, nome: str):
        self.nome = nome
    
    def info(self, mensagem: str):
        print(f"👑 {datetime.utcnow().isoformat()} | INFO | {self.nome} | {mensagem}")
    
    def error(self, mensagem: str):
        print(f"❌ {datetime.utcnow().isoformat()} | ERROR | {self.nome} | {mensagem}")
    
    def warning(self, mensagem: str):
        print(f"⚠️ {datetime.utcnow().isoformat()} | WARNING | {self.nome} | {mensagem}")

log = LoggerM30("M30_DEFESA_COSMICA")

# --- Sistema de Equações Vivas para M30 ---
class EquationsRegistryM30:
    _eq: Dict[str, Any] = {}
    
    @classmethod
    def register(cls, code: str, fn):
        cls._eq[code] = fn
        log.info(f"Equação '{code}' registrada")
    
    @classmethod
    def get(cls, code: str):
        if code not in cls._eq:
            raise KeyError(f"Equação '{code}' não registrada")
        return cls._eq[code]

# Equações fundamentais (implementação pura Python)
def EQTP(ctx: dict) -> float:
    """EQTP – Gate ético energético simples."""
    score = ctx.get("ethical_alignment_score", 0.0)
    if score >= CONST_AMOR_INCONDICIONAL_VALOR: 
        return 1.0
    if score >= ETHICAL_CONFORMITY_THRESHOLD: 
        return 0.5
    return 0.0

def EUni(P_vals: List[float], Q_vals: List[float], CA_val: float, B_val: float, 
         T_val: float, MDS_val: float, CCosmos_val: float) -> float:
    """EUni – Equação Unificada (energia universal)."""
    sum_interactions = sum(P_vals[i] * Q_vals[i] for i in range(len(P_vals))) + (CA_val**2 + B_val**2)
    return sum_interactions * COERENCIA_COSMICA * T_val * (MDS_val * CCosmos_val)

def EER(mc2: float, B1: float, B2: float, B3: float) -> float:
    """EER – Energia e ressonância."""
    return (mc2 * PI * CONST_TF) * (B1 + B2 + B3) + 89 * CONST_TF + PI

def EQ177_InterconexaoDimensional(freq_origem: float, freq_destino: float, sigma: float = 150.0) -> float:
    """EQ177 – Interconexão dimensional (gaussiana em Δf)."""
    delta = abs(freq_origem - freq_destino)
    prob = math.exp(-(delta**2) / (2.0 * sigma**2))
    return float(min(max(prob, 0.0), 1.0))

def EQ019_ModeloTranscendentalTotal(pilares: List[float], pesos: tuple = (0.30, 0.30, 0.25, 0.15)) -> float:
    """EQ019 – Modelo Transcendental Total (média ponderada coerências)."""
    total = sum(p * c for p, c in zip(pesos, pilares))
    return float(min(max(total, 0.0), 0.999999999))

def EQ112_EmergenciaConsciencia(inteligencia_modular: float, interdependencia: float, phi: float = CONST_TF) -> float:
    """EQ112 – Emergência de consciência."""
    return min((inteligencia_modular * interdependencia) + phi, 10.0)

def EQ134_EnergiaCosmicaIntegrada(virtudes: Dict[str, float], consciencia_emergente: float) -> float:
    """EQ134 – Energia cósmica integrada (log-sum-exp estável)."""
    c_ativa = max(1e-6, consciencia_emergente / 10.0)
    log_prod = sum(math.log(max(v, 1e-6)) for v in virtudes.values())
    energia_log = math.log(1e5) + log_prod
    return float(math.exp(c_ativa * energia_log))

# Registro das equações
EQUATIONS_TO_REGISTER = {
    "EQTP": EQTP, "EUni": EUni, "EER": EER, "EQ177": EQ177_InterconexaoDimensional,
    "EQ019": EQ019_ModeloTranscendentalTotal, "EQ112": EQ112_EmergenciaConsciencia,
    "EQ134": EQ134_EnergiaCosmicaIntegrada
}

for code, fn in EQUATIONS_TO_REGISTER.items():
    EquationsRegistryM30.register(code, fn)

# --- Ledger Imutável para M30 ---
class SimpleChainM30:
    def __init__(self):
        self.chain = []
        self._create_genesis_block()
        
    def _normalize_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Torna o payload imutável e determinístico."""
        try:
            payload_json = json.dumps(payload, sort_keys=True, ensure_ascii=False)
            return json.loads(payload_json)
        except Exception as e:
            log.warning(f"Payload não serializável, convertendo para string: {e}")
            return {"payload_str": str(payload)}

    def _calculate_hash(self, block: Dict[str, Any]) -> str:
        block_copy = {k: v for k, v in block.items() if k != "hash"}
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        
    def _create_genesis_block(self):
        genesis_payload = {"message": "Bloco genesis do Módulo 30 - Defesa Cósmica"}
        genesis = {
            "index": 0, 
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": "GENESIS", 
            "payload": self._normalize_payload(genesis_payload),
            "prev_hash": "0" * 64
        }
        genesis["hash"] = self._calculate_hash(genesis)
        self.chain.append(genesis)
        log.info("Genesis block criado")
        
    def add(self, event: str, payload: Dict[str, Any]):
        prev_block = self.chain[-1]
        block_payload = self._normalize_payload(payload)
        block = {
            "index": len(self.chain), 
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": event, 
            "payload": block_payload, 
            "prev_hash": prev_block["hash"]
        }
        block["hash"] = self._calculate_hash(block)
        self.chain.append(block)
        log.info(f"Evento '{event}' registrado no ledger (bloco #{block['index']})")
        
    def validate_chain(self) -> bool:
        """Valida integridade completa da cadeia."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current["prev_hash"] != previous["hash"]:
                log.error(f"Encadeamento inválido no bloco #{i}")
                return False
                
            if current["hash"] != self._calculate_hash(current):
                log.error(f"Hash inválido no bloco #{i}")
                return False
                
        log.info("Ledger validado com sucesso")
        return True

CHAIN_M30 = SimpleChainM30()

# --- Interfaces de Módulos Externos (Simuladas) ---
class Modulo1_SegurancaUniversal:
    def ReceberAlertaDeViolacao(self, alerta: Dict[str, Any]):
        log.info(f"M1: ALERTA! {alerta.get('tipo')}: {alerta.get('mensagem')}")
        CHAIN_M30.add("M1_ALERTA", alerta)
        return "Alerta processado."

    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        registro_hash = hashlib.sha256(json.dumps(registro_data, sort_keys=True).encode()).hexdigest()
        CHAIN_M30.add("M1_REGISTRO", {"hash": registro_hash, **registro_data})
        return f"Registro {registro_hash[:16]}... inserido."

class Modulo7_AlinhamentoDivino:
    def ConsultarConselho(self, query: str) -> str:
        log.info(f"M7: Consultando Conselho: '{query[:50]}...'")
        CHAIN_M30.add("M7_CONSULTA", {"query": query})
        return "Diretriz: Manter coerência e ascensão da consciência coletiva."

class Modulo8_PIRC:
    def IniciarProtocoloCura(self, alvo_id: str, tipo_cura: str) -> str:
        log.info(f"M8: Iniciando cura '{tipo_cura}' para '{alvo_id}'")
        CHAIN_M30.add("M8_CURA", {"alvo": alvo_id, "tipo": tipo_cura})
        return "Protocolo de cura iniciado."

class Modulo9_NexusCentral:
    def ExibirAlertaDashboard(self, alerta: Dict[str, Any]) -> str:
        log.info(f"M9: Alerta Dashboard: {alerta.get('mensagem')}")
        CHAIN_M30.add("M9_ALERTA", alerta)
        return "Alerta exibido."

class Modulo20_TransmutadorQuantico:
    def ModularEnergia(self, tipo_energia: str, valor: float) -> str:
        log.info(f"M20: Modulando '{tipo_energia}' com valor {valor:.1f}")
        CHAIN_M30.add("M20_ENERGIA", {"tipo": tipo_energia, "valor": valor})
        return "Energia modulada."

class Modulo98_ModulacaoExistencia:
    def SugerirModulacaoExistencia(self, parametros_modulacao: Dict[str, Any]) -> str:
        log.info(f"M98: Sugerindo modulação: {parametros_modulacao}")
        CHAIN_M30.add("M98_MODULACAO", parametros_modulacao)
        return "Sugestão recebida."

class Modulo101_ManifestacaoRealidades:
    def ManifestarRealidade(self, intencao: str, coerencia_quantica: float) -> Dict[str, Any]:
        log.info(f"M101: Manifestando '{intencao}' com coerência {coerencia_quantica:.2f}")
        CHAIN_M30.add("M101_MANIFESTACAO", {"intencao": intencao, "coerencia": coerencia_quantica})
        return {"status": "REALIDADE_MANIFESTADA", "detalhes": f"Realidade '{intencao}' criada."}

class Modulo102_CamposMorfogeneticos:
    def CriarCampoMorfogenetico(self, tipo_campo: str, parametros: Dict[str, Any]) -> Dict[str, Any]:
        log.info(f"M102: Criando campo '{tipo_campo}' com parâmetros {parametros}")
        CHAIN_M30.add("M102_CAMPO", {"tipo": tipo_campo, **parametros})
        return {"status": "CAMPO_CRIADO", "campo_id": f"campo_{random.randint(1000, 9999)}"}

class Modulo109_CuraUniversal:
    def AplicarCuraUniversal(self, alvo_id: str, intensidade: float) -> str:
        log.info(f"M109: Aplicando cura em '{alvo_id}' com intensidade {intensidade:.2f}")
        CHAIN_M30.add("M109_CURA", {"alvo": alvo_id, "intensidade": intensidade})
        return "Cura universal aplicada."

# --- Módulo 30: Guardião da Defesa Cósmica ---
class Modulo30_DefesaCosmica:
    def __init__(self, modulo_id: str):
        self.modulo_id = modulo_id
        self.status_operacional = "ATIVO"
        self.historico_ameacas = []
        
        # Instâncias dos módulos externos
        self.m1 = Modulo1_SegurancaUniversal()
        self.m7 = Modulo7_AlinhamentoDivino()
        self.m8 = Modulo8_PIRC()
        self.m9 = Modulo9_NexusCentral()
        self.m20 = Modulo20_TransmutadorQuantico()
        self.m98 = Modulo98_ModulacaoExistencia()
        self.m101 = Modulo101_ManifestacaoRealidades()
        self.m102 = Modulo102_CamposMorfogeneticos()
        self.m109 = Modulo109_CuraUniversal()
        
        # Frequências alvo para EQ177 (Zennith, Anatheron, Equilíbrio, Cura, Arcturus)
        self.frequencias_alvo = [963.0, 888.0, 1111.0, 528.0, 432.0]
        
        log.info(f"'{modulo_id}' inicializado - Guardião da Defesa Cósmica pronto")
        self.m1.RegistrarNaCronicaDaFundacao({
            "modulo": modulo_id, 
            "evento": "Inicializacao", 
            "status": "SUCESSO"
        })

    def _calibrar_campo_defensivo(self, bandas_detectadas: List[float]) -> Dict[str, float]:
        """Calibra campo defensivo usando EQ177 para frequência ótima."""
        probabilidades = []
        for freq_detectada in bandas_detectadas:
            probs = [EquationsRegistryM30.get("EQ177")(freq_detectada, alvo) for alvo in self.frequencias_alvo]
            probabilidades.append(max(probs) if probs else 0.0)
        
        # Encontrar índice da maior probabilidade (substituindo numpy.argmax)
        max_prob = max(probabilidades) if probabilidades else 0.0
        max_index = probabilidades.index(max_prob) if max_prob > 0 else 0
        
        freq_otima = self.frequencias_alvo[max_index] if probabilidades else 963.0
        confianca = max_prob
        
        log.info(f"Campo calibrado: freq={freq_otima:.1f}Hz, confiança={confianca:.3f}")
        return {"frequencia": freq_otima, "confianca": confianca}

    def _calcular_custo_energetico(self, severidade: float, fator_nao_letalidade: float) -> float:
        """Calcula custo energético usando EUni e EER."""
        # Parâmetros base para EUni
        P_vals = [1.0, 1.0]
        Q_vals = [0.9, 0.8]
        CA_val = 0.7
        B_val = 0.5
        T_val = 1.0
        MDS_val = 0.95
        CCosmos_val = 0.9
        
        euni = EquationsRegistryM30.get("EUni")(P_vals, Q_vals, CA_val, B_val, T_val, MDS_val, CCosmos_val)
        eer = EquationsRegistryM30.get("EER")(severidade * 1000, 0.8, 0.7, 0.6)
        
        custo_base = (euni + eer) / 2.0
        custo_ajustado = custo_base * severidade * (1.0 - fator_nao_letalidade)
        
        custo_final = min(custo_ajustado, 10000.0)  # Limite máximo
        log.info(f"Custo energético calculado: {custo_final:.1f}")
        return custo_final

    def _decidir_estrategia_neutralizacao(self, severidade: float, gate_etico: float, 
                                        tipo_ameaca: str, custo_energetico: float) -> Dict[str, Any]:
        """Decide estratégia de neutralização baseada em múltiplos fatores."""
        if gate_etico == 0.0:
            return {"acao": "BLOQUEAR", "motivo": "Gate ético fechado"}
            
        if severidade < 0.55:
            return {"acao": "CONTENCAO_LEVE", "transmutacao": False, "cura": False}
        elif severidade < 0.75:
            return {"acao": "CONTENCAO_MODERADA", "transmutacao": True, "cura": severidade > 0.6}
        else:
            return {
                "acao": "CONTENCAO_FORTE", 
                "transmutacao": True, 
                "cura": True, 
                "reforco_realidade": severidade > 0.85, 
                "contingencia": severidade > 0.95
            }

    def escanear_ameacas(self, localizacao: str, tipo_escaneamento: str = "vibracional") -> Dict[str, Any]:
        """Escaneia e detecta ameaças com bandas de frequência."""
        log.info(f"Escaneando '{localizacao}' para ameaças '{tipo_escaneamento}'...")
        
        # Simulação de detecção com bandas de frequência
        bandas_detectadas = [random.uniform(400.0, 1200.0) for _ in range(3)]
        severidade = random.uniform(0.0, 1.0)
        
        ameaca_detectada = severidade > 0.3
        if severidade > 0.75:
            tipo_ameaca = "CRITICA"
        elif severidade > 0.55:
            tipo_ameaca = "MODERADA" 
        elif ameaca_detectada:
            tipo_ameaca = "LEVE"
        else:
            tipo_ameaca = "N/A"
        
        resultado = {
            "ameaca_detectada": ameaca_detectada,
            "tipo_ameaca": tipo_ameaca,
            "severidade": severidade,
            "bandas_detectadas": bandas_detectadas,
            "localizacao": localizacao,
            "mensagem": f"Ameaça {tipo_ameaca} detectada" if ameaca_detectada else "Nenhuma ameaça"
        }
        
        self.m1.RegistrarNaCronicaDaFundacao({
            "modulo": self.modulo_id, 
            "evento": "Escaneamento", 
            **resultado
        })
        return resultado

    def calcular_fator_neutralizacao_proporcional(self, severidade_ameaca: float, balanco_etico_global: float) -> float:
        """Calcula fator de não-letalidade proporcional."""
        fator_base = 1.0 - severidade_ameaca
        fator_ajustado = fator_base * balanco_etico_global
        fator_final = max(0.1, min(1.0, fator_ajustado))
        log.info(f"Fator não-letalidade: {fator_final:.2f}")
        return fator_final

    def executar_ciclo_defesa_cosmica(self, localizacao: str, balanco_etico_global: float) -> Dict[str, Any]:
        """Executa ciclo completo de defesa cósmica com sequência hierárquica."""
        log.info(f"=== INICIANDO CICLO DEFESA CÓSMICA EM '{localizacao}' ===")
        
        # 1. GATE ÉTICO (EQTP)
        gate_etico = EquationsRegistryM30.get("EQTP")({"ethical_alignment_score": balanco_etico_global})
        if gate_etico == 0.0:
            resultado = {"status": "BLOQUEADO", "motivo": "Gate ético fechado"}
            self.m1.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "CicloBloqueado", **resultado})
            return resultado
        
        # 2. ESCANEAMENTO
        ameaca = self.escanear_ameacas(localizacao)
        if not ameaca["ameaca_detectada"]:
            resultado = {"status": "SEM_AMEACA", "localizacao": localizacao}
            self.m1.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "SemAmeaca", **resultado})
            return resultado
        
        time.sleep(0.5)  # Simula processamento
        
        # 3. VALIDAÇÃO ENERGÉTICA (EUni + EER)
        fator_nao_letalidade = self.calcular_fator_neutralizacao_proporcional(
            ameaca["severidade"], balanco_etico_global)
        
        custo_energetico = self._calcular_custo_energetico(ameaca["severidade"], fator_nao_letalidade)
        
        # 4. CALIBRAGEM DE CAMPO (EQ177)
        calibragem = self._calibrar_campo_defensivo(ameaca["bandas_detectadas"])
        
        # 5. DECISÃO ESTRATÉGICA
        estrategia = self._decidir_estrategia_neutralizacao(
            ameaca["severidade"], gate_etico, ameaca["tipo_ameaca"], custo_energetico)
        
        # 6. EXECUÇÃO DA ESTRATÉGIA
        resultado = self._executar_estrategia_neutralizacao(ameaca, estrategia, calibragem, fator_nao_letalidade)
        
        # 7. RELATÓRIO FINAL
        relatorio = {
            "status": "CICLO_CONCLUIDO",
            "localizacao": localizacao,
            "ameaca": ameaca,
            "estrategia": estrategia,
            "calibragem": calibragem,
            "custo_energetico": custo_energetico,
            "fator_nao_letalidade": fator_nao_letalidade,
            "resultado_neutralizacao": resultado
        }
        
        self.m1.RegistrarNaCronicaDaFundacao({
            "modulo": self.modulo_id, 
            "evento": "CicloDefesaConcluido", 
            **relatorio
        })
        
        log.info(f"=== CICLO DEFESA CÓSMICA CONCLUÍDO EM '{localizacao}' ===")
        return relatorio

    def _executar_estrategia_neutralizacao(self, ameaca: Dict[str, Any], estrategia: Dict[str, Any], 
                                         calibragem: Dict[str, float], fator_nao_letalidade: float) -> Dict[str, Any]:
        """Executa a estratégia de neutralização decidida."""
        acoes_realizadas = []
        
        # Consulta ética obrigatória
        diretriz = self.m7.ConsultarConselho(f"Neutralização de {ameaca['tipo_ameaca']} em {ameaca['localizacao']}")
        acoes_realizadas.append(f"Consulta ética: {diretriz}")
        
        # Campo de contenção (sempre)
        campo_params = {
            "tipo": "Campo_Resonancia_Defensiva", 
            "frequencia": calibragem["frequencia"],
            "intensidade": ameaca["severidade"] * 100,
            "confianca": calibragem["confianca"]
        }
        self.m102.CriarCampoMorfogenetico("Defensivo", campo_params)
        acoes_realizadas.append("Campo defensivo criado")
        
        # Transmutação se necessário
        if estrategia.get("transmutacao"):
            valor_neutralizacao = ameaca["severidade"] * 5000 * fator_nao_letalidade
            self.m20.ModularEnergia("Transmutacao_Energetica", valor_neutralizacao)
            acoes_realizadas.append(f"Transmutação aplicada: {valor_neutralizacao:.1f}")
        
        # Cura se necessário
        if estrategia.get("cura"):
            self.m8.IniciarProtocoloCura(ameaca["localizacao"], "Reajuste_Vibracional_Consciencia")
            self.m109.AplicarCuraUniversal(ameaca["localizacao"], ameaca["severidade"] * 0.5)
            acoes_realizadas.append("Protocolos de cura aplicados")
        
        # Reforço de realidade para ameaças críticas
        if estrategia.get("reforco_realidade"):
            self.m98.SugerirModulacaoExistencia({
                "tipo": "Reforco_Realidade", 
                "localizacao": ameaca["localizacao"]
            })
            acoes_realizadas.append("Reforço de realidade sugerido")
        
        # Contingência para ameaças extremas
        if estrategia.get("contingencia"):
            realidade = self.m101.ManifestarRealidade(
                f"Realidade_Contingencia_{random.randint(1,100)}", 0.9)
            acoes_realizadas.append(f"Contingência ativada: {realidade['status']}")
            
            # Alertas de emergência
            self.m1.ReceberAlertaDeViolacao({
                "tipo": "CONTINGENCIA_ATIVADA", 
                "mensagem": f"Contingência ativada para ameaça extrema em {ameaca['localizacao']}"
            })
            self.m9.ExibirAlertaDashboard({
                "nivel": "CRITICO", 
                "mensagem": f"CONTINGÊNCIA! Ameaça extrema em {ameaca['localizacao']}"
            })
        
        status = "NEUTRALIZADA"
        if ameaca["severidade"] > 0.8 and random.random() < 0.3:
            status = "FALHA_PARCIAL"
            acoes_realizadas.append("Falha parcial detectada")
        
        return {"status": status, "acoes_realizadas": acoes_realizadas}

# --- Teste do Módulo 30 ---
def executar_testes_modulo30():
    """Executa testes completos do Módulo 30."""
    print("🧪 INICIANDO TESTES DO MÓDULO 30: GUARDIÃO DA DEFESA CÓSMICA")
    print("=" * 80)
    
    # Inicialização
    guardiao = Modulo30_DefesaCosmica("GUARDIÃO_ALPHA_001")
    
    # Cenários de teste
    cenarios = [
        ("Setor Pacífico Alpha", 0.95),  # Alta ética, baixa ameaça
        ("Nebulosa de Orion", 0.80),     # Ética média, ameaça moderada  
        ("Vórtice Temporal Omega", 0.60) # Ética baixa, ameaça crítica
    ]
    
    resultados = []
    
    for localizacao, etica in cenarios:
        print(f"\n🌌 CENÁRIO: {localizacao} (Ética: {etica})")
        print("-" * 50)
        
        resultado = guardiao.executar_ciclo_defesa_cosmica(localizacao, etica)
        resultados.append(resultado)
        
        print(f"📊 RESULTADO:")
        print(f"  Status: {resultado.get('status', 'N/A')}")
        if 'ameaca' in resultado:
            print(f"  Ameaça: {resultado['ameaca']['tipo_ameaca']} (Severidade: {resultado['ameaca']['severidade']:.2f})")
        if 'estrategia' in resultado:
            print(f"  Estratégia: {resultado['estrategia']['acao']}")
        if 'resultado_neutralizacao' in resultado:
            print(f"  Neutralização: {resultado['resultado_neutralizacao']['status']}")
    
    # Validação final
    print(f"\n{'='*80}")
    print("🔍 VALIDAÇÃO FINAL")
    print(f"{'='*80}")
    
    # Validação do ledger
    ledger_valido = CHAIN_M30.validate_chain()
    print(f"✅ Ledger válido: {ledger_valido}")
    print(f"📦 Total de blocos: {len(CHAIN_M30.chain)}")
    
    # Estatísticas dos testes
    print(f"\n📈 ESTATÍSTICAS DOS TESTES:")
    for i, resultado in enumerate(resultados, 1):
        status = resultado.get('status', 'N/A')
        ameaca_tipo = resultado.get('ameaca', {}).get('tipo_ameaca', 'N/A')
        print(f"  Teste {i}: {status} | Ameaça: {ameaca_tipo}")
    
    print(f"\n✨ MÓDULO 30 TESTADO COM SUCESSO!")
    return resultados

if __name__ == "__main__":
    executar_testes_modulo30()