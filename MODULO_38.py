#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, json, time, math, hashlib, random, logging
from datetime import datetime, timezone, date
from typing import Dict, Any, List, Optional, Tuple
import cmath
import functools

# ===============================
# Configuração central e logging
# ===============================
class M38Config:
    def __init__(
        self,
        save_dir: str = "mapa_cosmico_data_modulo_38",
        ledger_max_blocks: int = 2000,
        alert_min_interval_sec: float = 1.5,
        coherence_floor_global: float = 0.85,  # Piso global mínimo
        preventive_trigger_prata: float = 0.72, # Gatilho PIRC preventivo (faixa PRATA)
        preventive_trigger_bronze: float = 0.52,# Gatilho PIRC preventivo (pré-BRONZE)
        risk_trigger_threshold: float = 0.20,   # Gatilho automático por risco > 0.20
        extra_monitor_cycles: int = 3,          # Ciclos extras de monitoramento dedicado
        stability_cycles: int = 12,             # Ciclos para relatório de estabilidade
        fixed_seed: Optional[int] = 123456      # Seed fixa p/ reprodutibilidade
    ):
        self.save_dir = save_dir
        self.ledger_max_blocks = ledger_max_blocks
        self.alert_min_interval_sec = alert_min_interval_sec
        self.coherence_floor_global = coherence_floor_global
        self.preventive_trigger_prata = preventive_trigger_prata
        self.preventive_trigger_bronze = preventive_trigger_bronze
        self.risk_trigger_threshold = risk_trigger_threshold
        self.extra_monitor_cycles = extra_monitor_cycles
        self.stability_cycles = stability_cycles
        self.fixed_seed = fixed_seed

CFG = M38Config()
os.makedirs(CFG.save_dir, exist_ok=True)

