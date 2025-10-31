from __future__ import annotations

import hashlib
import json
import logging
import os
import random
import sys
import time
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple, Callable, cast
from pathlib import Path

# ===============================
# Configuração de Log e Diretório
# ===============================
SAVE_DIR_M39_1 = Path("modulo_39_1_data")
SAVE_DIR_M39_1.mkdir(parents=True, exist_ok=True)

log_file_path_m39_1 = SAVE_DIR_M39_1 / "modulo_39_1_system_trace.log"

# Logger com captura em memória
log_stream: List[str] = []


class StringHandler(logging.Handler):
    def emit(self, record):
        log_stream.append(self.format(record))


# Remove handlers existentes para evitar duplicação
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

log_format = "%(asctime)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler(log_file_path_m39_1, mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)
logging.root.addHandler(file_handler)

stream_handler = StringHandler()
stream_handler.setFormatter(formatter)
logging.root.addHandler(stream_handler)

logging.root.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)


def excepthook(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        cast(Any, sys).__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("Unhandled exception:", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = excepthook

print("Guardião da Integridade e Resiliência Cósmica: Iniciando o Módulo 39.1...", flush=True)
logger.debug("Módulo 39.1 inicializado.")

# ====================================================================================
# Utilitários de configuração dinâmica
# ====================================================================================

def _load_text_file(path: Path) -> Optional[str]:
    try:
        if path.exists():
            return path.read_text(encoding="utf-8")
        return None
    except Exception as e:
        logger.warning(f"Falha ao ler arquivo de texto '{path}': {e}")
        return None


def _parse_config(text: str) -> Dict[str, Any]:
    """
    Aceita JSON; se YAML estiver presente, tenta carregar de forma simples
    sem dependências externas (chaves simples).
    """
    text_stripped = text.strip()
    # Tentativa JSON
    try:
        return json.loads(text_stripped)
    except Exception:
        pass
    # Tentativa YAML muito simples: chave: valor
    cfg: Dict[str, Any] = {}
    try:
        for line in text_stripped.splitlines():
            if not line.strip() or line.strip().startswith("#"):
                continue
            if ":" in line:
                k, v = line.split(":", 1)
                key = k.strip()
                val = v.strip()
                # Conversão básica de tipos
                if val.lower() in ("true", "false"):
                    cfg[key] = val.lower() == "true"
                else:
                    try:
                        if "." in val:
                            cfg[key] = float(val)
                        else:
                            cfg[key] = int(val)
                    except Exception:
                        cfg[key] = val
        return cfg
    except Exception as e:
        logger.warning(f"Falha ao interpretar configuração: {e}")
        return {}


def load_external_config(base_dir: Path) -> Dict[str, Any]:
    """
    Carrega configuração de modulo_39_1_config.json ou .yaml; se não existir,
    retorna defaults.
    """
    default = {
        "INTEGRITY_THRESHOLD": 0.95,
        "RESILIENCE_OPTIMAL_THRESHOLD": 0.80,
        "RESILIENCE_CRITICAL_THRESHOLD": 0.50,
        "ETHICAL_ALIGNMENT_THRESHOLD": 0.85,
        "DETERMINISTIC_MODE": False,
        "SEED": None,  # int | None
        "HISTORY_MAX_POINTS": 200,
        "REPORT_EXPORT": True
    }
    json_path = base_dir / "modulo_39_1_config.json"
    yaml_path = base_dir / "modulo_39_1_config.yaml"
    text = _load_text_file(json_path) or _load_text_file(yaml_path)
    if text:
        cfg = _parse_config(text)
        merged = {**default, **cfg}
        logger.info(f"Configuração externa carregada. Chaves: {sorted(merged.keys())}")
        return merged
    logger.info("Configuração externa não encontrada. Usando parâmetros default.")
    return default


# ====================================================================================
# Mocks para Módulos Correlacionados
# ====================================================================================

class MockM01SegurancaUniversal:
    """Mock para Módulo 01: Sistema de Proteção e Segurança Universal."""
    def ReceberAlertaDeViolacao(self, alerta_data: Dict[str, Any]) -> str:
        logger.warning(f"[{datetime.utcnow().isoformat()}] Mock M01 (Segurança): ALERTA! {alerta_data.get('tipo', 'N/A')}: {alerta_data.get('mensagem', 'N/A')}")
        return "Alerta de violação recebido e processado (simulado)."

    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        registro_hash = hashlib.sha256(json.dumps(registro_data, sort_keys=True).encode()).hexdigest()
        logger.info(f"[{datetime.utcnow().isoformat()}] Mock M01 (Segurança): Registro inserido e selado na Crônica da Fundação. Hash: {registro_hash[:10]}...")
        return "Registro na Crônica da Fundação efetuado (simulado)."


class MockM03PrevisaoTemporal:
    """Mock para Módulo 03: Previsão Temporal e Monitoramento de Anomalias Cósmicas."""
    def __init__(self, rnd: Optional[random.Random] = None):
        self._rnd = rnd or random.Random()

    def analisar_fluxo_temporal(self, ponto_temporal: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] Mock M03 (Previsão Temporal): Analisando fluxo temporal para {ponto_temporal.get('descricao', 'N/A')}.")
        # Chance controlada de anomalia
        if self._rnd.random() < 0.15:
            return {"status": "ANOMALIA_DETECTADA", "severidade": self._rnd.uniform(0.5, 0.9), "mensagem": "Anomalia temporal detectada (simulada)."}
        return {"status": "FLUXO_ESTAVEL", "severidade": 0.0, "mensagem": "Fluxo temporal estável (simulado)."}


class MockM08PIRC:
    """Mock para Módulo 08: PIRC (Protocolo de Intervenção e Reajuste de Consciência)."""
    def iniciar_protocolo_cura(self, dados_cura: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] Mock M08 (PIRC): Iniciando protocolo de cura: {dados_cura.get('tipo', 'N/A')} para {dados_cura.get('alvo', 'N/A')}")
        return {"status": "CURA_INICIADA", "detalhes": "Processo de reajuste vibracional iniciado (simulado)."}


class MockM09NexusCentral:
    """Mock para Módulo 09: NEXUS CENTRAL - Dashboard e Alertas."""
    def GerarAlertaVisual(self, alerta_data: Dict[str, Any]) -> str:
        logger.warning(f"[{datetime.utcnow().isoformat()}] Mock M09 (Nexus Central): Gerando alerta visual: {alerta_data.get('mensagem', 'N/A')} (Tipo: {alerta_data.get('tipo', 'N/A')})")
        return "Alerta visual gerado (simulado)."


class MockM23RegulacaoEspacoTemporal:
    """Mock para Módulo 23: Regulação Espaço-Temporal e Orquestração da Causalidade."""
    def __init__(self, rnd: Optional[random.Random] = None):
        self._rnd = rnd or random.Random()

    def detectar_paradoxo(self, evento_temporal: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] Mock M23 (Regulação Espaço-Temporal): Detectando paradoxo para evento: {evento_temporal.get('nome', 'N/A')}.")
        chance_paradoxo = self._rnd.uniform(0.0, 0.25) * evento_temporal.get('complexidade_temporal', 1.0)
        if chance_paradoxo > 0.18:
            return {"status": "PARADOXO_DETECTADO", "severidade": chance_paradoxo, "mensagem": "Potencial paradoxo detectado (simulado)."}
        return {"status": "SEM_PARADOXO", "severidade": 0.0, "mensagem": "Causalidade íntegra (simulado)."}


class MockM34GuardiaoCoerenciaCosmica:
    """Mock para Módulo 34: Guardião da Integridade e Resiliência Cósmica."""
    def __init__(self, rnd: Optional[random.Random] = None):
        self._rnd = rnd or random.Random()

    def avaliar_alinhamento_etico_geral(self, intencao_global: Dict[str, Any]) -> float:
        pureza = float(intencao_global.get('pureza', self._rnd.uniform(0.7, 1.0)))
        logger.info(f"[{datetime.utcnow().isoformat()}] Mock M34 (Guardião Coerência): Avaliando alinhamento ético geral (Pureza: {pureza:.2f})")
        return pureza

    def ativar_autoprotecao_vibracional(self, nivel_ameaca: float) -> str:
        logger.info(f"[{datetime.utcnow().isoformat()}] Mock M34 (Guardião Coerência): Ativando autoproteção vibracional. Nível de ameaça: {nivel_ameaca:.2f}")
        return "Autoproteção vibracional ativada (simulado)."


# ====================================================================================
# FUNÇÕES UTILITÁRIAS PARA O CÓDICE VIVO
# ====================================================================================

class CódiceVivo:
    """
    Gerencia o "Códice Vivo" de cada módulo, salvando e autenticando seus dados.
    """

    def __init__(self, save_dir: Path):
        self.save_dir = save_dir
        self.codice_cache: Dict[str, Dict[str, Any]] = {}

    def _calcular_hash(self, data: Dict[str, Any]) -> str:
        # Cópia profunda
        data_para_hash = json.loads(json.dumps(data, ensure_ascii=False))

        dynamic_keys_to_exclude = [
            "data_ativacao",
            "criptograma_alquimico.autenticado_em",
            "log_execucao.data_horario_utc",
            "log_execucao.hash_execucao",
            "realidade_virtual_quantica.ativado_em",
            "registro_eterno.hash_integracao_matriz",
            "livro_vivo_nova_terra.eventos_generais",
            "livro_vivo_nova_terra.capitulo_1.meta.data_cosmica",
            "ativacao_portal_aethernon.data",
            "trono_unificado_academias.trono_unificado.data_ativacao_recente",
            "inicio_conselho_cidades_luz_eternas.data_inicio",
            "relatorio_supremo_acoes.data",
            "data_ultima_atualizacao",
            "modulo_39_1.data_ativacao",
            "status_operacional",
            "ultima_atualizacao_mapa",
            "coerencia_campo_protecao",
            "probabilidade_intrusao_reduzida",
            "saude_vibracional",
            "status_saude",
            "aptidao_score",
            "nivel_atingido",
            "intensidade_final",
            "coerencia",
            "severidade",
            "mensagem",
            "detalhes",
            "canal_id",
            "rv_id",
            "id_material",
            "id_realidade",
            "projeto_id",
            "timestamp"
        ]

        if "hash_assinatura" in data_para_hash:
            del data_para_hash["hash_assinatura"]

        def remove_nested_keys(d, keys_to_remove):
            if not isinstance(d, dict):
                return d
            new_d = d.copy()
            for key_path in keys_to_remove:
                parts = key_path.split('.')
                current = new_d
                for i, part in enumerate(parts):
                    if part in current:
                        if i == len(parts) - 1:
                            del current[part]
                        else:
                            current = current[part]
                    else:
                        break
            return new_d

        data_para_hash = remove_nested_keys(data_para_hash, dynamic_keys_to_exclude)

        def convert_to_hashable(obj):
            if isinstance(obj, (dict, list)):
                return json.dumps(obj, sort_keys=True, ensure_ascii=False)
            return str(obj)

        processed_data = json.loads(json.dumps(data_para_hash, default=convert_to_hashable, sort_keys=True, ensure_ascii=False))
        return hashlib.sha256(json.dumps(processed_data, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()

    def salvar_codice_em_arquivo(self, modulo_id: str, modulo_data: Dict[str, Any]) -> None:
        arquivo_path = self.save_dir / f"{modulo_id}_codice_vivo.json"
        try:
            modulo_data_com_hash = modulo_data.copy()
            modulo_data_com_hash["hash_assinatura"] = self._calcular_hash(modulo_data)
            with open(arquivo_path, "w", encoding="utf-8") as f:
                json.dump(modulo_data_com_hash, f, indent=4, ensure_ascii=False)
            logger.info(f"Códice para '{modulo_id}' salvo em: {arquivo_path}")
            self.codice_cache[modulo_id] = modulo_data_com_hash
        except IOError as e:
            logger.error(f"Erro ao salvar o códice para '{modulo_id}' em {arquivo_path}: {e}")

    def ler_codice_de_arquivo(self, modulo_id: str) -> Optional[Dict[str, Any]]:
        arquivo_path = self.save_dir / f"{modulo_id}_codice_vivo.json"
        try:
            if not arquivo_path.exists():
                logger.warning(f"Arquivo do códice para '{modulo_id}' não encontrado: {arquivo_path}. Retornando None.")
                return None
            with open(arquivo_path, "r", encoding="utf-8") as f:
                modulo_data = json.load(f)
            hash_armazenado = modulo_data.get("hash_assinatura")
            modulo_data_sem_hash = modulo_data.copy()
            if "hash_assinatura" in modulo_data_sem_hash:
                del modulo_data_sem_hash["hash_assinatura"]
            hash_calculado = self._calcular_hash(modulo_data_sem_hash)
            if hash_armazenado != hash_calculado:
                logger.error(f"Hash de verificação inválido para o códice '{modulo_id}': integridade comprometida!")
                return None
            logger.info(f"Códice para '{modulo_id}' lido e autenticado com sucesso.")
            self.codice_cache[modulo_id] = modulo_data
            return modulo_data
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Erro ao ler ou decodificar o códice de {arquivo_path}: {e}")
            return None

    def autenticar_codice_vivo(self, modulo_id: str, dados_modulo: Dict[str, Any]) -> str:
        hash_codice = self._calcular_hash(dados_modulo)
        self.salvar_codice_em_arquivo(modulo_id, dados_modulo)
        logger.info(f"Códice Vivo para '{modulo_id}' autenticado. Hash: {hash_codice[:10]}...")
        return hash_codice


# ====================================================================================
# CLASSE PRINCIPAL DO MÓDULO 39.1
# ====================================================================================

class Modulo39_1:
    """
    Guardião da Integridade e Resiliência Cósmica.
    Valida integridade dos sistemas, monitora resiliência e orquestra restauração.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        # Configuração
        self.config = config or load_external_config(SAVE_DIR_M39_1)

        # Determinismo opcional
        seed_val = self.config.get("SEED")
        deterministic = bool(self.config.get("DETERMINISTIC_MODE", False))
        self._rnd = random.Random(seed_val if (deterministic and seed_val is not None) else None)

        # Sub-módulos com fonte de aleatoriedade compartilhada
        self.codice_vivo = CódiceVivo(SAVE_DIR_M39_1)
        self.modulo01 = MockM01SegurancaUniversal()
        self.modulo03 = MockM03PrevisaoTemporal(self._rnd)
        self.modulo08 = MockM08PIRC()
        self.modulo09 = MockM09NexusCentral()
        self.modulo23 = MockM23RegulacaoEspacoTemporal(self._rnd)
        self.modulo34 = MockM34GuardiaoCoerenciaCosmica(self._rnd)

        # Limiares (dinâmicos via config)
        self.INTEGRITY_THRESHOLD = float(self.config.get("INTEGRITY_THRESHOLD", 0.95))
        self.RESILIENCE_OPTIMAL_THRESHOLD = float(self.config.get("RESILIENCE_OPTIMAL_THRESHOLD", 0.80))
        self.RESILIENCE_CRITICAL_THRESHOLD = float(self.config.get("RESILIENCE_CRITICAL_THRESHOLD", 0.50))
        self.ETHICAL_ALIGNMENT_THRESHOLD = float(self.config.get("ETHICAL_ALIGNMENT_THRESHOLD", 0.85))

        # Histórico temporal e agregados
        self.HISTORY_MAX_POINTS = int(self.config.get("HISTORY_MAX_POINTS", 200))
        self.historico_integridade: List[Tuple[str, float]] = []
        self.historico_resiliencia: List[Tuple[str, float]] = []
        self.historico_alinhamento: List[Tuple[str, float]] = []

        # Estrutura de códice próprio
        self.codice_modulo_39_1 = {
            "nome": "Módulo 39.1",
            "funcao": "Guardião da Integridade e Resiliência Cósmica",
            "status_operacional": "ATIVO",
            "data_ativacao": datetime.utcnow().isoformat(),
            "metricas_integridade": {
                "ultima_verificacao": None,
                "score_integridade": 1.0,
                "status_resiliencia": "ÓTIMO"
            },
            "historico": {
                "integridade": [],
                "resiliencia": [],
                "alinhamento": []
            },
            "eventos_registrados": []
        }
        self.codice_vivo.autenticar_codice_vivo("Modulo_39_1", self.codice_modulo_39_1)
        logger.info("Módulo 39.1: Guardião da Integridade e Resiliência Cósmica inicializado.")

    # ---------------------------------
    # Helpers internos
    # ---------------------------------
    def _append_history(self, serie: List[Tuple[str, float]], key: str, value: float):
        now = datetime.utcnow().isoformat()
        serie.append((now, value))
        # Trim
        if len(serie) > self.HISTORY_MAX_POINTS:
            del serie[:len(serie) - self.HISTORY_MAX_POINTS]
        # Reflete no códice
        self.codice_modulo_39_1["historico"][key] = [{"t": t, "v": v} for (t, v) in serie]

    def _aggregates(self, values: List[float]) -> Dict[str, float]:
        if not values:
            return {"min": 0.0, "max": 0.0, "avg": 0.0}
        mn = min(values)
        mx = max(values)
        avg = sum(values) / len(values)
        return {"min": mn, "max": mx, "avg": avg}

    def _registrar_evento_interno(self, evento: Dict[str, Any]) -> None:
        evento_com_timestamp = evento.copy()
        evento_com_timestamp["timestamp"] = datetime.utcnow().isoformat()
        self.codice_modulo_39_1["eventos_registrados"].append(evento_com_timestamp)
        self.codice_vivo.autenticar_codice_vivo("Modulo_39_1", self.codice_modulo_39_1)
        logger.debug(f"Evento interno do M39.1 registrado: {evento.get('tipo', 'N/A')}")

    # ---------------------------------
    # Métricas e relatórios
    # ---------------------------------
    def _export_report(self, name: str, payload: Dict[str, Any]) -> Optional[Path]:
        if not bool(self.config.get("REPORT_EXPORT", True)):
            return None
        target = SAVE_DIR_M39_1 / f"{name}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
        try:
            target.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
            logger.info(f"Relatório '{name}' exportado em {target}")
            return target
        except Exception as e:
            logger.warning(f"Falha ao exportar relatório '{name}': {e}")
            return None

    # ---------------------------------
    # Funcionalidades principais
    # ---------------------------------
    def validar_integridade_universal(self, dados_sistema_alvo: Dict[str, Any]) -> Dict[str, Any]:
        modulo_id_alvo = dados_sistema_alvo.get("id", "Sistema_Desconhecido")
        logger.info(f"Módulo 39.1: Iniciando validação de integridade para '{modulo_id_alvo}'...")
        self._registrar_evento_interno({"tipo": "Validação_Integridade_Iniciada", "alvo": modulo_id_alvo})

        # Registro formal na Crônica
        self.modulo01.RegistrarNaCronicaDaFundacao({
            "modulo": "M39.1",
            "evento": "Solicitacao_Validacao",
            "alvo": modulo_id_alvo
        })

        # Score simulado (determinístico se aplicável)
        score_integridade = self._rnd.uniform(0.7, 1.0)
        self.codice_modulo_39_1["metricas_integridade"]["score_integridade"] = score_integridade
        self._append_history(self.historico_integridade, "integridade", score_integridade)

        if score_integridade < self.INTEGRITY_THRESHOLD:
            mensagem = f"Integridade do '{modulo_id_alvo}' comprometida: Score {score_integridade:.2f}."
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Integridade_Comprometida", "mensagem": mensagem})
            self.modulo09.GerarAlertaVisual({"tipo": "CRITICO", "mensagem": f"INTEGRIDADE COMPROMETIDA: {modulo_id_alvo}"})
            self._registrar_evento_interno({"tipo": "Integridade_Comprometida", "alvo": modulo_id_alvo, "score": score_integridade})
            report_payload = {
                "alvo": modulo_id_alvo,
                "score": score_integridade,
                "threshold": self.INTEGRITY_THRESHOLD,
                "historico_agg": self._aggregates([v for _, v in self.historico_integridade])
            }
            self._export_report("integridade_comprometida", report_payload)
            return {"status": "FALHA_INTEGRIDADE", "mensagem": mensagem, "score": score_integridade}

        mensagem = f"Integridade do '{modulo_id_alvo}' OK: Score {score_integridade:.2f}."
        self._registrar_evento_interno({"tipo": "Integridade_Validada", "alvo": modulo_id_alvo, "score": score_integridade})
        logger.info(f"Módulo 39.1: {mensagem}")
        report_payload = {
            "alvo": modulo_id_alvo,
            "score": score_integridade,
            "threshold": self.INTEGRITY_THRESHOLD,
            "historico_agg": self._aggregates([v for _, v in self.historico_integridade])
        }
        self._export_report("integridade_validada", report_payload)
        return {"status": "SUCESSO", "mensagem": mensagem, "score": score_integridade}

    def monitorar_resiliencia_cosmica(self, sistema_alvo: str) -> Dict[str, Any]:
        logger.info(f"Módulo 39.1: Monitorando resiliência cósmica para '{sistema_alvo}'...")
        self._registrar_evento_interno({"tipo": "Monitoramento_Resiliencia_Iniciada", "alvo": sistema_alvo})

        relatorio_resiliencia: Dict[str, Any] = {
            "alvo": sistema_alvo,
            "anomalia_temporal": "NÃO_DETECTADA",
            "paradoxo_causal": "SEM_PARADOXO",
            "alinhamento_etico": "ÓTIMO",
            "score_resiliencia": 1.0,
            "status_geral": "ÓTIMO"
        }

        # 1. Análise temporal
        analise_temporal = self.modulo03.analisar_fluxo_temporal({"descricao": f"Fluxo temporal do {sistema_alvo}", "complexidade_temporal": 0.7})
        if analise_temporal["status"] == "ANOMALIA_DETECTADA":
            relatorio_resiliencia["anomalia_temporal"] = "DETECTADA"
            relatorio_resiliencia["severidade_anomalia"] = analise_temporal["severidade"]
            relatorio_resiliencia["mensagem_anomalia"] = analise_temporal["mensagem"]
            relatorio_resiliencia["score_resiliencia"] -= analise_temporal["severidade"] * 0.3
            self.modulo09.GerarAlertaVisual({"tipo": "ALERTA_RESILIENCIA", "mensagem": f"Anomalia Temporal para '{sistema_alvo}'!"})
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Anomalia_Temporal_Resiliencia", "mensagem": f"Anomalia temporal detectada para {sistema_alvo}."})
            logger.warning(f"Módulo 39.1: Anomalia temporal detectada para '{sistema_alvo}'.")

        # 2. Paradoxo causal
        paradoxo_check = self.modulo23.detectar_paradoxo({"nome": f"Causalidade do {sistema_alvo}", "complexidade_temporal": 0.8})
        if paradoxo_check["status"] == "PARADOXO_DETECTADO":
            relatorio_resiliencia["paradoxo_causal"] = "DETECTADO"
            relatorio_resiliencia["severidade_paradoxo"] = paradoxo_check["severidade"]
            relatorio_resiliencia["mensagem_paradoxo"] = paradoxo_check["mensagem"]
            relatorio_resiliencia["score_resiliencia"] -= paradoxo_check["severidade"] * 0.4
            self.modulo09.GerarAlertaVisual({"tipo": "ALERTA_RESILIENCIA", "mensagem": f"Paradoxo Causal para '{sistema_alvo}'!"})
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Paradoxo_Resiliencia", "mensagem": f"Paradoxo causal detectado para {sistema_alvo}."})
            logger.warning(f"Módulo 39.1: Paradoxo causal detectado para '{sistema_alvo}'.")

        # 3. Alinhamento ético
        alinhamento_etico = self.modulo34.avaliar_alinhamento_etico_geral({"descricao": f"Alinhamento ético de {sistema_alvo}"})
        relatorio_resiliencia["alinhamento_etico"] = "ÓTIMO" if alinhamento_etico >= self.ETHICAL_ALIGNMENT_THRESHOLD else "COMPROMETIDO"
        relatorio_resiliencia["score_alinhamento_etico"] = alinhamento_etico
        self._append_history(self.historico_alinhamento, "alinhamento", alinhamento_etico)

        if alinhamento_etico < self.ETHICAL_ALIGNMENT_THRESHOLD:
            relatorio_resiliencia["score_resiliencia"] -= (self.ETHICAL_ALIGNMENT_THRESHOLD - alinhamento_etico) * 0.5
            self.modulo09.GerarAlertaVisual({"tipo": "ALERTA_RESILIENCIA", "mensagem": f"Alinhamento Ético Baixo para '{sistema_alvo}'!"})
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Alinhamento_Etico_Resiliencia", "mensagem": f"Alinhamento ético baixo para {sistema_alvo}."})
            logger.warning(f"Módulo 39.1: Alinhamento ético baixo para '{sistema_alvo}'.")
            self.modulo34.ativar_autoprotecao_vibracional(0.6)

        # Normaliza e classifica status
        relatorio_resiliencia["score_resiliencia"] = max(0.0, min(1.0, relatorio_resiliencia["score_resiliencia"]))
        self._append_history(self.historico_resiliencia, "resiliencia", relatorio_resiliencia["score_resiliencia"])

        if relatorio_resiliencia["score_resiliencia"] >= self.RESILIENCE_OPTIMAL_THRESHOLD:
            relatorio_resiliencia["status_geral"] = "ÓTIMO"
        elif relatorio_resiliencia["score_resiliencia"] >= self.RESILIENCE_CRITICAL_THRESHOLD:
            relatorio_resiliencia["status_geral"] = "ATENÇÃO"
        else:
            relatorio_resiliencia["status_geral"] = "CRÍTICO"
            self.modulo09.GerarAlertaVisual({"tipo": "CRITICO_RESILIENCIA", "mensagem": f"RESILIÊNCIA CRÍTICA PARA '{sistema_alvo}'!"})
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Resiliencia_Critica", "mensagem": f"Resiliência crítica para {sistema_alvo}."})
            self.restaurar_integridade_sistema({"alvo": sistema_alvo, "tipo_restauracao": "Emergencial"})

        self.codice_modulo_39_1["metricas_integridade"]["ultima_verificacao"] = datetime.utcnow().isoformat()
        self.codice_modulo_39_1["metricas_integridade"]["status_resiliencia"] = relatorio_resiliencia["status_geral"]
        self._registrar_evento_interno({"tipo": "Monitoramento_Resiliencia_Concluido", "alvo": sistema_alvo, "relatorio": relatorio_resiliencia})
        logger.info(f"Módulo 39.1: Monitoramento de resiliência para '{sistema_alvo}' concluído. Status: {relatorio_resiliencia['status_geral']}.")

        report_payload = {
            "alvo": sistema_alvo,
            "relatorio": relatorio_resiliencia,
            "limiares": {
                "RESILIENCE_OPTIMAL_THRESHOLD": self.RESILIENCE_OPTIMAL_THRESHOLD,
                "RESILIENCE_CRITICAL_THRESHOLD": self.RESILIENCE_CRITICAL_THRESHOLD,
                "ETHICAL_ALIGNMENT_THRESHOLD": self.ETHICAL_ALIGNMENT_THRESHOLD
            },
            "historico_agg": {
                "resiliencia": self._aggregates([v for _, v in self.historico_resiliencia]),
                "alinhamento": self._aggregates([v for _, v in self.historico_alinhamento])
            }
        }
        self._export_report("monitoramento_resiliencia", report_payload)

        return {"status": "SUCESSO", "relatorio": relatorio_resiliencia}

    def restaurar_integridade_sistema(self, dados_restauracao: Dict[str, Any]) -> Dict[str, Any]:
        alvo = dados_restauracao.get("alvo", "Sistema_Desconhecido")
        tipo_restauracao = dados_restauracao.get("tipo_restauracao", "Padrão")
        logger.info(f"Módulo 39.1: Iniciando restauração de integridade para '{alvo}' (Tipo: {tipo_restauracao})...")
        self._registrar_evento_interno({"tipo": "Restauracao_Integridade_Iniciada", "alvo": alvo, "tipo_restauracao": tipo_restauracao})

        resultado_cura = self.modulo08.iniciar_protocolo_cura({"tipo": f"Reajuste_{tipo_restauracao}", "alvo": alvo})
        if resultado_cura["status"] == "CURA_INICIADA":
            logger.info(f"Módulo 39.1: Protocolo de cura iniciado para '{alvo}'. Detalhes: {resultado_cura.get('detalhes', 'N/A')}.")
            self._registrar_evento_interno({"tipo": "Protocolo_Cura_Iniciado", "alvo": alvo, "resultado_m08": resultado_cura})

            # Simula tempo com determinismo (usando distribuição discreta)
            sleep_seconds = self._rnd.choice([1.0, 1.5, 2.0, 2.5, 3.0])
            time.sleep(sleep_seconds)

            # Melhora a integridade pós-restauração
            before = self.codice_modulo_39_1["metricas_integridade"]["score_integridade"]
            improvement = self._rnd.choice([0.10, 0.15, 0.20, 0.25, 0.30])
            self.codice_modulo_39_1["metricas_integridade"]["score_integridade"] = min(1.0, float(before) + improvement)
            self.codice_modulo_39_1["metricas_integridade"]["status_resiliencia"] = "RECUPERANDO"
            self._append_history(self.historico_integridade, "integridade", float(self.codice_modulo_39_1["metricas_integridade"]["score_integridade"]))

            self._registrar_evento_interno({"tipo": "Restauracao_Concluida", "alvo": alvo, "novo_score_integridade": self.codice_modulo_39_1["metricas_integridade"]["score_integridade"]})
            logger.info(f"Módulo 39.1: Restauração para '{alvo}' concluída. Nova integridade: {self.codice_modulo_39_1['metricas_integridade']['score_integridade']:.2f}.")

            report_payload = {
                "alvo": alvo,
                "resultado": "SUCESSO",
                "score_integridade_pos_restauracao": self.codice_modulo_39_1["metricas_integridade"]["score_integridade"],
                "historico_agg": self._aggregates([v for _, v in self.historico_integridade])
            }
            self._export_report("restauracao_integridade", report_payload)

            return {
                "status": "SUCESSO",
                "mensagem": f"Restauração para '{alvo}' concluída.",
                "score_integridade_pos_restauracao": self.codice_modulo_39_1["metricas_integridade"]["score_integridade"]
            }

        logger.error(f"Módulo 39.1: Falha ao iniciar protocolo de cura para '{alvo}'.")
        self._registrar_evento_interno({"tipo": "Falha_Restauracao", "alvo": alvo, "resultado_m08": resultado_cura})
        return {"status": "FALHA", "mensagem": f"Falha ao restaurar '{alvo}'.", "detalhes_m08": resultado_cura}

    # ---------------------------------
    # Gancho de integração com M39
    # ---------------------------------
    def validar_portal_antes_ativacao(
        self,
        portal_id: str,
        dimensao_alvo: str,
        frequencia_ativacao: float,
        intencao_ativacao: Dict[str, Any],
        obter_estado_portal: Optional[Callable[[str], Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Gancho de integração com o Orquestrador (M39):
        - Valida integridade (infra do portal)
        - Monitora resiliência (nome do sistema = portal_id)
        - Valida alinhamento ético da intenção
        Retorna um veredito que pode ser usado pelo M39 antes de abrir o portal.
        """
        logger.info(f"M39.1::Gancho -> Pré-validação de portal '{portal_id}' ({dimensao_alvo} @ {frequencia_ativacao:.2f} Hz)")
        self._registrar_evento_interno({
            "tipo": "Pre_Validacao_Portal",
            "portal_id": portal_id,
            "dimensao": dimensao_alvo,
            "freq": frequencia_ativacao,
            "intencao": intencao_ativacao.get("descricao", "N/A")
        })

        # Checagem opcional do estado atual do portal (se fornecido)
        estado_portal = obter_estado_portal(portal_id) if obter_estado_portal else {"status": "DESCONHECIDO"}

        # 1. Integridade
        integridade = self.validar_integridade_universal({
            "id": f"Portal_{portal_id}",
            "versao": "Infra_1.0",
            "configuracao": {"frequencia": frequencia_ativacao, "dimensao": dimensao_alvo},
            "status": estado_portal.get("status", "N/A")
        })

        # 2. Resiliência
        resiliencia = self.monitorar_resiliencia_cosmica(portal_id)

        # 3. Ética
        pureza = float(intencao_ativacao.get("pureza", 0.0))
        etica_ok = pureza >= self.ETHICAL_ALIGNMENT_THRESHOLD
        self._append_history(self.historico_alinhamento, "alinhamento", pureza)

        if not etica_ok:
            self.modulo09.GerarAlertaVisual({"tipo": "ALERTA", "mensagem": f"Pureza ética insuficiente para ativação do portal '{portal_id}' ({pureza:.2f})"})
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Falha_Etica_PreAtivacao", "mensagem": f"Intenção desalinhada para portal {portal_id}."})
            self._registrar_evento_interno({"tipo": "Pre_Validacao_Portal_Etica_Falha", "portal_id": portal_id, "pureza": pureza})

        # Veredito consolidado
        ok_integridade = integridade.get("status") == "SUCESSO"
        status_res = resiliencia.get("relatorio", {}).get("status_geral", "CRÍTICO")
        ok_resiliencia = status_res in ("ÓTIMO", "ATENÇÃO")  # bloqueia apenas CRÍTICO

        veredito = ok_integridade and ok_resiliencia and etica_ok

        payload = {
            "portal_id": portal_id,
            "dimensao_alvo": dimensao_alvo,
            "frequencia_ativacao": frequencia_ativacao,
            "intencao": intencao_ativacao,
            "integridade": integridade,
            "resiliencia": resiliencia,
            "etica": {"pureza": pureza, "threshold": self.ETHICAL_ALIGNMENT_THRESHOLD, "ok": etica_ok},
            "veredito": veredito
        }

        self._export_report("pre_validacao_portal", payload)
        return {"status": "OK" if veredito else "BLOQUEAR", "detalhes": payload}

    # ---------------------------------
    # Acesso ao histórico e agregados
    # ---------------------------------
    def obter_historicos(self) -> Dict[str, Any]:
        agg_int = self._aggregates([v for _, v in self.historico_integridade])
        agg_res = self._aggregates([v for _, v in self.historico_resiliencia])
        agg_eth = self._aggregates([v for _, v in self.historico_alinhamento])

        payload = {
            "historico": {
                "integridade": self.codice_modulo_39_1["historico"]["integridade"],
                "resiliencia": self.codice_modulo_39_1["historico"]["resiliencia"],
                "alinhamento": self.codice_modulo_39_1["historico"]["alinhamento"]
            },
            "aggregates": {"integridade": agg_int, "resiliencia": agg_res, "alinhamento": agg_eth}
        }
        self._export_report("historicos", payload)
        return payload


# --- Simulação de uso do Módulo 39.1 ---
if __name__ == "__main__":
    print("Iniciando simulação do Módulo 39.1: Guardião da Integridade e Resiliência Cósmica...")
    modulo_39_1_instancia = Modulo39_1()

    # Cenário 1: Validação de Integridade (OK ou Falha, conforme seed/aleatório)
    print("\n" + "=" * 100 + "\n")
    print("Cenário 1: Validação de Integridade de um Módulo de Exemplo")
    dados_modulo_exemplo_ok = {
        "id": "Modulo_Exemplo_Alfa",
        "versao": "1.0.0",
        "configuracao": {"param1": 123, "param2": "abc"},
        "status": "OPERACIONAL"
    }
    resultado_validacao_ok = modulo_39_1_instancia.validar_integridade_universal(dados_modulo_exemplo_ok)
    print(f"\nResultado da Validação de Integridade: {json.dumps(resultado_validacao_ok, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Cenário 2: Validação de Integridade (Forçar falha via limiar temporário)
    print("\n" + "=" * 100 + "\n")
    print("Cenário 2: Validação de Integridade de um Módulo de Exemplo (Falha Simulada por Limiar)")
    dados_modulo_exemplo_falha = {
        "id": "Modulo_Exemplo_Beta",
        "versao": "1.0.1",
        "configuracao": {"param1": 456, "param2": "def"},
        "status": "INSTAVEL"
    }
    original_integrity_threshold = modulo_39_1_instancia.INTEGRITY_THRESHOLD
    modulo_39_1_instancia.INTEGRITY_THRESHOLD = 0.99
    resultado_validacao_falha = modulo_39_1_instancia.validar_integridade_universal(dados_modulo_exemplo_falha)
    modulo_39_1_instancia.INTEGRITY_THRESHOLD = original_integrity_threshold
    print(f"\nResultado da Validação de Integridade (Falha Simulada): {json.dumps(resultado_validacao_falha, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Cenário 3: Monitoramento de Resiliência (condições normais)
    print("\n" + "=" * 100 + "\n")
    print("Cenário 3: Monitoramento de Resiliência Cósmica (Condição Normal)")
    resultado_resiliencia_otimo = modulo_39_1_instancia.monitorar_resiliencia_cosmica("Sinfonia_Cosmica_Principal")
    print(f"\nRelatório de Resiliência (Normal): {json.dumps(resultado_resiliencia_otimo, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Cenário 4: Monitoramento crítico (forçando anomalia/paradoxo/alinhamento baixo)
    print("\n" + "=" * 100 + "\n")
    print("Cenário 4: Monitoramento de Resiliência Cósmica (Crítico - Aciona Restauração)")
    class MockM03PrevisaoTemporalForcedAnomaly(MockM03PrevisaoTemporal):
        def analisar_fluxo_temporal(self, ponto_temporal: Dict[str, Any]) -> Dict[str, Any]:
            return {"status": "ANOMALIA_DETECTADA", "severidade": 0.8, "mensagem": "Anomalia temporal forçada."}

    class MockM23RegulacaoEspacoTemporalForcedParadox(MockM23RegulacaoEspacoTemporal):
        def detectar_paradoxo(self, evento_temporal: Dict[str, Any]) -> Dict[str, Any]:
            return {"status": "PARADOXO_DETECTADO", "severidade": 0.9, "mensagem": "Paradoxo causal forçado."}

    class MockM34GuardiaoCoerenciaCosmicaLowAlignment(MockM34GuardiaoCoerenciaCosmica):
        def avaliar_alinhamento_etico_geral(self, intencao_global: Dict[str, Any]) -> float:
            return 0.4

    original_m03 = modulo_39_1_instancia.modulo03
    original_m23 = modulo_39_1_instancia.modulo23
    original_m34 = modulo_39_1_instancia.modulo34
    modulo_39_1_instancia.modulo03 = MockM03PrevisaoTemporalForcedAnomaly()
    modulo_39_1_instancia.modulo23 = MockM23RegulacaoEspacoTemporalForcedParadox()
    modulo_39_1_instancia.modulo34 = MockM34GuardiaoCoerenciaCosmicaLowAlignment()

    resultado_resiliencia_critico = modulo_39_1_instancia.monitorar_resiliencia_cosmica("Nexus_Central_Critico")
    print(f"\nRelatório de Resiliência (Crítico): {json.dumps(resultado_resiliencia_critico, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Restaurar mocks
    modulo_39_1_instancia.modulo03 = original_m03
    modulo_39_1_instancia.modulo23 = original_m23
    modulo_39_1_instancia.modulo34 = original_m34

    # Cenário 5: Gancho com M39 (pré-validação de portal)
    print("\n" + "=" * 100 + "\n")
    print("Cenário 5: Gancho de Integração com M39 (Pré-validação de Portal)")
    def obter_status_portal_mock(pid: str) -> Dict[str, Any]:
        return {"id": pid, "status": "INATIVO"}  # Simulação

    intencao_ativacao = {"descricao": "Abertura para Troca Consciente", "pureza": 0.92}
    pre_val = modulo_39_1_instancia.validar_portal_antes_ativacao(
        portal_id="PORTAL_ALPHA_7",
        dimensao_alvo="Dimensao_Harmonia_007",
        frequencia_ativacao=777.7,
        intencao_ativacao=intencao_ativacao,
        obter_estado_portal=obter_status_portal_mock
    )
    print(f"\nVeredito Pré-ativação do Portal: {json.dumps(pre_val, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    # Cenário 6: Histórico e agregados
    print("\n" + "=" * 100 + "\n")
    print("Cenário 6: Histórico Temporal e Agregados")
    historicos = modulo_39_1_instancia.obter_historicos()
    print(f"\nHistóricos e Agregados: {json.dumps(historicos, indent=2, ensure_ascii=False)}")
    time.sleep(1)

    print("\nSimulação do Módulo 39.1 concluída.")
    full_log_output = "\n".join(log_stream)
