#!/usr/bin/env python3
# MÓDULO 33: DIRETRIZES DO OBSERVADOR DIVINO · Fundação Alquimista
# Versão 2.1 (Definitivo) – Oráculo ético-vibracional com:
# - Equações vivas (EQTP, EQ019, EQ177, EQ112, EQ134)
# - Ledger interno
# - VERITAS (M44) padronizado
# - Propostas no CONCILIVM (M45) com prioridade inteligente (energia/tema)
# - Relatório ampliado (pilares_raw, freq_equalizada)
# - Maturidade variável por intenção (context-aware)

import math
import hashlib
import json
import random
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple

# ───────────────────────────── 0. CONSTANTES FUNDAMENTAIS ─────────────────────
PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
CONST_TF = 1.61803398875
C_LIGHT = 299792458
H_BAR = 1.054571817e-34

COERENCIA_COSMICA = 1.414
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
ETHICAL_CONFORMITY_THRESHOLD = 0.75
ETHICAL_THRESHOLD_DEFAULT = 0.69
ETHICAL_THRESHOLD_HIGH = 0.85

EQ019_LIMIAR = 0.60
RHO_ALERTA_TECNICO = 0.15
SEVERIDADE_ALERTA = 0.75
SEVERIDADE_CRITICO = 0.85

PESOS_PILARES = (0.30, 0.30, 0.25, 0.15)
VIRTUDES_PADRAO = {"amor": 0.92, "gratidão": 0.90, "verdade": 0.91, "compaixao": 0.89}

# Temas críticos para prioridade Alta quando a diretriz toca o sistema
TEMAS_SISTEMICOS_CRITICOS = {
    "Integridade Operacional": ["integridade", "operacional", "conformidade", "segurança"],
    "Harmonia Coletiva": ["harmonia", "coletiva", "unidade", "coerência"],
    "Proteção Cósmica": ["proteção", "defesa", "ameaça", "risco"],
    "Portais/Temporal": ["portal", "temporal", "linhas do tempo", "travessia"]
}

# ───────────────────────────── 1. SISTEMA DE LOG ──────────────────────────────
class LoggerM33:
    def __init__(self, nome: str):
        self.nome = nome

    def info(self, mensagem: str):
        print(f"✨ {datetime.utcnow().isoformat()} | INFO | {self.nome} | {mensagem}")

    def warning(self, mensagem: str):
        print(f"⚠️ {datetime.utcnow().isoformat()} | WARNING | {self.nome} | {mensagem}")

    def error(self, mensagem: str):
        print(f"❌ {datetime.utcnow().isoformat()} | ERROR | {self.nome} | {mensagem}")

log = LoggerM33("M33_OBSERVADOR_DIVINO")

# ───────────────────────────── 2. REGISTRY DE EQUAÇÕES ────────────────────────
class EquationsRegistryM33:
    _eq: Dict[str, Any] = {}
    @classmethod
    def register(cls, code: str, fn):
        cls._eq[code] = fn
        log.info(f"Equação '{code}' registrada")
    @classmethod
    def get(cls, code: str):
        if code not in cls._eq: raise KeyError(f"Equação '{code}' não registrada")
        return cls._eq[code]

def EQTP(ctx: dict) -> float:
    score = ctx.get("ethical_alignment_score", 0.0)
    if score >= CONST_AMOR_INCONDICIONAL_VALOR: return 1.0
    if score >= ETHICAL_CONFORMITY_THRESHOLD: return 0.5
    return 0.0

def EQ019(pilares: List[float], pesos: Tuple[float, float, float, float] = PESOS_PILARES) -> float:
    total = sum(p * c for p, c in zip(pesos, pilares))
    return float(min(max(total, 0.0), 0.999999999))

def EQ177(freq_origem: float, freq_destino: float, sigma: float = 150.0) -> float:
    delta = abs(freq_origem - freq_destino)
    prob = math.exp(-(delta**2) / (2.0 * sigma**2))
    return float(min(max(prob, 0.0), 1.0))

def EQ112(inteligencia_modular: float, interdependencia: float, phi: float = CONST_TF) -> float:
    return min((inteligencia_modular * interdependencia) + phi, 10.0)

def EQ134(virtudes: Dict[str, float], consciencia_emergente: float) -> float:
    c_ativa = max(1e-6, consciencia_emergente / 10.0)
    log_prod = sum(math.log(max(v, 1e-6)) for v in virtudes.values())
    energia_log = math.log(1e5) + log_prod
    return float(math.exp(c_ativa * energia_log))

