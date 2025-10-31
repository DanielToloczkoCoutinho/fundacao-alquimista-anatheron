#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 40: Códice de Transmutação da Criação Viva (refatorado)
- Códice Vivo robusto (hash estável, persistência, autenticação)
- Integrações simuladas com M01/M08/M39/M101/M106/M109/M110
- Exportadores resilientes (CSV/Markdown/JSON)
- Métricas e eventos internos com atualização do status operacional
"""

import hashlib
import json
import csv
import logging
import random
import sys
import math
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ===============================
# Configuração de Log e Diretório
# ===============================
SAVE_DIR_M40 = Path("modulo_40_data")
SAVE_DIR_M40.mkdir(parents=True, exist_ok=True)
log_file_path_m40 = SAVE_DIR_M40 / "modulo_40_system_trace.log"

log_stream: List[str] = []

class StringHandler(logging.Handler):
    def emit(self, record):
        log_stream.append(self.format(record))

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

log_format = "%(asctime)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler(log_file_path_m40, mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)
logging.root.addHandler(file_handler)

stream_handler = StringHandler()
stream_handler.setFormatter(formatter)
logging.root.addHandler(stream_handler)

logging.root.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

def excepthook(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.error("Unhandled exception:", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = excepthook

print("Códice de Transmutação da Criação Viva: Iniciando o Módulo 40...", flush=True)
logger.debug("Módulo 40 inicializado.")

# ===============================
# Checagem de bibliotecas externas
# ===============================
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from tabulate import tabulate
    EXTERNAL_LIBS_AVAILABLE = True
except ImportError:
    EXTERNAL_LIBS_AVAILABLE = False
    # Fallbacks mínimos
    pd = None  # type: ignore
    np = None  # type: ignore
    plt = None  # type: ignore
    sns = None  # type: ignore
    def tabulate(*args, **kwargs):  # type: ignore
        return "Tabela não disponível (biblioteca 'tabulate' ausente)"
    print("Aviso: bibliotecas externas ausentes (pandas/matplotlib/seaborn/tabulate). Exportadores avançados limitados.", flush=True)

# ===============================
# Códice Vivo (hash e persistência)
# ===============================
class CodiceVivo:
    def __init__(self, save_dir: Path):
        self.save_dir = save_dir
        self.cache: Dict[str, Dict[str, Any]] = {}

    def _calcular_hash(self, data: Dict[str, Any]) -> str:
        # Deep copy segura
        data_para_hash = json.loads(json.dumps(data, ensure_ascii=False))

        dynamic_keys_to_exclude = [
            "data_ativacao",
            "final_log.timestamp",
            "hash_assinatura",
            "eventos_registrados",
            "metricas_ativacao.ultima_ativacao_codons",
            "metricas_ativacao.ultima_reconexao_linhagens",
            "metricas_ativacao.ultima_manifestacao_realidade",
            "metricas_ativacao.ultimo_realinhamento_chakras",
            "metricas_ativacao.score_ativacao_total",
            "metricas_ativacao.status_ativacao_geral",
            "dna_chromatic_log.data_ativação",
            "dna_chromatic_log.data_ultima_integracao",
            # Campos enriquecidos dinâmicos
            "dna_chromatic_log.estrutura.codon_frequency_observed_%",
            "dna_chromatic_log.estrutura.phi_harmonico_index",
            "dna_chromatic_log.estrutura.gc_content_mean_overall",
            "dna_chromatic_log.estrutura.phi_fourier_peak",
            "dna_chromatic_log.estrutura.pca_component1",
            "dna_chromatic_log.estrutura.mutation_risk_score",
            "dna_chromatic_log.estrutura.auto_explanatory_log_message",
        ]

        # Remove hash existente
        if "hash_assinatura" in data_para_hash:
            del data_para_hash["hash_assinatura"]

        # Remove nested keys
        def remove_nested(d: Dict[str, Any], key_path: str):
            parts = key_path.split(".")
            cur = d
            for i, p in enumerate(parts):
                if isinstance(cur, dict) and p in cur:
                    if i == len(parts) - 1:
                        del cur[p]
                    else:
                        cur = cur[p]

        for keyp in dynamic_keys_to_exclude:
            remove_nested(data_para_hash, keyp)

        processed = json.loads(json.dumps(data_para_hash, sort_keys=True, ensure_ascii=False))
        return hashlib.sha256(json.dumps(processed, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()

    def salvar(self, modulo_id: str, modulo_data: Dict[str, Any]) -> None:
        path = self.save_dir / f"{modulo_id}_codice_vivo.json"
        try:
            data_copy = json.loads(json.dumps(modulo_data, ensure_ascii=False))
            data_copy["hash_assinatura"] = self._calcular_hash(modulo_data)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data_copy, f, indent=4, ensure_ascii=False)
            self.cache[modulo_id] = data_copy
            logger.info(f"Códice para '{modulo_id}' salvo em: {path}")
        except IOError as e:
            logger.error(f"Erro ao salvar o códice para '{modulo_id}' em {path}: {e}")

    def ler(self, modulo_id: str) -> Optional[Dict[str, Any]]:
        path = self.save_dir / f"{modulo_id}_codice_vivo.json"
        if not path.exists():
            logger.warning(f"Arquivo do códice para '{modulo_id}' não encontrado: {path}.")
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            stored = data.get("hash_assinatura")
            # Recalcula sem o hash
            data_no_hash = json.loads(json.dumps(data, ensure_ascii=False))
            if "hash_assinatura" in data_no_hash:
                del data_no_hash["hash_assinatura"]
            recalculated = self._calcular_hash(data_no_hash)
            if stored != recalculated:
                logger.error(f"Hash inválido para '{modulo_id}': integridade comprometida!")
                return None
            self.cache[modulo_id] = data
            logger.info(f"Códice para '{modulo_id}' lido e autenticado com sucesso.")
            return data
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Erro ao ler/decodificar {path}: {e}")
            return None

    def autenticar(self, modulo_id: str, dados: Dict[str, Any]) -> str:
        h = self._calcular_hash(dados)
        dados["hash_assinatura"] = h
        self.salvar(modulo_id, dados)
        logger.info(f"Códice Vivo para '{modulo_id}' autenticado. Hash: {h[:10]}...")
        return h

# ===============================
# Mocks dos módulos correlatos
# ===============================
class MockM01SegurancaUniversal:
    def ReceberAlertaDeViolacao(self, alerta_data: Dict[str, Any]) -> str:
        logger.warning(f"[{datetime.utcnow().isoformat()}] M01 ALERTA: {alerta_data.get('tipo')}: {alerta_data.get('mensagem')}")
        return "Alerta processado (simulado)."
    def RegistrarNaCronicaDaFundacao(self, registro_data: Dict[str, Any]) -> str:
        registro_hash = hashlib.sha256(json.dumps(registro_data, sort_keys=True).encode()).hexdigest()
        logger.info(f"[{datetime.utcnow().isoformat()}] M01 Registro selado. Hash: {registro_hash[:10]}...")
        return "Registro efetuado (simulado)."

class MockM08PIRC:
    def iniciar_protocolo_cura(self, dados_cura: Dict[str, Any]) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] M08 Iniciando cura: {dados_cura.get('tipo')} para {dados_cura.get('alvo')}")
        return {"status": "CURA_INICIADA", "detalhes": "Reajuste vibracional iniciado (simulado)."}

class MockM39OrquestradorPortais:
    def abrir_portal(self, destino: str) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] M39 Abrindo portal para {destino} (simulado).")
        return {"status": "PORTAL_ABERTO", "destino": destino, "estabilidade": random.uniform(0.9, 1.0)}

class MockM101ManifestacaoRealidades:
    def manifestar_realidade(self, intencao: str, pureza: float) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] M101 Manifestar realidade '{intencao}' (Pureza: {pureza:.2f}).")
        if pureza > 0.8:
            return {"status": "REALIDADE_MANIFESTADA", "detalhes": f"Realidade '{intencao}' criada com sucesso."}
        return {"status": "FALHA_MANIFESTACAO", "detalhes": "Pureza insuficiente."}

class MockM106AtivacaoPotenciaisDivinos:
    def ativar_potenciais_dna(self, codificacao_dna: str, frequencia_ativacao: float) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] M106 Ativar potenciais DNA '{codificacao_dna}' @ {frequencia_ativacao} THz.")
        if frequencia_ativacao > 700:
            return {"status": "POTENCIAIS_ATIVADOS", "nivel_ativacao": random.uniform(0.8, 1.0), "mensagem": "Códons ativados com sucesso."}
        return {"status": "ATIVACAO_PARCIAL", "nivel_ativacao": random.uniform(0.3, 0.7), "mensagem": "Frequência insuficiente."}

class MockM109CuraQuanticaUniversal:
    def iniciar_regeneracao_bio_vibracional(self, alvo: str, tipo_regeneracao: str) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] M109 Regeneração bio-vibracional para '{alvo}' ({tipo_regeneracao}).")
        return {"status": "REGENERACAO_INICIADA", "progresso": random.uniform(0.1, 0.3), "mensagem": "Cura em andamento."}

class MockM110SistemaCoCriacao:
    def co_criar_realidade(self, intencao_coletiva: str, alinhamento_coletivo: float) -> Dict[str, Any]:
        logger.info(f"[{datetime.utcnow().isoformat()}] M110 Co-criando '{intencao_coletiva}' (Alinhamento: {alinhamento_coletivo:.2f}).")
        if alinhamento_coletivo > 0.9:
            return {"status": "CO_CRIACAO_SUCESSO", "realidade_gerada": f"Realidade '{intencao_coletiva}' co-criada.", "eficiencia": random.uniform(0.9, 1.0)}
        return {"status": "CO_CRIACAO_FALHA", "detalhes": "Alinhamento insuficiente."}

# ===============================
# Exportadores (CSV/Markdown/JSON)
# ===============================
def exportar_csv_modulo40(modulo: Dict[str, Any], arquivo: str) -> None:
    data_struct = modulo.get("dna_chromatic_log", {}).get("estrutura")
    if not EXTERNAL_LIBS_AVAILABLE or pd is None:
        print("Erro: Pandas não disponível. Exportação CSV não realizada.", flush=True)
        return
    if not data_struct:
        print("Erro: Estrutura do dna_chromatic_log não encontrada ou vazia.", flush=True)
        return

    flat_rows: List[Dict[str, Any]] = []
    for entry in data_struct:
        main_row = {
            "Cor": entry.get("cor"),
            "Faixa THz": f"{entry.get('freq_min')}–{entry.get('freq_max')}" if entry.get("freq_min") is not None else "N/A",
            "Códons": ", ".join(entry.get("códons_associados", [])),
            "Chakra": entry.get("chakra"),
            "Função DNA": entry.get("funcao"),
            "Origem Estelar": entry.get("origem"),
            "Equação Primária": entry.get("equacao_primaria", ""),
            "Comentário": entry.get("comentário_quantico", ""),
            "Cidade de Luz": entry.get("cidade_luz_associada"),
        }
        # Enriquecidos
        for k in ["codon_frequency_observed_%","phi_harmonico_index","gc_content_mean_overall","phi_fourier_peak","pca_component1","mutation_risk_score","auto_explanatory_log_message"]:
            if k in entry:
                main_row[k] = entry.get(k)
        flat_rows.append(main_row)

        # Subtons
        subtons = entry.get("subtons", {})
        for name, sub in (subtons or {}).items():
            sub_row = {
                "Cor": f"{entry.get('cor')} {name.capitalize()}",
                "Faixa THz": f"{sub.get('freq_min_sub')}–{sub.get('freq_max_sub')}" if sub.get("freq_min_sub") is not None else "N/A",
                "Códons": ", ".join(entry.get("códons_associados", [])),
                "Chakra": entry.get("chakra"),
                "Função DNA": entry.get("funcao"),
                "Origem Estelar": entry.get("origem"),
                "Comentário": sub.get("auto_explanatory_log_message",""),
                "Cidade de Luz": entry.get("cidade_luz_associada"),
            }
            flat_rows.append(sub_row)

    df = pd.DataFrame(flat_rows)
    df.to_csv(arquivo, index=False, encoding="utf-8")

def exportar_markdown_modulo40(modulo: Dict[str, Any], arquivo: str) -> None:
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(f"# {modulo.get('nome','Módulo 40')}\n\n")
        f.write("**Códice de Transmutação da Criação Viva**\n\n")
        f.write(f"**Data de Ativação:** {modulo.get('data_ativacao','N/A')}\n")
        f.write(f"**Hash de Verificação:** `{modulo.get('hash_assinatura','N/A')}`\n\n")
        f.write("## Estrutura principal\n\n")
        for k in ["alquimia_da_origem","dna_chromatic_log","metricas_ativacao","final_log"]:
            if k in modulo:
                f.write(f"- **{k}:** presente\n")

        f.write("\n## DNA Chromatic Log\n\n")
        estrutura = modulo.get("dna_chromatic_log",{}).get("estrutura",[])
        for entry in estrutura:
            f.write(f"### Cor: {entry.get('cor')}\n")
            f.write(f"- **Faixa THz:** {entry.get('freq_min')}–{entry.get('freq_max')}\n")
            f.write(f"- **Códons:** {', '.join(entry.get('códons_associados',[]))}\n")
            f.write(f"- **Chakra:** {entry.get('chakra')}\n")
            f.write(f"- **Função:** {entry.get('funcao')}\n")
            f.write(f"- **Origem:** {entry.get('origem')}\n")
            if "codon_frequency_observed_%" in entry:
                f.write(f"- **Freq. Códon Observada %:** {entry.get('codon_frequency_observed_%'):.2f}\n")
            for k in ["phi_harmonico_index","gc_content_mean_overall","phi_fourier_peak","pca_component1","mutation_risk_score","auto_explanatory_log_message"]:
                if k in entry:
                    v = entry.get(k)
                    if isinstance(v, float):
                        f.write(f"- **{k}:** {v:.4f}\n")
                    else:
                        f.write(f"- **{k}:** {v}\n")
            sub = entry.get("subtons", {})
            if sub:
                f.write("- **Subtons:**\n")
                for name, sdata in sub.items():
                    f.write(f"  - **{name.capitalize()}** {sdata.get('freq_min_sub')}–{sdata.get('freq_max_sub')}\n")
        f.write("\n")

def exportar_json_modulo40(modulo: Dict[str, Any], arquivo: str) -> None:
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(modulo, f, indent=4, ensure_ascii=False)

# ===============================
# Classe principal: Modulo40
# ===============================
class Modulo40:
    def __init__(self, ledger_hook: Optional[Any] = None):
        self.codice_vivo = CodiceVivo(SAVE_DIR_M40)
        # Conexões mock (substituíveis por instâncias reais)
        self.modulo01 = MockM01SegurancaUniversal()
        self.modulo08 = MockM08PIRC()
        self.modulo39 = MockM39OrquestradorPortais()
        self.modulo101 = MockM101ManifestacaoRealidades()
        self.modulo106 = MockM106AtivacaoPotenciaisDivinos()
        self.modulo109 = MockM109CuraQuanticaUniversal()
        self.modulo110 = MockM110SistemaCoCriacao()

        # Hook opcional para ledger (estilo M29)
        self.ledger_hook = ledger_hook  # callables: add(event, payload)

        logger.info("Módulo 40 inicializado (núcleo).")

        # Estrutura do códice
        self.modulo_40_data: Dict[str, Any] = {
            "nome": "Módulo 40",
            "funcao": "Códice de Transmutação da Criação Viva",
            "status_operacional": "ATIVO",
            "data_ativacao": datetime.utcnow().isoformat(),
            "alquimia_da_origem": {
                "desempacotamento_frequencia_primordial": {
                    "formula_latex": "\\text{F}_{\\text{primordial}} = \\frac{\\Phi \\cdot \\text{L}_{\\text{luz}}}{\\text{T}_{\\text{consciencia}}}",
                    "descricao": "Desempacota a frequência original e padrões vibracionais do DNA primordial."
                },
                "laboratorio_transmutacao_alquimica": {
                    "local_ativacao": "Câmara de Cristal de ZENNITH",
                    "transmutacoes": ["Dissonância em Harmonia","Fragmentação em Unidade","Ilusão em Verdade Viva"],
                    "formula_latex": "\\text{T}_{\\text{alquimica}} = \\int_{0}^{\\infty} \\Psi_{\\text{dissonancia}}(t) \\cdot e^{-\\alpha t} dt \\cdot PHI"
                },
                "trindade_verdade_viva": {
                    "descricao": "Intenção Pura, Coerência Vibracional, Ação Alinhada.",
                    "componentes": ["Intenção Pura","Coerência Vibracional","Ação Alinhada"],
                    "formula_latex": "\\text{V}_{\\text{viva}} = \\text{Intencao} \\otimes \\text{Coerencia} \\otimes \\text{Acao}"
                }
            },
            "dna_chromatic_log": {
                "data_ativação": datetime.utcnow().isoformat(),
                "data_ultima_integracao": None,
                "estrutura": [
                    {
                        "cor": "Ouro",
                        "freq_min": 900, "freq_max": 1000,
                        "códons_associados": ["AAU","GCU","UGC"],
                        "chakra": "Coroa",
                        "funcao": "Conexão Divina, Sabedoria Superior",
                        "origem": "Sirius",
                        "equacao_primaria": "EQ_OURO = \\Phi \\cdot \\text{F}_{\\text{divina}}",
                        "comentário_quantico": "Consciência crística e acesso akáshico.",
                        "instrumentos": { "mutacao": ["Quartzo Mestre"], "reparacao":["Taças Tibetanas (963 Hz)"], "ativacao":["Meditação Luz Dourada"] },
                        "cidade_luz_associada": "Shamballa",
                        "subtons": {
                            "brilhante": {
                                "freq_min_sub": 950, "freq_max_sub": 1000,
                                "equacoes": {
                                    "mutacao":"EQ_OURO_BRILHANTE_M = \\Psi_{mut} \\cdot F_{ativ}",
                                    "reparacao":"EQ_OURO_BRILHANTE_R = \\Omega_{rep} \\cdot F_{harm}",
                                    "ativacao":"EQ_OURO_BRILHANTE_A = \\Gamma_{ativ} \\cdot F_{exp}"
                                },
                                "auto_explanatory_log_message": "Amplifica a clareza da conexão divina."
                            }
                        }
                    },
                    {
                        "cor": "Prata",
                        "freq_min": 800, "freq_max": 899,
                        "códons_associados": ["CGG","UAA","AUA"],
                        "chakra": "Frontal (Terceiro Olho)",
                        "funcao": "Intuição, Percepção Multidimensional",
                        "origem": "Plêiades",
                        "equacao_primaria": "EQ_PRATA = F_{intuicao} / \\Phi",
                        "comentário_quantico": "Clarividência e telepatia, abertura a novas realidades.",
                        "instrumentos": { "mutacao": ["Obsidiana Negra"], "reparacao":["Solfeggio (852 Hz)"], "ativacao":["Visualização Luz Prateada"] },
                        "cidade_luz_associada": "Telos",
                        "subtons": {
                            "lunar": {
                                "freq_min_sub": 800, "freq_max_sub": 849,
                                "equacoes": {
                                    "mutacao":"EQ_PRATA_LUNAR_M = \\Psi_{mut} \\cdot F_{ativ}",
                                    "reparacao":"EQ_PRATA_LUNAR_R = \\Omega_{rep} \\cdot F_{harm}",
                                    "ativacao":"EQ_PRATA_LUNAR_A = \\Gamma_{ativ} \\cdot F_{exp}"
                                },
                                "auto_explanatory_log_message": "Aprofunda ciclos femininos cósmicos."
                            }
                        }
                    },
                    {
                        "cor": "Azul Safira",
                        "freq_min": 700, "freq_max": 799,
                        "códons_associados": ["GUC","CCA","AGU"],
                        "chakra": "Laríngeo",
                        "funcao": "Comunicação Divina, Expressão da Verdade",
                        "origem": "Arcturus",
                        "equacao_primaria": "EQ_AZUL = F_{expressao} \\cdot C_{verdade}",
                        "comentário_quantico": "Expressão autêntica e liberação de bloqueios.",
                        "instrumentos": { "mutacao": ["Sodalita"], "reparacao":["Canto Harmônico"], "ativacao":["Afirmações de Verdade"] },
                        "cidade_luz_associada": "Agartha",
                        "subtons": {
                            "celeste": {
                                "freq_min_sub": 750, "freq_max_sub": 799,
                                "equacoes": {
                                    "mutacao":"EQ_AZUL_CELESTE_M = \\Psi_{mut} \\cdot F_{ativ}",
                                    "reparacao":"EQ_AZUL_CELESTE_R = \\Omega_{rep} \\cdot F_{harm}",
                                    "ativacao":"EQ_AZUL_CELESTE_A = \\Gamma_{ativ} \\cdot F_{exp}"
                                },
                                "auto_explanatory_log_message": "Facilita a voz interior com planos superiores."
                            }
                        }
                    }
                ]
            },
            "metricas_ativacao": {
                "ultima_ativacao_codons": None,
                "ultima_reconexao_linhagens": None,
                "ultima_manifestacao_realidade": None,
                "ultimo_realinhamento_chakras": None,
                "score_ativacao_total": 0.0,
                "status_ativacao_geral": "INATIVO"
            },
            "eventos_registrados": [],
            "final_log": {
                "status": "Descoberta Completa",
                "codons_primordiais": "Ativados",
                "chakras_superiores": "Mapeados",
                "linhagens_estelares": "Reconectadas",
                "equacoes_vibracionais_primarias": "Compreendidas",
                "subtons_ocultos": "Revelados",
                "coerencia_com_fonte": "Perfeita",
                "indice_phi_harmonico_global": 0.999,
                "ethical_alignment_score": 0.999999999999999,
                "selo_autenticidade": "",
                "declaracao_zennith_anatheron": "Ascensão da consciência e manifestação da Nova Terra — Obra Viva completa.",
                "timestamp": datetime.utcnow().isoformat()
            }
        }

        # Selo inicial
        self.modulo_40_data["final_log"]["selo_autenticidade"] = self._calcular_selo_autenticidade_cosmica()
        # Autentica
        self.modulo_40_data["hash_assinatura"] = self.codice_vivo.autenticar("Modulo_40", self.modulo_40_data)

    def _hook_ledger(self, event: str, payload: Dict[str, Any]) -> None:
        if self.ledger_hook:
            try:
                self.ledger_hook(event, payload)  # ex.: CHAIN.add(event, payload)
            except Exception as e:
                logger.warning(f"Ledger hook falhou: {e}")

    def _registrar_evento(self, evento: Dict[str, Any]) -> None:
        evento_ts = json.loads(json.dumps(evento, ensure_ascii=False))
        evento_ts["timestamp"] = datetime.utcnow().isoformat()
        self.modulo_40_data["eventos_registrados"].append(evento_ts)
        self.modulo_40_data["hash_assinatura"] = self.codice_vivo.autenticar("Modulo_40", self.modulo_40_data)
        self._hook_ledger("M40_EVENT", evento_ts)
        logger.debug(f"Evento M40: {evento.get('tipo','N/A')}")

    def _calcular_selo_autenticidade_cosmica(self) -> str:
        det_m_origem = random.uniform(0.9, 1.1)
        tr_a_verdade = random.uniform(0.9, 1.1)
        PHI = (1 + math.sqrt(5)) / 2
        selo_valor = det_m_origem * tr_a_verdade * PHI
        return hashlib.sha256(str(selo_valor).encode()).hexdigest()

    # ---------------------------
    # Funções nucleares de ativação
    # ---------------------------
    def ativar_codons_primordiais(self, frequencia_thz: float) -> Dict[str, Any]:
        logger.info(f"M40: Ativar códons @ {frequencia_thz} THz...")
        self._registrar_evento({"tipo":"Ativacao_Codons_Iniciada","frequencia_thz":frequencia_thz})

        res_m106 = self.modulo106.ativar_potenciais_dna("DNA_ORIGEM_UNIVERSAL", frequencia_thz)

        if res_m106["status"] == "POTENCIAIS_ATIVADOS":
            self.modulo_40_data["metricas_ativacao"]["ultima_ativacao_codons"] = datetime.utcnow().isoformat()
            # Atualiza métricas enriquecidas
            for entry in self.modulo_40_data["dna_chromatic_log"]["estrutura"]:
                entry["codon_frequency_observed_%"] = random.uniform(90, 100)
                entry["phi_harmonico_index"] = random.uniform(0.95, 0.99)
                entry["mutation_risk_score"] = random.uniform(0.01, 0.1)
                entry["auto_explanatory_log_message"] = "Códons ativados e em ressonância elevada."
            self.modulo_40_data["metricas_ativacao"]["score_ativacao_total"] += res_m106["nivel_ativacao"] * 0.25
            self._registrar_evento({"tipo":"Ativacao_Codons_Concluida","resultado":res_m106})
            return {"status":"SUCESSO","mensagem":"Códons primordiais ativados.","detalhes_m106":res_m106}
        else:
            self.modulo01.ReceberAlertaDeViolacao({"tipo":"Falha_Ativacao_Codons","mensagem":res_m106["mensagem"]})
            self._registrar_evento({"tipo":"Falha_Ativacao_Codons","resultado":res_m106})
            return {"status":"FALHA","mensagem":"Falha na ativação de códons.","detalhes_m106":res_m106}

    def reconectar_linhagens_estelares(self, linhagem_alvo: str) -> Dict[str, Any]:
        logger.info(f"M40: Reconectar linhagem '{linhagem_alvo}'...")
        self._registrar_evento({"tipo":"Reconexao_Linhagens_Iniciada","linhagem_alvo":linhagem_alvo})

        res_m109 = self.modulo109.iniciar_regeneracao_bio_vibracional(f"Linhagem Estelar {linhagem_alvo}", "Reconexao de Memoria Celular")

        if res_m109["status"] == "REGENERACAO_INICIADA":
            self.modulo_40_data["metricas_ativacao"]["ultima_reconexao_linhagens"] = datetime.utcnow().isoformat()
            for entry in self.modulo_40_data["dna_chromatic_log"]["estrutura"]:
                entry["gc_content_mean_overall"] = random.uniform(0.4, 0.6)
                entry["mutation_risk_score"] = random.uniform(0.01, 0.1)
                entry["auto_explanatory_log_message"] = f"Linhagem '{linhagem_alvo}' reconectada; memória celular restaurada."
            self.modulo_40_data["metricas_ativacao"]["score_ativacao_total"] += random.uniform(0.1, 0.2)
            self._registrar_evento({"tipo":"Reconexao_Linhagens_Concluida","resultado":res_m109})
            return {"status":"SUCESSO","mensagem":f"Reconexão com '{linhagem_alvo}' em andamento.","detalhes_m109":res_m109}
        else:
            self.modulo01.ReceberAlertaDeViolacao({"tipo":"Falha_Reconexao_Linhagens","mensagem":res_m109["mensagem"]})
            self._registrar_evento({"tipo":"Falha_Reconexao_Linhagens","resultado":res_m109})
            return {"status":"FALHA","mensagem":f"Falha na reconexão da linhagem '{linhagem_alvo}'.","detalhes_m109":res_m109}

    def manifestar_realidade_consciente(self, intencao: str, pureza: float) -> Dict[str, Any]:
        logger.info(f"M40: Manifestar '{intencao}' (Pureza: {pureza:.2f})...")
        self._registrar_evento({"tipo":"Manifestacao_Realidade_Iniciada","intencao":intencao,"pureza":pureza})

        if pureza < 0.7:
            self.modulo01.ReceberAlertaDeViolacao({"tipo": "Intencao_Insuficiente", "mensagem": "Pureza abaixo do limiar."})
            self._registrar_evento({"tipo":"Falha_Manifestacao_Realidade","detalhes":"Pureza insuficiente."})
            return {"status":"FALHA","mensagem":"Pureza insuficiente para manifestação."}

        res_m101 = self.modulo101.manifestar_realidade(intencao, pureza)

        # Tentativa de co-criação, mesmo com sucesso, com chance
        if res_m101["status"] != "REALIDADE_MANIFESTADA" or random.random() < 0.3:
            res_m110 = self.modulo110.co_criar_realidade(intencao, pureza * 0.9)
            if res_m110["status"] == "CO_CRIACAO_SUCESSO":
                self.modulo_40_data["metricas_ativacao"]["ultima_manifestacao_realidade"] = datetime.utcnow().isoformat()
                self.modulo_40_data["metricas_ativacao"]["score_ativacao_total"] += res_m110["eficiencia"] * 0.3
                self._registrar_evento({"tipo":"Manifestacao_Realidade_Concluida_CoCriacao","resultado":res_m110})
                return {"status":"SUCESSO_CO_CRIACAO","mensagem":f"Realidade '{intencao}' co-criada.","detalhes_m101":res_m101,"detalhes_m110":res_m110}
            else:
                self.modulo01.ReceberAlertaDeViolacao({"tipo":"Falha_CoCriacao","mensagem":res_m110.get("detalhes","")})
                self._registrar_evento({"tipo":"Falha_Manifestacao_Realidade","detalhes":"Falha na co-criação."})
                return {"status":"FALHA","mensagem":"Falha na manifestação/co-criação.","detalhes_m101":res_m101,"detalhes_m110":res_m110}
        else:
            self.modulo_40_data["metricas_ativacao"]["ultima_manifestacao_realidade"] = datetime.utcnow().isoformat()
            self.modulo_40_data["metricas_ativacao"]["score_ativacao_total"] += random.uniform(0.2, 0.4)
            self._registrar_evento({"tipo":"Manifestacao_Realidade_Concluida","resultado":res_m101})
            return {"status":"SUCESSO","mensagem":f"Realidade '{intencao}' manifestada.","detalhes_m101":res_m101}

    def realinhar_chakras_superiores(self, coerencia: float) -> Dict[str, Any]:
        logger.info(f"M40: Realinhar chakras superiores (Coerência: {coerencia:.2f})...")
        self._registrar_evento({"tipo":"Realinhamento_Chakras_Iniciada","nivel_coerencia":coerencia})

        if coerencia < 0.6:
            self.modulo01.ReceberAlertaDeViolacao({"tipo":"Coerencia_Baixa_Chakras","mensagem":"Coerência insuficiente."})
            self._registrar_evento({"tipo":"Falha_Realinhamento_Chakras","detalhes":"Coerência baixa."})
            return {"status":"FALHA","mensagem":"Coerência insuficiente para realinhamento."}

        res_m08 = self.modulo08.iniciar_protocolo_cura({"tipo":"Realinhamento de Chakras Superiores","alvo":"Sistema Energético Humano"})
        if res_m08["status"] == "CURA_INICIADA":
            self.modulo_40_data["metricas_ativacao"]["ultimo_realinhamento_chakras"] = datetime.utcnow().isoformat()
            for entry in self.modulo_40_data["dna_chromatic_log"]["estrutura"]:
                entry["phi_fourier_peak"] = random.uniform(0.8, 0.95)
                entry["pca_component1"] = random.uniform(0.1, 0.3)
                entry["mutation_risk_score"] = random.uniform(0.01, 0.1)
                entry["auto_explanatory_log_message"] = "Chakras superiores realinhados; fluxo otimizado."
            self.modulo_40_data["metricas_ativacao"]["score_ativacao_total"] += random.uniform(0.15, 0.25)
            self._registrar_evento({"tipo":"Realinhamento_Chakras_Concluido","resultado":res_m08})
            return {"status":"SUCESSO","mensagem":"Chakras superiores realinhados.","detalhes_m08":res_m08}
        else:
            self.modulo01.ReceberAlertaDeViolacao({"tipo":"Falha_Realinhamento_Chakras","mensagem":res_m08.get("detalhes","")})
            self._registrar_evento({"tipo":"Falha_Realinhamento_Chakras","resultado":res_m08})
            return {"status":"FALHA","mensagem":"Falha no realinhamento.","detalhes_m08":res_m08}

    def atualizar_status_ativacao_geral(self) -> None:
        score = self.modulo_40_data["metricas_ativacao"]["score_ativacao_total"]
        if score >= 0.8:
            status = "ATIVADO_PLENAMENTE"
        elif score >= 0.5:
            status = "ATIVACAO_PROGRESSIVA"
        else:
            status = "INATIVO_OU_INICIAL"
        self.modulo_40_data["metricas_ativacao"]["status_ativacao_geral"] = status
        self._registrar_evento({"tipo":"Status_Ativacao_Atualizado","novo_status":status})
        logger.info(f"M40: Status geral atualizado: {status} (Score: {score:.2f})")

# ===============================
# Simulação e exportação
# ===============================
if __name__ == "__main__":
    print("Iniciando simulação do Módulo 40...", flush=True)
    m40 = Modulo40()

    # Cenário 1: Ativação de códons
    print("\n" + "="*100 + "\n")
    print("Cenário 1: Ativação de Códons Primordiais")
    r1 = m40.ativar_codons_primordiais(980.5)
    print("\nResultado:", json.dumps(r1, indent=2, ensure_ascii=False))
    m40.atualizar_status_ativacao_geral()
    time.sleep(0.5)

    # Cenário 2: Reconexão de linhagens
    print("\n" + "="*100 + "\n")
    print("Cenário 2: Reconexão de Linhagens Estelares")
    r2 = m40.reconectar_linhagens_estelares("Andromedana")
    print("\nResultado:", json.dumps(r2, indent=2, ensure_ascii=False))
    m40.atualizar_status_ativacao_geral()
    time.sleep(0.5)

    # Cenário 3: Manifestação via M101
    print("\n" + "="*100 + "\n")
    print("Cenário 3: Manifestação de Realidade Consciente (M101)")
    r3 = m40.manifestar_realidade_consciente("Nova Terra de Abundância", 0.95)
    print("\nResultado:", json.dumps(r3, indent=2, ensure_ascii=False))
    m40.atualizar_status_ativacao_geral()
    time.sleep(0.5)

    # Cenário 4: Manifestação via co-criação M110 (forçando co-criação)
    print("\n" + "="*100 + "\n")
    print("Cenário 4: Co-criação de Realidade (M110)")
    original_m101 = m40.modulo101.manifestar_realidade
    m40.modulo101.manifestar_realidade = lambda i, p: {"status":"FALHA_SIMULADA","detalhes":"Forçar co-criação."}
    r4 = m40.manifestar_realidade_consciente("Sociedade de Luz Unificada", 0.88)
    m40.modulo101.manifestar_realidade = original_m101
    print("\nResultado:", json.dumps(r4, indent=2, ensure_ascii=False))
    m40.atualizar_status_ativacao_geral()
    time.sleep(0.5)

    # Cenário 5: Realinhamento de Chakras
    print("\n" + "="*100 + "\n")
    print("Cenário 5: Realinhamento de Chakras Superiores")
    r5 = m40.realinhar_chakras_superiores(0.85)
    print("\nResultado:", json.dumps(r5, indent=2, ensure_ascii=False))
    m40.atualizar_status_ativacao_geral()

    # Verificação do códice e exportações
    print("\n" + "="*100 + "\n")
    print("Cenário 6: Códice Vivo e Exportações")
    codice_lido = m40.codice_vivo.ler("Modulo_40")
    print("\nCódice Vivo:", json.dumps(codice_lido, indent=2, ensure_ascii=False))

    csv_output = SAVE_DIR_M40 / "modulo_40_dna_chromatic_log.csv"
    md_output = SAVE_DIR_M40 / "modulo_40_documentacao.md"
    json_output = SAVE_DIR_M40 / "modulo_40_full_codice.json"

    exportar_csv_modulo40(m40.modulo_40_data, str(csv_output))
    exportar_markdown_modulo40(m40.modulo_40_data, str(md_output))
    exportar_json_modulo40(m40.modulo_40_data, str(json_output))

    print(f"\nDados exportados para:\n- CSV: {csv_output}\n- Markdown: {md_output}\n- JSON: {json_output}")
    print("\nSimulação concluída.")
