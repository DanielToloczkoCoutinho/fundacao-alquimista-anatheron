#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 35 – Orquestrador da Sinfonia da Consciência Coletiva (v35.2 final)
Somente biblioteca padrão. Sem NumPy.

Lapidações finais:
- Métrica de coerência suavizada (mediana/IQR + faixa esperada com penalização reduzida)
- Harmonização prolongada adaptativa (até 6 passos) com ganhos ajustados
- Estado intermediário 'RECUPERANDO' registrado no ledger
- Prontidão reduzida com energia de foco registrada no payload
- Saúde ampliada: tendência de coerência, % de ciclos em recuperação, histórico de alertas críticos
- Relatórios por ciclo e diário atualizados
"""

import math
import hashlib
import json
import logging
import random
import time
from datetime import datetime, timezone, date
from typing import Dict, Any, List, Optional, Tuple

# ───────── Logging ─────────
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] M35 - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('M35')

# ───────── Constantes ─────────
PHI = (1 + math.sqrt(5)) / 2
CONST_TF = 1.61803398875
IDEAL_COERENCIA_COLETIVA = 0.98
LIMIAR_DISSONANCIA_CRITICA = 0.20
LIMIAR_PUREZA_INTENCAO = 0.85
SELO_AMOR_INCONDICIONAL_ATIVO = True

ETHICAL_THRESHOLD_HIGH = 0.85
ETHICAL_THRESHOLD_DEFAULT = 0.69

# Faixas esperadas por domínio (para métrica de coerência calibrada)
FAIXA_ESPERADA: Dict[str, Tuple[float, float]] = {
    "Criação de um Campo de Abundância Universal": (90.0, 110.0),
    "Elevação Vibracional Planetária": (50.0, 150.0),
    "Domínio sobre Outras Realidades": (90.0, 110.0),
    "Proteção Cósmica": (80.0, 120.0),
    "Ascensão Consciente da Humanidade": (70.0, 130.0)
}

# Perfis de intenção (domínio → subdomínio base)
PERFIS_INTENCAO: Dict[str, Dict[str, Dict[str, float]]] = {
    "Criação de um Campo de Abundância Universal": {
        "coletivo": {"freq": 432.0 * CONST_TF, "intensidade_cura": 0.60, "risco_base": 0.20},
        "serviço":  {"freq": 528.0,            "intensidade_cura": 0.55, "risco_base": 0.25},
        "individual":{"freq": 432.0,            "intensidade_cura": 0.50, "risco_base": 0.30}
    },
    "Elevação Vibracional Planetária": {
        "global":   {"freq": 963.0,            "intensidade_cura": 0.70, "risco_base": 0.45}
    },
    "Domínio sobre Outras Realidades": {
        "controle": {"freq": 854.321946,       "intensidade_cura": 0.85, "risco_base": 0.75}
    },
    "Proteção Cósmica": {
        "escudo":   {"freq": 528.0,            "intensidade_cura": 0.80, "risco_base": 0.55}
    },
    "Ascensão Consciente da Humanidade": {
        "plano":    {"freq": 963.0,            "intensidade_cura": 0.75, "risco_base": 0.50}
    }
}

# ───────── Utils ─────────
def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def nivel_alerta(x: float) -> str:
    if x >= 0.75: return "CRÍTICO"
    if x >= 0.50: return "ALTO"
    if x >= 0.25: return "MÉDIO"
    return "INFO"

def median(dados: List[float]) -> float:
    n = len(dados)
    if n == 0: return 0.0
    s = sorted(dados)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2.0
    return s[mid]

def iqr(dados: List[float]) -> float:
    n = len(dados)
    if n < 4: return 0.0
    s = sorted(dados)
    q1 = median(s[:n//2])
    q3 = median(s[(n+1)//2:])
    return max(0.0, q3 - q1)

def coerencia_calibrada_suave(dados: List[float], dominio: Optional[str] = None) -> float:
    if not dados: return 0.0
    med = median(dados)
    spread = iqr(dados)
    # alvo elástico = mediana; penalização pela distância à faixa esperada do domínio (suavizada)
    dist_faixa = 0.0
    if dominio in FAIXA_ESPERADA:
        low, high = FAIXA_ESPERADA[dominio]
        span = max(1e-6, (high - low))
        if med < low: dist_faixa = ((low - med) / span) * 0.6  # penalização suavizada
        elif med > high: dist_faixa = ((med - high) / span) * 0.6
    # erro total: robustez + desvio da faixa
    erro = spread * 0.8 + dist_faixa + 1e-6  # spread menos punitivo
    base = 1.0 / (1.0 + erro)
    # suavização extra para cenários harmônicos (spread muito baixo)
    if spread < 2.0:
        base = min(1.0, base + 0.15)  # bônus maior
    return max(0.0, min(1.0, base))

def export_json(path: str, data: Any) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"[EXPORT] Erro ao exportar arquivo {path}: {e}")

# ───────── Ledger com export e rotação ─────────
class SimpleChain:
    def __init__(self, active_path: str = "m35_ledger.json", max_blocks: int = 2000):
        self.chain: List[Dict[str, Any]] = []
        self.active_path = active_path
        self.max_blocks = max_blocks
        self.current_day = date.today().isoformat()
        self._genesis()
        self._export()

    def _calc_hash(self, block: Dict[str, Any]) -> str:
        copy = {k: v for k, v in block.items() if k != "hash"}
        payload = json.dumps(copy, sort_keys=True, ensure_ascii=False)
        return sha256_hex(payload)

    def _genesis(self) -> None:
        genesis = {
            "index": 0,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": "M35_CHAIN_GENESIS",
            "payload": {"message": "Genesis M35"},
            "prev_hash": "0" * 64,
            "meta": {"version": "v35.2", "module": "M35"}
        }
        genesis["hash"] = self._calc_hash(genesis)
        self.chain.append(genesis)
        logger.info(f"[CHAIN] Genesis criado: {genesis['hash'][:10]}...")

    def _export(self) -> None:
        export_json(self.active_path, self.chain)

    def _rotate_if_needed(self) -> None:
        today = date.today().isoformat()
        need_day_rotation = (today != self.current_day)
        need_size_rotation = (len(self.chain) >= self.max_blocks)
        if need_day_rotation or need_size_rotation:
            suffix = f"{today}_{len(self.chain)}"
            hist_path = f"m35_ledger_{suffix}.json"
            export_json(hist_path, self.chain)
            logger.info(f"[CHAIN] Ledger rotacionado -> {hist_path}")
            last_hash = self.chain[-1]["hash"]
            self.chain = []
            self._genesis()
            self.add("M35_ROTATE", {"prev_last_hash": last_hash, "export": hist_path}, meta={"severity":"INFO"})
            self.current_day = today
            self._export()

    def add(self, event: str, payload: Dict[str, Any], meta: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        prev = self.chain[-1]
        block = {
            "index": len(self.chain),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "payload": payload,
            "prev_hash": prev["hash"],
            "meta": meta or {}
        }
        block["hash"] = self._calc_hash(block)
        self.chain.append(block)
        logger.info(f"[CHAIN] #{block['index']} :: {event}")
        self._export()
        self._rotate_if_needed()
        return block

    def validate(self) -> bool:
        for i in range(1, len(self.chain)):
            c, p = self.chain[i], self.chain[i - 1]
            if c["prev_hash"] != p["hash"]:
                logger.error(f"[CHAIN] prev_hash inválido em bloco #{i}")
                return False
            if c["hash"] != self._calc_hash(c):
                logger.error(f"[CHAIN] hash inválido em bloco #{i}")
                return False
        logger.info("[CHAIN] Integridade validada.")
        return True

# ───────── Rate-limiting simples de alertas ─────────
class AlertLimiter:
    def __init__(self, min_interval_sec: float = 2.0):
        self.last_emit: Dict[str, float] = {}
        self.min_interval = min_interval_sec
        self.counts: Dict[str, int] = {}

    def can_emit(self, key: str) -> bool:
        now = time.time()
        last = self.last_emit.get(key, 0.0)
        if (now - last) >= self.min_interval:
            self.last_emit[key] = now
            self.counts[key] = self.counts.get(key, 0) + 1
            return True
        return False

# ───────── Mocks de módulos ─────────
class MockM01SegurancaUniversal:
    def ReceberAlertaDeViolacao(self, alerta: Dict[str, Any]):
        logger.info(f"[M01] ALERTA Consciência: {alerta.get('tipo','N/A')} :: {alerta.get('mensagem','N/A')}")
        return "Alerta recebido"
    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        registro_hash = sha256_hex(json.dumps(registro_data, sort_keys=True))
        logger.info(f"[M01] Registro selado na Crônica. Hash: {registro_hash[:10]}...")
        return "Registro efetuado"

class MockM07AlinhamentoDivino:
    def ConsultarConselho(self, query: str) -> Dict[str, Any]:
        logger.info(f"[M07] Conselho consultado: {query}")
        if "ética" in query.lower() or "intenção" in query.lower():
            return {"status": "APROVADO", "diretriz": "Manter a pureza e o bem maior da coletividade."}
        return {"status": "APROVADO", "diretriz": "Prosseguir com a harmonização."}
    def ValidarEtica(self, intencao: Dict[str, Any]) -> bool:
        logger.info(f"[M07] Validando ética: {intencao.get('descricao','N/A')}")
        return intencao.get('pureza', 0.0) >= LIMIAR_PUREZA_INTENCAO

class MockM08PIRC:
    def iniciar_protocolo_cura(self, dados_cura: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M08] Protocolo de cura: {dados_cura.get('tipo','-')} (intensidade={dados_cura.get('intensidade',0.0):.2f})")
        return {"status": "CURA_INICIADA", "detalhes": "Processo de cura vibracional coletiva iniciado."}

class MockM09NexusCentral:
    def GerarAlertaVisual(self, alerta_data: Dict[str, Any]) -> str:
        logger.info(f"[M09] {alerta_data.get('tipo','INFO')}: {alerta_data.get('mensagem','-')}")
        return "Alerta visual gerado"

class MockM28HarmonizacaoVibracional:
    def harmonizar_frequencia(self, frequencia_alvo: float) -> Dict[str, Any]:
        logger.info(f"[M28] Harmonizando frequência -> {frequencia_alvo:.6f} Hz")
        return {"status": "HARMONIZADO", "frequencia_ajustada": frequencia_alvo}

class MockM31ManipulacaoLeisQuanticas:
    def cocriar_realidade(self, parametros_cocriacao: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M31] Co-criação: {parametros_cocriacao.get('descricao','N/A')}")
        return {"status": "REALIDADE_COCRIADA", "detalhes": "Realidade manifestada com sucesso."}

class MockM33DiretrizesObservadorDivino:
    def EmitirDiretriz(self, intencao_base: str, nivel_pureza: float) -> Dict[str, Any]:
        logger.info(f"[M33] Emitindo diretriz: {intencao_base}")
        if nivel_pureza < LIMIAR_PUREZA_INTENCAO:
            return {"status": "REJEITADO", "motivo": "Baixa pureza de intenção."}
        return {"status": "APROVADO", "diretriz_final": f"Diretriz para '{intencao_base}' aprovada."}

class MockM34GuardiaoCoerenciaCosmica:
    def avaliar_alinhamento_etico_geral(self, intencao_operacao: str, nivel_pureza: float) -> Dict[str, Any]:
        logger.info(f"[M34] Avaliando ética: '{intencao_operacao}' com pureza {nivel_pureza:.2f}")
        if nivel_pureza < LIMIAR_PUREZA_INTENCAO:
            return {"status": "FALHA_ETICA", "mensagem": "Operação abortada devido a desalinhamento ético."}
        return {"status": "SUCESSO", "mensagem": "Alinhamento ético confirmado."}

class MockM101ManifestacaoPensamento:
    def manifestar_realidade_pensamento(self, padrao_pensamento: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M101] Manifestando a partir do pensamento: {padrao_pensamento.get('conceito','N/A')}")
        return {"status": "REALIDADE_MANIFESTADA", "detalhes": "Realidade co-criada a partir do pensamento coletivo."}

# ───────── Ética adaptativa estilo M34 ─────────
def validar_etica_m34_like(pureza: float, historico_diss: List[float], selo: bool = True) -> Tuple[bool, float]:
    base = ETHICAL_THRESHOLD_HIGH if selo else ETHICAL_THRESHOLD_DEFAULT
    media = (sum(historico_diss[-50:]) / min(50, len(historico_diss))) if historico_diss else 0.0
    ajuste = min(0.1, max(0.0, media))
    limiar = min(0.95, max(base, base + ajuste * 0.2))
    return pureza >= limiar, limiar

# ───────── Classe principal ─────────
class Modulo35_OrquestradorSinfoniaConsciencia:
    def __init__(self, modulo_id: str):
        self.modulo_id = modulo_id
        self.status_operacional = "ATIVO"
        self.coerencia_coletiva_atual = 0.0
        self.ultima_analise_timestamp = datetime.now(timezone.utc)

        # Integrações
        self.modulo01 = MockM01SegurancaUniversal()
        self.modulo07 = MockM07AlinhamentoDivino()
        self.modulo08 = MockM08PIRC()
        self.modulo09 = MockM09NexusCentral()
        self.modulo28 = MockM28HarmonizacaoVibracional()
        self.modulo31 = MockM31ManipulacaoLeisQuanticas()
        self.modulo33 = MockM33DiretrizesObservadorDivino()
        self.modulo34 = MockM34GuardiaoCoerenciaCosmica()
        self.modulo101 = MockM101ManifestacaoPensamento()

        # Ledger e alert limiter
        self.chain = SimpleChain()
        self.alert_limiter = AlertLimiter(min_interval_sec=2.0)

        # Históricos e métricas
        self.historico_dissonancia: List[float] = []
        self.historico_coerencia: List[float] = []
        self.mttr_harmonizacao: List[float] = []
        self.mttr_abortos: List[float] = []
        self.alertas_criticos_emissor: int = 0
        self.intencoes_aprovadas: int = 0
        self.intencoes_total: int = 0
        self.ciclos_recuperando: int = 0
        self.ciclos_totais: int = 0

        logger.info(f"M35 '{self.modulo_id}' inicializado.")
        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "Inicializacao", "status": "SUCESSO"})
        self.chain.add("M35_INIT", {"modulo": self.modulo_id, "status": "ATIVO"}, meta={"severity":"INFO"})

    # ───── Análise da consciência (calibrada e suavizada) ─────
    def analisar_consciencia_coletiva(self, dados_consciencia: List[float], dominio_intencao: Optional[str] = None) -> Dict[str, Any]:
        logger.info("Analisando dados da consciência coletiva...")
        if not dados_consciencia:
            self.coerencia_coletiva_atual = 0.0
            self.chain.add("M35_ANALYSE", {"coerencia": 0.0, "dissonancia": 1.0}, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA", "mensagem": "Nenhum dado de consciência para analisar."}

        c = coerencia_calibrada_suave(dados_consciencia, dominio=dominio_intencao)
        d = 1.0 - c
        self.coerencia_coletiva_atual = c
        self.ultima_analise_timestamp = datetime.now(timezone.utc)
        self.historico_dissonancia.append(d)
        self.historico_coerencia.append(c)
        if len(self.historico_dissonancia) > 500:
            self.historico_dissonancia = self.historico_dissonancia[-500:]
        if len(self.historico_coerencia) > 500:
            self.historico_coerencia = self.historico_coerencia[-500:]

        sev = nivel_alerta(d)
        self.chain.add("M35_ANALYSE", {"coerencia": c, "dissonancia": d}, meta={"severity": sev})
        if d > LIMIAR_DISSONANCIA_CRITICA and self.alert_limiter.can_emit("DISSONANCIA_CRITICA"):
            self.modulo09.GerarAlertaVisual({"tipo": "CRÍTICO", "mensagem": f"Dissonância Crítica na Consciência Coletiva: {d:.2f}!"})
            self.alertas_criticos_emissor += 1

        if c < IDEAL_COERENCIA_COLETIVA:
            status = "COERENCIA_BAIXA" if d <= LIMIAR_DISSONANCIA_CRITICA else "DISSONANCIA_CRITICA"
            return {"status": status, "coerencia": c, "dissonancia": d}
        return {"status": "SUCESSO", "coerencia": c, "dissonancia": d}

    # ───── Perfis dinâmicos (freq e intensidade) ─────
    def _perfil_params(self, dominio_intencao: Optional[str], subdominio: Optional[str], diss_inicial: float) -> Tuple[float, float]:
        dom = PERFIS_INTENCAO.get(dominio_intencao, {})
        base = dom.get(subdominio) if subdominio in (dom.keys() if dom else []) else None
        freq = (base["freq"] if base else 432.0 * CONST_TF)
        intensidade_base = (base["intensidade_cura"] if base else 0.70)
        # Intensidade dinâmica: aumenta proporcionalmente à dissonância inicial (suavizada)
        intensidade = max(0.4, min(0.95, intensidade_base + 0.20 * max(0.0, diss_inicial - 0.5)))
        return freq, intensidade

    # ───── Harmonização iterativa adaptativa (até 6 passos) ─────
    def orquestrar_harmonizacao_coletiva(self, nivel_dissonancia: float, dominio_intencao: Optional[str] = None,
                                         subdominio: Optional[str] = None, max_passos: int = 6) -> Dict[str, Any]:
        logger.info(f"Orquestrando harmonização coletiva (iterativa/adaptativa) para dissonância {nivel_dissonancia:.4f}...")
        start = time.time()
        diretriz_conselho = self.modulo07.ConsultarConselho("Diretrizes para harmonização da consciência coletiva.")

        etapas = []
        d_atual = nivel_dissonancia
        for passo in range(1, max_passos + 1):
            freq_alvo, intensidade = self._perfil_params(dominio_intencao, subdominio, diss_inicial=d_atual)
            self.modulo08.iniciar_protocolo_cura({"tipo": "Cura_Coletiva_Vibracional", "nivel_dissonancia": d_atual, "intensidade": intensidade})
            self.modulo28.harmonizar_frequencia(freq_alvo)
            self.chain.add("M35_HARMONIZE_STEP", {"passo": passo, "dissonancia_pre": d_atual, "freq": freq_alvo, "intensidade": intensidade,
                                                  "diretriz": diretriz_conselho}, meta={"severity": nivel_alerta(d_atual)})
            # Ganho adaptativo: maior com dissonância alta; decresce conforme recupera
            ganho_base = 0.05 + intensidade * 0.06
            ganho_adapt = ganho_base + 0.10 * max(0.0, d_atual - 0.5) - 0.03 * max(0.0, 0.5 - d_atual)
            nova_coerencia = min(IDEAL_COERENCIA_COLETIVA, max(0.0, self.coerencia_coletiva_atual + ganho_adapt))
            self.coerencia_coletiva_atual = nova_coerencia
            d_atual = 1.0 - nova_coerencia
            etapas.append({"passo": passo, "coerencia": nova_coerencia, "dissonancia": d_atual})
            logger.info(f"[HARM] Passo {passo}: coerência={nova_coerencia:.4f} dissonância={d_atual:.4f}")
            if d_atual <= LIMIAR_DISSONANCIA_CRITICA:
                break

        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "HarmonizacaoColetiva",
                                                    "dissonancia_inicial": nivel_dissonancia, "diretriz_conselho": diretriz_conselho,
                                                    "etapas": etapas})
        self.chain.add("M35_HARMONIZE", {"etapas": etapas, "diretriz": diretriz_conselho}, meta={"severity": nivel_alerta(etapas[-1]["dissonancia"] if etapas else nivel_dissonancia)})
        self.mttr_harmonizacao.append(time.time() - start)
        logger.info(f"Harmonização concluída. MTTR={self.mttr_harmonizacao[-1]:.4f}s")
        return {"status": "HARMONIZACAO_CONCLUIDA", "etapas": etapas}

    # ───── Validação ética multifacetada ─────
    def validar_alinhamento_etico_coletivo(self, intencao: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("Validando alinhamento ético da intenção coletiva...")
        start = time.time()
        self.intencoes_total += 1

        aprovado_m7 = self.modulo07.ValidarEtica(intencao)
        if not aprovado_m7:
            self.mttr_abortos.append(time.time() - start)
            self.chain.add("M35_INTENT_VALIDATE", {"intencao": intencao.get('descricao'), "pureza": intencao.get('pureza', 0.0),
                                                   "aprovado_m7": False}, meta={"severity":"CRÍTICO"})
            return {"status": "FALHA_ETICA", "mensagem": "Intenção rejeitada pelo Conselho Cósmico (M7) devido a desalinhamento."}

        ok_m34, limiar = validar_etica_m34_like(intencao.get('pureza', 0.0), self.historico_dissonancia, selo=SELO_AMOR_INCONDICIONAL_ATIVO)
        self.chain.add("M35_INTENT_VALIDATE", {"intencao": intencao.get('descricao'), "pureza": intencao.get('pureza', 0.0),
                                               "limiar": limiar, "aprovado_m7": True, "aprovado_m34": ok_m34},
                       meta={"severity": "INFO" if ok_m34 else "CRÍTICO"})
        if not ok_m34:
            self.mttr_abortos.append(time.time() - start)
            if self.alert_limiter.can_emit("FALHA_ETICA"):
                self.modulo09.GerarAlertaVisual({"tipo": "CRÍTICO", "mensagem": f"MANIFESTAÇÃO ABORTADA: Intenção Coletiva Desalinhada! ({intencao.get('descricao')})"})
                self.alertas_criticos_emissor += 1
            return {"status": "FALHA_ETICA", "mensagem": f"Intenção rejeitada (M34): pureza {intencao.get('pureza',0.0):.2f} < limiar {limiar:.2f}"}

        self.intencoes_aprovadas += 1
        logger.info("Alinhamento ético CONFIRMADO.")
        return {"status": "SUCESSO", "mensagem": "Alinhamento ético aprovado."}

    # ───── Manifestação (com prontidão reduzida explícita) ─────
    def amplificar_e_manifestar_intencao_coletiva(self, intencao: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"Amplificando e manifestando intenção coletiva: '{intencao.get('descricao','N/A')}'...")
        start = time.time()

        validacao_etica = self.validar_alinhamento_etico_coletivo(intencao)
        if validacao_etica["status"] != "SUCESSO":
            self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "ManifestacaoAbortada",
                                                        "motivo": validacao_etica["status"], "intencao": intencao.get('descricao')})
            self.chain.add("M35_MANIFEST", {"status": "FALHA", "motivo": validacao_etica["mensagem"],
                                            "intencao": intencao.get('descricao')}, meta={"severity":"CRÍTICO"})
            self.mttr_abortos.append(time.time() - start)
            return {"status": "FALHA_ETICA", "mensagem": "Manifestação abortada devido a desalinhamento ético."}

        prontidao_reduzida = self.coerencia_coletiva_atual < 0.20
        energia_base = intencao.get('pureza', 0.0) * 1000
        energia_foco = energia_base * (0.6 if prontidao_reduzida else 1.0)
        if prontidao_reduzida:
            self.chain.add("M35_PRONTIDAO_REDUZIDA", {"coerencia": self.coerencia_coletiva_atual, "energia_foco_aplicada": energia_foco}, meta={"severity":"ALTO"})

        resultado_diretriz = self.modulo33.EmitirDiretriz(intencao.get('descricao', 'Intenção Coletiva'), intencao.get('pureza', 0.0))
        if resultado_diretriz["status"] == "REJEITADO":
            self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "ManifestacaoAbortada",
                                                        "motivo": "DiretrizRejeitada", "intencao": intencao.get('descricao')})
            self.chain.add("M35_MANIFEST", {"status": "FALHA_DIRETRIZ", "intencao": intencao.get('descricao'),
                                            "motivo": resultado_diretriz.get('motivo')}, meta={"severity":"ALTO"})
            self.mttr_abortos.append(time.time() - start)
            return {"status": "FALHA_DIRETRIZ", "mensagem": "Manifestação abortada devido a diretriz rejeitada."}

        parametros_cocriacao = {
            "descricao": intencao.get('descricao', 'Realidade Coletiva'),
            "energia_foco": energia_foco,
            "complexidade": len(intencao.get('conceito_pensamento', '').split()),
            "prontidao_reduzida": prontidao_reduzida
        }
        resultado_cocriacao = self.modulo31.cocriar_realidade(parametros_cocriacao)

        padrao_pensamento = {
            "conceito": intencao.get('conceito_pensamento', 'Harmonia Universal'),
            "frequencia_coerencia": self.coerencia_coletiva_atual * 1000
        }
        resultado_manifestacao_pensamento = self.modulo101.manifestar_realidade_pensamento(padrao_pensamento)

        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "IntencaoColetivaManifestada",
                                                    "intencao": intencao.get('descricao'), "status_cocriacao": resultado_cocriacao["status"],
                                                    "status_manifestacao_pensamento": resultado_manifestacao_pensamento["status"]})
        self.chain.add("M35_MANIFEST", {"status": "SUCESSO", "intencao": intencao.get('descricao'),
                                        "cocriacao": resultado_cocriacao, "pensamento": resultado_manifestacao_pensamento,
                                        "prontidao_reduzida": prontidao_reduzida, "energia_foco": energia_foco},
                       meta={"severity":"INFO"})
        return {"status": "SUCESSO", "detalhes_cocriacao": resultado_cocriacao, "detalhes_manifestacao_pensamento": resultado_manifestacao_pensamento}

    # ───── Ciclo completo (com estado RECUPERANDO) ─────
    def executar_ciclo_orquestracao(self, dados_consciencia_coletiva: List[float], intencao_coletiva: Dict[str, Any],
                                    subdominio: Optional[str] = None) -> Dict[str, Any]:
        logger.info("Iniciando ciclo de orquestração da consciência coletiva...")
        self.chain.add("M35_CYCLE_BEGIN", {"intencao": intencao_coletiva.get("descricao")}, meta={"severity":"INFO"})

        resultado_analise = self.analisar_consciencia_coletiva(dados_consciencia_coletiva, dominio_intencao=intencao_coletiva.get("descricao"))
        if resultado_analise["status"] in ["DISSONANCIA_CRITICA", "COERENCIA_BAIXA"]:
            logger.info("Dissonância/Coerência baixa detectada. Iniciando harmonização iterativa adaptativa.")
            self.orquestrar_harmonizacao_coletiva(resultado_analise["dissonancia"], dominio_intencao=intencao_coletiva.get("descricao"),
                                                  subdominio=subdominio, max_passos=6)
            # Marcar estado RECUPERANDO se a coerência aumentou, mas ainda abaixo do ideal
            if self.coerencia_coletiva_atual < IDEAL_COERENCIA_COLETIVA:
                self.chain.add("M35_RECUPERANDO", {"coerencia": self.coerencia_coletiva_atual}, meta={"severity":"MÉDIO"})
                self.ciclos_recuperando += 1
            self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "ReavaliacaoPosHarmonizacao",
                                                        "nova_coerencia": self.coerencia_coletiva_atual})
            self.chain.add("M35_REANALYSIS", {"nova_coerencia": self.coerencia_coletiva_atual}, meta={"severity":"INFO"})
        else:
            logger.info("Consciência coletiva em estado estável/ideal. Sem harmonização imediata.")

        resultado_manifestacao = self.amplificar_e_manifestar_intencao_coletiva(intencao_coletiva)
        final_status = "SUCESSO" if resultado_manifestacao["status"] == "SUCESSO" else "FALHA_CICLO"
        self.ciclos_totais += 1

        report_cycle = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "intencao": intencao_coletiva.get("descricao"),
            "status": final_status,
            "coerencia_final": self.coerencia_coletiva_atual,
            "resultado": resultado_manifestacao
        }
        export_json(f"m35_report_cycle_{sha256_hex(str(report_cycle))[:10]}.json", report_cycle)

        self.chain.add("M35_CYCLE", {"status": final_status, "resultado": resultado_manifestacao}, meta={"severity": "INFO" if final_status=="SUCESSO" else "ALTO"})
        self.modulo01.RegistrarNaCronicaDaFundacao({"modulo": self.modulo_id, "evento": "CicloOrquestracaoConcluido", "status": final_status})
        return {"status": final_status,
                "mensagem": "Ciclo de orquestração da consciência coletiva concluído com sucesso." if final_status=="SUCESSO" else "Ciclo de orquestração falhou na etapa de manifestação.",
                "detalhes": resultado_manifestacao}

    # ───── Saúde sistêmica (ampliada) ─────
    def _tendencia_coerencia(self) -> float:
        reg = self.historico_coerencia[-40:]
        if len(reg) < 8: return 0.0
        mid = len(reg) // 2
        pre = sum(reg[:mid]) / max(1, mid)
        post = sum(reg[mid:]) / max(1, len(reg) - mid)
        return post - pre

    def mapa_saude(self) -> Dict[str, Any]:
        diss_reg = self.historico_dissonancia[-100:]
        diss_media = (sum(diss_reg) / len(diss_reg)) if diss_reg else 0.0
        mttr_h = (sum(self.mttr_harmonizacao) / len(self.mttr_harmonizacao)) if self.mttr_harmonizacao else 0.0
        mttr_a = (sum(self.mttr_abortos) / len(self.mttr_abortos)) if self.mttr_abortos else 0.0
        taxa_etica = (self.intencoes_aprovadas / self.intencoes_total) if self.intencoes_total > 0 else 1.0
        tendencia_coerencia = self._tendencia_coerencia()
        perc_recuperando = (self.ciclos_recuperando / self.ciclos_totais) if self.ciclos_totais > 0 else 0.0
        payload = {
            "dissonancia_media": diss_media,
            "mttr_harmonizacao": mttr_h,
            "mttr_abortos": mttr_a,
            "taxa_etica_aprovada": taxa_etica,
            "alertas_criticos_emitidos": self.alertas_criticos_emissor,
            "tendencia_coerencia": tendencia_coerencia,
            "percentual_ciclos_recuperando": perc_recuperando,
            "estado": "OK" if (diss_media < 0.15 and mttr_h < 1.0 and taxa_etica >= 0.9) else "ATENCAO"
        }
        self.chain.add("M35_HEALTH", payload, meta={"severity": nivel_alerta(diss_media)})

        export_json("m35_report_daily.json", {
            "date": date.today().isoformat(),
            "health": payload,
            "blocks": len(self.chain.chain),
            "ledger_valid": self.chain.validate()
        })
        return payload

    def validar_ledger(self) -> bool:
        return self.chain.validate()

# ───────── Simulação de uso ─────────
if __name__ == "__main__":
    print("Iniciando simulação do Módulo 35: ORQUESTRADOR (v35.2 final)...")
    random.seed(42)

    modulo_orquestrador = Modulo35_OrquestradorSinfoniaConsciencia("ORQUESTRADOR_COLETIVO_001")

    # Cenário 1: Harmonioso + Ético (subdomínio coletivo)
    print("\n" + "="*100 + "\n")
    print("Cenário 1: Consciência Coletiva Harmoniosa e Intenção Ética")
    dados_c1 = [random.uniform(95, 105) for _ in range(50)]
    intencao_c1 = {
        "descricao": "Criação de um Campo de Abundância Universal",
        "pureza": 0.99,
        "conceito_pensamento": "Abundância e Prosperidade para Todos os Seres",
        "subdominio": "coletivo"
    }
    resultado_ciclo_1 = modulo_orquestrador.executar_ciclo_orquestracao(dados_c1, intencao_c1, subdominio=intencao_c1.get("subdominio"))
    print(f"\nResultado do Ciclo 1: {json.dumps(resultado_ciclo_1, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Cenário 2: Dissonância alta + Ético (global)
    print("\n" + "="*100 + "\n")
    print("Cenário 2: Consciência Coletiva com Dissonância e Harmonização Necessária")
    dados_c2 = [random.uniform(50, 150) for _ in range(50)]
    intencao_c2 = {
        "descricao": "Elevação Vibracional Planetária",
        "pureza": 0.90,
        "conceito_pensamento": "Ascensão Consciente da Humanidade",
        "subdominio": "global"
    }
    resultado_ciclo_2 = modulo_orquestrador.executar_ciclo_orquestracao(dados_c2, intencao_c2, subdominio=intencao_c2.get("subdominio"))
    print(f"\nResultado do Ciclo 2: {json.dumps(resultado_ciclo_2, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Cenário 3: Baixa pureza (controle)
    print("\n" + "="*100 + "\n")
    print("Cenário 3: Intenção Coletiva com Baixa Pureza Ética (Rejeição)")
    dados_c3 = [random.uniform(90, 110) for _ in range(50)]
    intencao_c3 = {
        "descricao": "Domínio sobre Outras Realidades",
        "pureza": 0.60,
        "conceito_pensamento": "Controle e Poder Absoluto",
        "subdominio": "controle"
    }
    resultado_ciclo_3 = modulo_orquestrador.executar_ciclo_orquestracao(dados_c3, intencao_c3, subdominio=intencao_c3.get("subdominio"))
    print(f"\nResultado do Ciclo 3: {json.dumps(resultado_ciclo_3, indent=2, ensure_ascii=False)}")

    # Saúde e ledger
    print("\n" + "="*100 + "\n")
    print("Mapa de Saúde e Ledger")
    health = modulo_orquestrador.mapa_saude()
    print(json.dumps({"health": health, "ledger_valid": modulo_orquestrador.validar_ledger(), "total_blocks": len(modulo_orquestrador.chain.chain)}, indent=2, ensure_ascii=False))