for code, fn in {"EQTP": EQTP, "EQ019": EQ019, "EQ177": EQ177, "EQ112": EQ112, "EQ134": EQ134}.items():
    EquationsRegistryM33.register(code, fn)

# ───────────────────────────── 3. LEDGER INTERNO ──────────────────────────────
class SimpleChainM33:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self._create_genesis_block()
    def _normalize_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
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
        genesis_payload = {"message": "Bloco genesis do M33 - Observador Divino"}
        genesis = {"index": 0, "timestamp": datetime.utcnow().isoformat() + "Z",
                   "event": "GENESIS", "payload": self._normalize_payload(genesis_payload),
                   "prev_hash": "0"*64}
        genesis["hash"] = self._calculate_hash(genesis)
        self.chain.append(genesis)
        log.info("Genesis block criado")
    def add(self, event: str, payload: Dict[str, Any]):
        prev_block = self.chain[-1]
        block_payload = self._normalize_payload(payload)
        block = {"index": len(self.chain), "timestamp": datetime.utcnow().isoformat() + "Z",
                 "event": event, "payload": block_payload, "prev_hash": prev_block["hash"]}
        block["hash"] = self._calculate_hash(block)
        self.chain.append(block)
        log.info(f"Evento '{event}' registrado no ledger (bloco #{block['index']})")
    def validate_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]; previous = self.chain[i-1]
            if current["prev_hash"] != previous["hash"]:
                log.error(f"Encadeamento inválido no bloco #{i}"); return False
            if current["hash"] != self._calculate_hash(current):
                log.error(f"Hash inválido no bloco #{i}"); return False
        log.info("Ledger validado com sucesso"); return True

CHAIN_M33 = SimpleChainM33()

# ───────────────────────────── 4. INTEGRAÇÕES SIMULADAS ───────────────────────
def _cht_hash(action_id: str, timestamp_utc: str, metadata_json: str, member_guid: str) -> str:
    data_string = f"{action_id}:{timestamp_utc}:{metadata_json}:{member_guid}"
    return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

class M44_VERITAS:
    def add_event(self, event_type: str, payload: Dict[str, Any]):
        # Padronização: M33_INIT, M33_GATE, M33_EQ019, M33_COMPAT, M33_EGAL, M33_PROPOSTA, M33_DIRETRIZ_EMITIDA, M33_AUDIT, M33_ABORT
        h = _cht_hash(event_type, datetime.utcnow().isoformat() + "Z", json.dumps(payload, sort_keys=True), "M33_AUTOMATION")
        CHAIN_M33.add("M44_EVENT", {"event_type": event_type, "payload": payload, "cht_hash": h})
        return {"status": "recorded", "cht_hash": h}

class M45_CONCILIVM:
    def create_proposal(self, title: str, description: str, proposed_by: str, priority: str = "Alta", category: str = "Diretriz"):
        pid = hashlib.sha256(f"{title}:{datetime.utcnow().isoformat()}".encode('utf-8')).hexdigest()[:8]
        payload = {"id": pid, "title": title, "description": description, "proposed_by": proposed_by, "priority": priority, "category": category}
        CHAIN_M33.add("M45_PROPOSAL", payload)
        return payload
    def finalize(self, proposal_id: str, outcome: str):
        CHAIN_M33.add("M45_FINALIZE", {"proposal_id": proposal_id, "outcome": outcome})
        return {"status": "decree", "proposal_id": proposal_id, "outcome": outcome}

class M7_CONSELHO:
    def consultar(self, query: str) -> str:
        CHAIN_M33.add("M7_CONSULT", {"query": query})
        return "Diretriz: Integridade, serviço ao bem maior e coerência vibracional."

class M9_DASHBOARD:
    def alertar(self, nivel: str, mensagem: str, contexto: Dict[str, Any]):
        CHAIN_M33.add("M9_ALERTA", {"nivel": nivel, "mensagem": mensagem, "contexto": contexto})
        return {"status": "exibido"}

class M28_HARMONIA:
    def equalizar(self, frequencia_alvo: float):
        CHAIN_M33.add("M28_EQUALIZAR", {"frequencia_alvo": frequencia_alvo})
        return {"status": "HARMONIZADO", "frequencia_ajustada": frequencia_alvo}

