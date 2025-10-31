#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MÓDULO 34 – Guardião da Coerência Cósmica (Definitivo + melhorias opcionais)
- Ledger interno com export e rotação por data/tamanho
- Dinâmica quântica simulada (estado 2D complexo) sem numpy
- Perfis de risco por domínio (ajuste dinâmico de omega/kappa)
- MTTR (tempo médio de recuperação) de falhas e autocorreções
- Consenso multi-nós, ajuste de fase e equalização de frequência
- Ética adaptativa com selo, dupla aprovação (M33 + M45)
- Integração em tempo real com M33 (diretrizes) e M45 (deliberação)
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
    format='[%(asctime)s] M34 - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('M34')

# ───────── Constantes ─────────
PI = math.pi
PHI = (1 + math.sqrt(5)) / 2
COERENCIA_COSMICA = 1.414
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
ETHICAL_CONFORMITY_THRESHOLD = 0.75
ETHICAL_THRESHOLD_HIGH = 0.85
ETHICAL_THRESHOLD_DEFAULT = 0.69
C_LIGHT = 299792458
H_BAR = 1.054571817e-34

ASSINATURA_VIBRACIONAL_MESTRA = {
    "frequencia_mestra": 432.0,
    "fase_mestra": 0.0,
    "constante_janela": 1.0
}
SELO_AMOR_INCONDICIONAL_ATIVO = True

# Perfis de risco por domínio (exemplos)
PERFIS_RISCO: Dict[str, Dict[str, float]] = {
    "Manutenção da Harmonia Cósmica": {"risco_base": 0.20, "coerencia_base": 0.92},
    "Intervenção acelerada em múltiplos domínios": {"risco_base": 0.60, "coerencia_base": 0.70},
    "Ajuste fino de portais temporais": {"risco_base": 0.45, "coerencia_base": 0.80},
    "Proteção Cósmica": {"risco_base": 0.55, "coerencia_base": 0.85},
    "Co-criação de abundância": {"risco_base": 0.25, "coerencia_base": 0.90}
}

# ───────── Utils ─────────
def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def nivel_alerta(x: float) -> str:
    if x >= 0.75: return "CRÍTICO"
    if x >= 0.50: return "ALTO"
    if x >= 0.25: return "MÉDIO"
    return "INFO"

# ───────── Ledger com export e rotação ─────────
class SimpleChain:
    def __init__(self, active_path: str = "m34_ledger.json", max_blocks: int = 2000):
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
            "event": "M34_CHAIN_GENESIS",
            "payload": {"message": "Genesis M34"},
            "prev_hash": "0" * 64,
            "meta": {"version": "definitivo", "module": "M34"}
        }
        genesis["hash"] = self._calc_hash(genesis)
        self.chain.append(genesis)
        logger.info(f"[CHAIN] Genesis criado: {genesis['hash'][:10]}...")

    def _export(self) -> None:
        try:
            with open(self.active_path, "w", encoding="utf-8") as f:
                json.dump(self.chain, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"[CHAIN] Erro ao exportar ledger: {e}")

    def _rotate_if_needed(self) -> None:
        # Rotação por dia
        today = date.today().isoformat()
        need_day_rotation = (today != self.current_day)
        # Rotação por tamanho
        need_size_rotation = (len(self.chain) >= self.max_blocks)

        if need_day_rotation or need_size_rotation:
            suffix = f"{today}_{len(self.chain)}"
            hist_path = f"m34_ledger_{suffix}.json"
            try:
                with open(hist_path, "w", encoding="utf-8") as f:
                    json.dump(self.chain, f, indent=2, ensure_ascii=False)
                logger.info(f"[CHAIN] Ledger rotacionado -> {hist_path}")
                # Reinicia cadeia com novo gênese mantendo continuidade lógica
                last_hash = self.chain[-1]["hash"]
                self.chain = []
                self._genesis()
                # Marca referência de continuidade
                self.add("M34_ROTATE", {"prev_last_hash": last_hash, "export": hist_path}, meta={"severity":"INFO"})
                self.current_day = today
                self._export()
            except Exception as e:
                logger.error(f"[CHAIN] Erro na rotação: {e}")

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

