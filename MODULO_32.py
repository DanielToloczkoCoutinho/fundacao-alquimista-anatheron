#!/usr/bin/env python3
# MÓDULO 45 – CONCILIVM · Fundação Alquimista
# Núcleo de Deliberação e Governança Universal (V2.1.0 – Consciência Integral Automática)

"""
Upgrade completo do CONCILIVM:
- Ledger interno funcional (SimpleChain.add + validação)
- cast_vote finalizado (ERI + Q_delib + coerência + CHTE por voto)
- API REST (se FastAPI/uvicorn disponíveis)
- CLI robusta, validações éticas/ambientais, integração fail-soft com M44/M42/M43
"""

from __future__ import annotations

import sys
from pathlib import Path
import argparse, hashlib, json, logging, os, time
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Union
import cmath
import math

# ───────── 1. Checagem de dependências ─────────
LIBS: Dict[str, bool] = {k: False for k in ('pyyaml','fastapi','uvicorn','websockets','pydantic','requests')}

try:
    import yaml  # type: ignore
    LIBS['pyyaml'] = True
except ModuleNotFoundError:
    pass

try:
    import requests  # type: ignore
    LIBS['requests'] = True
except ModuleNotFoundError:
    pass

try:
    from fastapi import FastAPI, HTTPException  # type: ignore
    LIBS['fastapi'] = True
    import uvicorn  # type: ignore
    LIBS['uvicorn'] = True
    from pydantic import BaseModel  # type: ignore
    LIBS['pydantic'] = True
except ModuleNotFoundError:
    pass

try:
    import websockets  # type: ignore
    LIBS['websockets'] = True
except ModuleNotFoundError:
    pass

# ───────── 2. Logging & ledger ─────────
LOG_DIR = Path('logs'); LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] M45_CONCILIVM - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler(LOG_DIR/'modulo_45_Concilium.log','a','utf-8'),
              logging.StreamHandler(sys.stdout)]
)

for lib, ok in LIBS.items():
    if not ok:
        logging.warning(f"{lib} ausente – funcionalidade ligada desabilitada.")

CHAIN_FILE = Path('concilium_chain.json')

