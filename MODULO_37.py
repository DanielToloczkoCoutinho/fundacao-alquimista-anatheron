#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, json, time, math, hashlib, random, logging, traceback
from datetime import datetime, timezone, date
from typing import Dict, Any, List, Optional, Tuple

# ===============================
# Configuração central e logging
# ===============================

class M37Config:
    def __init__(
        self,
        save_dir: str = "engenharia_temporal_data",
        alert_min_interval_sec: float = 1.5,
        ledger_max_blocks: int = 2000,
        coherence_floor_temporal: float = 0.85,  # Piso temporal (eleva cenários com boa estabilidade)
        density_ideal: float = 1.0e12,
        stability_threshold: float = 0.85,
        paradox_critical_threshold: float = 0.10,
        resonance_success_threshold: float = 0.90,  # para classificar sincronizações perfeitas
        seed: Optional[int] = None
    ):
        self.save_dir = save_dir
        self.alert_min_interval_sec = alert_min_interval_sec
        self.ledger_max_blocks = ledger_max_blocks
        self.coherence_floor_temporal = coherence_floor_temporal
        self.density_ideal = density_ideal
        self.stability_threshold = stability_threshold
        self.paradox_critical_threshold = paradox_critical_threshold
        self.resonance_success_threshold = resonance_success_threshold
        self.seed = seed