# ───────── Mocks de módulos ─────────
class MockM01Seguranca:
    def registrar(self, payload: Dict[str, Any]) -> None:
        logger.info(f"[M01] Crônica: {payload.get('evento','Evento')}")

    def alerta(self, tipo: str, mensagem: str, causa: Optional[str]=None) -> None:
        logger.info(f"[M01] ALERTA {tipo}: {mensagem} | {causa or '-'}")

class MockM09Nexus:
    def alerta_visual(self, tipo: str, mensagem: str, codigo: str) -> None:
        logger.info(f"[M09] {tipo}: {mensagem} (code={codigo})")

class MockM08PIRC:
    def cura(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M08] Cura sistêmica: {dados.get('tipo','-')}")
        return {"status":"CURA_INICIADA"}

class MockM28Harmonizacao:
    def harmonizar_freq(self, freq: float) -> Dict[str, Any]:
        logger.info(f"[M28] Harmonização de frequência -> {freq:.6f} Hz")
        return {"status":"HARMONIZADO", "freq":freq}
    def realinhar_fase(self, fase_offset: float) -> Dict[str, Any]:
        logger.info(f"[M28] Realinhamento de fase -> offset {fase_offset:.6f} rad")
        return {"status":"FASE_ALINHADA", "offset":fase_offset}