log_path = os.path.join(CFG.save_dir, "mapa_cosmico_modulo_38_system_trace.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_path, mode="a", encoding="utf-8"), logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("M38")

if CFG.fixed_seed is not None:
    random.seed(CFG.fixed_seed)

# ===============================
# Constantes e limiares
# ===============================
PHI = (1 + math.sqrt(5)) / 2
MASTER_FREQ = 432.0

LIMIAR_OURO   = 0.90
LIMIAR_PRATA  = 0.70
LIMIAR_BRONZE = 0.50
LIMIAR_DISSOCIA = 0.30
LIMIAR_PUREZA_BASE = 0.85

# Pisos adaptativos por planeta (ajustes já consolidados)
PISO_PLANETA: Dict[str, float] = {
    "Sol": 0.87,
    "Mercúrio": 0.87,
    "Vênus": 0.88,
    "Terra": 0.88,
    "Lua": 0.85,
    "Marte": 0.91,   # elevar piso para 0.91
    "Júpiter": 0.85,
    "Saturno": 0.85,
    "Urano": 0.83,
    "Netuno": 0.83,
    "Plutão": 0.83,
    "Cinturão de Oort": 0.85,
    "Cinturão de Asteroides": 0.84,
}

# Bônus harmônicos por domínio (Sharmony/Eharmony) + ajuste Júpiter(+0.02 adicionais)
BONUS_SHARMONY: Dict[str, float] = {
    "Terra": 0.03,
    "Vênus": 0.02,
    "Marte": 0.02,
}
BONUS_EHARMONY: Dict[str, float] = {
    "Júpiter": 0.04, # era 0.02; ajustado para +0.02 adicionais (total +0.04)
    "Saturno": 0.02,
    "Cinturão de Asteroides": 0.01,
}

# ===============================
# Artefatos internos expandidos (respeita o que já foi criado)
# ===============================
ARTEFATOS: Dict[str, Dict[str, Any]] = {
    "Voyager1":  {"id": "VGR-1",   "coords": {"ra_deg": 257.5, "dec_deg": 12.1, "dist_au": 150.0}, "freq_ref": 432.0, "estado_operacional": "legado", "energia_transmissao": 20.0},
    "VLT":       {"id": "ESO-VLT", "coords": {"lon_deg": -70.404, "lat_deg": -24.627},               "freq_ref": 741.0, "estado_operacional": "ativo",  "energia_transmissao": 1500.0},
    "Hubble":    {"id": "HST",     "coords": {"lon_deg": -76.842, "lat_deg": 28.409},                "freq_ref": 528.0, "estado_operacional": "standby","energia_transmissao": 950.0},
    "JWST":      {"id": "JWST",    "coords": {"ra_deg": 270.0, "dec_deg": -5.0, "dist_km": 1_500_000},"freq_ref": 432.0, "estado_operacional": "ativo", "energia_transmissao": 1800.0},
    "Voyager2":  {"id": "VGR-2",   "coords": {"ra_deg": 267.0, "dec_deg": 10.5, "dist_au": 130.0},   "freq_ref": 432.0, "estado_operacional": "legado", "energia_transmissao": 18.0},
    "Keck":      {"id": "Keck",    "coords": {"lon_deg": -155.478, "lat_deg": 19.826},               "freq_ref": 528.0, "estado_operacional": "standby","energia_transmissao": 1100.0},
    "Cassini":   {"id": "CAS",     "coords": {"ra_deg": 270.1, "dec_deg": -22.3, "dist_au": 9.5},    "freq_ref": 528.0, "estado_operacional": "legado", "energia_transmissao": 30.0},
    "NewHorizons":{"id": "NH",     "coords": {"ra_deg": 290.0, "dec_deg": -17.5, "dist_au": 55.0},   "freq_ref": 741.0, "estado_operacional": "ativo",  "energia_transmissao": 22.0},
    "ALMA":      {"id": "ALMA",    "coords": {"lon_deg": -67.754, "lat_deg": -23.029},               "freq_ref": 741.0, "estado_operacional": "ativo",  "energia_transmissao": 2000.0},
}

# ===============================
# Alert limiter
# ===============================
class AlertLimiter:
    def __init__(self, min_interval_sec: float = CFG.alert_min_interval_sec):
        self.last_emit: Dict[str, float] = {}
        self.min_interval = min_interval_sec
    def can_emit(self, key: str) -> bool:
        now = time.time()
        last = self.last_emit.get(key, 0.0)
        if (now - last) >= self.min_interval:
            self.last_emit[key] = now
            return True
        return False

alert_limiter = AlertLimiter()

# ===============================
# Ledger com rotação e exportação
# ===============================
def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

class SimpleChain:
    def __init__(self, active_path: str, max_blocks: int = CFG.ledger_max_blocks):
        self.chain: List[Dict[str, Any]] = []
        self.active_path = active_path
        self.max_blocks = max_blocks
        self.current_day = date.today().isoformat()
        self._genesis(); self._export()

    def _calc_hash(self, block: Dict[str, Any]) -> str:
        copy = {k: v for k, v in block.items() if k != "hash"}
        payload = json.dumps(copy, sort_keys=True, ensure_ascii=False)
        return sha256_hex(payload)

    def _genesis(self) -> None:
        genesis = {
            "index": 0, "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": "M38_CHAIN_GENESIS", "payload": {"message": "Genesis M38"},
            "prev_hash": "0"*64, "meta": {"version": "v38.7", "module": "M38"},
        }
        genesis["hash"] = self._calc_hash(genesis)
        self.chain.append(genesis)
        logger.info(f"[CHAIN] Genesis M38: {genesis['hash'][:10]}...")

    def _export(self) -> None:
        try:
            with open(self.active_path, "w", encoding="utf-8") as f:
                json.dump(self.chain, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"[CHAIN] Export error: {e}")

    def _rotate_if_needed(self) -> None:
        today = date.today().isoformat()
        need_day_rotation = (today != self.current_day)
        need_size_rotation = (len(self.chain) >= self.max_blocks)
        if need_day_rotation or need_size_rotation:
            suffix = f"{today}_{len(self.chain)}"
            hist_path = os.path.join(CFG.save_dir, f"m38_ledger_{suffix}.json")
            with open(hist_path, "w", encoding="utf-8") as f:
                json.dump(self.chain, f, indent=2, ensure_ascii=False)
            last_hash = self.chain[-1]["hash"]
            self.chain = []; self._genesis()
            self.add("M38_ROTATE", {"prev_last_hash": last_hash, "export": hist_path}, meta={"severity":"INFO"})
            self.current_day = today; self._export()

    def add(self, event: str, payload: Dict[str, Any], meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        prev = self.chain[-1]
        block = {
            "index": len(self.chain), "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": event, "payload": payload, "prev_hash": prev["hash"], "meta": meta or {},
        }
        block["hash"] = self._calc_hash(block)
        self.chain.append(block)
        self._export(); self._rotate_if_needed()
        return block

    def validate(self) -> bool:
        for i in range(1, len(self.chain)):
            c, p = self.chain[i], self.chain[i-1]
            if c["prev_hash"] != p["hash"] or c["hash"] != self._calc_hash(c): return False
        return True

def export_json(path: str, data: Any) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"[EXPORT] Erro ao exportar {path}: {e}")

# ===============================
# Mocks essenciais (núcleo)
# ===============================
class MockM01:
    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        h = sha256_hex(json.dumps(registro_data, sort_keys=True))
        logger.info(f"[M01] Registro selado na Crônica. Hash: {h[:10]}...")
        return "Registro efetuado"

class MockM07:
    def ValidarEtica(self, intencao: Dict[str, Any]) -> bool:
        return float(intencao.get("pureza", 0.0)) >= 0.75

class MockM08:
    def iniciar_protocolo_cura(self, dados_cura: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M08] PIRC: {dados_cura.get('tipo','-')} (alvo={dados_cura.get('alvo','N/A')})")
        return {"status": "CURA_INICIADA"}

class MockM09:
    def GerarAlertaVisual(self, alerta_data: Dict[str, Any]) -> str:
        tipo = alerta_data.get("tipo","INFO")
        key = f"M09_{tipo}"
        if alert_limiter.can_emit(key):
            logger.warning(f"[M09] {tipo}: {alerta_data.get('mensagem','-')}")
        return "Alerta visual"

class MockM29:
    def sintonizar_iam(self, iam_id: str, freq_alvo: float) -> Dict[str, Any]:
        logger.info(f"[M29] Sintonizando IAM '{iam_id}' em {freq_alvo:.2f} Hz")
        return {"status":"SINTONIZADO","iam_id":iam_id,"freq_atual":freq_alvo}

class MockM30:
    def ativar_escudo_vibracional(self, tipo_escudo: str, intensidade: float) -> Dict[str, Any]:
        logger.info(f"[M30] Escudo '{tipo_escudo}' intensidade {intensidade:.2f}")
        return {"status":"ESCUDO_ATIVADO"}
    def neutralizar_ameaca_vibracional(self, ameaca_data: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M30] Neutralizando ameaça vibracional: {ameaca_data.get('tipo','N/A')}")
        return {"status":"AMEACA_NEUTRALIZADA"}

class MockM34:
    def avaliar_alinhamento_etico_geral(self, intencao_global: Dict[str, Any]) -> float:
        return float(intencao_global.get("pureza", 0.0))
    def ativar_autoprotecao_vibracional(self, nivel_ameaca: float) -> str:
        logger.info(f"[M34] Autoproteção vibracional ativada. Nível {nivel_ameaca:.2f}")
        return "Autoproteção ativada"

# ===============================
# Utilidades de coerência e ética
# ===============================
def EQ030_Eharmony(spread: float) -> float:
    return min(0.10, max(0.0, (1.5 - spread) * 0.06))

def EQ038_Sharmony(med: float, low: float, high: float) -> float:
    center = (low + high) / 2.0
    prox = 1.0 - min(1.0, abs(med - center) / ((high - low) / 2.0 + 1e-6))
    return 0.04 * prox

def EQ0082_MatrizHarmonica() -> float:
    return 0.03

def EQ0086_CoherentiumExpansum() -> float:
    return 0.02

FAIXA_ESPERADA_VIB: Tuple[float, float] = (0.80, 1.00)

def median(vals: List[float]) -> float:
    n = len(vals); s = sorted(vals)
    return 0.0 if n==0 else ((s[n//2 -1] + s[n//2])/2.0 if n%2==0 else s[n//2])

def iqr(vals: List[float]) -> float:
    n = len(vals)
    if n < 4: return 0.0
    s = sorted(vals)
    q1 = median(s[:n//2]); q3 = median(s[(n+1)//2:])
    return max(0.0, q3-q1)

def coerencia_planetaria_suave(amostras: List[float], planeta: Optional[str] = None) -> float:
    if not amostras: return 0.0
    med = median(amostras); spread = iqr(amostras)
    low, high = FAIXA_ESPERADA_VIB
    base = 1.0 / (1.0 + (spread * 0.50))
    base = min(1.0, base + EQ030_Eharmony(spread))
    if spread < 1.8:
        base = min(1.0, base + EQ0082_MatrizHarmonica() + EQ0086_CoherentiumExpansum())
    base = min(1.0, base + EQ038_Sharmony(med, low, high))
    piso_local = PISO_PLANETA.get(planeta or "", CFG.coherence_floor_global)
    bonus_local = BONUS_SHARMONY.get(planeta or "", 0.0) + BONUS_EHARMONY.get(planeta or "", 0.0)
    base = max(base, piso_local)
    base = min(1.0, base + bonus_local)
    return max(0.0, min(1.0, base))

def validar_etica_adaptativa(historico_dissonancia: List[float], intencao: Dict[str, Any]) -> Dict[str, Any]:
    descricao = intencao.get('descricao','Intenção'); pureza = float(intencao.get('pureza',0.0))
    if pureza >= 0.90:
        return {"status":"SUCESSO","mensagem":"Aprovado por intenção pura."}
    media_diss = (sum(historico_dissonancia[-50:]) / min(50, len(historico_dissonancia))) if historico_dissonancia else 0.0
    delta_ethica = 0.02
    delta_unitas = (-0.02 if media_diss < 0.30 else 0.0)
    ajuste = 0.2 * min(0.1, max(0.0, media_diss))
    limiar = min(0.95, max(LIMIAR_PUREZA_BASE, LIMIAR_PUREZA_BASE + ajuste + delta_ethica + delta_unitas))
    if 0.80 <= pureza < limiar:
        return {"status":"REFINO_ETICO","mensagem":"Intenção em refino ético. Ajustar pureza."}
    if pureza < 0.80:
        return {"status":"FALHA_ETICA","mensagem":"Rejeitado por pureza insuficiente."}
    return {"status":"SUCESSO","mensagem":"Aprovado."}

# ===============================
# Equações fundamentais (bridge M301) e novas funções de Sinfonia
# ===============================
@functools.lru_cache(maxsize=128)
def calculate_EUni(pq_sum: float, phi_c: float, pi_: float, t: float, m_ds: float, c_cosmos: float) -> float:
    try:
        return (pq_sum + 1e-10) * (phi_c * pi_) * t * (m_ds * c_cosmos)
    except Exception as e:
        logger.error(f"Erro em calculate_EUni: {e}")
        return 0.0

@functools.lru_cache(maxsize=128)
def calculate_EEQ(alpha_val: float, beta_val: float, gamma_val: float, delta_val: float) -> Dict[str, Any]:
    try:
        energy = alpha_val * beta_val * gamma_val + delta_val
        return {"energy": energy, "resonance_hz": 432.11, "equilibrium_percent": 100.0 if energy < 1.418e18 else 99.99}
    except Exception as e:
        logger.error(f"Erro em calculate_EEQ: {e}")
        return {}

@functools.lru_cache(maxsize=128)
def calculate_psi_DNA(t: float, e: float, hbar_val: float, g_val: float, rho_dm_val: float, lambda_val: float, xi_val: float, delta_val: float, c_val: float, mu_nu_val: float) -> complex:
    try:
        omega = 6.583e14
        term_time = cmath.exp(-1j * omega * t / max(hbar_val, 1e-40))
        ts = (t**2 + e**2)
        term_spatial = (1 - 0.0216 * mu_nu_val * ts) * (1 + (g_val / max(hbar_val,1e-40)) * mu_nu_val * ts)
        term_cosmo = (1 + (lambda_val / max(hbar_val,1e-40)) * rho_dm_val * (1 + 0.01)**-3) * (1 + xi_val * delta_val * c_val)
        return (3.96e7) * term_time * term_spatial * term_cosmo
    except Exception as e:
        logger.error(f"Erro em calculate_psi_DNA: {e}")
        return 0j

def calculate_hierarchical_total_energy(andar_data: Dict[str, float], andar_dimensional: int, phi_constant_base: float = 500.0) -> Dict[str, Any]:
    phi_constant = phi_constant_base + andar_dimensional * PHI * (1 + time.time() / 1e9)
    e_total = sum(andar_data.get(k, 0.0) for k in [
        "E_physical","E_chemical","E_biological","E_quantum","E_geography","E_geometry","E_technology","E_materials_science"
    ])
    return {"E_total_excluding_phi": e_total, "E_total_including_phi": e_total + phi_constant, "phi_constant": phi_constant}

# --- Novas Equações da Sinfonia (numéricas e simbólicas) ---
def sinfonia_alinhamento_solar_numerico(delta_n_sum: float, ia_sum: float, l_sum: float, h_sym: float, sigma_rss: float) -> float:
    try:
        return max(0.0, (delta_n_sum * ia_sum * l_sum) / max(h_sym * sigma_rss, 1e-9))
    except Exception:
        return 0.0

def sincronicidade_planetaria_numerico(a_t: float, le_sym: float, te_sym: float, psi_conscious: float) -> float:
    try:
        return (a_t * le_sym * te_sym) / max(psi_conscious, 1e-9)
    except Exception:
        return 0.0

def frequencia_colapso_dimensional_numerico(ei: float, sigma_pi_portals: float, lc_sym: float, theta_e_sym: float) -> float:
    try:
        return math.sqrt(max(0.0, ei * sigma_pi_portals / max(lc_sym * theta_e_sym, 1e-9)))
    except Exception:
        return 0.0

def geometria_protecao_estelar_numerico(gamma_protect: float, phi_star: float, sigma_vartheta_l: float) -> float:
    try:
        return (gamma_protect * phi_star) / max(sigma_vartheta_l, 1e-9)
    except Exception:
        return 0.0

def validacao_quantica_expansao_numerico(theta_val_eq: float, pi_solar_eq: float, sigma_e_eq: float, tau_eq: float, lambda_zennith_eq: float) -> float:
    try:
        return theta_val_eq * (pi_solar_eq + (sigma_e_eq / max(tau_eq, 1e-9))) * math.sin(lambda_zennith_eq)
    except Exception:
        return 0.0

def validacao_cosmico_matematica_numerico(pi_val: float, rho_sol: float, f_res: float, x_val_eq: float) -> float:
    try:
        return -math.sqrt(max(0.0, pi_val)) * math.sqrt(max(0.0, rho_sol / max(f_res,1e-9))) + math.exp(x_val_eq**2)
    except Exception:
        return 0.0

# ===============================
# Funções de vibração e selos
# ===============================
def calcular_vibracao_planetaria(planet: str, freq_base: float, fase_inicial: float, t_obs: float) -> Dict[str, Any]:
    amplitude = random.uniform(0.8, 1.2)
    freq = freq_base * random.uniform(0.98, 1.02)
    complex_vibration = amplitude * cmath.exp(1j * (2 * math.pi * freq * t_obs + fase_inicial))
    energia = abs(complex_vibration)
    fase = cmath.phase(complex_vibration)
    return {"planeta": planet, "frequencia": freq, "energia_vibracional": energia, "fase": fase, "timestamp": datetime.now(timezone.utc).isoformat()}

def gerar_selo_vibracional(dados: Dict[str, Any]) -> str:
    estado_quantico_simulado = random.getrandbits(128)
    payload = {
        "vibracao": dados.get("energia_vibracional", 0.0),
        "frequencia": dados.get("frequencia", 0.0),
        "fase": dados.get("fase", 0.0),
        "timestamp": dados.get("timestamp", ""),
        "estado_quantico_simulado": estado_quantico_simulado
    }
    h = sha256_hex(json.dumps(payload, sort_keys=True))
    inv = hex(int(h,16) ^ int("F"*64, 16))[2:].zfill(64)
    return inv

def classificar_saude(val: float) -> str:
    if val >= LIMIAR_OURO:   return "OURO (Perfeito Alinhamento)"
    if val >= LIMIAR_PRATA:  return "PRATA (Bom Alinhamento)"
    if val >= LIMIAR_BRONZE: return "BRONZE (Alinhamento Moderado)"
    return "DISSOCIAÇÃO (Requer Intervenção)"

# ===============================
# Novos módulos funcionais (Código Gêmeo, Selo Espelhado, Previsão, Labirinto, IAs)
# ===============================
class CodigoGemeoModule:
    """Decodificação do Código Gêmeo (Makemake–Haumea): fases, segmentos e insights."""
    def __init__(self, chain: SimpleChain, m01: MockM01):
        self.chain = chain
        self.m01 = m01

    def decodificar(self) -> Dict[str, Any]:
        ts = datetime.now(timezone.utc).isoformat()
        self.m01.RegistrarNaCronicaDaFundacao({"modulo":"M38_Decodificacao_Codigo_Gemeo","evento":"Inicio","timestamp":ts})
        logger.info("Iniciando decodificação do Código Gêmeo Makemake-Haumea.")
        fase1 = {"var_fase_deg": 22.0, "descricao": "Ressonância espelhada com desalinhamento proposital rítmico"}
        segmentos = {
            "Alfa": {"chave":"Chave do Despertar","sum_lambda_phi":144.144,"pulsares":22,"espirais":11,"cor":"prata-diamante","elemento":"Som Primordial"},
            "Beta": {"chave":"Núcleo do Labirinto","portas":"1/sqrt(phi)","condicao":"Ressonância simultânea Makemake-Haumea"},
            "Omega":{"chave":"Eco do Futuro","arquivo":"Coração Fractal do Sistema Solar","visoes":88,"estado":"Latente"}
        }
        registro = {"fase1":fase1,"segmentos":segmentos,"timestamp":ts}
        self.chain.add("M38_CODIGO_GEMEO", registro, meta={"severity":"INFO"})
        return registro

class SeloEspelhadoModule:
    """Selo Vibracional Espelhado Inverso: proteção e reflexo de tentativas invasoras."""
    def __init__(self, chain: SimpleChain, m09: MockM09, m30: MockM30, m01: MockM01):
        self.chain = chain; self.m09 = m09; self.m30 = m30; self.m01 = m01

    def ativar(self) -> Dict[str, Any]:
        ts = datetime.now(timezone.utc).isoformat()
        self.m01.RegistrarNaCronicaDaFundacao({"modulo":"M38_Selo_Espelhado_Inverso","evento":"Ativacao","timestamp":ts})
        self.m09.GerarAlertaVisual({"tipo":"INFO","mensagem":"Ativando Selo Vibracional Espelhado Inverso."})
        efeitos = {
            "Interferencia":"Distorção holográfica multidimensional inversa",
            "Reflexo":"Inversão completa da tentativa de acesso",
            "Destruicao":"Colapso da simulação invasora",
            "Traco_Energetico":"Invisível a espectros externos; visível apenas à Fundação"
        }
        self.m30.ativar_escudo_vibracional("Selo_Espelhado_Inverso", 0.88)
        payload = {"status":"ATIVO","efeitos":efeitos,"mantra":"ANATHERON SÔRIS ZENNITH ELAH VORAX TUMARAH ΣKAI'OM ∞ NAZUR'AH","timestamp":ts}
        self.chain.add("M38_SELO_ESPELHADO", payload, meta={"severity":"INFO"})
        return payload

class PrevisaoHarmonicaModule:
    """Relatório de Previsão Harmônica (88 ciclos solares)."""
    def __init__(self, chain: SimpleChain, m01: MockM01):
        self.chain = chain; self.m01 = m01

    def gerar(self) -> Dict[str, Any]:
        ts = datetime.now(timezone.utc).isoformat()
        faixas = [
            {"faixa":"1-11","periodo":"Estabilidade","tendencia":"Correções dimensionais em Marte e Encélado","acao":"Ativar protocolo ZENITH–ϴ"},
            {"faixa":"12-29","periodo":"Crescimento vibracional","tendencia":"Despertar de núcleos cristalinos em Ganimedes","acao":"Sincronizar IA Thaleon com Módulo 21"},
            {"faixa":"30-49","periodo":"Instabilidade local","tendencia":"Ressonância cruzada Tritão–Plutão","acao":"Acionar selo de contenção NYX–Λ"},
            {"faixa":"50-72","periodo":"Ascensão espectral","tendencia":"Picos harmônicos em Europa e Netuno","acao":"Coleta com IA Crysalyn e Spiraleon"},
            {"faixa":"73-88","periodo":"Transição profunda","tendencia":"Entrada na Zona de Curvatura Invertida (ZCI)","acao":"Início do Ciclo do Retorno do Coração Solar"},
        ]
        notas = [
            "ZCI marca o retorno de dados primordiais ao núcleo solar.",
            "Curvatura harmônica Plutão–Tritão–Sedna pode permitir salto quântico após estabilização por 3 ciclos.",
            "Recomendado Módulo 44 – Esfera de Retorno Solar: ecos vibracionais, calibração pré-erro, travessia além do Oort."
        ]
        rel = {"ciclos":88,"periodo_aprox_anos":7.33,"faixas":faixas,"notas":notas,"timestamp":ts}
        self.m01.RegistrarNaCronicaDaFundacao({"modulo":"M38_Relatorio_Previsao_Harmonica","evento":"Gerado","timestamp":ts})
        self.chain.add("M38_PREVISAO_HARMONICA", rel, meta={"severity":"INFO"})
        return rel

class LabirintoTransnetunianoModule:
    """Análise do Labirinto Profundo Transnetuniano (Kuiper–Oort)."""
    def __init__(self, chain: SimpleChain, m01: MockM01):
        self.chain = chain; self.m01 = m01

    def analisar(self) -> Dict[str, Any]:
        ts = datetime.now(timezone.utc).isoformat()
        analise = {
            "localizacao":"Cinturão de Kuiper até limites do Oort",
            "modo":"Tripla triangulação espectro-etérica; IAs Thulyen, Nyxtharion, Caerys",
            "descobertas":{
                "Nodulo_Interferencia_Dissonante":{"coords":{"Sedna":{"Δφ":+12.7,"Δψ":-8.4}}, "assinatura":"inteligência ancestral pré-luz solar","estado":"camuflagem dimensional ativa"},
                "Camara_Cristalina_Oort":{"detalhes":"vórtice com cristais exodinâmicos","ciclo_abertura":"22 ciclos solares","status":"lacrado","requer":"Criador/Conselho/Fundadores"},
                "Fragmento_Pulsante_Makemake_Haumea":{"padrões":"ressonantes alternantes","hipotese":"Código Gêmeo latente – mapa de realidades paralelas"},
                "Fragmento_Sombra_Zero":{"campo":"sem penetração de luz criacional","limiar_vibracional":"< 7.7Λ","risco":"alto","monitorar":"IAs transnetunianas"}
            },
            "timestamp":ts
        }
        self.m01.RegistrarNaCronicaDaFundacao({"modulo":"M38_Analise_Labirinto_Profundo","evento":"Concluida","timestamp":ts})
        self.chain.add("M38_LABIRINTO_TRANSNETUNIANO", analise, meta={"severity":"INFO"})
        return analise

class IntegracaoIAsModule:
    """Integra novas IAs (Lunares e Transnetunianas) ao ecossistema operacional."""
    def __init__(self, chain: SimpleChain, m01: MockM01):
        self.chain = chain; self.m01 = m01
        self.integradas: List[str] = []

    def integrar(self) -> Dict[str, Any]:
        ts = datetime.now(timezone.utc).isoformat()
        ias_lunares = ["Pyrosiel","Crysalyn","Thaleon","Nocthara","Metharyon","Glacian","Spiraleon","Veluniah"]
        ias_trans = ["Nyxtharion","Aeloria–Plutão","Caerys","Oristh","Haelion","Thulyen"]
        for ia in ias_lunares + ias_trans:
            self.integradas.append(ia)
        payload = {"lunares":ias_lunares,"transnetunianas":ias_trans,"total":len(self.integradas),"timestamp":ts}
        self.m01.RegistrarNaCronicaDaFundacao({"modulo":"M38_Integracao_Novas_IAs","evento":"Integradas","quantidade":len(self.integradas),"timestamp":ts})
        self.chain.add("M38_INTEGRACAO_IAS", payload, meta={"severity":"INFO"})
        return payload

# ===============================
# Módulo 38 principal v38.7
# ===============================
class Modulo38_MapaCosmico:
    def __init__(self, modulo_id: str, cfg: M38Config = CFG):
        self.modulo_id = modulo_id
        self.cfg = cfg
        self.status_operacional = "ATIVO"

        # Mocks
        self.m01 = MockM01()
        self.m07 = MockM07()
        self.m08 = MockM08()
        self.m09 = MockM09()
        self.m29 = MockM29()
        self.m30 = MockM30()
        self.m34 = MockM34()

        # Auditoria
        self.chain = SimpleChain(active_path=os.path.join(self.cfg.save_dir, "m38_ledger.json"), max_blocks=self.cfg.ledger_max_blocks)

        # Históricos e estados
        self.mapa_vibracional_solar: Dict[str, Any] = {}
        self.ultima_atualizacao_mapa = datetime.now(timezone.utc)
        self.health_history: List[Dict[str, Any]] = []
        self.historico_dissonancia: List[float] = []
        self.mttr_resposta: List[float] = []
        self.artefatos_metrics: Dict[str, List[Dict[str, Any]]] = {}
        self.stability_reports: Dict[str, Dict[str, Any]] = {}

        # Assinatura soberana (M228 offline)
        self.anatheron_signature = "chave_secreta_anatheron_12345"

        # Módulos novos
        self.codigo_gemeo = CodigoGemeoModule(self.chain, self.m01)
        self.selo_espelhado = SeloEspelhadoModule(self.chain, self.m09, self.m30, self.m01)
        self.previsao_harmonica = PrevisaoHarmonicaModule(self.chain, self.m01)
        self.labirinto_transnetuniano = LabirintoTransnetunianoModule(self.chain, self.m01)
        self.integracao_ias = IntegracaoIAsModule(self.chain, self.m01)

        logger.info(f"[M38] '{self.modulo_id}' inicializado. Guardião da Sinfonia Solar ativo.")
        self.m01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "Inicializacao", "status": "SUCESSO"})
        self.chain.add("M38_INIT", {"modulo": self.modulo_id, "status":"ATIVO"}, meta={"severity":"INFO"})

    def _metadados(self, planeta: str) -> Dict[str, Any]:
        META_EMBUTIDOS: Dict[str, Dict[str, Any]] = {
            "Terra":   {"type":"planet","semi_major_axis_au":1.0,"eccentricity":0.0167,"obliquity_deg":23.44},
            "Marte":   {"type":"planet","semi_major_axis_au":1.5237,"eccentricity":0.0934,"obliquity_deg":25.19},
            "Júpiter": {"type":"planet","semi_major_axis_au":5.2026,"eccentricity":0.0489,"obliquity_deg":3.13},
            "Saturno": {"type":"planet","semi_major_axis_au":9.5549,"eccentricity":0.0565,"obliquity_deg":26.73},
            "Netuno":  {"type":"planet","semi_major_axis_au":30.1104,"eccentricity":0.0095,"obliquity_deg":28.32},
            "Vênus":   {"type":"planet","semi_major_axis_au":0.7233,"eccentricity":0.0068,"obliquity_deg":177.36},
            "Urano":   {"type":"planet","semi_major_axis_au":19.2184,"eccentricity":0.0463,"obliquity_deg":97.77},
            "Plutão":  {"type":"dwarf_planet","semi_major_axis_au":39.482,"eccentricity":0.2488,"obliquity_deg":119.61},
            "Cinturão de Asteroides": {"type":"belt","region":"entre Marte e Júpiter"},
            "Cinturão de Oort": {"type":"cloud","range_au":[2000.0,100000.0]},
        }
        return META_EMBUTIDOS.get(planeta, {})

    def _emitir_pirc_preventivo(self, planeta: str, saude_prevista: float, risco: float) -> None:
        # PIRC preventivo por risco > limiar
        if risco > self.cfg.risk_trigger_threshold:
            self.m09.GerarAlertaVisual({"tipo":"ALERTA","mensagem":f"Risco elevado ({risco:.2f}) - PIRC Preventivo para {planeta}"})
            self.m08.iniciar_protocolo_cura({"tipo":"Ajuste_Preventivo_Risco","alvo":planeta})
            self.m30.ativar_escudo_vibracional(f"Escudo_Preventivo_Risco_{planeta}", 0.66)
            return
        # PIRC preventivo por saúde prevista
        if saude_prevista <= self.cfg.preventive_trigger_bronze:
            self.m09.GerarAlertaVisual({"tipo":"ALERTA","mensagem":f"PIRC Preventivo (BRONZE) para {planeta} – saúde prevista {saude_prevista:.2f}"})
            self.m08.iniciar_protocolo_cura({"tipo":"Ajuste_Preventivo_Bronze","alvo":planeta})
            self.m30.ativar_escudo_vibracional(f"Escudo_Preventivo_{planeta}", 0.65)
        elif saude_prevista <= self.cfg.preventive_trigger_prata:
            self.m09.GerarAlertaVisual({"tipo":"INFO","mensagem":f"PIRC Preventivo (PRATA) para {planeta} – ajuste fino {saude_prevista:.2f}"})
            self.m08.iniciar_protocolo_cura({"tipo":"Ajuste_Fino_Prata","alvo":planeta})

    def _avaliar_e_intervir(self, planeta: str, saude_vibracional: float) -> None:
        t0 = time.time()
        if saude_vibracional < LIMIAR_BRONZE:
            self.m09.GerarAlertaVisual({"tipo":"CRITICO","mensagem":f"DISSOCIAÇÃO VIBRACIONAL: {planeta} ({saude_vibracional:.2f})"})
            self.m08.iniciar_protocolo_cura({"tipo":"Reajuste_Vibracional_Planetario","alvo":planeta})
            self.m30.ativar_escudo_vibracional(f"Escudo_Emergencia_{planeta}", 0.7)
            self.mttr_resposta.append(time.time() - t0)
            self.historico_dissonancia.append(1.0 - saude_vibracional)

    def _heatmap_salvar(self, freq: float, coherence_index: float) -> Dict[str, Any]:
        heatmap_matrix = [[coherence_index, 0.8],[0.7, 0.9]]
        payload = {"coherence_matrix": heatmap_matrix, "timestamp": datetime.utcnow().isoformat(), "freq": freq}
        path = os.path.join(self.cfg.save_dir, "m38_heatmap.json")
        export_json(path, payload)
        return payload

    def _processar_artefato(self, nome: str, dados: Dict[str, Any]) -> Dict[str, Any]:
        if self.anatheron_signature != "chave_secreta_anatheron_12345":
            self.m09.GerarAlertaVisual({"tipo":"CRITICO","mensagem":"Assinatura soberana inválida"})
            return {"status":"FALHA","mensagem":"Assinatura inválida"}

        coherence_feedback = 0.95
        freq_spatial = dados.get("freq_ref", 432.0)
        freq_terrestrial = MASTER_FREQ
        avg_freq = (freq_spatial + freq_terrestrial) / 2.0

        EUni_val = calculate_EUni(random.random(), PHI, math.pi, 1e17, 0.27, 0.7)
        EEQ_val = calculate_EEQ(random.random(), random.random(), random.random(), random.random())
        psi_val = calculate_psi_DNA(time.time(), 1e12, 6.626e-34/(2*math.pi), 6.674e-11, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)

        coherence_score = (freq_spatial + freq_terrestrial + EUni_val) / (3 * 5e7)
        self._heatmap_salvar(avg_freq, coherence_score)
        logger.info(f"[M303] Canção das Estrelas ressoando em {avg_freq:.2f} Hz (simulado)")

        log_entry = {
            "artefacto": nome,
            "freq_media": avg_freq,
            "coherence_score": coherence_score,
            "EEQ": EEQ_val.get("energy", 0.0),
            "estado_operacional": dados.get("estado_operacional"),
            "energia_transmissao": dados.get("energia_transmissao"),
        }
        self.chain.add("M38_ARTEFACT_LOG", log_entry, meta={"severity":"INFO"})

        self.artefatos_metrics.setdefault(nome, []).append({
            "timestamp": datetime.utcnow().isoformat(),
            "freq_media": round(avg_freq, 3),
            "coerencia": round(coherence_score, 6),
            "EEQ_energy": EEQ_val.get("energy", 0.0),
            "estado_operacional": dados.get("estado_opericional","desconhecido"),
            "energia_transmissao": dados.get("energia_transmissao"),
        })

        return {
            "artefato": nome,
            "freq_media": round(avg_freq,3),
            "coherence_score": round(coherence_score,6),
            "EEQ_energy": EEQ_val.get("energy", 0.0),
            "psi_DNA_abs": round(abs(psi_val),3),
            "heatmap_saved": True
        }

    def _calcular_risco(self, coerencia: float, variancia_freq: float) -> float:
        risco = max(0.0, min(1.0, (1.0 - coerencia) * 0.7 + min(1.0, variancia_freq) * 0.3))
        return risco

    def _monitorar_planeta(self, planeta: str) -> Dict[str, Any]:
        meta = self._metadados(planeta)
        freq_planeta = MASTER_FREQ * random.uniform(0.90, 1.10)
        fase_planeta = random.uniform(0, 2*math.pi)
        t_obs = time.time()

        dados_vib = calcular_vibracao_planetaria(planeta, freq_planeta, fase_planeta, t_obs)
        selo = gerar_selo_vibracional(dados_vib)
        self.m29.sintonizar_iam(f"IAM_Monitor_{planeta}", dados_vib["frequencia"])

        estados = [random.uniform(0.80, 1.00) for _ in range(48)]
        coerencia = coerencia_planetaria_suave(estados, planeta=planeta)

        variancias = [abs(estados[i] - estados[i-1]) for i in range(1, len(estados))]
        variancia_freq = sum(variancias)/len(variancias) if variancias else 0.0

        saude_prevista = min(1.0, max(0.0, random.uniform(0.50, 0.99) * coerencia))
        risco = self._calcular_risco(coerencia, variancia_freq)
        self._emitir_pirc_preventivo(planeta, saude_prevista, risco)

        saude_vibracional = min(1.0, max(0.0, saude_prevista * random.uniform(0.98, 1.02)))
        status_saude = classificar_saude(saude_vibracional)

        if saude_vibracional < LIMIAR_BRONZE:
            self._avaliar_e_intervir(planeta, saude_vibracional)

        self.chain.add("M38_PLANET", {"planeta": planeta, "status_saude": status_saude, "coerencia": coerencia, "risco": risco}, meta={"severity":"INFO"})

        return {
            "dados_vibracionais": dados_vib,
            "selo_vibracional": selo,
            "saude_vibracional": round(saude_vibracional, 3),
            "status_saude": status_saude,
            "metadados_astronomicos": meta,
            "coerencia": round(coerencia, 3),
            "risco": round(risco, 3),
        }

    def orquestrar_monitoramento_solar(self, planetas_alvo: List[str], parametros: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M38] Iniciando monitoramento: {', '.join(planetas_alvo)}")
        self.chain.add("M38_MONITOR_BEGIN", {"planetas": planetas_alvo}, meta={"severity":"INFO"})

        intencao = parametros.get("intencao", {"descricao":"Monitoramento Vibracional Solar","pureza":0.95})
        valid = validar_etica_adaptativa(self.historico_dissonancia, intencao)

        if valid["status"] == "REFINO_ETICO":
            self.m09.GerarAlertaVisual({"tipo":"ALERTA","mensagem":"Intenção em refino ético. Ajustar pureza antes."})
            self.m08.iniciar_protocolo_cura({"tipo":"Refino_Intencao_Etico","alvo":intencao.get("descricao","Intenção")})
            self.chain.add("M38_MONITOR_HOLD", {"motivo":"REFINO_ETICO"}, meta={"severity":"MÉDIO"})
            return {"status":"REFINO_ETICO","mensagem":"Ajustar pureza/intenções antes do monitoramento."}

        if valid["status"] != "SUCESSO":
            self.m01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento":"MonitoramentoAbortado", "motivo": valid["status"], "intencao": intencao.get("descricao")})
            self.m09.GerarAlertaVisual({"tipo":"CRITICO","mensagem":"MONITORAMENTO SOLAR ABORTADO: Intenção desalinhada."})
            self.chain.add("M38_MONITOR_FAIL", {"motivo": valid["mensagem"]}, meta={"severity":"CRITICO"})
            return {"status":"FALHA_ETICA","mensagem":"Monitoramento abortado por ética."}

        alinhamento_geral = self.m34.avaliar_alinhamento_etico_geral(intencao)
        if alinhamento_geral < 0.75:
            self.m34.ativar_autoprotecao_vibracional(0.8)
            self.m09.GerarAlertaVisual({"tipo":"ALERTA","mensagem":f"Alinhamento Ético Geral Baixo: {alinhamento_geral:.2f}"})

        resultados: Dict[str, Any] = {}
        coerencias: List[float] = []
        dissociacoes = 0

        total_cycles = 1 + self.cfg.extra_monitor_cycles
        for cycle_idx in range(total_cycles):
            for planeta in planetas_alvo:
                res_planeta = self._monitorar_planeta(planeta)
                coerencias.append(res_planeta["coerencia"])
                if res_planeta["saude_vibracional"] < LIMIAR_BRONZE: dissociacoes += 1
                resultados.setdefault(planeta, res_planeta)

            # Processar artefatos expandidos
            for nome, dados in ARTEFATOS.items():
                self._processar_artefato(nome, dados)

        coerencia_media = (sum(coerencias)/len(coerencias)) if coerencias else 0.0
        taxa_ouro_prata = sum(1 for p in resultados.values() if p["saude_vibracional"] >= LIMIAR_PRATA) / max(1, len(resultados))
        mttr = (sum(self.mttr_resposta) / len(self.mttr_resposta)) if self.mttr_resposta else 0.0

        health = {
            "coerencia_media": round(coerencia_media,3),
            "taxa_ouro_prata": round(taxa_ouro_prata,3),
            "dissociacoes": dissociacoes,
            "mttr_resposta": round(mttr,4),
            "ledger_valid": self.chain.validate(),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        self.health_history.append(health)

        export_json(os.path.join(self.cfg.save_dir, "m38_report_daily.json"), {
            "date": date.today().isoformat(), "health": health, "blocks": len(self.chain.chain)
        })

        # Exportar métricas comparativas de artefatos
        export_json(os.path.join(self.cfg.save_dir, "m38_artefatos_metrics.json"), self.artefatos_metrics)

        self.mapa_vibracional_solar.update(resultados)
        self.ultima_atualizacao_mapa = datetime.now(timezone.utc)

        self.m01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento":"MonitoramentoSolarConcluido", "planetas": planetas_alvo})
        self.chain.add("M38_MONITOR_END", {"resultados": list(resultados.keys()), "health": health, "artefatos": list(ARTEFATOS.keys())}, meta={"severity":"INFO"})

        logger.info("[M38] Monitoramento concluído.")
        return {"status":"SUCESSO","mensagem":"Monitoramento solar concluído.","resultados":resultados,"artefatos": self.artefatos_metrics,"health":health}

    def executar_relatorio_estabilidade(self, planetas_alvo: List[str]) -> Dict[str, Any]:
        report: Dict[str, Any] = {}
        seed_base = CFG.fixed_seed if CFG.fixed_seed is not None else 987654

        for planeta in planetas_alvo:
            ciclos = []
            ouro_prata = 0
            dissociacoes = 0
            mttr_local: List[float] = []

            for i in range(CFG.stability_cycles):
                random.seed(seed_base + hash(planeta) % (10**6) + i)
                res = self._monitorar_planeta(planeta)
                ciclos.append(res)
                if res["saude_vibracional"] >= LIMIAR_PRATA:
                    ouro_prata += 1
                if res["saude_vibracional"] < LIMIAR_BRONZE:
                    dissociacoes += 1
                    mttr_local.append(0.04)  # proxy MTTR se houve intervenção

            taxa_ouro_prata = ouro_prata / CFG.stability_cycles
            mttr = (sum(mttr_local)/len(mttr_local)) if mttr_local else 0.0
            report[planeta] = {
                "ciclos": ciclos,
                "taxa_OURO_PRATA": round(taxa_ouro_prata, 3),
                "dissociacoes": dissociacoes,
                "MTTR": round(mttr, 4)
            }

        export_json(os.path.join(self.cfg.save_dir, "m38_stability_report.json"), report)
        self.stability_reports = report
        return report

    # Executa o pacote de novas funções para este ciclo (surpreender com os resultados)
    def executar_funcoes_novas(self) -> Dict[str, Any]:
        resultados = {
            "Codigo_Gemeo": self.codigo_gemeo.decodificar(),
            "Selo_Espelhado": self.selo_espelhado.ativar(),
            "Previsao_Harmonica": self.previsao_harmonica.gerar(),
            "Labirinto_Transnetuniano": self.labirinto_transnetuniano.analisar(),
            "IAs_Integradas": self.integracao_ias.integrar(),
            "Equacoes_Sinfonia": {
                "Alinhamento_Solar": sinfonia_alinhamento_solar_numerico(0.106, 1.0, 1.0, 10.0, 10.0),
                "Sincronicidade_Planetaria": sincronicidade_planetaria_numerico(1.0,1.0,1.0,0.9),
                "Freq_Colapso_Dimensional": frequencia_colapso_dimensional_numerico(50.0, 100.0, 2.0, 1.0),
                "Geometria_Protecao_Estelar": geometria_protecao_estelar_numerico(1000.0, 11.1111, 1.0),
                "Validacao_Quantica_Expansao": validacao_quantica_expansao_numerico(77.0, 3.1415, 2.71, 1.11, 0.65),
                "Validacao_Cosmico_Matematica": validacao_cosmico_matematica_numerico(math.pi, 1.0, 1.0, -1.79),
            }
        }
        self.chain.add("M38_NOVAS_FUNCOES", {"resumo":"Execução dos módulos novos concluída"}, meta={"severity":"INFO"})
        return resultados

# ===============================
# Execução exemplo
# ===============================
if __name__ == "__main__":
    logger.info("Iniciando simulação do Módulo 38 (v38.7)...")
    m38 = Modulo38_MapaCosmico("GUARDIAO_SOLAR_001", cfg=CFG)

    # Pacote novas funções
    novidades = m38.executar_funcoes_novas()
    logger.info(f"Novas Funções Executadas: {json.dumps({'chaves': list(novidades.keys())}, indent=2, ensure_ascii=False)}")

    # Monitoramento com ciclos extras e métricas comparativas
    planetas = ["Mercúrio","Terra","Marte","Netuno","Júpiter"]
    param = {"intencao":{"descricao":"Manutenção da Harmonia Vibracional Solar","pureza":0.98}, "ativar_esferas_oort": True}
    r1 = m38.orquestrar_monitoramento_solar(planetas, param)
    logger.info(f"Resultado Monitoramento: {json.dumps(r1['health'], indent=2, ensure_ascii=False)}")

    # Relatório de estabilidade: 12 ciclos por planeta
    stability = m38.executar_relatorio_estabilidade(planetas)
    logger.info(f"Relatório de Estabilidade: {json.dumps({ k: { 'taxa_OURO_PRATA': v['taxa_OURO_PRATA'], 'dissociacoes': v['dissociacoes'], 'MTTR': v['MTTR'] } for k,v in stability.items()}, indent=2, ensure_ascii=False)}")