CFG = M37Config()
os.makedirs(CFG.save_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(CFG.save_dir, "modulo_37_system_trace.log"), mode="a", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("M37")

if CFG.seed is not None:
    random.seed(CFG.seed)

# ===============================
# Limitador de alertas por tipo
# ===============================

class AlertLimiter:
    """
    Limitador de emissão por chave (ex.: M09_CRITICO, M09_ALERTA, M09_INFO)
    para reduzir ruído do Nexus sem perder informação.
    """
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
# Bônus de coerência (Eharmony/Sharmony) e suporte
# ===============================

def median(vals: List[float]) -> float:
    n = len(vals)
    if n == 0: return 0.0
    s = sorted(vals); mid = n // 2
    return (s[mid - 1] + s[mid]) / 2.0 if n % 2 == 0 else s[mid]

def iqr(vals: List[float]) -> float:
    n = len(vals)
    if n < 4: return 0.0
    s = sorted(vals)
    q1 = median(s[:n//2]); q3 = median(s[(n+1)//2:])
    return max(0.0, q3 - q1)

def EQ030_Eharmony(spread: float) -> float:
    # Bônus suave para baixa dispersão (herdado da família M36)
    return min(0.10, max(0.0, (1.5 - spread) * 0.06))

def EQ038_Sharmony(med: float, low: float, high: float) -> float:
    # Bônus por centralidade do mediano em relação à faixa esperada
    center = (low + high) / 2.0
    prox = 1.0 - min(1.0, abs(med - center) / ((high - low) / 2.0 + 1e-6))
    return 0.04 * prox

def EQ0082_MatrizHarmonica() -> float:
    return 0.03

def EQ0086_CoherentiumExpansum() -> float:
    return 0.02

# Faixas esperadas por domínio (ajustáveis)
FAIXA_ESPERADA: Dict[str, Tuple[float, float]] = {
    "Ascensão Coletiva Universal": (80.0, 120.0),
    "Criação de Linha Temporal Paralela": (70.0, 130.0),
    "Abertura de Portal Dimensional Instável": (60.0, 140.0),
    "Elevação Planetária": (50.0, 150.0),
}

# ===============================
# Ledger simples para auditoria
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
            "index": 0,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": "M37_CHAIN_GENESIS",
            "payload": {"message": "Genesis M37"},
            "prev_hash": "0"*64,
            "meta": {"version": "v37.9", "module": "M37"},
        }
        genesis["hash"] = self._calc_hash(genesis)
        self.chain.append(genesis)
        logger.info(f"[CHAIN] Genesis M37: {genesis['hash'][:10]}...")

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
            hist_path = os.path.join(CFG.save_dir, f"m37_ledger_{suffix}.json")
            with open(hist_path, "w", encoding="utf-8") as f:
                json.dump(self.chain, f, indent=2, ensure_ascii=False)
            last_hash = self.chain[-1]["hash"]
            self.chain = []; self._genesis()
            self.add("M37_ROTATE", {"prev_last_hash": last_hash, "export": hist_path}, meta={"severity":"INFO"})
            self.current_day = today; self._export()

    def add(self, event: str, payload: Dict[str, Any], meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        prev = self.chain[-1]
        block = {
            "index": len(self.chain),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": event, "payload": payload,
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

# ===============================
# Mocks e conectores offline
# ===============================

class MockM01SegurancaUniversal:
    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        h = sha256_hex(json.dumps(registro_data, sort_keys=True))
        logger.info(f"[M01] Registro selado na Crônica. Hash: {h[:10]}...")
        return "Registro efetuado"

class MockM07AlinhamentoDivino:
    def ValidarEtica(self, intencao: Dict[str, Any]) -> bool:
        return float(intencao.get("pureza", 0.0)) >= 0.75

class MockM08PIRC:
    def iniciar_protocolo_cura(self, dados_cura: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M08] PIRC: {dados_cura.get('tipo','-')} (alvo={dados_cura.get('alvo','N/A')})")
        return {"status": "CURA_INICIADA"}

class MockM09NexusCentral:
    def GerarAlertaVisual(self, alerta_data: Dict[str, Any]) -> str:
        tipo = alerta_data.get("tipo","INFO"); key = f"M09_{tipo}"
        if alert_limiter.can_emit(key):
            logger.warning(f"[M09] {tipo}: {alerta_data.get('mensagem','-')}")
        return "Alerta visual"

# Conectores offline (M29/M45). Sem dependência externa.
class OfflineConnectorM29:
    """Wcreation offline: clamp cosh-like control para suavização de energia temporal."""
    def Wcreation(self, t: float, r: float = 1.0) -> float:
        x = min(max(0.0, 0.02 * t), 2.0)
        return (math.cosh(x) / max(1.0, r**2)) * 0.02 + 1.0

class OfflineConnectorM45:
    """Sharmony/Eharmony offline: bônus de coerência e centralidade."""
    def Eharmony(self, spread: float) -> float:
        return EQ030_Eharmony(spread)
    def Sharmony(self, med: float, low: float, high: float) -> float:
        return EQ038_Sharmony(med, low, high)

# ===============================
# Funções de coerência temporal v37
# ===============================

def coerencia_temporal_v37(
    amostras: List[float],
    dominio: Optional[str],
    densidade_linhas: float,
    estabilidade_campo: float,
    cfg: M37Config = CFG,
    m45: Optional[OfflineConnectorM45] = None
) -> float:
    """
    Coerência temporal com:
    - base por densidade ideal e estabilidade
    - bônus Eharmony/Sharmony/Matriz/Coherentium
    - piso temporal (eleva cenários estáveis)
    """
    if not amostras:
        return 0.0

    med = median(amostras)
    spread = iqr(amostras)
    desvio_densidade = abs(densidade_linhas - cfg.density_ideal) / cfg.density_ideal
    base_linear = max(0.0, 1.0 - desvio_densidade - (1.0 - estabilidade_campo))

    # Bônus de baixa dispersão e harmônicos
    eh = (m45.Eharmony(spread) if m45 else EQ030_Eharmony(spread))
    base = min(1.0, base_linear + eh)

    if spread < 1.8:
        base = min(1.0, base + EQ0082_MatrizHarmonica() + EQ0086_CoherentiumExpansum())

    if dominio in FAIXA_ESPERADA:
        low, high = FAIXA_ESPERADA[dominio]
        sh = (m45.Sharmony(med, low, high) if m45 else EQ038_Sharmony(med, low, high))
        base = min(1.0, base + sh)

    # Piso temporal: se há boa estabilidade, garante coerência mínima
    if estabilidade_campo >= cfg.stability_threshold:
        base = max(base, cfg.coherence_floor_temporal)

    return max(0.0, min(1.0, base))

# ===============================
# Classe principal Módulo 37
# ===============================

class Modulo37_EngenhariaTemporal:
    def __init__(self, modulo_id: str, cfg: M37Config = CFG):
        self.modulo_id = modulo_id
        self.cfg = cfg

        self.modulo01 = MockM01SegurancaUniversal()
        self.modulo07 = MockM07AlinhamentoDivino()
        self.modulo08 = MockM08PIRC()
        self.modulo09 = MockM09NexusCentral()
        self.m29 = OfflineConnectorM29()
        self.m45 = OfflineConnectorM45()

        # Auditoria
        self.chain = SimpleChain(
            active_path=os.path.join(self.cfg.save_dir, "m37_ledger.json"),
            max_blocks=self.cfg.ledger_max_blocks
        )

        # Históricos para saúde
        self.ciclos_total = 0
        self.ciclos_sucesso = 0
        self.linhas_instaveis = 0
        self.mttr_estabilizacao: List[float] = []
        self.coerencias_observadas: List[float] = []

        logger.info(f"M37 '{self.modulo_id}' inicializado.")
        self.modulo01.RegistrarNaCronicaDaFundacao({
            "modulo": self.modulo_id, "evento": "Inicializacao", "status": "SUCESSO"
        })
        self.chain.add("M37_INIT", {"modulo": self.modulo_id, "status":"ATIVO"}, meta={"severity":"INFO"})

    # --- Orquestração principal ---
    def orquestrar_evento_sincronizado(self, evento_data: Dict[str, Any], intencao: Dict[str, Any]) -> Dict[str, Any]:
        nome = evento_data.get("nome","Evento")
        dominio = nome if nome in FAIXA_ESPERADA else None
        self.chain.add("M37_ORCH_BEGIN", {"evento": nome}, meta={"severity":"INFO"})

        # Ética
        if not self.modulo07.ValidarEtica(intencao):
            self.modulo01.RegistrarNaCronicaDaFundacao({
                "modulo": self.modulo_id, "evento": "OrquestracaoAbortada", "motivo": "FalhaEtica", "intencao": intencao.get("descricao")
            })
            self.modulo09.GerarAlertaVisual({"tipo":"CRITICO","mensagem":f"ORQUESTRAÇÃO ABORTADA: Falha ética ({intencao.get('descricao','-')})"})
            self.chain.add("M37_ORCH_FAIL", {"motivo":"FalhaEtica"}, meta={"severity":"CRITICO"})
            return {"status":"FALHA_ETICA","mensagem":"Desalinhamento ético na intenção."}

        # Paradoxo (simples, baseado em complexidade)
        chance_paradoxo = random.uniform(0.0, 0.2) * float(evento_data.get("complexidade_temporal",1.0))
        if chance_paradoxo > self.cfg.paradox_critical_threshold:
            self.modulo09.GerarAlertaVisual({"tipo":"ALERTA","mensagem":f"Potencial paradoxo detectado ({nome})"})
            self.chain.add("M37_PARADOXO", {"evento": nome, "severidade": chance_paradoxo}, meta={"severity":"ALTO"})

        # Recalibrar (simulado): usar uma small wait como MTTR amostral
        t0 = time.time()
        time.sleep(0.04)  # custo de recalibração simulado
        self.mttr_estabilizacao.append(time.time() - t0)
        self.chain.add("M37_PARADOXO_RECALIBRADO", {"evento": nome}, meta={"severity":"INFO"})

        # Modulação do campo com M29 (Wcreation offline) — energia/estabilidade auxiliar
        tnow = time.time()
        w_factor = self.m29.Wcreation(tnow)
        intensidade = float(intencao.get("impacto_previsto", 1.0))
        estabilidade_base = min(1.0, 0.80 + 0.05 * (w_factor - 1.0))  # suavização

        self.chain.add("M37_FIELD", {"w_factor": w_factor, "estabilidade_base": estabilidade_base, "intensidade":intensidade}, meta={"severity":"INFO"})

        # Avaliar linhas alvo
        status_linhas: Dict[str, str] = {}
        linhas = evento_data.get("linhas_alvo", [])

        for linha_id in linhas:
            densidade = self.cfg.density_ideal * random.uniform(0.92, 1.08)
            estabilidade = min(1.0, max(self.cfg.stability_threshold, estabilidade_base * random.uniform(0.98, 1.02)))

            # Coerência com bônus e piso temporal
            amostras = [random.uniform(densidade*0.999, densidade*1.001) for _ in range(50)]
            coerencia = coerencia_temporal_v37(amostras, dominio, densidade, estabilidade, cfg=self.cfg, m45=self.m45)
            self.coerencias_observadas.append(coerencia)

            if coerencia >= self.cfg.resonance_success_threshold:
                status_linhas[linha_id] = "SINCRONIZADO_PERFEITAMENTE"
                self.chain.add("M37_SYNC", {"linha": linha_id, "coerencia": coerencia}, meta={"severity":"INFO"})
            elif coerencia >= self.cfg.stability_threshold:
                # Elevar “variação” para “perfeito” quando estabilidade for boa e bônus altos
                # critério: spread baixo e sharmony alto implícito -> aqui aproximado via coerência
                status_linhas[linha_id] = "SINCRONIZADO_COM_VARIACAO"
                self.chain.add("M37_SYNC_VAR", {"linha": linha_id, "coerencia": coerencia}, meta={"severity":"MÉDIO"})
            else:
                status_linhas[linha_id] = "SINCRONIZADO_INSTAVEL"
                self.linhas_instaveis += 1
                self.modulo09.GerarAlertaVisual({"tipo":"CRITICO","mensagem":f"Sincronização instável ({nome}) na {linha_id}"})
                # dispor PIRC para estabilização
                self.modulo08.iniciar_protocolo_cura({"tipo":"Estabilizacao_Linha_Temporal", "alvo": linha_id})
                self.chain.add("M37_SYNC_UNSTABLE", {"linha": linha_id, "coerencia": coerencia}, meta={"severity":"ALTO"})

        self.modulo01.RegistrarNaCronicaDaFundacao({
            "modulo": self.modulo_id, "evento":"EventoSincronizado", "evento_nome": nome, "status_linhas": status_linhas
        })
        self.chain.add("M37_ORCH_END", {"evento": nome, "status_linhas": status_linhas}, meta={"severity":"INFO"})

        return {"status":"SUCESSO", "mensagem":"Evento orquestrado.", "detalhes_sincronizacao": status_linhas}

    def executar_ciclo_engenharia_temporal(self, evento_data: Dict[str, Any], intencao: Dict[str, Any]) -> Dict[str, Any]:
        self.ciclos_total += 1
        self.chain.add("M37_CYCLE_BEGIN", {"evento": evento_data.get("nome")}, meta={"severity":"INFO"})

        resultado = self.orquestrar_evento_sincronizado(evento_data, intencao)
        final_status = "SUCESSO" if resultado["status"] == "SUCESSO" else "FALHA"

        if final_status == "SUCESSO":
            self.ciclos_sucesso += 1

        self.chain.add("M37_CYCLE", {"status": final_status, "resultado": resultado}, meta={"severity": "INFO" if final_status=="SUCESSO" else "ALTO"})
        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento":"CicloEngenhariaTemporalConcluido", "status": final_status})
        return resultado

    # --- Saúde agregada (health map diário) ---
    def mapa_saude_diario(self) -> Dict[str, Any]:
        taxa_sucesso = (self.ciclos_sucesso / self.ciclos_total) if self.ciclos_total > 0 else 1.0
        mttr = (sum(self.mttr_estabilizacao) / len(self.mttr_estabilizacao)) if self.mttr_estabilizacao else 0.0
        perc_instaveis = (self.linhas_instaveis / max(1, self.ciclos_total))  # por ciclo
        coerencia_media = (sum(self.coerencias_observadas) / len(self.coerencias_observadas)) if self.coerencias_observadas else 0.0

        payload = {
            "taxa_sucesso": round(taxa_sucesso, 3),
            "mttr_estabilizacao": round(mttr, 4),
            "percentual_linhas_instaveis_por_ciclo": round(perc_instaveis, 3),
            "coerencia_media": round(coerencia_media, 3),
            "ledger_valid": self.chain.validate(),
        }

        # Exporta snapshot diário
        try:
            with open(os.path.join(self.cfg.save_dir, "m37_report_daily.json"), "w", encoding="utf-8") as f:
                json.dump({
                    "date": date.today().isoformat(),
                    "health": payload,
                    "blocks": len(self.chain.chain),
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"[EXPORT] Erro ao exportar health: {e}")

        self.chain.add("M37_HEALTH", payload, meta={"severity": "ALTO" if coerencia_media < 0.75 else "INFO"})
        return payload

# ===============================
# Execução de exemplo (opcional)
# ===============================

if __name__ == "__main__":
    logger.info("Iniciando simulação do Módulo 37 (v37.9)...")
    m37 = Modulo37_EngenhariaTemporal("ENGENHARIA_TEMPORAL_001")

    # Cenário: Ascensão Coletiva
    evento_c1 = {
        "nome": "Ascensão Coletiva Universal",
        "descricao": "Sincronização de frequências para ascensão de consciências.",
        "complexidade_temporal": 0.8,
        "linhas_alvo": ["Linha_Alfa_1", "Linha_Beta_2", "Linha_Gama_3"],
    }
    intencao_c1 = {"descricao": "Elevação da Consciência Planetária", "pureza": 0.98, "impacto_previsto": 1000.0}
    resultado1 = m37.executar_ciclo_engenharia_temporal(evento_c1, intencao_c1)
    logger.info(f"Resultado 1: {resultado1}")

    # Cenário: Criação paralela (paradoxo possível)
    evento_c2 = {
        "nome": "Criação de Linha Temporal Paralela",
        "descricao": "Realidade alternativa para estudos de viabilidade.",
        "complexidade_temporal": 2.8,
        "linhas_alvo": ["Linha_Delta_4"],
    }
    intencao_c2 = {"descricao": "Expansão da Compreensão Multiversal", "pureza": 0.90, "impacto_previsto": 500.0}
    resultado2 = m37.executar_ciclo_engenharia_temporal(evento_c2, intencao_c2)
    logger.info(f"Resultado 2: {resultado2}")

    # Cenário: Intenção desalinhada (falha ética)
    evento_c3 = {
        "nome": "Alteração de Eventos Históricos",
        "descricao": "Modificação do passado para otimizar futuro.",
        "complexidade_temporal": 4.5,
        "linhas_alvo": ["Linha_Epsilon_5"],
    }
    intencao_c3 = {"descricao": "Controle de Destino Coletivo", "pureza": 0.60, "impacto_previsto": 1800.0}
    resultado3 = m37.executar_ciclo_engenharia_temporal(evento_c3, intencao_c3)
    logger.info(f"Resultado 3: {resultado3}")

    # Mapa de saúde
    health = m37.mapa_saude_diario()
    logger.info(f"Mapa de Saúde: {health}")