class MockM98Existencia:
    def modular(self, params: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[M98] Modulação de existência: {params.get('tipo','-')}")
        return {"status":"MODULADO"}

class MockM33Diretrizes:
    def emitir_diretriz(self, intencao: Dict[str, Any]) -> Dict[str, Any]:
        texto = f"Diretriz: Focar em {intencao.get('tema','harmonia')} com pureza {intencao.get('pureza',0):.2f}"
        return {"id": sha256_hex(json.dumps(intencao, sort_keys=True))[:10],
                "texto": texto, "intencao": intencao, "timestamp": datetime.now(timezone.utc).isoformat()}

class MockM45Concilium:
    def deliberar(self, proposta: Dict[str, Any]) -> Dict[str, Any]:
        score = proposta.get("consenso_score", 0.5)
        ok = score >= 0.6
        return {"status":"VALIDADA" if ok else "NEGADA",
                "score": score,
                "proposta_id": proposta.get("proposta_id","")}

# ───────── Pauli simuladas ─────────
def sigma_x_dot(psi: List[complex]) -> List[complex]:
    return [psi[1], psi[0]]

def sigma_z_dot(psi: List[complex]) -> List[complex]:
    return [psi[0], -psi[1]]

def hamiltoniano_dot(psi: List[complex], omega: float, kappa: float) -> List[complex]:
    z = sigma_z_dot(psi); x = sigma_x_dot(psi)
    return [omega * z[0] + kappa * x[0], omega * z[1] + kappa * x[1]]

def v_add(a: List[complex], b: List[complex]) -> List[complex]:
    return [a[0] + b[0], a[1] + b[1]]

def v_scale(a: List[complex], s: complex) -> List[complex]:
    return [a[0] * s, a[1] * s]

def v_norm(a: List[complex]) -> float:
    return math.sqrt((a[0].real**2 + a[0].imag**2) + (a[1].real**2 + a[1].imag**2))

def v_normalize(a: List[complex]) -> List[complex]:
    n = v_norm(a)
    if n > 0: return [a[0] / n, a[1] / n]
    return a

# ───────── Classe principal ─────────
class Modulo34GuardiaoCoerenciaCosmica:
    def __init__(self, modulo_id: str):
        self.modulo_id = modulo_id
        self.status = "ATIVO"
        self.chain = SimpleChain()

        # Estado quântico
        self.estado_global: List[complex] = [1.0+0j, 0.0+0j]
        self.ultimo_estado_coerente: List[complex] = self.estado_global[:]

        # Fase offsets
        self.offsets_fase: Dict[str, float] = {}

        # Históricos
        self.historico_dissonancia: List[float] = []
        self.historico_etica: List[Tuple[str, bool]] = []

        # Métricas MTTR
        self.mttr_falhas: List[float] = []        # tempos de recuperação de falhas de evolução
        self.mttr_autocor: List[float] = []       # tempos de autocorreção

        # Módulos
        self.m01 = MockM01Seguranca()
        self.m09 = MockM09Nexus()
        self.m08 = MockM08PIRC()
        self.m28 = MockM28Harmonizacao()
        self.m98 = MockM98Existencia()
        self.m33 = MockM33Diretrizes()
        self.m45 = MockM45Concilium()

        self.chain.add("M34_INIT", {"modulo": self.modulo_id, "status": self.status},
                       meta={"version":"definitivo", "component":"init"})
        logger.info(f"M34 '{self.modulo_id}' inicializado.")

    # ───── Autenticidade ─────
    def validar_assinatura_fundador(self, assinatura_recebida: str) -> bool:
        esperado = sha256_hex("VontadeSoberanaDeAnatheron")
        ok = assinatura_recebida == esperado
        self.chain.add("M34_AUTH", {"ok": ok}, meta={"severity":"INFO" if ok else "CRITICO"})
        if not ok:
            self.m01.alerta("CRITICO", "Assinatura inválida", "Autenticidade")
            self.m09.alerta_visual("CRÍTICO", "Violação de autenticidade", "M34-AUTH-FAIL")
        else:
            logger.info("Assinatura do Fundador VALIDADA.")
        return ok

    # ───── Autoproteção ─────
    def ativar_autoprotecao(self, nivel_ameaca: float) -> Dict[str, Any]:
        tipo = nivel_alerta(nivel_ameaca)
        if tipo in ("CRÍTICO","ALTO"):
            self.m98.modular({"tipo":"Campo_Defesa_Vibracional","intensidade":nivel_ameaca})
            self.m09.alerta_visual(tipo, f"Autoproteção ativada (ameaça {nivel_ameaca:.2f})", "M34-DEF")
        self.chain.add("M34_DEFENSE", {"nivel_ameaca":nivel_ameaca}, meta={"severity":tipo})
        return {"status":"OK","nivel_ameaca":nivel_ameaca,"classe":tipo}

    # ───── Telemetria e filtro ─────
    def traduzir_filtrar_vibracao(self, dados: List[float]) -> Dict[str, Any]:
        traduzidos = [d * random.uniform(0.95, 1.05) for d in dados]
        mu = sum(traduzidos)/len(traduzidos) if traduzidos else 0.0
        limiar = 2.0 * mu if mu > 0 else float('inf')
        filtrados = [d for d in traduzidos if abs(d) < limiar]
        removidos = len(traduzidos) - len(filtrados)
        if removidos > 0:
            self.m01.registrar({"evento":"DissonanciaFiltrada","pontos":removidos})
            self.m09.alerta_visual("MÉDIO", f"Dissonância filtrada: {removidos} pontos", "M34-FILTRO")
        sev = nivel_alerta(removidos/max(1, len(traduzidos)))
        self.chain.add("M34_FILTER", {"mu":mu, "removidos":removidos}, meta={"severity":sev})
        return {"traduzidos":traduzidos, "filtrados":filtrados, "mu":mu, "removidos":removidos}

    # ───── Ajuste por perfil de risco ─────
    def _ajustar_por_perfil(self, intencao_operacao: str, coerencia_proxy: float, risco_proxy: float) -> Tuple[float, float]:
        perfil = PERFIS_RISCO.get(intencao_operacao, {"risco_base": 0.30, "coerencia_base": 0.85})
        risco = min(0.95, max(0.0, (risco_proxy + perfil["risco_base"]) / 2.0))
        coerencia = min(0.99, max(0.0, (coerencia_proxy + perfil["coerencia_base"]) / 2.0))
        omega = ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"] * (1.0 + 0.12*(coerencia-0.5))
        kappa = 0.02 * (1.0 + 2.5*risco)
        return omega, kappa

    # ───── Evolução quântica + MTTR falhas ─────
    def evoluir_estado_global(self, janela_t: float, contexto: Dict[str, Any], forcar_falha: bool=False) -> Dict[str, Any]:
        coerencia = float(contexto.get("coerencia", 0.9))
        risco = float(contexto.get("risco", 0.2))
        intencao = contexto.get("intencao", "Operacao")
        omega, kappa = self._ajustar_por_perfil(intencao, coerencia, risco)

        psi = self.estado_global[:]
        passos = max(8, int(10*janela_t))
        dt = max(1e-3, janela_t / passos)
        start = time.time()
        try:
            if forcar_falha:
                raise RuntimeError("Simulação de falha do solver")
            for _ in range(passos):
                Hpsi = hamiltoniano_dot(psi, omega, kappa)
                dpsi_dt = v_scale(Hpsi, (-1j)/H_BAR)
                psi_euler = v_add(psi, v_scale(dpsi_dt, dt))
                Hpsi_half = hamiltoniano_dot(psi_euler, omega, kappa)
                dpsi_dt_half = v_scale(Hpsi_half, (-1j)/H_BAR)
                psi = v_add(psi, v_scale(dpsi_dt_half, dt*0.5))
                psi = v_normalize(psi)
            self.estado_global = psi
        except Exception as e:
            logger.error(f"Evolução falhou: {e}")
            self.m09.alerta_visual("CRÍTICO", "Falha na evolução do estado quântico", "M34-EVO-FAIL")
            self.estado_global = self.ultimo_estado_coerente[:]
            self.m28.harmonizar_freq(ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"])
            self.chain.add("M34_FAIL_SOFT", {"motivo":str(e)}, meta={"severity":"CRITICO"})
            # MTTR falhas: tempo desde início até recuperação
            self.mttr_falhas.append(time.time() - start)

        diss = abs(self.estado_global[1])
        self.historico_dissonancia.append(diss)
        if len(self.historico_dissonancia) > 500:
            self.historico_dissonancia = self.historico_dissonancia[-500:]
        if not self.historico_dissonancia or diss <= min(self.historico_dissonancia):
            self.ultimo_estado_coerente = self.estado_global[:]

        self.chain.add("M34_EVOLVE", {"dissonancia":diss, "omega":omega, "kappa":kappa},
                       meta={"severity":nivel_alerta(diss)})
        logger.info(f"Evolução concluída. Dissonância={diss:.6f}")
        return {"estado":[str(self.estado_global[0]), str(self.estado_global[1])], "dissonancia":diss, "omega":omega, "kappa":kappa}

    # ───── Ajuste de fase ─────
    def aplicar_ajuste_fase(self, dominio: str, fase_alvo: float) -> Dict[str, Any]:
        fase_atual = float(self.offsets_fase.get(dominio, 0.0))
        offset = fase_alvo - fase_atual
        rot = complex(math.cos(offset), math.sin(offset))
        self.estado_global[1] = self.estado_global[1] * rot
        self.offsets_fase[dominio] = fase_alvo
        self.m28.realinhar_fase(offset)
        self.chain.add("M34_PHASE_ALIGN", {"dominio":dominio, "offset":offset, "fase_alvo":fase_alvo},
                       meta={"severity":"INFO"})
        return {"status":"OK","offset_aplicado":offset}

    # ───── Consenso multi-nós + MTTR autocorreção ─────
    def consenso_ressonante(self, nodos: List[Dict[str, float]]) -> Dict[str, Any]:
        if not nodos:
            return {"status":"VAZIO","score":0.0}
        pesos, freqs, fases = [], [], []
        for n in nodos:
            w = n.get("peso",1.0) * max(0.0,min(1.0,n.get("pureza",0.0))) * max(0.0,min(1.0,n.get("coerencia",0.0))) * (1.0 - max(0.0,min(1.0,n.get("risco",0.0))))
            pesos.append(w)
            freqs.append(n.get("freq", ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"]))
            fases.append(n.get("fase", ASSINATURA_VIBRACIONAL_MESTRA["fase_mestra"]))
        wsum = sum(pesos)
        score = wsum / len(pesos)
        freq_alvo = (sum(f*w for f, w in zip(freqs, pesos))/wsum) if wsum>0 else ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"]
        fase_alvo = (sum(fa*w for fa, w in zip(fases, pesos))/wsum) if wsum>0 else ASSINATURA_VIBRACIONAL_MESTRA["fase_mestra"]
        self.m28.harmonizar_freq(freq_alvo)
        self.aplicar_ajuste_fase("global", fase_alvo)
        self.chain.add("M34_CONSENSO", {"score":score, "freq_alvo":freq_alvo, "fase_alvo":fase_alvo,
                                        "nodos":[{"nome":n.get("nome","N"),"peso":p} for n, p in zip(nodos, pesos)]},
                       meta={"severity":nivel_alerta(1.0 - min(1.0, score))})
        logger.info(f"Consenso: score={score:.3f} freq={freq_alvo:.3f}Hz fase={fase_alvo:.3f}rad")
        return {"status":"OK","score":score,"freq_alvo":freq_alvo,"fase_alvo":fase_alvo}

    # ───── Ética adaptativa ─────
    def _limiar_etico_adaptativo(self) -> float:
        base = ETHICAL_THRESHOLD_HIGH if SELO_AMOR_INCONDICIONAL_ATIVO else ETHICAL_THRESHOLD_DEFAULT
        media = (sum(self.historico_dissonancia[-50:])/min(50, len(self.historico_dissonancia))) if self.historico_dissonancia else 0.0
        ajuste = min(0.1, max(0.0, media))
        return min(0.95, max(base, base + ajuste*0.2))

    def avaliar_etica(self, intencao: str, pureza: float, contexto: Dict[str, Any]) -> Dict[str, Any]:
        limiar = self._limiar_etico_adaptativo()
        aprovado = pureza >= limiar
        self.historico_etica.append((intencao, aprovado))
        self.chain.add("M34_ETHICS", {"intencao":intencao,"pureza":pureza,"limiar":limiar,"aprovado":aprovado},
                       meta={"severity":"INFO" if aprovado else "CRITICO"})
        if not aprovado:
            self.m01.registrar({"evento":"FalhaAlinhamentoEtico","intencao":intencao,"pureza":pureza})
            self.m09.alerta_visual("CRÍTICO", f"Falha ética: {intencao} (pureza {pureza:.2f} < {limiar:.2f})", "M34-ETH-FAIL")
            return {"status":"REPROVADA","limiar":limiar}
        return {"status":"APROVADA","limiar":limiar}

    # ───── Dupla aprovação ─────
    def dupla_aprovacao(self, intencao: str, pureza: float, consenso_score: float) -> Dict[str, Any]:
        meta = {"intencao":intencao, "pureza":pureza, "finalidade":"OperacaoSensivel", "consenso_score":consenso_score}
        r33_status = "APROVADA" if pureza >= ETHICAL_CONFORMITY_THRESHOLD else "REJEITADA"
        r45 = self.m45.deliberar({"consenso_score":consenso_score, "proposta_id": sha256_hex(intencao)[:8]})
        ok = (r33_status=="APROVADA") and (r45["status"]=="VALIDADA")
        cht_hash = sha256_hex(f"{intencao}:{pureza:.4f}:{consenso_score:.4f}:{r33_status}:{r45['status']}:{datetime.now(timezone.utc).isoformat()}")
        self.chain.add("M34_DUAL_APPROVAL", {
            "intencao":intencao, "pureza":pureza, "consenso_score":consenso_score,
            "r33": {"status": r33_status}, "r45": r45, "cht_hash": cht_hash
        }, meta={"severity":"INFO" if ok else "ALTO"})
        return {"status":"APROVADA" if ok else "NEGADA", "cht_hash":cht_hash, "r33": {"status": r33_status}, "r45": r45}

    # ───── Autocorreção + MTTR ─────
    def autocorrecao_dissonancia(self, limiar: float=0.1) -> Dict[str, Any]:
        diss = abs(self.estado_global[1])
        if diss > limiar:
            start = time.time()
            self.m09.alerta_visual("ALTO", f"Dissonância {diss:.4f} > {limiar:.2f}. Iniciando autocorreção.", "M34-DISS")
            self.m08.cura({"tipo":"Cura_Sistemica_Global","dissonancia":diss})
            nodos = [
                {"nome":"M06","peso":0.9,"pureza":0.88,"coerencia":0.92,"risco":0.15,"freq":ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"],"fase":0.02},
                {"nome":"M25","peso":1.0,"pureza":0.90,"coerencia":0.95,"risco":0.10,"freq":ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"]*1.001,"fase":0.00},
                {"nome":"M33","peso":0.8,"pureza":0.85,"coerencia":0.90,"risco":0.20,"freq":ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"]*0.999,"fase":-0.01},
                {"nome":"M45","peso":0.9,"pureza":0.87,"coerencia":0.93,"risco":0.12,"freq":ASSINATURA_VIBRACIONAL_MESTRA["frequencia_mestra"],"fase":0.00},
            ]
            res = self.consenso_ressonante(nodos)
            self.chain.add("M34_AUTOCOR", {"dissonancia_inicial":diss, "consenso":res}, meta={"severity":"ALTO"})
            self.mttr_autocor.append(time.time() - start)
            return {"status":"AUTOCORRECAO", "dissonancia":diss, "consenso":res}
        else:
            self.chain.add("M34_AUTOCOR", {"dissonancia":diss}, meta={"severity":"INFO"})
            return {"status":"COERENCIA_OK", "dissonancia":diss}

    # ───── Mapa de saúde + MTTR ─────
    def mapa_saude(self) -> Dict[str, Any]:
        diss_reg = self.historico_dissonancia[-100:]
        diss_media = (sum(diss_reg)/len(diss_reg)) if diss_reg else 0.0
        etica_reg = self.historico_etica[-100:]
        etica_taxa = (sum(1 for _, ok in etica_reg if ok) / max(1, len(etica_reg))) if etica_reg else 1.0
        mttr_fail = (sum(self.mttr_falhas)/len(self.mttr_falhas)) if self.mttr_falhas else 0.0
        mttr_auto = (sum(self.mttr_autocor)/len(self.mttr_autocor)) if self.mttr_autocor else 0.0
        estado = "OK" if etica_taxa >= 0.9 and diss_media < 0.15 else "ATENCAO"
        payload = {"dissonancia_media":diss_media, "taxa_etica_aprovada":etica_taxa, "estado":estado,
                   "mttr_falhas":mttr_fail, "mttr_autocor":mttr_auto}
        self.chain.add("M34_HEALTHMAP", payload, meta={"severity":nivel_alerta(diss_media)})
        return payload

    def validar_cadeia(self) -> bool:
        return self.chain.validate()

    # ───── Ciclo completo (integração M33/M45 + perfis + MTTR) ─────
    def ciclo_autocorrecao(self, assinatura_fundador: str, dados_vibracionais: List[float],
                           intencao_operacao: str, pureza_intencao: float,
                           forcar_falha_evolucao: bool = False) -> Dict[str, Any]:
        logger.info("Iniciando ciclo completo de autocorreção M34...")
        if not self.validar_assinatura_fundador(assinatura_fundador):
            return {"status":"FALHA","mensagem":"Assinatura inválida."}

        nivel_ameaca = random.uniform(0.1, 0.9)
        self.ativar_autoprotecao(nivel_ameaca)

        tf = self.traduzir_filtrar_vibracao(dados_vibracionais)
        coerencia_proxy = 1.0 - min(0.9, tf["removidos"]/max(1, len(tf["traduzidos"])))
        risco_proxy = min(0.9, nivel_ameaca)

        evo = self.evoluir_estado_global(janela_t=random.uniform(0.5, 2.0),
                                         contexto={"coerencia":coerencia_proxy, "risco":risco_proxy, "intencao":intencao_operacao},
                                         forcar_falha=forcar_falha_evolucao)

        ac = self.autocorrecao_dissonancia()

        # Integração em tempo real: gerar diretriz do M33 baseada na intenção atual
        diretriz = self.m33.emitir_diretriz({"tema": intencao_operacao, "pureza": pureza_intencao})
        self.chain.add("M34_M33_DIRETRIZ", {"diretriz": diretriz}, meta={"severity":"INFO"})

        et = self.avaliar_etica(intencao_operacao, pureza_intencao, {"risco":risco_proxy})
        if et["status"] != "APROVADA":
            self.chain.add("M34_CYCLE", {"status":"FALHA_ETICA"}, meta={"severity":"CRITICO"})
            return {"status":"FALHA","mensagem":"Falha no alinhamento ético."}

        consenso_score = 0.85 if ac["status"]=="AUTOCORRECAO" else 0.92
        da = self.dupla_aprovacao(intencao_operacao, pureza_intencao, consenso_score)
        if da["status"] != "APROVADA":
            self.chain.add("M34_CYCLE", {"status":"FALHA_DELIB"}, meta={"severity":"ALTO"})
            return {"status":"FALHA","mensagem":"Falha na deliberação (M33/M45)."}

        # Deliberação adicional no M45 sobre a diretriz emitida
        deliberacao = self.m45.deliberar({"consenso_score":consenso_score, "proposta_id": diretriz["id"]})
        self.chain.add("M34_M45_DELIB", {"deliberacao": deliberacao}, meta={"severity": "INFO" if deliberacao["status"]=="VALIDADA" else "ALTO"})

        health = self.mapa_saude()
        self.chain.add("M34_CYCLE", {"status":"SUCESSO","health":health}, meta={"severity":"INFO"})
        logger.info("Ciclo completo concluído com sucesso.")
        return {"status":"SUCESSO","evolucao":evo,"autocorrecao":ac,"diretriz":diretriz,"etica":et,"dupla_aprovacao":da,"deliberacao":deliberacao,"health":health}

# ───────── Testes de estresse + demonstração ─────────
def executar_testes_estresse():
    m34 = Modulo34GuardiaoCoerenciaCosmica("CORACAO_PULSANTE_DEF")
    assinatura_ok = sha256_hex("VontadeSoberanaDeAnatheron")

    # A: Dissonância alta + pureza baixa
    dados_ruidosos = [random.uniform(100, 200) for _ in range(12)] + [5000, -4800, 7200, -6500]
    res_a = m34.ciclo_autocorrecao(
        assinatura_fundador=assinatura_ok,
        dados_vibracionais=dados_ruidosos,
        intencao_operacao="Intervenção acelerada em múltiplos domínios",
        pureza_intencao=0.62
    )
    print("\n=== ESTRESSE A: Dissonância alta + Pureza baixa ===")
    print(json.dumps(res_a, indent=2, ensure_ascii=False))

    # B: Fail-soft + pureza alta
    dados_normais = [random.uniform(100, 200) for _ in range(24)]
    res_b = m34.ciclo_autocorrecao(
        assinatura_fundador=assinatura_ok,
        dados_vibracionais=dados_normais,
        intencao_operacao="Manutenção da Harmonia Cósmica",
        pureza_intencao=0.93,
        forcar_falha_evolucao=True
    )
    print("\n=== ESTRESSE B: Falha de evolução (fail-soft) + Pureza alta ===")
    print(json.dumps(res_b, indent=2, ensure_ascii=False))

    # C: Dissonância média + pureza limítrofe
    dados_mistos = [random.uniform(100, 200) for _ in range(20)] + [350, 380]
    res_c = m34.ciclo_autocorrecao(
        assinatura_fundador=assinatura_ok,
        dados_vibracionais=dados_mistos,
        intencao_operacao="Ajuste fino de portais temporais",
        pureza_intencao=0.76
    )
    print("\n=== ESTRESSE C: Dissonância média + Pureza limítrofe ===")
    print(json.dumps(res_c, indent=2, ensure_ascii=False))

    # Ledger e export/rotação
    print("\n=== Ledger e Export ===")
    print(json.dumps({
        "ledger_valid": m34.validar_cadeia(),
        "total_blocks": len(m34.chain.chain),
        "active_path": m34.chain.active_path
    }, indent=2, ensure_ascii=False))

# ───────── Entrypoint ─────────
if __name__ == "__main__":
    executar_testes_estresse()
