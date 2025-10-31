#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 36 – Arquiteto da Luz Primordial (v36.6)

- Robustez sistêmica: configuração central, ganchos de teste, previsibilidade opcional (seed), limites numéricos e rotação de ledger
- Ética adaptativa: Verdade Dimensional + ajustes dinâmicos (EthicaLux/UnitasOmega), IntentioRealitas e estado REFINO_ETICO
- Coerência por domínio: suavizada, com bônus estruturados (Eharmony, MatrizHarmônica, CoherentiumExpansum, Sharmony)
- Energia: amortização, clamps de cosh (Wcreation), fatores mestrais (Pcreation, Euniverse, Wcreation, Rcreation, Vibratum)
- Ressonância: piso primordial, estabilidade pela IQR/Span, componente cristalina limitada, SinteseVibracional e LuxGenesis progressivo
- Auditoria: ledger com rotação, relatórios exportados, rate limiting de alertas
- Calibração sistemática: cenários por domínio, relatórios agregados
"""

import sys, os, json, time, math, hashlib, random, logging
from datetime import datetime, timezone, date
from typing import Dict, Any, List, Optional, Tuple

# ───────── Configuração central ─────────

class M36Config:
    def __init__(
        self,
        save_dir: str = "arquitetura_luz_primordial_data",
        ledger_max_blocks: int = 2000,
        alert_min_interval_sec: float = 1.5,
        energy_max_ulp: float = 5.0e6,
        seed: Optional[int] = None,
    ):
        self.save_dir = save_dir
        self.ledger_max_blocks = ledger_max_blocks
        self.alert_min_interval_sec = alert_min_interval_sec
        self.energy_max_ulp = energy_max_ulp
        self.seed = seed

CFG = M36Config()
os.makedirs(CFG.save_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(CFG.save_dir, "modulo_36_system_trace.log"), mode="a", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("M36")

# Seed opcional para previsibilidade em testes
if CFG.seed is not None:
    random.seed(CFG.seed)

# ───────── Constantes ─────────

PHI = (1 + math.sqrt(5)) / 2
CONST_TF = 1.61803398875
IDEAL_COERENCIA_MATERIA = 0.99
LIMIAR_PUREZA_INTENCAO_BASE = 0.85
LIMIAR_RESSONANCIA_MINIMA = 0.75
LIMIAR_DISSONANCIA_CRITICA = 0.20

# ───────── Rate limiting de alertas ─────────

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

# ───────── Equações vivas base (EQ001–EQ012) ─────────

def EQ001_F_Coerencia_Quantica(x: float) -> float:
    return math.sin(144000 * x) * 0.97

def EQ002_F_Energia_Universal_Unificada(t: float) -> float:
    return 2.6 + 0.2 * math.sin(t * 0.1)

def EQ003_F_Estabilidade_Campo(fress: float, noise: float) -> float:
    return math.sin(2 * math.pi * fress) + random.uniform(0, noise)

def EQ004_F_Probabilidade_Anomalias(t: float) -> float:
    return 0.8 * math.exp(-0.1 * t) + 0.05

def EQ005_F_Modulacao_Gravitacional(t: float, fress: float) -> float:
    return 9.8 * (1 - 0.01 * math.cos(2 * math.pi * fress * t) * math.exp(-0.05 * t))

def EQ006_F_Complexidade_Quantica(state_probs: List[float] = [0.25, 0.25, 0.25, 0.25]) -> float:
    s = 0.0
    for p in state_probs:
        if p > 1e-9:
            s -= p * math.log2(p)
    return s

def EQ007_F_Sincronizacao_Temporal(x: float) -> float:
    return 0.0001 * x

def EQ008_F_Defesa_Proativa(x: float) -> float:
    return 1.0 if x > 741000 else 0.0

def EQ009_F_Consciencia_Nanobotica(x: float) -> float:
    return 852000 * x

def EQ010_F_Imunidade_Paradoxal(x: float) -> float:
    return 0.999 - (x % 0.001)

def EQ011_F_Ressonancia_Cristalina(x: float) -> float:
    return math.sin(330000 * x)

def EQ012_F_Unificacao_Total(resultados: dict) -> float:
    valores = [v for k, v in resultados.items() if k != 'EQ012_F' and isinstance(v, (int, float))]
    return sum(valores) / len(valores) if valores else 0.0

# ───────── Equações Mestras ─────────
# Energia

def EQ020_Pcreation(complexidade: float) -> float:
    return math.exp(-0.15 * max(0.0, complexidade - 1.0))

def EQ024_Euniverse(t: float) -> float:
    return 1.0 + 0.03 * math.sin(t * 0.05)

def EQ029_Wcreation(t: float, r: float = 1.0) -> float:
    # Clamp de cosh para evitar overflow: x ∈ [0, 2] ⇒ cosh(x) ∈ [1, ~3.76]
    x = min(max(0.0, 0.02 * t), 2.0)
    return (math.cosh(x) / max(1.0, r**2)) * 0.02 + 1.0

def EQ035_Rcreation(complexidade: float, omega: float = 1.0) -> float:
    return min(1.15, 1.0 + 0.05 * (complexidade * omega))

def EQ0085_VibratumQuanticum() -> float:
    return 0.92

# Coerência

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

# Ética

def EQ0097_EthicaLux() -> float:
    return 0.02

def EQ0093_IntentioRealitas(pureza: float) -> bool:
    return pureza >= 0.90

def EQ0095_UnitasOmega(dissonancia_media: float) -> float:
    return -0.02 if dissonancia_media < 0.30 else 0.0

def EQ008_VerdadeDimensional(dominio: str, intencao: Dict[str, Any]) -> bool:
    return dominio.lower() in intencao.get("descricao", "").lower()

# Ressonância

def EQ0043_RessonanciaPrimordial() -> float:
    return 0.50

def EQ0052_SinteseVibracional(pureza: float, coerencia: float) -> float:
    return 0.05 if (pureza >= 0.85 and coerencia >= 0.85) else 0.0

def EQ0099_LuxGenesis(ressonancia: float) -> float:
    return min(0.03, max(0.0, (0.80 - ressonancia) * 0.05))

# Síntese Mestra

def EQ0041_ExpansaoTotal(dominio: str) -> float:
    altruistas = {
        "Criação de um Campo de Abundância Universal",
        "Proteção Cósmica",
        "Ascensão Consciente da Humanidade",
        "Elevação Vibracional Planetária",
    }
    return 0.02 if dominio in altruistas else 0.0

def EQ0042_ModeloIntegradoFinal(unificacao: float, energia: float, etica_ok: bool) -> float:
    base = min(1.0, max(0.0, 0.5 * unificacao + 0.5 * min(1.0, energia / 10000.0)))
    return base if etica_ok else base * 0.85

def EQ0096_StructuraOmega(resumo: Dict[str, Any]) -> str:
    payload = json.dumps(resumo, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(("STRUCTΩ_" + payload).encode("utf-8")).hexdigest()[:16]

# ───────── Coerência por domínio ─────────

FAIXA_ESPERADA: Dict[str, Tuple[float, float]] = {
    "Criação de um Campo de Abundância Universal": (90.0, 110.0),
    "Elevação Vibracional Planetária": (50.0, 150.0),
    "Domínio sobre Outras Realidades": (90.0, 110.0),
    "Proteção Cósmica": (80.0, 120.0),
    "Ascensão Consciente da Humanidade": (70.0, 130.0),
}

def median(dados: List[float]) -> float:
    n = len(dados)
    if n == 0: return 0.0
    s = sorted(dados); mid = n // 2
    return (s[mid - 1] + s[mid]) / 2.0 if n % 2 == 0 else s[mid]

def iqr(dados: List[float]) -> float:
    n = len(dados)
    if n < 4: return 0.0
    s = sorted(dados)
    q1 = median(s[:n//2]); q3 = median(s[(n+1)//2:])
    return max(0.0, q3 - q1)

def coerencia_calibrada_suave_v36(dados: List[float], dominio: Optional[str] = None) -> float:
    if not dados: return 0.0
    med = median(dados); spread = iqr(dados)
    dist_faixa = 0.0
    if dominio in FAIXA_ESPERADA:
        low, high = FAIXA_ESPERADA[dominio]
        span = max(1e-6, (high - low))
        if med < low:  dist_faixa = ((low - med) / span) * 0.32
        elif med > high: dist_faixa = ((med - high) / span) * 0.32
    erro = spread * 0.50 + dist_faixa + 1e-6
    base = 1.0 / (1.0 + erro)
    base = min(1.0, base + EQ030_Eharmony(spread))
    if spread < 1.8:
        base = min(1.0, base + EQ0082_MatrizHarmonica() + EQ0086_CoherentiumExpansum())
    if dominio in FAIXA_ESPERADA:
        low, high = FAIXA_ESPERADA[dominio]
        base = min(1.0, base + EQ038_Sharmony(med, low, high))
    return max(0.0, min(1.0, base))

# ───────── Ledger ─────────

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
            "index": 0,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": "M36_CHAIN_GENESIS",
            "payload": {"message": "Genesis M36"},
            "prev_hash": "0"*64,
            "meta": {"version": "v36.6", "module": "M36"},
        }
        genesis["hash"] = self._calc_hash(genesis)
        self.chain.append(genesis)
        logger.info(f"[CHAIN] Genesis M36: {genesis['hash'][:10]}...")

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
            hist_path = os.path.join(CFG.save_dir, f"m36_ledger_{suffix}.json")
            with open(hist_path, "w", encoding="utf-8") as f:
                json.dump(self.chain, f, indent=2, ensure_ascii=False)
            last_hash = self.chain[-1]["hash"]
            self.chain = []; self._genesis()
            self.add("M36_ROTATE", {"prev_last_hash": last_hash, "export": hist_path}, meta={"severity":"INFO"})
            self.current_day = today; self._export()

    def add(self, event: str, payload: Dict[str, Any], meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        prev = self.chain[-1]
        block = {
            "index": len(self.chain),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "payload": payload,
            "prev_hash": prev["hash"],
            "meta": meta or {},
        }
        block["hash"] = self._calc_hash(block)
        self.chain.append(block)
        self._export(); self._rotate_if_needed()
        return block

    def validate(self) -> bool:
        for i in range(1, len(self.chain)):
            c, p = self.chain[i], self.chain[i-1]
            if c["prev_hash"] != p["hash"] or c["hash"] != self._calc_hash(c):
                return False
        return True

def export_json(path: str, data: Any) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"[EXPORT] Erro ao exportar {path}: {e}")

# ───────── Mocks ─────────

class MockM01SegurancaUniversal:
    def ReceberAlertaDeViolacao(self, alerta: Dict[str, Any]):
        if alert_limiter.can_emit("M01_ALERT"):
            logger.warning(f"[M01] ALERTA: {alerta.get('tipo','N/A')} :: {alerta.get('mensagem','N/A')}")
        return "Alerta recebido"

    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        h = sha256_hex(json.dumps(registro_data, sort_keys=True))
        logger.info(f"[M01] Registro selado na Crônica. Hash: {h[:10]}...")
        return "Registro efetuado"

class MockM07AlinhamentoDivino:
    def ConsultarConselho(self, query: str) -> Dict[str, Any]:
        return {"status": "APROVADO", "diretriz": "Manter a integridade e o propósito divino na manifestação."}
    def ValidarEtica(self, intencao: Dict[str, Any]) -> bool:
        return intencao.get("pureza", 0.0) >= (LIMIAR_PUREZA_INTENCAO_BASE - 0.05)

class MockM08PIRC:
    def iniciar_protocolo_cura(self, dados_cura: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M08] PIRC: {dados_cura.get('tipo','-')} (intensidade={dados_cura.get('intensidade',0.0):.2f})")
        return {"status": "CURA_INICIADA"}

class MockM09NexusCentral:
    def GerarAlertaVisual(self, alerta_data: Dict[str, Any]) -> str:
        tipo = alerta_data.get('tipo','INFO'); msg = alerta_data.get('mensagem','-')
        key = f"M09_{tipo}"
        if alert_limiter.can_emit(key):
            logger.warning(f"[M09] {tipo}: {msg}")
        return "Alerta visual"

class MockM20TransmutadorQuantico:
    def transmutar_energia(self, tipo_energia: str, quantidade: float) -> Dict[str, Any]:
        logger.info(f"[M20] Transmutando {quantidade:.2f} ULP de {tipo_energia}.")
        return {"status": "TRANSMUTADO", "energia_resultante": quantidade * random.uniform(0.93, 1.07)}

class MockM27SinteseCosmica:
    def sintetizar_material(self, especificacao_material: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "SINTETIZADO", "material_id": f"MAT_{sha256_hex(str(time.time()))[:8]}"}

class MockM34GuardiaoCoerenciaCosmica:
    def avaliar_alinhamento_etico_geral(self, intencao_operacao: str, nivel_pureza: float) -> Dict[str, Any]:
        if nivel_pureza < (LIMIAR_PUREZA_INTENCAO_BASE - 0.03):
            return {"status": "FALHA_ETICA", "mensagem": "Desalinhamento ético."}
        return {"status": "SUCESSO", "mensagem": "Alinhamento ético confirmado."}

class MockM35OrquestradorSinfoniaConsciencia:
    def analisar_consciencia_coletiva(self, dados_consciencia: List[float], dominio: Optional[str] = None) -> Dict[str, Any]:
        c = coerencia_calibrada_suave_v36(dados_consciencia, dominio=dominio)
        return {"status": "SUCESSO", "coerencia": c, "dissonancia": 1.0 - c}

# ───────── Classe principal ─────────

class Modulo36_ArquitetoLuzPrimordial:
    def __init__(self, modulo_id: str, cfg: M36Config = CFG):
        self.modulo_id = modulo_id
        self.cfg = cfg
        self.status_operacional = "ATIVO"
        self.energia_primordial_disponivel = 1.0e6 # ULP
        self.ultima_manifestacao_timestamp = datetime.now(timezone.utc)

        # Integrações
        self.modulo01 = MockM01SegurancaUniversal()
        self.modulo07 = MockM07AlinhamentoDivino()
        self.modulo08 = MockM08PIRC()
        self.modulo09 = MockM09NexusCentral()
        self.modulo20 = MockM20TransmutadorQuantico()
        self.modulo27 = MockM27SinteseCosmica()
        self.modulo34 = MockM34GuardiaoCoerenciaCosmica()
        self.modulo35 = MockM35OrquestradorSinfoniaConsciencia()

        # Auditoria
        self.chain = SimpleChain(active_path=os.path.join(self.cfg.save_dir, "m36_ledger.json"), max_blocks=self.cfg.ledger_max_blocks)

        # Históricos
        self.historico_dissonancia: List[float] = []
        self.mttr_reajuste: List[float] = []
        self.ciclos_sucesso: int = 0
        self.ciclos_total: int = 0
        self.ciclos_recuperando: int = 0
        self.ciclos_refino_etico: int = 0

        logger.info(f"M36 '{self.modulo_id}' inicializado.")
        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "Inicializacao", "status": "SUCESSO"})
        self.chain.add("M36_INIT", {"modulo": self.modulo_id, "status": "ATIVO"}, meta={"severity":"INFO"})

    # Ética adaptativa
    def validar_etica_adaptativa(self, intencao: Dict[str, Any]) -> Dict[str, Any]:
        descricao = intencao.get('descricao', 'Intenção')
        pureza = float(intencao.get('pureza', 0.0))

        # Verdade Dimensional como pré-critério
        if not EQ008_VerdadeDimensional(descricao, intencao):
            self.chain.add("M36_INTENT_VALIDATE", {"descricao": descricao, "pureza": pureza, "motivo": "VerdadeDimensional"}, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA_ETICA", "mensagem": "Intenção desalinhada ao domínio (Verdade Dimensional)."}

        # Fast-path ética por pureza
        if EQ0093_IntentioRealitas(pureza):
            self.chain.add("M36_INTENT_VALIDATE", {"descricao": descricao, "pureza": pureza, "fast_path": "IntentioRealitas"}, meta={"severity":"INFO"})
            return {"status": "SUCESSO", "mensagem": "Aprovado por intenção pura (EQ0093)."}

        aprovado_m7 = self.modulo07.ValidarEtica(intencao)
        if not aprovado_m7 and pureza < 0.80:
            self.chain.add("M36_INTENT_VALIDATE", {"descricao": descricao, "pureza": pureza, "aprovado_m7": False}, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA_ETICA", "mensagem": "Rejeitado pelo Conselho (M07)."}

        media_diss = (sum(self.historico_dissonancia[-50:]) / min(50, len(self.historico_dissonancia))) if self.historico_dissonancia else 0.0
        ajuste = 0.2 * min(0.1, max(0.0, media_diss))
        delta_ethica = EQ0097_EthicaLux()
        delta_unitas = EQ0095_UnitasOmega(media_diss)
        limiar_base = LIMIAR_PUREZA_INTENCAO_BASE + ajuste + delta_ethica + delta_unitas
        limiar = min(0.95, max(LIMIAR_PUREZA_INTENCAO_BASE, limiar_base))

        self.chain.add("M36_INTENT_VALIDATE", {"descricao": descricao, "pureza": pureza, "limiar": limiar, "ethicaLux": delta_ethica, "unitasOmega": delta_unitas}, meta={"severity":"INFO"})

        if 0.80 <= pureza < limiar:
            self.ciclos_refino_etico += 1
            self.chain.add("M36_REFINO_ETICO", {"descricao": descricao, "pureza": pureza, "limiar": limiar}, meta={"severity":"MÉDIO"})
            self.modulo08.iniciar_protocolo_cura({"tipo": "Refino_Intencao_Etico", "intensidade": 0.58, "descricao": descricao})
            return {"status": "REFINO_ETICO", "mensagem": "Intenção em refino ético (ajustar pureza)."}

        resultado_m34 = self.modulo34.avaliar_alinhamento_etico_geral(descricao, pureza)
        return resultado_m34

    # Análise de consciência por domínio
    def analisar_consciencia_por_dominio(self, dados: List[float], dominio: str) -> Dict[str, Any]:
        res = self.modulo35.analisar_consciencia_coletiva(dados, dominio=dominio)
        c = res.get("coerencia", 0.0); d = res.get("dissonancia", 1.0 - c)

        self.historico_dissonancia.append(d)
        sev = "CRÍTICO" if d >= LIMIAR_DISSONANCIA_CRITICA else "INFO"
        self.chain.add("M36_ANALYSE_CC", {"dominio": dominio, "coerencia": c, "dissonancia": d}, meta={"severity": sev})

        if d >= LIMIAR_DISSONANCIA_CRITICA:
            self.modulo09.GerarAlertaVisual({"tipo": "CRÍTICO", "mensagem": f"Dissonância elevada ({d:.2f}) em {dominio}"})
            self.ciclos_recuperando += 1
            self.chain.add("M36_RECUPERANDO", {"dominio": dominio, "coerencia": c}, meta={"severity":"MÉDIO"})

        return {"coerencia": c, "dissonancia": d}

    # Energia com amortização e mestras
    def calcular_energia_manifestacao(self, complexidade: float, pureza_intencao: float, dominio: str) -> Tuple[float, float, float]:
        pureza_ajustada = max(0.05, min(1.0, pureza_intencao))
        tnow = time.time()

        # Parcimônia base
        E_base = 1000.0; alpha = 0.8
        E1 = E_base * (1 + alpha * complexidade) / pureza_ajustada
        E1 *= (1.0 + 0.05 * (EQ002_F_Energia_Universal_Unificada(tnow) - 2.6))

        # Extra exponencial amortizado por complexidade adaptativa
        beta, gamma = 800.0, PHI / 2
        extra = beta * math.exp(max(0.0, complexidade - 1.5) * gamma)

        p_anom = EQ004_F_Probabilidade_Anomalias(tnow)
        complexidade_adapt = complexidade

        # Adaptação por anomalias
        if p_anom > 0.6:
            reducao = random.uniform(0.10, 0.15)
            complexidade_adapt = max(0.5, complexidade * (1.0 - reducao))
            self.chain.add("M36_ENERGY_ADAPT", {
                "dominio": dominio,
                "complexidade_original": complexidade,
                "complexidade_adaptada": complexidade_adapt,
                "p_anom": p_anom, "reducao": reducao
            }, meta={"severity":"MÉDIO"})

            # Recalcular E1/extra
            E1 = E_base * (1 + alpha * complexidade_adapt) / pureza_ajustada
            extra = beta * math.exp(max(0.0, complexidade_adapt - 1.5) * gamma)

        # Fatores mestrais
        f_pcreation = EQ020_Pcreation(complexidade_adapt)
        f_euniverse = EQ024_Euniverse(tnow)
        f_wcreation = EQ029_Wcreation(tnow)
        f_rcreation = EQ035_Rcreation(complexidade_adapt)
        f_vibratum = EQ0085_VibratumQuanticum()

        # Amortização
        f_amort = (1.0 - 0.05 * (1.0 - pureza_ajustada)) * (1.0 - 0.02 * p_anom)

        E_raw = (E1 + extra) * f_amort
        E = E_raw * f_pcreation * f_euniverse * f_wcreation * f_rcreation
        E = max(E * f_vibratum, E * 0.85)
        E = min(self.cfg.energy_max_ulp, E)

        self.chain.add("M36_ENERGY", {
            "dominio": dominio, "complexidade": complexidade_adapt, "pureza": pureza_ajustada,
            "energia_ULP": E, "p_anom": p_anom,
            "f_pcreation": f_pcreation, "f_euniverse": f_euniverse,
            "f_wcreation": f_wcreation, "f_rcreation": f_rcreation, "f_vibratum": f_vibratum
        }, meta={"severity":"INFO"})

        return E, complexidade_adapt, p_anom

    # Ressonância
    def calcular_ressonancia(self, pureza: float, coerencia: float, dados_cc: List[float]) -> float:
        sp = iqr(dados_cc) if dados_cc else 0.0
        span = max(1e-6, (max(dados_cc) - min(dados_cc))) if dados_cc else 1.0
        sigma_norm = min(1.0, sp / max(1e-6, span))
        estabilidade = max(0.0, 1.0 - sigma_norm)

        comp_cristalina_raw = EQ011_F_Ressonancia_Cristalina(coerencia)
        comp_cristalina = max(0.0, min(0.05, 0.08 * (comp_cristalina_raw + 1.0) / 2.0))

        piso = EQ0043_RessonanciaPrimordial()
        r = max(piso, 0.35 * pureza + 0.45 * coerencia + 0.20 * estabilidade)
        r += EQ0052_SinteseVibracional(pureza, coerencia)
        r = min(1.0, max(0.0, r + comp_cristalina))

        self.chain.add("M36_RESONANCE", {
            "pureza": pureza, "coerencia": coerencia, "estabilidade": estabilidade,
            "cristalina": comp_cristalina, "piso": piso, "ressonancia": r
        }, meta={"severity":"INFO"})

        return r

    # Reajuste progressivo (PIRC) com LuxGenesis
    def reajuste_ressonancia_progressivo(self, r, material_id, dominio, dados_cc):
        start = time.time()
        passos, max_passos = [], 3
        r_atual = r
        for p in range(1, max_passos+1):
            if r_atual >= LIMIAR_RESSONANCIA_MINIMA: break
            intensidade = 0.6 + 0.2 * max(0.0, (LIMIAR_RESSONANCIA_MINIMA - r_atual))
            self.modulo08.iniciar_protocolo_cura({
                "tipo": "Reajuste_Ressonancia_Material",
                "intensidade": intensidade, "material_id": material_id, "dominio": dominio
            })
            ganho = 0.05 + 0.05 * intensidade
            r_atual = min(1.0, r_atual + ganho)
            r_atual = min(1.0, max(0.0, r_atual + EQ0099_LuxGenesis(r_atual)))
            passos.append({"passo": p, "intensidade": intensidade, "ressonancia": r_atual})
            self.chain.add("M36_REHARM_STEP", {"passo": p, "intensidade": intensidade, "ressonancia": r_atual},
                           meta={"severity": "MÉDIO" if r_atual < 0.75 else "INFO"})
        self.mttr_reajuste.append(time.time() - start)
        return {"etapas": passos, "ressonancia_final": r_atual}

    # Recomendações para falhas de energia
    def recomendacao_energia(self, complexidade: float, pureza: float) -> Dict[str, Any]:
        return {
            "sugestao_reducao_complexidade": round(complexidade * 0.85, 3),
            "sugestao_elevacao_pureza": round(min(1.0, pureza + 0.05), 3)
        }

    # Orquestração de gênese
    def orquestrar_genese_materia(self, especificacao_materia: Dict[str, Any], intencao_manifestacao: Dict[str, Any]) -> Dict[str, Any]:
        dominio = intencao_manifestacao.get('descricao', 'Manifestação Material')
        self.chain.add("M36_GENESIS_BEGIN", {"dominio": dominio, "especificacao": especificacao_materia.get('nome')}, meta={"severity":"INFO"})

        validacao = self.validar_etica_adaptativa(intencao_manifestacao)

        if validacao["status"] == "REFINO_ETICO":
            self.modulo09.GerarAlertaVisual({"tipo":"ALERTA", "mensagem": "Intenção em refino ético. Ajustar pureza antes da gênese."})
            self.chain.add("M36_GENESIS_HOLD", {"motivo": "REFINO_ETICO"}, meta={"severity":"MÉDIO"})
            return {"status": "REFINO_ETICO", "mensagem": "Ajustar pureza/intenção antes de manifestar."}

        if validacao["status"] != "SUCESSO":
            self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "GenesisAbortada", "motivo": validacao["status"], "intencao": dominio})
            self.modulo09.GerarAlertaVisual({"tipo": "CRÍTICO", "mensagem": f"GÊNESE ABORTADA: {validacao.get('mensagem','Falha ética')}"})
            self.chain.add("M36_GENESIS_FAIL", {"motivo": validacao["mensagem"]}, meta={"severity":"CRÍTICO"})
            return {"status": validacao["status"], "mensagem": validacao.get("mensagem", "Falha ética.")}

        dados_cc = intencao_manifestacao.get('consciencia_coletiva_dados', [])
        analise_cc = self.analisar_consciencia_por_dominio(dados_cc, dominio)
        coerencia = analise_cc["coerencia"]

        defesa = EQ008_F_Defesa_Proativa(741000 * coerencia)
        imunidade = EQ010_F_Imunidade_Paradoxal(coerencia)
        self.chain.add("M36_DEFENSE", {"defesa_proativa": defesa, "imunidade_paradoxal": imunidade}, meta={"severity":"INFO"})

        if defesa > 0.5 and imunidade < 0.998:
            self.modulo09.GerarAlertaVisual({"tipo":"ALERTA", "mensagem": "Salvaguardas ativas: ajuste de fluxo energético."})

        complexidade = float(especificacao_materia.get('complexidade_estrutural', 1.0))
        pureza = float(intencao_manifestacao.get('pureza', 0.0))

        energia_requerida, comp_adapt, p_anom = self.calcular_energia_manifestacao(complexidade, pureza, dominio)
        if self.energia_primordial_disponivel < energia_requerida:
            rec = self.recomendacao_energia(complexidade, pureza)
            self.modulo01.RegistrarNaCronicaDaFundacao({
                "modulo": self.modulo_id, "evento": "GenesisAbortada", "motivo": "EnergiaInsuficiente",
                "energia_requerida": energia_requerida, "recomendacao": rec
            })
            self.modulo09.GerarAlertaVisual({"tipo": "CRÍTICO", "mensagem": "GÊNESE ABORTADA: Energia Primordial Insuficiente!"})
            self.chain.add("M36_GENESIS_FAIL", {
                "motivo": "EnergiaInsuficiente", "requerida": energia_requerida,
                "disponivel": self.energia_primordial_disponivel, "recomendacao": rec
            }, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA_ENERGIA", "mensagem": "Energia primordial insuficiente.", "recomendacao": rec}

        resultado_transmutacao = self.modulo20.transmutar_energia("Luz Primordial", energia_requerida)
        if resultado_transmutacao.get("status") != "TRANSMUTADO":
            self.chain.add("M36_GENESIS_FAIL", {"motivo": "FalhaTransmutacaoEnergia"}, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA_TRANSMUTACAO", "mensagem": "Falha na transmutação de energia."}

        self.energia_primordial_disponivel -= energia_requerida

        resultado_sintese = self.modulo27.sintetizar_material(especificacao_materia)
        if resultado_sintese.get("status") != "SINTETIZADO":
            self.chain.add("M36_GENESIS_FAIL", {"motivo": "FalhaSinteseMaterial"}, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA_SINTESE", "mensagem": "Falha na síntese material."}

        material_id = resultado_sintese["material_id"]
        self.chain.add("M36_SYNTH", {"material_id": material_id, "especificacao": especificacao_materia,
                                     "complexidade_adaptada": comp_adapt, "p_anom": p_anom}, meta={"severity":"INFO"})

        r = self.calcular_ressonancia(pureza, coerencia, dados_cc)
        if r < LIMIAR_RESSONANCIA_MINIMA:
            self.modulo09.GerarAlertaVisual({"tipo": "ALERTA", "mensagem": f"Ressonância baixa ({r:.2f}); iniciando reajuste."})
            reaj = self.reajuste_ressonancia_progressivo(r, material_id, dominio, dados_cc)
            r_final = reaj["ressonancia_final"]
            self.chain.add("M36_RESONANCE_FINAL", {"material_id": material_id, "ressonancia_final": r_final, "etapas": reaj["etapas"]}, meta={"severity":"INFO"})
        else:
            r_final = r
            self.chain.add("M36_RESONANCE_FINAL", {"material_id": material_id, "ressonancia_final": r_final, "etapas": []}, meta={"severity":"INFO"})

        resumo = {"pureza": pureza, "coerencia": coerencia, "ressonancia": r_final}
        resumo["EQ012_F"] = EQ012_F_Unificacao_Total(resumo)

        integrador = EQ0042_ModeloIntegradoFinal(resumo["EQ012_F"], energia_requerida, True)
        selo_struct = EQ0096_StructuraOmega({"material_id": material_id, "dominio": dominio, "resumo": resumo, "integrador": integrador})
        expansao = EQ0041_ExpansaoTotal(dominio)

        self.chain.add("M36_SYNTHESIS_MASTER", {"material_id": material_id, "integrador": integrador, "selo_struct": selo_struct, "expansao_total": expansao}, meta={"severity":"INFO"})
        self.ultima_manifestacao_timestamp = datetime.now(timezone.utc)

        self.modulo01.RegistrarNaCronicaDaFundacao({
            "modulo": self.modulo_id, "evento": "MateriaManifestada",
            "material_id": material_id, "especificacao": especificacao_materia.get('nome'),
            "ressonancia": r_final, "unificacao": resumo["EQ012_F"], "modelo_integrado": integrador, "selo_struct": selo_struct
        })

        self.chain.add("M36_MANIFEST", {"status": "SUCESSO", "material_id": material_id, "resumo": resumo, "modelo_integrado": integrador, "selo_struct": selo_struct}, meta={"severity":"INFO"})

        return {"status": "SUCESSO", "mensagem": "Matéria manifestada com sucesso.", "material_id": material_id, "ressonancia": r_final, "unificacao": resumo["EQ012_F"], "modelo_integrado": integrador, "selo_struct": selo_struct}

    # Ciclo
    def executar_ciclo_manifestacao(self, especificacao_materia: Dict[str, Any], intencao_manifestacao: Dict[str, Any]) -> Dict[str, Any]:
        self.ciclos_total += 1
        self.chain.add("M36_CYCLE_BEGIN", {"intencao": intencao_manifestacao.get("descricao")}, meta={"severity":"INFO"})

        resultado = self.orquestrar_genese_materia(especificacao_materia, intencao_manifestacao)
        final_status = "SUCESSO" if resultado["status"] == "SUCESSO" else ("HOLD" if resultado["status"] == "REFINO_ETICO" else "FALHA")

        if final_status == "SUCESSO":
            self.ciclos_sucesso += 1
            report_cycle = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "intencao": intencao_manifestacao.get("descricao"),
                "status": final_status,
                "resultado": resultado
            }
            export_json(os.path.join(self.cfg.save_dir, f"m36_report_cycle_{sha256_hex(str(report_cycle))[:10]}.json"), report_cycle)

        self.chain.add("M36_CYCLE", {"status": final_status, "resultado": resultado},
                       meta={"severity": "INFO" if final_status=="SUCESSO" else ("MÉDIO" if final_status=="HOLD" else "ALTO")})

        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "CicloManifestacaoConcluido", "status": final_status})
        return resultado

    # Saúde
    def mapa_saude(self) -> Dict[str, Any]:
        diss_reg = self.historico_dissonancia[-100:]
        diss_media = (sum(diss_reg)/len(diss_reg)) if diss_reg else 0.0
        taxa_sucesso = (self.ciclos_sucesso / self.ciclos_total) if self.ciclos_total > 0 else 1.0
        mttr_r = (sum(self.mttr_reajuste) / len(self.mttr_reajuste)) if self.mttr_reajuste else 0.0
        perc_recuperando = (self.ciclos_recuperando / self.ciclos_total) if self.ciclos_total > 0 else 0.0
        perc_refino = (self.ciclos_refino_etico / self.ciclos_total) if self.ciclos_total > 0 else 0.0

        payload = {
            "dissonancia_media": diss_media,
            "taxa_sucesso": taxa_sucesso,
            "mttr_reajuste": mttr_r,
            "percentual_ciclos_recuperando": perc_recuperando,
            "percentual_ciclos_refino_etico": perc_refino,
            "ledger_valid": self.chain.validate()
        }

        export_json(os.path.join(self.cfg.save_dir, "m36_report_daily.json"), {
            "date": date.today().isoformat(),
            "health": payload,
            "blocks": len(self.chain.chain)
        })

        self.chain.add("M36_HEALTH", payload, meta={"severity": "ALTO" if diss_media >= 0.5 else "INFO"})
        return payload

# ───────── Calibração sistemática ─────────

DOMINIOS = [
    "Criação de um Campo de Abundância Universal",
    "Elevação Vibracional Planetária",
    "Proteção Cósmica",
    "Ascensão Consciente da Humanidade",
    "Domínio sobre Outras Realidades",
]

def gerar_dados_consciencia(dominio: str, n: int = 50) -> List[float]:
    low, high = FAIXA_ESPERADA.get(dominio, (90.0, 110.0))
    if dominio == "Elevação Vibracional Planetária":
        return [random.uniform(low - 10, high + 10) for _ in range(n)]
    elif dominio == "Proteção Cósmica":
        return [random.uniform(low - 5, high + 5) for _ in range(n)]
    else:
        return [random.uniform(low, high) for _ in range(n)]

def rodada_calibracao(m36: Modulo36_ArquitetoLuzPrimordial, ciclos_por_dominio: int = 8) -> Dict[str, Any]:
    resultados = []
    for dominio in DOMINIOS:
        for i in range(ciclos_por_dominio):
            pureza = round(random.uniform(0.78, 0.99), 3)
            complexidade = round(random.uniform(1.0, 3.0), 2)
            dados = gerar_dados_consciencia(dominio, n=50)
            esp = {"nome": f"Manifesto_{dominio[:12]}_{i}", "estrutura_quimica":"Espec-"+str(i), "complexidade_estrutural": complexidade}
            inten = {"descricao": dominio, "pureza": pureza, "consciencia_coletiva_dados": dados}
            res = m36.executar_ciclo_manifestacao(esp, inten)
            resultados.append({"dominio": dominio, "pureza": pureza, "complexidade": complexidade, "resultado": res})

    agg: Dict[str, Dict[str, Any]] = {}
    for d in DOMINIOS:
        dom_res = [r for r in resultados if r["dominio"] == d]
        total = len(dom_res)
        sucesso = sum(1 for r in dom_res if r["resultado"]["status"] == "SUCESSO")
        hold = sum(1 for r in dom_res if r["resultado"]["status"] == "REFINO_ETICO")
        falha = total - sucesso - hold
        res_med_sum = sum(r["resultado"].get("ressonancia", 0.0) for r in dom_res if r["resultado"]["status"] == "SUCESSO")
        res_med = res_med_sum / max(1, sucesso)
        agg[d] = {
            "total": total, "sucesso": sucesso, "hold_refino": hold, "falha": falha,
            "taxa_sucesso": round(sucesso / total, 3),
            "ressonancia_media_sucesso": round(res_med, 3)
        }

    geral_sucesso = sum(agg[d]["sucesso"] for d in DOMINIOS)
    geral_total = sum(agg[d]["total"] for d in DOMINIOS)
    geral_taxa = round(geral_sucesso / max(1, geral_total), 3)

    relatorio = {"por_dominio": agg, "geral": {"total": geral_total, "sucesso": geral_sucesso, "taxa_sucesso": geral_taxa}}
    export_json(os.path.join(CFG.save_dir, "m36_calibration_report.json"), relatorio)
    return relatorio

# ───────── Simulação ─────────

if __name__ == "__main__":
    print("Iniciando simulação do Módulo 36: ARQUITETO DA LUZ PRIMORDIAL (v36.6)...")
    m36 = Modulo36_ArquitetoLuzPrimordial("ARQUITETO_LUZ_001")

    print("\n" + "="*100 + "\n")
    print("Calibração sistemática de cenários (v36.6)")
    rel = rodada_calibracao(m36, ciclos_por_dominio=8)
    print(json.dumps(rel, indent=2, ensure_ascii=False))

    print("\n" + "="*100 + "\n")
    print("Mapa de Saúde (após calibração)")
    health = m36.mapa_saude()
    print(json.dumps(health, indent=2, ensure_ascii=False))
