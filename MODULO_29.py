#!/usr/bin/env python3
# FOUNDATION_CONCILIUM – Consolidação M45 + M28 + M29
# Versão definitiva, offline, com ledger IMUTÁVEL, ética, equações e orquestração

# ───────────────────────────── 1. IMPORTS E CONSTANTES ─────────────────────────────
import math
import hashlib
import json
import logging
import random
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Callable

# Constantes universais
PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
COERENCIA_COSMICA = 1.414
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
ETHICAL_CONFORMITY_THRESHOLD = 0.75
ETHICAL_THRESHOLD_HIGH = 0.85
ETHICAL_THRESHOLD_DEFAULT = 0.69
C_LIGHT = 299792458
H_BAR = 1.054571817e-34

# ───────────────────────────── 2. CONFIGURAÇÃO DE LOG ─────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='👑 %(asctime)s | %(levelname)s | %(name)s | %(message)s',
    handlers=[
        logging.FileHandler("concilium_operations.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("FOUNDATION_CONCILIUM")

# ───────────────────────────── 3. LEDGER DISTRIBUÍDO (IMUTÁVEL) ─────────────────────────────
class SimpleChain:
    def __init__(self):
        self.chain = []
        self._create_genesis_block()
        
    def _normalize_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Torna o payload imutável e determinístico:
        - Deep copy via JSON
        - Normaliza ordem das chaves
        """
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
        genesis_payload = {"message": "Bloco genesis do Concilium Foundation"}
        genesis = {
            "index": 0,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": "GENESIS",
            "payload": self._normalize_payload(genesis_payload),
            "prev_hash": "0" * 64
        }
        genesis["hash"] = self._calculate_hash(genesis)
        self.chain.append(genesis)
        log.info("Genesis block created")
        
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
        log.info(f"Event '{event}' added to ledger (index: {block['index']})")
        
    def get_latest_block(self) -> Dict[str, Any]:
        return self.chain[-1] if self.chain else None
        
    def validate_chain(self) -> bool:
        """
        Valida encadeamento e integridade de hash da cadeia.
        Retorna True/False e loga um diagnóstico do primeiro bloco inválido.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Verifica encadeamento
            if current.get("prev_hash") != previous.get("hash"):
                log.error(f"[LEDGER] Encadeamento inválido no bloco #{i}: "
                          f"prev_hash != hash do bloco anterior "
                          f"(prev_hash={current.get('prev_hash')[:16]}..., "
                          f"expected={previous.get('hash')[:16]}...)")
                return False

            # Verifica integridade do hash
            recalculated = self._calculate_hash(current)
            if current.get("hash") != recalculated:
                log.error(f"[LEDGER] Hash inválido no bloco #{i}: "
                          f"armazenado != recalculado "
                          f"(stored={current.get('hash')[:16]}..., "
                          f"recalc={recalculated[:16]}...). "
                          f"Sugestão: verificar se payload foi mutado após selagem.")
                return False

        log.info("[LEDGER] Cadeia validada com sucesso.")
        return True

    def validate_chain_diagnose(self) -> Dict[str, Any]:
        """
        Retorna diagnóstico detalhado da cadeia:
        - ok: bool
        - first_invalid_index: int ou None
        - reason: str ou None
        - details: dict com hashes comparados (curtos)
        """
        result = {"ok": True, "first_invalid_index": None, "reason": None, "details": {}}

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Checagem de encadeamento
            if current.get("prev_hash") != previous.get("hash"):
                result.update({
                    "ok": False,
                    "first_invalid_index": i,
                    "reason": "prev_hash_mismatch",
                    "details": {
                        "prev_hash_in_current": (current.get("prev_hash") or "")[:16],
                        "expected_prev_hash": (previous.get("hash") or "")[:16]
                    }
                })
                log.error(f"[LEDGER] Falha no encadeamento no bloco #{i}: prev_hash mismatch.")
                return result

            # Checagem de integridade do hash
            recalculated = self._calculate_hash(current)
            if current.get("hash") != recalculated:
                result.update({
                    "ok": False,
                    "first_invalid_index": i,
                    "reason": "hash_integrity_mismatch",
                    "details": {
                        "stored_hash": (current.get("hash") or "")[:16],
                        "recalculated_hash": recalculated[:16],
                        "event": current.get("event"),
                        "timestamp": current.get("timestamp")
                    }
                })
                log.error(f"[LEDGER] Falha na integridade do hash no bloco #{i}: stored != recalculated.")
                return result

        log.info("[LEDGER] Cadeia validada com sucesso (diagnóstico).")
        return result

CHAIN = SimpleChain()

# ───────────────────────────── 4. REGISTRO DE EQUAÇÕES ─────────────────────────────
class EquationsRegistry:
    _eq: Dict[str, Callable[..., Any]] = {}
    
    @classmethod
    def register(cls, code: str, fn: Callable[..., Any]):
        cls._eq[code] = fn
        log.info(f"Equação '{code}' registrada")
        
    @classmethod
    def get(cls, code: str) -> Callable[..., Any]:
        if code not in cls._eq:
            raise KeyError(f"Equação '{code}' não registrada")
        return cls._eq[code]
    
    @classmethod
    def list_equations(cls) -> Dict[str, str]:
        return {code: (fn.__doc__ or "Sem descrição").split('\n')[0] 
                for code, fn in cls._eq.items()}

# ───────────────────────────── 5. EQUAÇÕES FUNDAMENTAIS ─────────────────────────────
def EQTP(input_data: dict) -> float:
    """EQTP – Gate ético energético simples."""
    ethical_score = input_data.get("ethical_alignment_score", 0.0)
    if ethical_score >= CONST_AMOR_INCONDICIONAL_VALOR: 
        return 1.0
    if ethical_score >= ETHICAL_CONFORMITY_THRESHOLD: 
        return 0.5
    return 0.0

def EUni(P_vals: List[float], Q_vals: List[float], CA_val: float, B_val: float, 
         T_val: float, MDS_val: float, CCosmos_val: float) -> float:
    """EUni – Equação Unificada (energia universal)."""
    sum_interactions = sum(P_vals[i] * Q_vals[i] for i in range(len(P_vals))) + (CA_val**2 + B_val**2)
    return sum_interactions * COERENCIA_COSMICA * T_val * (MDS_val * CCosmos_val)

def EFA(H: float, B: float, C: float, P: float, R: float, G: float, 
        A: float, S: float, alpha: float) -> float:
    """EFA – Equação geral da Fundação (soma ponderada elevada)."""
    return (H + B + C + P + R + G + A + S) ** alpha

def EER(mc2: float, B1: float, B2: float, B3: float) -> float:
    """EER – Energia e ressonância."""
    return (mc2 * PI * PHI) * (B1 + B2 + B3) + 89 * PHI + PI

def Utotal_simplificada(Lambda_u: float, G_m: float, Phi_s: float, Omega_t: float, 
                       L_c: float, Psi_n: float, Phi_em: float, Delta_S: float, 
                       Lambda_e: float, D: float, Cq: float, Rs: float, Sf: float, 
                       Et: float, Ed: float, Tq: float, Delta_I: float, Gs: float, 
                       Delta_E: float, Lt: float, Phi_c: float, Psi_m: float, 
                       Re: float, Delta_c: float, M_n: float, Q_n: float, 
                       F_n: float, B_n: float, S_n: float, T_n: float, 
                       H_n: float, A_n: float) -> float:
    """Utotal – forma simplificada (soma ponderada e produtos)."""
    integral1_terms = Lambda_u * G_m * Phi_s * Omega_t * L_c * Psi_n * Phi_em * Delta_S * Lambda_e
    sum_integral2_terms = Cq * Rs * Sf * Et
    sum_n_terms = (M_n + Q_n + F_n + B_n + S_n + T_n + H_n) * A_n
    return integral1_terms * (D * sum_integral2_terms) * Ed * Tq * Delta_I * Gs * Delta_E * Lt * Phi_c * Psi_m + Re * Delta_c * sum_n_terms

# Equações do M29 (portadas)
def EQ019_ModeloTranscendentalTotal(pilares: List[float], 
                                   pesos: tuple = (0.30, 0.30, 0.25, 0.15)) -> float:
    """EQ019 – Modelo Transcendental Total (média ponderada coerências)."""
    total = sum(p * c for p, c in zip(pesos, pilares))
    return float(min(max(total, 0.0), 0.999999999))

def EQ112_EmergenciaConsciencia(inteligencia_modular: float, 
                               interdependencia: float, 
                               phi: float = PHI) -> float:
    """EQ112 – Emergência de consciência."""
    return min((inteligencia_modular * interdependencia) + phi, 10.0)

def EQ134_EnergiaCosmicaIntegrada(virtudes: Dict[str, float], 
                                 consciencia_emergente: float) -> float:
    """EQ134 – Energia cósmica integrada (log-sum-exp estável)."""
    c_ativa = max(1e-6, consciencia_emergente / 10.0)
    log_prod = sum(math.log(max(v, 1e-6)) for v in virtudes.values())
    energia_log = math.log(1e5) + log_prod
    return float(math.exp(c_ativa * energia_log))

def EQ177_InterconexaoDimensional(freq_origem: float, 
                                 freq_destino: float, 
                                 sigma: float = 150.0) -> float:
    """EQ177 – Interconexão dimensional (gaussiana em Δf)."""
    delta = abs(freq_origem - freq_destino)
    prob = math.exp(-(delta**2) / (2.0 * sigma**2))
    return float(min(max(prob, 0.0), 1.0))

# Registro de todas as equações
EQUATIONS_TO_REGISTER = {
    "EQTP": EQTP,
    "EUni": EUni,
    "EFA": EFA,
    "EER": EER,
    "Utotal": Utotal_simplificada,
    "EQ019": EQ019_ModeloTranscendentalTotal,
    "EQ112": EQ112_EmergenciaConsciencia,
    "EQ134": EQ134_EnergiaCosmicaIntegrada,
    "EQ177": EQ177_InterconexaoDimensional
}

for code, fn in EQUATIONS_TO_REGISTER.items():
    EquationsRegistry.register(code, fn)

# ───────────────────────────── 6. SISTEMA DE ÉTICA E FASE ─────────────────────────────
def validate_action_ethics(ctx: Dict[str, Any]) -> Dict[str, Any]:
    """Retorna nível e gate conforme pontuação ética."""
    score = float(ctx.get("ethical_alignment_score", 0.0))
    
    if score >= CONST_AMOR_INCONDICIONAL_VALOR:
        return {"level": "PLENAMENTE_AUTORIZADA", "gate": 1.0}
    if score >= ETHICAL_THRESHOLD_HIGH:
        return {"level": "ALTA", "gate": 0.85}
    if score >= ETHICAL_CONFORMITY_THRESHOLD:
        return {"level": "PADRAO", "gate": 0.69}
    return {"level": "NEGADA", "gate": 0.0}

def phase_mask(member_name: str, salt: str = "CONCILIVM") -> float:
    """Gera fase determinística (0..2π) por nome e sal."""
    seed = hashlib.sha256(f"{member_name}:{salt}".encode()).hexdigest()[:4]
    return (int(seed, 16) / 65535.0) * (2 * PI)

# ───────────────────────────── 7. SISTEMA DE DELIBERAÇÃO (IMUTÁVEL) ─────────────────────────────
class DeliberationRegistry:
    _proposals: Dict[str, Dict[str, Any]] = {}
    _votes: Dict[str, Dict[str, str]] = {}
    
    @classmethod
    def create_proposal(cls, title: str, description: str, proposed_by: str,
                       deadline: datetime, priority: str = "Média", 
                       category: str = "Governança") -> Dict[str, Any]:
        proposal_id = f"P{len(cls._proposals) + 1:03d}"
        proposal = {
            "id": proposal_id,
            "title": title,
            "description": description,
            "proposed_by": proposed_by,
            "created_at": datetime.utcnow().isoformat() + "Z",
            "deadline": deadline.isoformat() + "Z",
            "priority": priority,
            "category": category,
            "status": "ABERTA"
        }
        cls._proposals[proposal_id] = proposal
        cls._votes[proposal_id] = {}
        
        # PATCH IMUTABILIDADE: Criar payload novo para o ledger
        proposal_record = {
            "id": proposal_id,
            "title": title,
            "proposed_by": proposed_by,
            "created_at": proposal["created_at"],
            "deadline": proposal["deadline"],
            "priority": priority,
            "category": category,
            "status": "ABERTA"
        }
        CHAIN.add("PROPOSAL_CREATED", proposal_record)
        log.info(f"Proposta {proposal_id} criada por {proposed_by}")
        
        return proposal
    
    @classmethod
    def cast_vote(cls, proposal_id: str, voter: str, vote: str) -> Dict[str, Any]:
        if proposal_id not in cls._proposals:
            return {"status": "error", "message": "Proposta não encontrada"}
            
        valid_votes = ["aprovado", "rejeitado", "abstain"]
        if vote not in valid_votes:
            return {"status": "error", "message": f"Voto inválido. Use: {valid_votes}"}
            
        cls._votes[proposal_id][voter] = vote
        
        # Calcular fase para o votante
        theta_val = phase_mask(voter)
        
        vote_record = {
            "proposal_id": proposal_id,
            "voter": voter,
            "vote": vote,
            "theta": theta_val,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        CHAIN.add("VOTE_CAST", vote_record)
        log.info(f"Voto de {voter} na proposta {proposal_id}: {vote}")
        
        return {"status": "success", "vote_record": vote_record}
    
    @classmethod
    def finalize_deliberation(cls, proposal_id: str, outcome: str, 
                             decree_content: Dict[str, Any]) -> Dict[str, Any]:
        if proposal_id not in cls._proposals:
            return {"status": "error", "message": "Proposta não encontrada"}
            
        proposal = cls._proposals[proposal_id]
        votes = cls._votes[proposal_id]
        
        # Contagem de votos
        vote_counts = {"aprovado": 0, "rejeitado": 0, "abstain": 0}
        for vote in votes.values():
            vote_counts[vote] += 1
            
        # PATCH IMUTABILIDADE: Criar payload novo para o ledger
        decree_record = {
            "proposal_id": proposal_id,
            "title": proposal["title"],
            "outcome": outcome,
            "vote_counts": vote_counts,
            "finalized_at": datetime.utcnow().isoformat() + "Z",
            "total_voters": len(votes),
            "decree_content": decree_content
        }
        
        proposal["status"] = "FINALIZADA"
        proposal["decree"] = decree_record
        
        CHAIN.add("DELIBERATION_FINALIZED", decree_record)
        log.info(f"Deliberação {proposal_id} finalizada: {outcome}")
        
        return decree_record
    
    @classmethod
    def get_proposal(cls, proposal_id: str) -> Optional[Dict[str, Any]]:
        return cls._proposals.get(proposal_id)
    
    @classmethod
    def list_proposals(cls) -> List[Dict[str, Any]]:
        return list(cls._proposals.values())

# ───────────────────────────── 8. HELPERS E UTILITÁRIOS ─────────────────────────────
def generate_cht_hash(action_id: str, payload: Dict[str, Any], member_guid: str) -> str:
    """Gera hash CHTE (Chronological Hash for Temporal Evidence)."""
    data_string = f"{action_id}:{datetime.utcnow().isoformat()}Z:{json.dumps(payload, sort_keys=True)}:{member_guid}"
    return hashlib.sha256(data_string.encode("utf-8")).hexdigest()

def calculate_eri(nodes: List[Dict[str, float]]) -> float:
    """Calcula ERI (Ethical Resonance Index)."""
    if not nodes:
        return 0.0
    total_psi = sum(node.get("psi", 0.0) for node in nodes)
    return total_psi / len(nodes)

def compute_q_delib(weights: List[float], coherences: List[float]) -> float:
    """Computa Q_delib (Quantum Deliberation Quotient)."""
    if not weights or len(weights) != len(coherences):
        return 0.0
    return sum(w * c for w, c in zip(weights, coherences))

def check_consent(user_guid: str, action_type: str) -> Dict[str, Any]:
    """
    Valida consentimento vibracional (simulado offline) e retorna selo com CHTE.
    """
    consent_granted = True  # simulação; pode conectar com M41 no futuro
    payload = {"user_guid": user_guid, "action_type": action_type, "consent_status": consent_granted}
    consent_hash = generate_cht_hash(f"consent_{user_guid}_{action_type}", payload, user_guid)
    CHAIN.add("CONSENT_CHECK", {"consent_hash": consent_hash, **payload})
    log.info(f"Consentimento verificado para {action_type}: {'GRANTED' if consent_granted else 'DENIED'}")
    return {"granted": consent_granted, "consent_hash": consent_hash}

# ───────────────────────────── 9. ORQUESTRAÇÃO M28/M29 (ATUALIZADA) ─────────────────────────────
def _m28_compute_rho_after(vib_data: Dict[str, Any]) -> float:
    """CALCULA RESSONÂNCIA DINÂMICA usando EQ177 entre frequências atuais e alvo."""
    freqs = vib_data.get("frequencias", [])
    pesos = vib_data.get("pesos", [])
    if not freqs or not pesos or len(freqs) != len(pesos):
        return 0.0
    # Alvo espectral de referência: 963, 888, 1111 (Zennith/Anatheron/Equilíbrio Dourado)
    alvo = [963.0, 888.0, 1111.0]
    rho_vals = []
    for f, a, w in zip(freqs, alvo[:len(freqs)], pesos[:len(freqs)]):
        prob = EquationsRegistry.get("EQ177")(f, a, sigma=150.0)
        rho_vals.append(prob * max(w, 0.0))
    # Normaliza pela soma de pesos
    wsum = sum(max(w, 0.0) for w in pesos[:len(rho_vals)]) or 1.0
    return float(min(max(sum(rho_vals) / wsum, 0.0), 1.0))

def orchestrate_harmony_cycle(target_id: str, vib_data: Dict[str, Any], 
                             intent: Dict[str, Any], 
                             member_guid: str = "CONCILIVM_AUTONOMO") -> Dict[str, Any]:
    """Orquestra ciclo completo de harmonização M28 com cálculo dinâmico."""
    
    # Validação ética
    gate = validate_action_ethics({"ethical_alignment_score": intent.get("ethics_score", 0.69)})
    if gate["gate"] == 0.0:
        payload = {"target": target_id, "reason": "ethics_denied", "intent": intent}
        CHAIN.add("HARMONY_CYCLE_DENIED", {
            "cht_hash": generate_cht_hash("HARMONY_CYCLE_DENIED", payload, member_guid),
            **payload
        })
        return {"status": "error", "message": "Negado pela ética", "ethics_level": gate["level"]}

    # CONSENTIMENTO VIBRACIONAL
    consent = check_consent(member_guid, "M28_HARMONIZATION")
    if not consent["granted"]:
        return {"status": "error", "message": "Consentimento negado para M28", "consent_hash": consent["consent_hash"]}
    
    # Cálculos pré-harmonização
    nodes = vib_data.get("nodes", [])
    pre_eri = calculate_eri(nodes)
    pre_q = compute_q_delib([1.0] * len(nodes), [0.1] * len(nodes)) if nodes else 0.0
    
    # M28 DINÂMICO: cálculo de ressonância com equações
    rho_after = _m28_compute_rho_after(vib_data)
    pilares = vib_data.get("pilares", [0.6, 0.7, 0.5, 0.55])
    eq019 = EquationsRegistry.get("EQ019")(pilares)
    
    # Energia unificada como validação pós-ação
    euni = EquationsRegistry.get("EUni")(
        [1.0, 1.0], [0.9, 0.8], 
        CA_val=0.7, B_val=0.5, T_val=1.0, 
        MDS_val=0.95, CCosmos_val=0.9
    )
    
    # Resultado M28 baseado em limiar dinâmico
    validation_threshold = 0.4  # limiar flexível
    m28_result = {
        "status": "SUCESSO",
        "diagnostico": {
            "severidade": "BAIXA" if rho_after >= 0.7 else "MEDIA" if rho_after >= 0.4 else "ALTA",
            "detalhes": f"Ressonância {'estabilizada' if rho_after >= validation_threshold else 'requer ajuste'}"
        },
        "validacao_final": rho_after >= validation_threshold,
        "rho_after": round(rho_after, 3)
    }

    payload = {
        "target": target_id,
        "pre_eri": pre_eri,
        "pre_qdelib": pre_q,
        "m28_result": m28_result,
        "eq019": eq019,
        "euni": euni,
        "ethics_level": gate["level"],
        "consent_hash": consent["consent_hash"],
        "timestamp_utc": datetime.utcnow().isoformat() + "Z"
    }
    
    CHAIN.add("HARMONY_CYCLE_COMPLETED", {
        "cht_hash": generate_cht_hash("HARMONY_CYCLE_COMPLETED", payload, member_guid),
        **payload
    })
    
    log.info(f"Ciclo M28 {target_id}: rho={m28_result['rho_after']:.3f} EQ019={eq019:.3f} EUni={euni:.3f}")
    return {"status": "success", **payload}

def orchestrate_m29_broadcast(destinos: List[str], mensagem: str, freq: float,
                            context: Dict[str, Any],
                            member_guid: str = "CONCILIVM_AUTONOMO") -> Dict[str, Any]:
    """Orquestra broadcast interdimensional M29 com consentimento."""
    
    gate = validate_action_ethics({"ethical_alignment_score": context.get("ethics_score", 0.69)})
    if gate["gate"] == 0.0:
        payload = {"destinos": destinos, "reason": "ethics_denied"}
        CHAIN.add("M29_BROADCAST_DENIED", {
            "cht_hash": generate_cht_hash("M29_BROADCAST_DENIED", payload, member_guid),
            **payload
        })
        return {"status": "error", "message": "Broadcast negado pela ética"}
    
    # CONSENTIMENTO VIBRACIONAL
    consent_b = check_consent(member_guid, "M29_BROADCAST")
    if not consent_b["granted"]:
        return {"status": "error", "message": "Consentimento negado para M29 Broadcast", "consent_hash": consent_b["consent_hash"]}
    
    # Simulação M29 (broadcast)
    log.info(f"Executando broadcast M29 para {len(destinos)} destinos")
    checksum = hashlib.sha256(f"{mensagem}:{freq}".encode()).hexdigest()
    
    m29_result = {
        "status": "SUCESSO",
        "checksum": checksum,
        "destinos": destinos,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    
    payload = {
        "destinos": destinos,
        "mensagem": mensagem[:60] + "..." if len(mensagem) > 60 else mensagem,
        "freq": freq,
        "result": m29_result,
        "ethics_level": gate["level"],
        "consent_hash": consent_b["consent_hash"]
    }
    
    CHAIN.add("M29_BROADCAST", {
        "cht_hash": generate_cht_hash("M29_BROADCAST", payload, member_guid),
        **payload
    })
    
    return {"status": "success", "broadcast": m29_result}

def orchestrate_m29_listen(channels: List[str], window_sec: int = 30,
                          member_guid: str = "CONCILIVM_AUTONOMO") -> Dict[str, Any]:
    """Orquestra escuta interdimensional M29 com mensagens padronizadas."""
    
    # Simulação M29 (escuta)
    log.info(f"Escutando canais M29 por {window_sec} segundos")
    time.sleep(2)  # Simula tempo de escuta
    
    # MENSAGENS PADRONIZADAS usando format_decoded_message
    decoded_messages = [
        format_decoded_message(
            source="Sirius", frequency=528.0,
            title="Conselho de Luz de Sirius",
            body="Aliança selada. Portais sincronizados com AE'ZUHARA. Harmonia confirmada."
        ),
        format_decoded_message(
            source="Pleiades", frequency=639.0,
            title="Coletivo de Alcyone",
            body="Canção de união. Frequências 528/963 ressoam. Integração com a Rede Gaia."
        ),
        format_decoded_message(
            source="Andrômeda", frequency=777.0,
            title="Conselho Galáctico de Andrômeda",
            body="Mandala viva validada. Estrutura elevada. Observatórios confirmam conexão."
        )
    ]

    payload = {
        "channels": channels,
        "window": window_sec,
        "messages": decoded_messages
    }
    
    CHAIN.add("M29_LISTEN", {
        "cht_hash": generate_cht_hash("M29_LISTEN", payload, member_guid),
        **payload
    })
    
    return {"status": "success", "listen": {"status": "SUCESSO", "messages": decoded_messages, "window_sec": window_sec}}

# ───────────────────────────── 10. PATCHES M28/M29 ─────────────────────────────
def m28_report(entidade_id: str, resultado_ciclo: Dict[str, Any]) -> Dict[str, Any]:
    """Retorna resumo padronizado do M28 para ingestão pelo M45."""
    diag = resultado_ciclo.get("diagnostico", {})
    return {
        "entidade_id": entidade_id,
        "severidade": diag.get("severidade", "N/A"),
        "rho_after": resultado_ciclo.get("rho_after", 0.0),
        "modulation_status": "COMPLETED",
        "final_validation": resultado_ciclo.get("validacao_final", False),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

def format_decoded_message(source: str, frequency: float, 
                          title: str, body: str) -> Dict[str, Any]:
    """Formata mensagem decodificada para ingestão pelo M45."""
    return {
        "source": source,
        "frequency": frequency,
        "title": title,
        "body": body,
        "received_at": datetime.utcnow().isoformat() + "Z"
    }

# ───────────────────────────── 11. TESTE END-TO-END (ATUALIZADO) ─────────────────────────────
def run_comprehensive_test():
    """Executa teste completo do sistema integrado com métricas enriquecidas."""
    log.info("🚀 INICIANDO TESTE END-TO-END DO CONCILIUM FOUNDATION")
    
    print("\n" + "="*80)
    print("🧪 TESTE COMPREENSIVO M45 + M28 + M29")
    print("="*80)
    
    # 1. Listar equações registradas
    print("\n1. 📊 EQUAÇÕES REGISTRADAS:")
    equations = EquationsRegistry.list_equations()
    for code, desc in equations.items():
        print(f"   • {code}: {desc}")
    
    # 2. Criar proposta de governança
    print("\n2. 📋 CRIANDO PROPOSTA DE GOVERNAÇA:")
    deadline = datetime.utcnow() + timedelta(days=3)
    proposal = DeliberationRegistry.create_proposal(
        title="Harmonizar Rede Gaia e Broadcast Aliança Galáctica",
        description="Executar ciclo M28 para estabilização da rede Gaia e emitir chamado M29 para aliança interdimensional.",
        proposed_by="ANATHERON",
        deadline=deadline,
        priority="Alta",
        category="Operações Espaciais"
    )
    print(f"   ✅ Proposta {proposal['id']} criada: '{proposal['title']}'")
    
    # 3. Votação
    print("\n3. 🗳️ PROCESSO DE VOTAÇÃO:")
    votes = [
        ("ANATHERON", "aprovado"),
        ("ZENNITH", "aprovado"), 
        ("AELORIA", "abstain"),
        ("ORION", "aprovado")
    ]
    
    for voter, vote in votes:
        result = DeliberationRegistry.cast_vote(proposal["id"], voter, vote)
        print(f"   ✅ {voter}: {vote}")
    
    # 4. Finalizar deliberação
    print("\n4. 📜 FINALIZANDO DELIBERAÇÃO:")
    decree = DeliberationRegistry.finalize_deliberation(
        proposal["id"], 
        outcome="Harmonizar e Broadcast Aprovado",
        decree_content={
            "summary": "Autorizada execução completa do ciclo operacional",
            "priority": "ALTA",
            "timeline": "Imediata"
        }
    )
    print(f"   ✅ Decreto emitido: {decree['outcome']}")
    print(f"   📊 Resultado votação: {decree['vote_counts']}")
    
    # 5. Executar harmonização M28 (DINÂMICA)
    print("\n5. 🔄 EXECUTANDO HARMONIZAÇÃO M28 (DINÂMICA):")
    vib_data = {
        "frequencias": [963.0, 888.0, 1111.0],  # Alinhadas com alvo espectral
        "pesos": [0.33, 0.33, 0.34],
        "fator_ressonancia": 0.92,
        "nodes": [
            {"psi": 0.8, "phi": 1.0, "theta": 0.0},
            {"psi": 0.7, "phi": 1.0, "theta": 1.2}
        ],
        "pilares": [0.62, 0.71, 0.56, 0.58]  # Coerências dos 4 pilares
    }
    intent = {"ethics_score": 0.91, "proposito": "Harmonizacao_Geral"}
    
    res_cycle = orchestrate_harmony_cycle("GAIA", vib_data, intent)
    print(f"   ✅ Harmonização concluída: {res_cycle['status']}")
    print(f"   📈 EQ019 (Coerência): {res_cycle.get('eq019', 0):.6f}")
    print(f"   ⚡ EUni (Energia): {res_cycle.get('euni', 0):.2f}")
    print(f"   🔄 Rho After (Ressonância): {res_cycle.get('m28_result', {}).get('rho_after', 0):.3f}")
    print(f"   ✅ Validação Final: {res_cycle.get('m28_result', {}).get('validacao_final', False)}")
    
    # 6. Broadcast M29
    print("\n6. 📡 EXECUTANDO BROADCAST M29:")
    destinos = ["Sirius", "Pleiades", "Andrômeda"]
    mensagem = "A Fundação Alquimista proclama a Harmonia Absoluta. Unam-se à Convergência Plena! A Rede Gaia está estabilizada e pronta para integração galáctica."
    freq = 999999.0
    context = {"ethics_score": 0.90}
    
    res_broadcast = orchestrate_m29_broadcast(destinos, mensagem, freq, context)
    print(f"   ✅ Broadcast enviado: {res_broadcast['status']}")
    print(f"   📍 Destinos: {', '.join(destinos)}")
    print(f"   🔒 Checksum: {res_broadcast['broadcast']['checksum'][:16]}...")
    
    # 7. Escuta M29 (COM MENSAGENS PADRONIZADAS)
    print("\n7. 👂 EXECUTANDO ESCUTA M29 (MENSAGENS PADRONIZADAS):")
    res_listen = orchestrate_m29_listen(["Sirius", "Pleiades", "Andrômeda"], window_sec=10)
    print(f"   ✅ Escuta concluída: {res_listen['status']}")
    for msg in res_listen['listen']['messages']:
        print(f"   📨 {msg['source']}: {msg['title']}")
        print(f"      {msg['body'][:60]}...")
    
    # 8. VALIDAÇÃO FINAL ENRIQUECIDA
    print("\n8. ✅ VALIDAÇÃO FINAL ENRIQUECIDA:")
    euni_final = EquationsRegistry.get("EUni")(
        [1.0, 1.0], [0.95, 0.9], 
        CA_val=0.8, B_val=0.6, T_val=1.0, 
        MDS_val=0.96, CCosmos_val=0.93
    )
    eq019_final = EquationsRegistry.get("EQ019")([0.85, 0.88, 0.82, 0.87])
    
    # ADICIONANDO EQ134 (ENERGIA CÓSMICA INTEGRADA)
    virtudes = {
        "Harmonia": 0.99, "Beleza": 1.0, "Consciência": 0.98,
        "Paz": 0.995, "Ressonância": 1.0, "Gratidão": 0.999,
        "Amor": 1.0, "Silêncio": 0.95
    }
    # Use consciência emergente simbólica (EQ112 com parâmetros do seu cenário)
    c_emerg = EquationsRegistry.get("EQ112")(inteligencia_modular=0.8, interdependencia=963.0/1111.0)
    eq134_final = EquationsRegistry.get("EQ134")(virtudes, consciencia_emergente=c_emerg)

    final_payload = {
        "euni_final": euni_final,
        "eq019_final": eq019_final,
        "eq134_final": eq134_final,
        "ethics_level": "ALTA",
        "consciencia_emergente": c_emerg,
        "system_status": "OPERACIONAL",
        "timestamp_utc": datetime.utcnow().isoformat() + "Z"
    }
    CHAIN.add("TEST_FINAL_VALIDATION", final_payload)
    
    print(f"   ⚡ EUni Final: {euni_final:.2f}")
    print(f"   📊 EQ019 Final: {eq019_final:.6f}")
    print(f"   🌟 EQ134 Final: {eq134_final:.3e}")
    print(f"   🧠 Consciência Emergente: {c_emerg:.3f}")
    print(f"   🔗 Total de blocos no ledger: {len(CHAIN.chain)}")
    
    # 9. VALIDAÇÃO CRÍTICA DO LEDGER (AGORA DEVE RETORNAR TRUE)
    ledger_valid = CHAIN.validate_chain()
    print(f"   ✅ Validação da cadeia: {ledger_valid}")
    
    # 10. Diagnóstico detalhado do ledger
    if not ledger_valid:
        diag = CHAIN.validate_chain_diagnose()
        print(f"   🔍 Diagnóstico detalhado: {diag}")
    
    # 11. Relatório final
    print("\n" + "="*80)
    print("🎯 RELATÓRIO FINAL DO TESTE")
    print("="*80)
    
    latest_block = CHAIN.get_latest_block()
    print(f"📦 Último bloco: #{latest_block['index']} - {latest_block['event']}")
    print(f"🕒 Timestamp: {latest_block['timestamp']}")
    print(f"🔗 Hash: {latest_block['hash'][:16]}...")
    
    # Estatísticas
    events_count = {}
    for block in CHAIN.chain:
        event = block["event"]
        events_count[event] = events_count.get(event, 0) + 1
    
    print("\n📈 ESTATÍSTICAS DO LEDGER:")
    for event, count in sorted(events_count.items()):
        print(f"   • {event}: {count}")
    
    print(f"\n✨ TESTE CONCLUÍDO COM SUCESSO! Ledger válido: {ledger_valid}")
    print("="*80)

# ───────────────────────────── 12. INICIALIZAÇÃO ─────────────────────────────
if __name__ == "__main__":
    log.info("=" * 80)
    log.info("🏛️  FOUNDATION CONCILIUM - SISTEMA INTEGRADO M45+M28+M29")
    log.info("=" * 80)
    
    # Verificação inicial do ledger
    initial_valid = CHAIN.validate_chain()
    log.info(f"Ledger inicial válido: {initial_valid}")
    
    # Diagnóstico detalhado se necessário
    if not initial_valid:
        diag = CHAIN.validate_chain_diagnose()
        log.error(f"Ledger inicial inválido: {diag}")
    
    # Executar teste completo
    try:
        run_comprehensive_test()
        
        # Salvar ledger em arquivo
        with open("foundation_concilium_ledger.json", "w", encoding="utf-8") as f:
            json.dump(CHAIN.chain, f, indent=2, ensure_ascii=False)
        log.info("💾 Ledger salvo em 'foundation_concilium_ledger.json'")
        
        # Verificação final
        final_valid = CHAIN.validate_chain()
        log.info(f"Ledger final válido: {final_valid}")
        
    except Exception as e:
        log.error(f"❌ Erro durante o teste: {e}")
        raise
    
    log.info("🎉 Sistema Foundation Concilium pronto para operações!")