class M1_CRONICA:
    def registrar(self, registro_data: Dict[str, Any]) -> str:
        registro_hash = hashlib.sha256(json.dumps(registro_data, sort_keys=True).encode()).hexdigest()
        CHAIN_M33.add("M1_REGISTRO", {"hash": registro_hash, **registro_data})
        return registro_hash

# ───────────────────────────── 5. CLASSE DO MÓDULO 33 ─────────────────────────
class Modulo33_ObservadorDivino:
    def __init__(self, modulo_id: str):
        self.modulo_id = modulo_id
        self.status_operacional = "ATIVO"
        self.m44 = M44_VERITAS(); self.m45 = M45_CONCILIVM()
        self.m7 = M7_CONSELHO(); self.m9 = M9_DASHBOARD()
        self.m28 = M28_HARMONIA(); self.m1 = M1_CRONICA()
        self.frequencias_referencia = [432.0, 528.0, 639.0, 963.0]
        CHAIN_M33.add("M33_INIT", {"modulo": modulo_id, "status": "SUCESSO"})
        self.m44.add_event("M33_INIT", {"modulo": modulo_id, "status": "SUCESSO"})
        log.info(f"'{modulo_id}' inicializado – Oráculo ético-vibracional pronto")

    # ——— Utilitários de avaliação ———
    def _gate_etico(self, etica_global: float) -> float:
        gate = EquationsRegistryM33.get("EQTP")({"ethical_alignment_score": etica_global})
        CHAIN_M33.add("M33_GATE", {"etica_global": etica_global, "gate": gate})
        self.m44.add_event("M33_GATE", {"etica_global": etica_global, "gate": gate})
        return gate

    def _coerencia_pilares(self, pilares: List[float]) -> float:
        eq019 = EquationsRegistryM33.get("EQ019")(pilares)
        CHAIN_M33.add("M33_EQ019", {"pilares": pilares, "eq019": eq019})
        self.m44.add_event("M33_EQ019", {"pilares": pilares, "eq019": eq019})
        return eq019

    def _maturidade_contextual(self, intencao: str, base_inteligencia: float, base_interdependencia: float) -> float:
        # Ajusta maturidade baseado na intenção (temas sistêmicos aumentam interdependência)
        boost_inteligencia = 0.0
        boost_interdep = 0.0
        lowered = 0.0
        texto = intencao.lower()
        # Penaliza intenções egoicas
        if any(k in texto for k in ["dominação", "apoderar", "acumulo de poder", "explorar"]):
            lowered = 0.15
        # Aumenta maturidade em temas sistêmicos
        for _, keywords in TEMAS_SISTEMICOS_CRITICOS.items():
            if any(k in texto for k in keywords):
                boost_interdep += 0.05
                boost_inteligencia += 0.03
        inteligencia = max(0.1, min(1.0, base_inteligencia + boost_inteligencia - lowered))
        interdep = max(0.1, min(1.0, base_interdependencia + boost_interdep - lowered))
        maturidade = EquationsRegistryM33.get("EQ112")(inteligencia, interdep)
        CHAIN_M33.add("M33_MATURIDADE", {"intencao": intencao, "inteligencia_modular": inteligencia,
                                          "interdependencia": interdep, "maturidade": maturidade})
        return maturidade

    def _energia_integrada(self, virtudes: Dict[str, float], maturidade: float) -> float:
        energia = EquationsRegistryM33.get("EQ134")(virtudes, maturidade)
        CHAIN_M33.add("M33_ENERGIA", {"virtudes": virtudes, "maturidade": maturidade, "energia_integrada": energia})
        return energia

    def _compatibilidade_dimensional(self, freq_diretriz: float) -> Dict[str, float]:
        probs = [EquationsRegistryM33.get("EQ177")(freq_diretriz, alvo) for alvo in self.frequencias_referencia]
        melhor = max(probs) if probs else 0.0
        alvo_idx = probs.index(melhor) if probs else 0
        freq_alvo = self.frequencias_referencia[alvo_idx] if probs else 432.0
        CHAIN_M33.add("M33_COMPAT", {"freq_diretriz": freq_diretriz, "freq_alvo": freq_alvo, "compatibilidade": melhor})
        self.m44.add_event("M33_COMPAT", {"freq_diretriz": freq_diretriz, "freq_alvo": freq_alvo, "compatibilidade": melhor})
        return {"alvo": freq_alvo, "compatibilidade": melhor}

    # ——— Emissão, equalização e deliberação ———
    def _emitir_diretriz(self, texto: str, nivel: str, contexto: Dict[str, Any]):
        self.m9.alertar(nivel, texto, contexto)
        self.m44.add_event("M33_DIRETRIZ_EMITIDA", {"texto": texto, "nivel": nivel, "contexto": contexto})
        registro_hash = self.m1.registrar({"modulo": self.modulo_id, "evento": "DiretrizEmitida", "texto": texto, "contexto": contexto})
        return {"status": "EMITIDA", "hash_registro": registro_hash}

    def _equalizar_se_necessario(self, compat: Dict[str, float], limiar: float = 0.25) -> Optional[Dict[str, Any]]:
        if compat["compatibilidade"] < limiar:
            res = self.m28.equalizar(compat["alvo"])
            self.m44.add_event("M33_EGAL", {"freq_equalizada": compat["alvo"], "status": res["status"]})
            return res
        return None

    def _deliberar_diretriz(self, texto: str, prioridade: str = "Alta") -> Dict[str, Any]:
        prop = self.m45.create_proposal(title=f"Diretriz M33: {texto[:40]}", description=texto, proposed_by="M33_ORACULO", priority=prioridade, category="Diretriz")
        self.m44.add_event("M33_PROPOSTA", prop)
        return prop

    # ——— Lógica de prioridade inteligente ———
    def _prioridade_por_contexto(self, intencao: str, energia_integrada: float, coerencia_pilares: float, compat: float) -> str:
        texto = intencao.lower()
        tema_critico = any(k in texto for words in TEMAS_SISTEMICOS_CRITICOS.values() for k in words)
        alta_por_energia = energia_integrada > 1e4  # limiar ilustrativo para energia elevada
        baixa_compat = compat < RHO_ALERTA_TECNICO
        baixa_coerencia = coerencia_pilares < 0.65
        if tema_critico or alta_por_energia or baixa_compat or baixa_coerencia:
            return "Alta"
        return "Médio"

    # ——— Pipeline: gerar, validar e emitir ———
    def gerar_e_emitir_diretriz(self, intencao: str, etica_global: float, pilares: List[float],
                                 virtudes: Optional[Dict[str, float]] = None,
                                 inteligencia_modular: float = 0.9, interdependencia: float = 0.85,
                                 freq_diretriz: float = 432.0) -> Dict[str, Any]:
        log.info(f"=== INICIANDO DIRETRIZ M33: '{intencao}' ===")

        consulta = self.m7.consultar(f"Diretriz para: {intencao}")
        gate = self._gate_etico(etica_global)
        if gate == 0.0:
            bloqueio = {"status": "BLOQUEADA", "motivo": "Gate ético fechado", "intencao": intencao}
            self.m44.add_event("M33_ABORT", bloqueio)
            return bloqueio

        coerencia = self._coerencia_pilares(pilares)
        if coerencia < EQ019_LIMIAR:
            evento = {"status": "ABORTADA", "motivo": "Coerência dos pilares insuficiente", "eq019": coerencia, "pilares_raw": pilares}
            self.m44.add_event("M33_ABORT", evento)
            return evento

        maturidade = self._maturidade_contextual(intencao, inteligencia_modular, interdependencia)
        energia = self._energia_integrada(virtudes or VIRTUDES_PADRAO, maturidade)
        compat = self._compatibilidade_dimensional(freq_diretriz)
        equalizacao = self._equalizar_se_necessario(compat)

        prioridade = self._prioridade_por_contexto(intencao, energia_integrada=energia, coerencia_pilares=coerencia, compat=compat["compatibilidade"])
        proposta = self._deliberar_diretriz(intencao, prioridade)

        nivel = "INFO"
        if compat["compatibilidade"] < RHO_ALERTA_TECNICO: nivel = "ALERTA"
        contexto = {
            "intencao": intencao,
            "etica_global": etica_global,
            "pilares_raw": pilares,
            "coerencia_pilares": coerencia,
            "maturidade": maturidade,
            "energia_integrada": energia,
            "compatibilidade_dimensional": compat,
            "consulta_conselho": consulta,
            "freq_equalizada": (equalizacao or {}).get("frequencia_ajustada"),
            "prioridade_concilium": prioridade
        }
        emissao = self._emitir_diretriz(intencao, nivel, contexto)

        auditoria = {
            "intencao": intencao,
            "etica_global": etica_global,
            "eq019": coerencia,
            "pilares_raw": pilares,
            "maturidade": maturidade,
            "energia_integrada": energia,
            "compatibilidade": compat,
            "consulta_conselho": consulta,
            "proposta_concilium": proposta,
            "emissao": emissao,
            "freq_equalizada": (equalizacao or {}).get("frequencia_ajustada")
        }
        self.m44.add_event("M33_AUDIT", auditoria)
        self.m45.finalize(proposta["id"], outcome="DiretrizEmitida")

        relatorio = {
            "status": "DIRETRIZ_CONCLUIDA",
            "intencao": intencao,
            "pilares_raw": pilares,
            "coerencia_pilares": coerencia,
            "maturidade": maturidade,
            "energia_integrada": energia,
            "compatibilidade_dimensional": compat,
            "freq_equalizada": (equalizacao or {}).get("frequencia_ajustada"),
            "proposta_concilium": proposta,
            "emissao": emissao
        }
        CHAIN_M33.add("M33_RELATORIO", relatorio)
        log.info(f"=== DIRETRIZ M33 CONCLUÍDA: '{intencao}' ===")
        return relatorio