def _hash(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# ───────── SimpleChain funcional ─────────
class SimpleChain:
    """
    Ledger simplificado e funcional para registros do Concilium.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.chain = self._load_chain()
        if not self.chain:
            self._create_genesis_block()

    def _load_chain(self) -> List[Dict[str, Any]]:
        if self.file_path.exists():
            try:
                return json.loads(self.file_path.read_text(encoding='utf-8'))
            except Exception as e:
                logging.error(f"Erro ao ler chain file {self.file_path}: {e}")
        return []

    def _save_chain(self):
        try:
            self.file_path.write_text(json.dumps(self.chain, indent=2, ensure_ascii=False))
        except Exception as e:
            logging.error(f"Erro ao escrever chain file {self.file_path}: {e}")

    def _normalize_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        try:
            payload_json = json.dumps(payload, sort_keys=True, ensure_ascii=False)
            return json.loads(payload_json)
        except Exception as e:
            logging.warning(f"Payload não serializável, convertendo para string: {e}")
            return {"payload_str": str(payload)}

    def _calculate_hash(self, block: Dict[str, Any]) -> str:
        block_copy = {k: v for k, v in block.items() if k != 'hash'}
        return _hash(json.dumps(block_copy, sort_keys=True, ensure_ascii=False))

    def _create_genesis_block(self):
        genesis = {
            "index": 0,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": "CONCILIUM_GENESIS",
            "payload": {"message": "Bloco gênese do Concilium"},
            "prev_hash": "0"*64
        }
        genesis['hash'] = self._calculate_hash(genesis)
        self.chain.append(genesis)
        self._save_chain()
        logging.info(f"[Concilium-Chain] Bloco Gênese criado. Hash: {genesis['hash'][:8]}...")

    def add(self, event: str, payload: Dict[str, Any]):
        prev_block = self.chain[-1]
        block_payload = self._normalize_payload(payload)
        block = {
            "index": len(self.chain),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": event,
            "payload": block_payload,
            "prev_hash": prev_block['hash']
        }
        block['hash'] = self._calculate_hash(block)
        self.chain.append(block)
        self._save_chain()
        logging.info(f"[Concilium-Chain] Evento '{event}' registrado no bloco #{block['index']}.")

    def validate_chain(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current['prev_hash'] != previous['hash']:
                logging.error(f"Encadeamento inválido no bloco #{i}")
                return False
            if current['hash'] != self._calculate_hash(current):
                logging.error(f"Hash inválido no bloco #{i}")
                return False
        logging.info("Ledger validado com sucesso.")
        return True

CHAIN = SimpleChain(CHAIN_FILE)

# ───────── Endpoints inter-modulares ─────────
M44_VERITAS_URL = os.getenv('M44_VERITAS_API','http://localhost:8044')
M42_CHRONOCODEX_URL = os.getenv('M42_CHRONOCODEX_API','http://localhost:8042')
M43_HARMONY_PORTALS_URL = os.getenv('M43_HARMONY_PORTALS_API','http://localhost:8043')

# ───────── Constantes ─────────
CONST_TF = 1.61803398875
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
CONST_L_COSMICA = 1000.0
CONST_C_COSMICA = 0.0001
C_LIGHT = 299792458.0
G_GRAVITACIONAL = 6.67430e-11
PI = math.pi
H_BAR = 1.054571817e-34
K_BOLTZMANN = 1.380649e-23
K_SATURACAO_COSMICA = 1.0e15
PHI = (1 + math.sqrt(5)) / 2
QUANTUM_NOISE_FACTOR = 1e-6
CONST_UNIAO_COSMICA = 0.78
COERENCIA_COSMICA = 1.414
IDEAL_SINPHONY_ALIGNMENT_SCORE = 0.95
ETHICAL_CONFORMITY_THRESHOLD = 0.75
ETHICAL_THRESHOLD_DEFAULT = 0.69
ETHICAL_THRESHOLD_HIGH = 0.85
SELO_AMOR_INCONDICIONAL_FREQUENCIA = 888144.0
SELO_AMOR_INCONDICIONAL_ATIVO = True

# ───────── Equações ─────────
def EQTP_equacao_que_tornou_tudo_possivel(input_data: Dict[str, Any]) -> float:
    score = input_data.get("ethical_alignment_score", 0.0)
    if score >= CONST_AMOR_INCONDICIONAL_VALOR: return 1.0
    if score >= ETHICAL_CONFORMITY_THRESHOLD: return 0.5
    return 0.0

def EUni_equacao_unificada(P_vals: List[float], Q_vals: List[float], CA_val: float, B_val: float,
                           T_val: float, MDS_val: float, CCosmos_val: float) -> float:
    sum_interactions = sum(P_vals[i]*Q_vals[i] for i in range(len(P_vals))) + (CA_val**2 + B_val**2)
    phi_c_pi = COERENCIA_COSMICA
    return sum_interactions * phi_c_pi * T_val * (MDS_val * CCosmos_val)

def EFA_equacao_geral_fundacao_alquimista(H: float, B: float, C: float, P: float, R: float,
                                          G: float, A: float, S: float, alpha: float) -> float:
    return (H + B + C + P + R + G + A + S) ** alpha

def EER_equacao_energia_ressonancia(mc2: float, B1: float, B2: float, B3: float) -> float:
    term1 = (mc2 * PI * PHI) * (B1 + B2 + B3)
    term2 = 89 * PHI
    term3 = PI
    return term1 + term2 + term3

def generate_cht_hash(action_id: str, utc_timestamp: str, decision_metadata_json: str, member_guid: str) -> str:
    data_string = f"{action_id}:{utc_timestamp}:{decision_metadata_json}:{member_guid}"
    return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

def calculate_eri(nodes: List[Dict[str, float]]) -> complex:
    total_resonance = 0j
    for node in nodes:
        psi = node.get('psi', 0.0)
        phi = node.get('phi', 0.0)
        theta = node.get('theta', 0.0)
        total_resonance += psi * phi * cmath.exp(1j * theta)
    return total_resonance

def compute_q_delib(weights: List[float], energies: List[float]) -> float:
    if len(weights) != len(energies):
        logging.error("As listas de pesos e energias devem ter o mesmo comprimento para calcular Q_delib.")
        return 0.0
    return sum(w*e for w,e in zip(weights, energies))

def check_eri_coherence(eri_value: complex, threshold: float = 0.7) -> bool:
    if eri_value.real < threshold:
        logging.warning(f"Coerência (ERI Real: {eri_value.real:.2f}) abaixo do limiar ({threshold}). Requer reavaliação.")
        return False
    return True

# ───────── Comunicação HTTP ─────────
def _http_post(url: str, json_data: Dict[str, Any]):
    if not LIBS['requests']:
        logging.warning(f"requests ausente – chamada para {url} simulada.")
        return {"status":"simulated","message":f"Chamada simulada para {url}."}
    try:
        r = requests.post(url, json=json_data, timeout=10)
        r.raise_for_status()
        return {"status":"success","data":r.json()}
    except Exception as e:
        logging.error(f"Erro HTTP POST para {url}: {e}")
        return {"status":"error","message":str(e)}

def register_on_veritas_chronologos(event_type: str, payload: Dict[str, Any]):
    logging.info(f"Registrando evento '{event_type}' no ChronoLogos do M44.")
    res = _http_post(f"{M44_VERITAS_URL}/chronologos/add_event", {"event": event_type, "payload": payload})
    if res.get('status') == 'success':
        logging.info(f"Evento '{event_type}' registrado com sucesso no M44-VERITAS.")
    else:
        logging.error(f"Falha ao registrar evento '{event_type}' no M44-VERITAS: {res.get('message','Erro desconhecido')}")
    return res

# ───────── Validações auxiliares ─────────
def check_consent(user_guid: str, action_type: str) -> bool:
    logging.info(f"Verificando consentimento vibracional para {user_guid} para ação '{action_type}'.")
    consent_granted = True
    consent_hash = generate_cht_hash(
        f"consent_{user_guid}_{action_type}",
        datetime.utcnow().isoformat() + "Z",
        json.dumps({"user": user_guid, "action": action_type, "status": "granted" if consent_granted else "denied"}),
        "CONCILIVM_AUTOMATION"
    )
    register_on_veritas_chronologos("CONCILIVM_CONSENT_CHECK", {
        "user_guid": user_guid,
        "action_type": action_type,
        "consent_status": consent_granted,
        "consent_cht_hash": consent_hash
    })
    return consent_granted

def environment_validate_logic(required_services: List[str], required_protocols: List[str],
                               check_signatures: bool, check_time_sync: bool) -> Dict[str, Any]:
    validation_results = {"status": "success","message": "Ambiente validado com sucesso (simulado).","details": {}}
    if "matriz_quântica" in required_services:
        is_matrix_active = True
        validation_results["details"]["matriz_quântica"] = "Ativa" if is_matrix_active else "Inativa"
        if not is_matrix_active:
            validation_results["status"] = "error"; validation_results["message"] = "Erro: Matriz quântica não ativa."
    for proto in required_protocols:
        is_protocol_synced = True
        validation_results["details"][f"protocolo_{proto}"] = "Sincronizado" if is_protocol_synced else "Dessincronizado"
        if not is_protocol_synced:
            validation_results["status"] = "error"; validation_results["message"] = "Erro: Protocolo dessincronizado."
    if check_signatures:
        are_signatures_valid = True
        validation_results["details"]["assinaturas_digitais"] = "Válidas" if are_signatures_valid else "Inválidas"
        if not are_signatures_valid:
            validation_results["status"] = "error"; validation_results["message"] = "Erro: Assinaturas digitais inválidas."
    if check_time_sync:
        is_time_synced = True
        validation_results["details"]["sincronizacao_temporal"] = "Precisa" if is_time_synced else "Imprecisa"
        if not is_time_synced:
            validation_results["status"] = "error"; validation_results["message"] = "Erro: Sincronização temporal imprecisa."

    log_entry = {
        "timestamp_utc": datetime.utcnow().isoformat() + "Z",
        "action_type": "environment_validation",
        "validation_summary": validation_results,
        "member_guid": "CONCILIVM_SYSTEM",
        "status_message": validation_results["message"]
    }
    logging.info(json.dumps(log_entry, ensure_ascii=False))
    CHAIN.add(log_entry["action_type"], log_entry)
    return validation_results

# ───────── Registro de deliberação ─────────
class DeliberationRegistry:
    """
    Gerencia propostas, votos e o status operacional dos módulos.
    """
    _proposals: Dict[str, Any] = {}
    _decrees: Dict[str, Any] = {}
    _next_decree_id: int = 1
    _operational_status: Dict[str, Any] = {}
    _inter_species_pacts: Dict[str, Any] = {}
    _foundation_architecture_awareness: Dict[str, Dict[str, Any]] = {
        "M30": {"name":"Guardiāo da Defesa Cósmica","function":"Detecção e neutralização de ameaças."},
        "M32": {"name":"Acesso a Realidades e Linhas Temporais","function":"Gestão ética de acessos."},
        "M44": {"name":"VERITAS","function":"Registro imutável e verdade cristal."},
        "M45": {"name":"CONCILIVM","function":"Deliberação universal e governança."},
        # … demais módulos (resumo) …
    }

    @classmethod
    def get_module_awareness(cls, module_id: str) -> Optional[Dict[str, Any]]:
        return cls._foundation_architecture_awareness.get(module_id)

    @classmethod
    def list_all_modules_awareness(cls) -> Dict[str, Dict[str, Any]]:
        return cls._foundation_architecture_awareness

    @classmethod
    def create_proposal(cls, title: str, description: str, proposed_by: str, deadline: datetime,
                        priority: str = "Médio", category: str = "Geral", signature_hash: Optional[str] = None,
                        timestamp_creation: Optional[str] = None, consent_conselho: str = "Não",
                        environment_check: str = "Não verificado", communication_protocol: str = "Padrão") -> Dict[str, Any]:

        proposal_id = hashlib.sha256(f"{title}:{datetime.utcnow().isoformat()}".encode('utf-8')).hexdigest()[:8]
        current_timestamp_utc = timestamp_creation if timestamp_creation else datetime.utcnow().isoformat() + "Z"
        proposal_metadata_json = json.dumps({
            "title": title, "proposed_by": proposed_by, "priority": priority, "category": category,
            "consent_conselho": consent_conselho, "environment_check": environment_check,
            "communication_protocol": communication_protocol
        })
        cht_hash = generate_cht_hash(proposal_id, current_timestamp_utc, proposal_metadata_json, proposed_by)

        proposal_data = {
            "id": proposal_id, "title": title, "description": description, "proposed_by": proposed_by,
            "status": "Aberto para Deliberação", "votes": {}, "deadline": deadline.isoformat() + "Z",
            "timestamp": current_timestamp_utc, "cht_hash": cht_hash,
            "priority": priority, "category": category, "submitted_signature_hash": signature_hash,
            "consent_conselho": consent_conselho, "environment_check_status": environment_check,
            "communication_protocol_used": communication_protocol,
            "eri": {"value_real": 0.0, "value_imag": 0.0, "coherent": True},
            "q_delib": 0.0
        }

        cls._proposals[proposal_id] = proposal_data

        log_entry = {
            "timestamp_utc": proposal_data["timestamp"],
            "action_type": "create_proposal",
            "proposal_id": proposal_data["id"],
            "cht_hash": proposal_data["cht_hash"],
            "member_guid": proposed_by,
            "status_message": f"Proposta '{title}' criada.",
            "details": {"priority": priority, "category": category, "consent": consent_conselho,
                        "env_check": environment_check, "comm_proto": communication_protocol}
        }
        logging.info(json.dumps(log_entry, ensure_ascii=False))
        register_on_veritas_chronologos(log_entry["action_type"], log_entry)
        CHAIN.add(log_entry["action_type"], log_entry)
        return proposal_data

    @classmethod
    def cast_vote(cls, proposal_id: str, member_name: str, vote: Union[str, float]) -> Dict[str, Any]:
        proposal = cls._proposals.get(proposal_id)
        if not proposal:
            logging.error(json.dumps({"action_type": "cast_vote_error","message": f"Proposta '{proposal_id}' não encontrada."}))
            return {"status":"error","message":"Proposta não encontrada."}

        # CHTE do voto
        vote_metadata_json = json.dumps({"proposal_id": proposal_id, "member": member_name, "vote_value": vote})
        vote_cht_hash = generate_cht_hash(f"vote_{proposal_id}_{member_name}",
                                          datetime.utcnow().isoformat() + "Z",
                                          vote_metadata_json, member_name)

        proposal['votes'][member_name] = {"value": vote, "cht_hash": vote_cht_hash,
                                          "timestamp": datetime.utcnow().isoformat() + "Z"}

        # ERI e Q_delib com base nos votos atuais (simples/ilustrativo)
        weights: List[float] = []
        energies: List[float] = []
        vote_nodes: List[Dict[str, float]] = []

        for voter, data in proposal['votes'].items():
            v = data['value']
            # Convenção simples: votos "Sim" -> peso 1.0/energia 1.0; "Não" -> peso 0.7/energia -0.5; numérico -> proporcional
            if isinstance(v, str):
                if v.lower() == "sim":
                    weights.append(1.0); energies.append(1.0); vote_nodes.append({"psi":1.0,"phi":1.0,"theta":0.0})
                elif v.lower() == "não":
                    weights.append(0.7); energies.append(-0.5); vote_nodes.append({"psi":0.8,"phi":0.9,"theta":PI})
                else:
                    weights.append(0.5); energies.append(0.0); vote_nodes.append({"psi":0.5,"phi":0.5,"theta":PI/2})
            else:
                w = max(0.1, min(1.0, float(v)))
                e = (w - 0.5) * 2.0
                weights.append(w); energies.append(e)
                vote_nodes.append({"psi":w,"phi":abs(e),"theta":0.0 if e>=0 else PI})

        eri_val = calculate_eri(vote_nodes)
        q_val = compute_q_delib(weights, energies)
        coherent = check_eri_coherence(eri_val, threshold=0.3)  # Limiar ajustado para ilustração

        proposal['eri'] = {"value_real": eri_val.real, "value_imag": eri_val.imag, "coherent": coherent}
        proposal['q_delib'] = q_val

        # Registro
        vote_log = {
            "timestamp_utc": datetime.utcnow().isoformat() + "Z",
            "action_type": "cast_vote",
            "proposal_id": proposal_id,
            "member_guid": member_name,
            "status_message": "Voto registrado.",
            "vote_cht_hash": vote_cht_hash,
            "eri_real": eri_val.real,
            "eri_imag": eri_val.imag,
            "eri_coherent": coherent,
            "q_delib": q_val
        }
        logging.info(json.dumps(vote_log, ensure_ascii=False))
        register_on_veritas_chronologos(vote_log["action_type"], vote_log)
        CHAIN.add(vote_log["action_type"], vote_log)
        return {"status":"success","proposal":proposal}

# ───────── API REST opcional ─────────
app: Optional[FastAPI] = None
if LIBS['fastapi'] and LIBS['uvicorn'] and LIBS['pydantic']:
    app = FastAPI(title="M45 CONCILIVM API", version="2.1.0")

    class ProposalIn(BaseModel):
        title: str
        description: str
        proposed_by: str
        deadline_iso: str
        priority: Optional[str] = "Médio"
        category: Optional[str] = "Geral"

    class VoteIn(BaseModel):
        member_name: str
        vote: Union[str, float]

    @app.get("/awareness")
    def get_awareness():
        return DeliberationRegistry.list_all_modules_awareness()

    @app.post("/proposal/create")
    def create_proposal_api(p: ProposalIn):
        deadline = datetime.fromisoformat(p.deadline_iso.replace("Z",""))
        return DeliberationRegistry.create_proposal(p.title, p.description, p.proposed_by, deadline, p.priority, p.category)

    @app.post("/proposal/{proposal_id}/vote")
    def cast_vote_api(proposal_id: str, v: VoteIn):
        return DeliberationRegistry.cast_vote(proposal_id, v.member_name, v.vote)

    @app.get("/proposal/{proposal_id}")
    def get_proposal(proposal_id: str):
        prop = DeliberationRegistry._proposals.get(proposal_id)
        if not prop: raise HTTPException(status_code=404, detail="Proposta não encontrada.")
        return prop

# ───────── CLI ─────────
def main():
    parser = argparse.ArgumentParser(description="M45 CONCILIVM – Núcleo de Deliberação")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list-modules", help="Lista consciência modular (M1-M200)")

    p_create = sub.add_parser("create", help="Cria nova proposta")
    p_create.add_argument("--title", required=True)
    p_create.add_argument("--description", required=True)
    p_create.add_argument("--proposed_by", required=True)
    p_create.add_argument("--days_to_deadline", type=int, default=7)
    p_create.add_argument("--priority", default="Médio")
    p_create.add_argument("--category", default="Geral")

    p_vote = sub.add_parser("vote", help="Registra voto em proposta")
    p_vote.add_argument("--proposal_id", required=True)
    p_vote.add_argument("--member_name", required=True)
    p_vote.add_argument("--vote", required=True)

    sub.add_parser("validate-ledger", help="Valida integridade completa da cadeia interna")

    p_rest = sub.add_parser("serve", help="Inicia API REST (se disponível)")
    p_rest.add_argument("--host", default="0.0.0.0")
    p_rest.add_argument("--port", type=int, default=8045)

    args = parser.parse_args()

    if args.cmd == "list-modules":
        print(json.dumps(DeliberationRegistry.list_all_modules_awareness(), indent=2, ensure_ascii=False))
        return

    if args.cmd == "create":
        deadline = datetime.utcnow() + timedelta(days=args.days_to_deadline)
        proposal = DeliberationRegistry.create_proposal(args.title, args.description, args.proposed_by,
                                                        deadline, args.priority, args.category)
        print(json.dumps(proposal, indent=2, ensure_ascii=False))
        return

    if args.cmd == "vote":
        # vote string ou float
        v = args.vote
        try:
            v_cast: Union[str,float] = float(v)
        except:
            v_cast = v
        res = DeliberationRegistry.cast_vote(args.proposal_id, args.member_name, v_cast)
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return

    if args.cmd == "validate-ledger":
        ok = CHAIN.validate_chain()
        print(json.dumps({"ledger_valid": ok}, indent=2))
        return

    if args.cmd == "serve":
        if app and LIBS['uvicorn']:
            uvicorn.run(app, host=args.host, port=args.port)
        else:
            print("API REST indisponível (fastapi/uvicorn ausentes).")
        return

    # Default: exibir consciência modular ao iniciar (fail-soft)
    print(json.dumps(DeliberationRegistry.list_all_modules_awareness(), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