# ───────────────────────────── 6. TESTES DO MÓDULO 33 ─────────────────────────
def executar_testes_modulo33():
    print("🧪 MÓDULO 33: DIRETRIZES DO OBSERVADOR DIVINO (v2.1 Definitivo)")
    print("=" * 92)

    m33 = Modulo33_ObservadorDivino("M33_ORACULO_INTERNO")

    cenarios = [
        {"intencao": "Sustentar a Harmonia Coletiva", "etica": 0.95, "pilares": [0.88, 0.92, 0.90, 0.85], "virtudes": VIRTUDES_PADRAO, "freq": 432.0},
        {"intencao": "Reforçar Integridade Operacional", "etica": 0.80, "pilares": [0.75, 0.78, 0.72, 0.70], "virtudes": {"amor": 0.88, "gratidão": 0.85, "verdade": 0.86, "compaixao": 0.84}, "freq": 639.0},
        {"intencao": "Acesso não ético a recursos", "etica": 0.60, "pilares": [0.80, 0.82, 0.79, 0.77], "virtudes": {"amor": 0.75, "gratidão": 0.74, "verdade": 0.76, "compaixao": 0.73}, "freq": 528.0}
    ]

    resultados = []
    for c in cenarios:
        print(f"\n🌟 DIRETRIZ: {c['intencao']} (Ética: {c['etica']})")
        print("-" * 60)
        resultado = m33.gerar_e_emitir_diretriz(
            intencao=c["intencao"],
            etica_global=c["etica"],
            pilares=c["pilares"],
            virtudes=c["virtudes"],
            inteligencia_modular=0.9,
            interdependencia=0.85,
            freq_diretriz=c["freq"]
        )
        resultados.append(resultado)
        print("📊 RESULTADO:")
        print(f" Status: {resultado.get('status', 'N/A')}")
        print(f" EQ019 (pilares): {resultado.get('coerencia_pilares', 0.0):.3f}")
        print(f" Maturidade: {resultado.get('maturidade', 0.0):.2f}")
        compat = resultado.get('compatibilidade_dimensional', {"compatibilidade": 0.0})
        print(f" Compatibilidade: {compat.get('compatibilidade', 0.0):.3f}")
        print(f" Prioridade: {resultado.get('proposta_concilium', {}).get('priority', 'N/A')}")
        print(f" Freq equalizada: {resultado.get('freq_equalizada', '—')}")

    print(f"\n{'='*92}")
    print("🔍 VALIDAÇÃO FINAL DO LEDGER")
    print(f"{'='*92}")
    ledger_valido = CHAIN_M33.validate_chain()
    print(f"✅ Ledger válido: {ledger_valido}")
    print(f"📦 Total de blocos: {len(CHAIN_M33.chain)}")

    print("\n📈 ESTATÍSTICAS:")
    for i, r in enumerate(resultados, 1):
        status = r.get('status', 'N/A')
        print(f" Teste {i}: {status}")

    print("\n✨ MÓDULO 33 (Definitivo) TESTADO COM SUCESSO!")
    return resultados

# ───────────────────────────── 7. ENTRYPOINT ──────────────────────────────────
if __name__ == "__main__":
    executar_testes_modulo33()
