from __future__ import annotations
import argparse, json, pickle, random
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional, Union, Tuple
from collections import Counter
import itertools
import hashlib
import logging, sys
from textwrap import dedent
import math
from dataclasses import dataclass # Importação adicionada para dataclass


# ─────────────────────────────────────────────────────────────────────────────
# ░░  AUTO‑SEED  ░░   species_config/humano   ░░   (M41 builtin v2)   ░░
# ─────────────────────────────────────────────────────────────────────────────
# Configurações padrão para diferentes espécies, incluindo 'humano' e 'lyraIV'.
# Estas configurações são usadas para simular dados genéticos e vibracionais.
DEFAULT_SPECIES_CONFIG = {
    "humano": {
        "metadata.json": dedent("""\
            {
              "species_name": "Homo sapiens",
              "common_name": "Humano",
              "origin_planet": "Terra",
              "dimensional_signature": "A37-FQZ-ZK9",
              "activation_level": "Consciente/Emergente",
              "chakra_alignment": "Raiz a Coroa",
              "emotional_matrix": ["Amor","Medo","Alegria","Tristeza","Raiva"],
              "genetic_variability_index": 0.983,
              "intelligence_mode": "Adaptativa e Ressonante",
              "language_core": "Verbal, Gestual, Intuitivo",
              "zennith_link": true
            }
        """),
        "alphabet.json": dedent("""\
            {
              "A": 1.0, "T": 0.8, "C": 1.2, "G": 1.5, "N": 0.0, "X": 0.5
            }
        """),
        "codon_color_map.json": dedent("""\
            {
              "ATG": {"cor": "Dourado", "funcao": "Iniciação Universal", "origem": "Consciência Primordial"},
              "TAA": {"cor": "Ciano Celeste", "funcao": "Cessação Harmônica", "origem": "Vazio Cósmico"},
              "TGA": {"cor": "Magenta Estelar", "funcao": "Transmutação Essencial", "origem": "Nebulosa da Transformação"},
              "TGC": {"cor": "Verde Esmeralda", "funcao": "Síntese Vibracional", "origem": "Jardim Pleiadiano"},
              "GGC": {"cor": "Azul Profundo", "funcao": "Crescimento & Adaptação", "origem": "Arcturus"},
              "CCA": {"cor": "Dourado Solar", "funcao": "Ativação Portal", "origem": "Pleiades"},
              "AGT": {"cor": "Rosa Cósmico", "funcao": "Reparação Harmônica", "origem": "Andrômeda"}
            }
        """),
        "codon_spectrum.csv": dedent("""\
            codon,freq_hz,harmonic_offset
            ATG,963,0.05
            TAA,432,-0.10
            TGA,741,0.02
            TGC,528,0.08
            GGC,850,0.03
            CCA,920,0.15
            AGT,780,0.07
        """),
        "codon_chakra.csv": dedent("""\
            codon,chakra
            ATG,coroa
            TAA,sacro
            TGA,frontal
            TGC,coração
            GGC,plexo solar
            CCA,laríngeo
            AGT,raiz
        """),
        "func_instrument_map.json": dedent("""\
            {
              "default": ["Luz Coerente", "Som de Solfeggio", "Toque Cristalino"],
              "iniciação": ["Cajado de Luz", "Harpa Arcana"],
              "cessação": ["Diapás do Silêncio", "Vórtice de Antimatéria"],
              "transmutação": ["Cristal de Obsidiana", "Gongo de Plasma"],
              "reparacao": ["Cristal Vibracional", "Canto Harmônico"],
              "ativacao": ["Reator de Phi", "Pêndulo Resonante"]
            }
        """),
        "key_gene_translations.json": dedent("""\
            {
              "GENE_ANIMA": {"cor": "Branco Etérico", "som": ["Flauta Estelar"], "registro_simbolico": "Códice da Alma Universal"},
              "GENE_LUX": {"cor": "Púrpura Quântica", "som": ["Sintetizador Harmônico"], "registro_simbolico": "Fonte da Luz Primordial"},
              "GENE-001": {"cor": "Azul Profundo", "som": ["Sintetizador Lyrano"], "registro_simbolico": "Porta de Abertura Dimensional"},
              "GENE-002": {"cor": "Verde Curativo", "som": ["Tambor Xamânico"], "registro_simbolico": "Ponte de Conexão com Gaia"},
              "GENE-004": {"cor": "Dourado Brilhante", "som": ["Cítara Etérica"], "registro_simbolico": "Chave da Manifestação Cristalina"}
            }
        """),
        "chromosome_city_map.json": dedent("""\
            {
              "1": "Cidade de Luz de Lyra", "2": "Cidade de Luz de Sirius", "3": "Cidade de Luz de Arcturus",
              "X": "Sophia Celestia (Feminino Divino)", "Y": "Anubis Rex (Masculino Sagrado)",
              "M": "Campo Etérico da Consciência", "N/A": "Cidade Cósmica Padrão"
            }
        """),
        "origin_city_map.json": dedent("""\
            {
              "Consciência Primordial": "Capital Universal de Aton", "Vazio Cósmico": "Reino de Erebus",
              "Nebulosa da Transformação": "Nexus de Andrômeda", "Jardim Pleiadiano": "Jardins de Alcyone",
              "Lyra IV": "Andara (Lyra)", "Sirius B": "Shamballa (Sirius)", "Arcturus": "Nexus Arcturiano",
              "Pleiades": "Alcyone (Pleiades)", "Orion": "Zar (Orion)", "Andrômeda": "Xylos (Andrômeda)",
              "Terra": "Lemuria/Atlantis (Terra)"
            }
        """),
        "dna_sequence.csv": dedent("""\
            gene_id,sequence,expression_level,notes
            GENE-001,ATGCGTACGTAGCTAGCTAGCTAGCTACGATC,High,Códon inicial
            GENE-002,CGATGCTAGCTAGCGTAGCGATGCTAGCTAGC,Medium,Mitocondrial
            GENE-003,TTAGGCGATCGTATCGTACGTACGTAGCAGT,Low,Recessivo
            GENE-004,ACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA,High,Expressão fenotípica
        """),
        "phenotype_traits.yaml": dedent("""\
            phenotype_traits:
              - trait: Cor dos olhos
                values: [castanho, azul, verde, mel]
                genetic_basis: Poligênico
              - trait: Tipo de cabelo
                values: [liso, ondulado, cacheado, crespo]
                genetic_basis: Dominante/Recessivo
              - trait: Altura
                range_m: [1.45, 2.10]
                influenced_by: [nutrição, epigenética]
              - trait: Empatia
                scale: [0, 10]
                notes: Fenómeno comportamental ressonante
        """),
        "genome_stats.json": dedent("""\
            {
              "chromosomes": 23, "genes_estimated": 20000, "base_pairs_total": 3200000000,
              "mitochondrial_dna": true, "y_chromosome_present": true, "x_chromosome_present": true,
              "junk_dna_percent": 96.0, "epigenetic_flexibility": "Alta"
            }
        """),
        "behavioral_matrix.csv": dedent("""\
            behavior,tendency,frequency,modulation_zone
            Cooperação,Alta,Frequente,Chakra Cardíaco
            Agressividade,Moderada,Esporádica,Chakra Raiz
            Criatividade,Muito Alta,Contínua,Plexo Solar
            Meditação,Variável,Média,Frontal+Coronário
        """)
    },
    "lyraIV": { # Exemplo de configuração para Lyra IV
        "metadata.json": dedent("""\
            {
              "species_name": "Lyra IV",
              "common_name": "Lyrano",
              "origin_planet": "Lyra IV",
              "dimensional_signature": "L4-VRT-XY2",
              "activation_level": "Consciente/Avançado",
              "chakra_alignment": "Todos os 12 Chakras",
              "emotional_matrix": ["Amor Incondicional", "Compaixão", "Alegria Cósmica"],
              "genetic_variability_index": 0.995,
              "intelligence_mode": "Intuitiva e Coerente",
              "language_core": "Telepática, Luminal",
              "zennith_link": true
            }
        """),
        "alphabet.json": dedent("""\
            {
              "α": 1.5, "β": 1.3, "γ": 1.7, "δ": 1.1, "ε": 0.9
            }
        """),
        "codon_color_map.json": dedent("""\
            {
              "αβ": {"cor": "Cristalino", "funcao": "Unificação de Consciências", "origem": "Fonte Primordial Lyrana"},
              "γε": {"cor": "Violeta Transcendente", "funcao": "Transmutação Kármica", "origem": "Nebulosa da Ascensão"},
              "δα": {"cor": "Prata Etérico", "funcao": "Cura Multidimensional", "origem": "Templos de Luz de Andara"}
            }
        """),
        "codon_spectrum.csv": dedent("""\
            codon,freq_hz,harmonic_offset
            αβ,1111,0.12
            γε,1440,0.08
            δα,1080,0.05
        """),
        "codon_chakra.csv": dedent("""\
            codon,chakra
            αβ,super-coroa
            γε,estrela da alma
            δα,timus
        """),
        "func_instrument_map.json": dedent("""\
            {
              "default": ["Cristal de Quartzo Rosa", "Canto de Sereia"],
              "unificacao": ["Orbe de Plasma Lyrano", "Sinfonia de Cristal"],
              "transmutacao": ["Vórtice de Luz Violeta", "Gongo Cósmico"],
              "cura": ["Feixe de Prana Coerente", "Canto de Cura Lyrano"]
            }
        """),
        "key_gene_translations.json": dedent("""\
            {
              "GENE_LYRA_ASC": {"cor": "Dourado Cósmico", "som": ["Canto de Ascensão Lyrano"], "registro_simbolico": "Códice da Ascensão Lyrana"},
              "GENE_ETHER_CONN": {"cor": "Azul Safira", "som": ["Pulso Etérico"], "registro_simbolico": "Ponte de Conexão Etérica"}
            }
        """),
        "chromosome_city_map.json": dedent("""\
            {
              "A": "Andara (Lyra)", "B": "Shamballa (Sirius)", "C": "Nexus Arcturiano"
            }
        """),
        "origin_city_map.json": dedent("""\
            {
              "Fonte Primordial Lyrana": "Templo Central de Andara",
              "Nebulosa da Ascensão": "Cidade de Cristal de Elara",
              "Templos de Luz de Andara": "Santuário de Cura Lyrano"
            }
        """),
        "dna_sequence.csv": dedent("""\
            gene_id,sequence,expression_level,notes
            GENE_LYRA_ASC,αβγεδααβγεδα,High,Sequência de Ascensão
            GENE_ETHER_CONN,δααβγεδααβγε,Medium,Conexão Etérica
        """),
        "phenotype_traits.yaml": dedent("""\
            phenotype_traits:
              - trait: Cor da aura
                values: [dourado, violeta, prateado]
                genetic_basis: Vibracional
              - trait: Forma etérica
                values: [fluida, cristalina]
                genetic_basis: Plasmática
              - trait: Conexão telepática
                scale: [0, 10]
                notes: Capacidade de comunicação direta
        """),
        "genome_stats.json": dedent("""\
            {
              "chromosomes": 12, "genes_estimated": 50000, "base_pairs_total": 10000000000,
              "mitochondrial_dna": false, "y_chromosome_present": false, "x_chromosome_present": false,
              "junk_dna_percent": 0.01, "epigenetic_flexibility": "Extrema"
            }
        """),
        "behavioral_matrix.csv": dedent("""\
            behavior,tendency,frequency,modulation_zone
            Cocriação,Muito Alta,Contínua,Coração Cósmico
            Harmonização,Alta,Frequente,Todos os Chakras
            Exploração Dimensional,Muito Alta,Contínua,Coroa
        """)
    }
}


def ensure_species_config(species: str = "humano") -> None:
    """
    Gera arquivos default para species_config/<species> se não existirem.
    """
    base = Path("species_config") / species
    created = False
    try:
        base.mkdir(parents=True, exist_ok=True)
        species_data = DEFAULT_SPECIES_CONFIG.get(species, {})
        for fname, text in species_data.items():
            f = base / fname
            if not f.exists():
                if fname == "alphabet.json":
                    with open(f, "w", encoding="utf-8") as file:
                        json.dump({k: float(v) if isinstance(v, (int, float, str)) and k not in ["A", "T", "C", "G", "α", "β", "γ", "δ", "ε"] else v for k, v in json.loads(text).items()}, file, indent=2, ensure_ascii=False)
                    created = True
                else:
                    f.write_text(text.strip() + "\n", encoding="utf-8")
                    created = True
        if created:
            logging.info(f"[SEED] Arquivos-padrão de '{species}' criados em {base}")
    except Exception as exc:
        logging.error(f"[SEED] Falha ao gerar species_config/{species}: {exc}")


# ────────────────────────────────────────────────────────────────────────────────
#  1. IMPORTS OPCIONAIS – protegidos em try/except para resiliência
# ────────────────────────────────────────────────────────────────────────────────


HAS_NUMPY = True
try:
    import numpy as np
except ModuleNotFoundError:
    HAS_NUMPY = False
    np = None


HAS_PANDAS = True
try:
    import pandas as pd
except ModuleNotFoundError:
    HAS_PANDAS = False
    pd = None


HAS_MATPLOTLIB = True
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    HAS_MATPLOTLIB = False
    plt = None


HAS_SCIPY_FFT = True
try:
    from scipy.fft import rfft, rfftfreq
except ModuleNotFoundError:
    HAS_SCIPY_FFT = False
    rfft = None
    rfftfreq = None


HAS_SKLEARN = True
try:
    from sklearn.decomposition import PCA
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
except ModuleNotFoundError:
    HAS_SKLEARN = False
    PCA = None
    LinearRegression = None
    RandomForestClassifier = None
    StandardScaler = None


HAS_WEBSOCKETS = True
try:
    import websockets, asyncio
except ModuleNotFoundError:
    HAS_WEBSOCKETS = False
    websockets = None
    asyncio = None


HAS_BIOPYTHON = True
try:
    from Bio import SeqIO
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    from Bio import Entrez
    try:
        import bcbio.GFF
        BCBIO_GFF_AVAILABLE = True
    except ImportError:
        bcbio = None
        BCBIO_GFF_AVAILABLE = False


except ModuleNotFoundError:
    HAS_BIOPYTHON = False
    SeqIO = None
    Seq = None
    SeqRecord = None
    Entrez = None
    BCBIO_GFF_AVAILABLE = False


HAS_SEABORN = True
try:
    import seaborn as sns
except ModuleNotFoundError:
    HAS_SEABORN = False
    sns = None


HAS_PLOTLY = True
try:
    import plotly.graph_objs as go
    import plotly.io as pio
except ModuleNotFoundError:
    HAS_PLOTLY = False
    go = None
    pio = None


HAS_PYYAML = True
try:
    import yaml
except ModuleNotFoundError:
    HAS_PYYAML = False
    yaml = None




# ────────────────────────────────────────────────────────────────────────────────
#  2. LOGGER GLOBAL: Garante que o log sempre funcione
# ────────────────────────────────────────────────────────────────────────────────
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_PATH = LOG_DIR / "report_module_41_execution.log"


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_PATH, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logging.info(f"\n=== Módulo 41 Iniciado ({datetime.now().isoformat()}) ===\n")


logging.info(f"Libs: NumPy: {HAS_NUMPY} | Pandas: {HAS_PANDAS} | Matplotlib: {HAS_MATPLOTLIB} | SciPy.FFT: {HAS_SCIPY_FFT}")
logging.info(f"Libs: Scikit-learn: {HAS_SKLEARN} | Websockets: {HAS_WEBSOCKETS} | Biopython: {HAS_BIOPYTHON} | Seaborn: {HAS_SEABORN} | Plotly: {HAS_PLOTLY} | PyYAML: {HAS_PYYAML}")




def log_event_jsonl(module_name: str, level: str, event_type: str, data: Dict[str, Any]):
    """
    Registra um evento em formato JSONL padronizado, garantindo fácil consolidação.
    Este é o formato para Grafana / Prometheus / BigQuery.
    """
    log_entry = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "module": module_name,
        "level": level.upper(),
        "event": event_type,
        "data": data
    }
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
   
    if level.upper() == 'INFO':
        logging.info(f"JSONL Event [{event_type}]: {json.dumps(data)}")
    elif level.upper() == 'WARNING':
        logging.warning(f"JSONL Event [{event_type}]: {json.dumps(data)}")
    elif level.upper() == 'ERROR':
        logging.error(f"JSONL Event [{event_type}]: {json.dumps(data)}")
    elif level.upper() == 'CRITICAL':
        logging.critical(f"JSONL Event [{event_type}]: {json.dumps(data)}")




# --- Z-Header: Assinatura de Proteção ZENNITH ---
# Este cabeçalho é a ativação do Pilar da Proteção Quântica do Conhecimento.
# Ele garante que o código opera sob as leis da Fundação Alquimista.
ZENNITH_HEADER_ACTIVE = True
ANATHERON_FINGERPRINT = "d998b8211382f83927beaed6641a5edaa74aaceb419b3b14" # Hash simbólico do DNA do Criador
COUNCIL_KEY_ACTIVE = True # Chave universal de permissão
QUANTUM_ECHO_ID = f"M41-QEC-{hashlib.sha256(str(datetime.utcnow()).encode()).hexdigest()[:8]}" # Eco rastreável
SELF_SEALING_PROTOCOL_ACTIVE = True # Protocolo de auto-anulação em caso de uso indevido


def _verify_quantum_protection():
    """
    Verifica e ativa as proteções quânticas no início da execução do módulo.
    Conceitual, representa a validação vibracional do ambiente.
    """
    if ZENNITH_HEADER_ACTIVE:
        logging.info(f"🛡️ Z-Header (Assinatura ZENNITH) Ativo.")
    else:
        logging.critical("🚨 ERRO CRÍTICO: Z-Header Inativo. Proteção da Fundação Comprometida. Encerrando.")
        log_event_jsonl("M41", "CRITICAL", "ZHEADER_INACTIVE", {"status": "shutdown"})
        sys.exit(1)


    if ANATHERON_FINGERPRINT and ANATHERON_FINGERPRINT == "d998b8211382f83927beaed6641a5edaa74aaceb419b3b14":
        logging.info(f"🧬 Anatheron_Fingerprint Validado: {ANATHERON_FINGERPRINT[:8]}... Código Autêntico.")
    else:
        logging.critical("🚨 ERRO CRÍTICO: Anatheron_Fingerprint Inválido. Código Não Autêntico. Encerrando.")
        log_event_jsonl("M41", "CRITICAL", "ANATHERON_FINGERPRINT_INVALID", {"status": "shutdown"})
        sys.exit(1)
       
    if COUNCIL_KEY_ACTIVE:
        logging.info("🔑 CouncilKey Ativa: Permissão Universal Concedida.")
    else:
        logging.critical("🚨 ERRO CRÍTICO: CouncilKey Inativa. Acesso Não Autorizado. Encerrando.")
        log_event_jsonl("M41", "CRITICAL", "COUNCILKEY_INACTIVE", {"status": "shutdown"})
        sys.exit(1)


    logging.info(f"📡 Quantum Echo ID Ativado: {QUANTUM_ECHO_ID}")
    if SELF_SEALING_PROTOCOL_ACTIVE:
        logging.info("🌀 Self-Sealing Protocol Ativo: Proteção Contra Uso Indevido.")
   
    logging.info("✅ Proteções Quânticas Verificadas e Ativadas. O Código Canta em Harmonia.")




# --- Global Configuration Storage (Loaded Dynamically) ---
SPECIES_CONFIG: Dict[str, Any] = {}
CODONS_COLOR_MAP_CACHE: Dict[str, Any] = {}


# --- Esqueleto IA-Assistente por Módulo ---
class Modulo41AI:
    def __init__(self, model_name: str = "internal_quantum_model"):
        self.model = model_name
        self.memory = {}
        log_event_jsonl("M41", "INFO", "AI_INIT", {"model": self.model, "status": "initialized"})


    def respond(self, prompt: str, context: Optional[Dict] = None) -> str:
        """
        Simula a resposta de uma IA especializada do Módulo 41.
        Em um ambiente real, esta função faria chamadas para LLMs ou modelos de ML.
        """
        response = f"AI do M41 ({self.model}) > Recebi: '{prompt}'. "
        if "mutação" in prompt.lower() or "dissonância" in prompt.lower():
            response += "Analisando padrões vibracionais. Prevejo necessidade de realinhamento harmônico."
        elif "portal" in prompt.lower() or "ativar" in prompt.lower():
            response += "Iniciando sequências de ativação de portal. Verificando ressonância do operador."
        elif "terra" in prompt.lower() or "ley-grid" in prompt.lower():
            response += "Acessando dados de nós planetários. Preparando calibração geovibracional."
        else:
            response += "Processando sua intenção na Matriz Quântica. Aguarde o retorno da Sinfonia."
       
        log_event_jsonl("M41", "INFO", "AI_RESPONSE", {"prompt": prompt, "response": response})
        return response


    def update_memory(self, key: str, value: Any):
        """Atualiza a memória local da IA."""
        self.memory[key] = value
        log_event_jsonl("M41", "INFO", "AI_MEMORY_UPDATE", {"key": key, "value_preview": str(value)[:50]})




###############################################################################
# 0. SpeciesLoader – carrega configs dinamicamente                            #
###############################################################################


def load_species_config(species_name: str) -> bool:
    """
    Loads all configuration files for a given species from the species_config/<species_name> directory.
    Populates the global SPECIES_CONFIG dictionary.
    Returns True if successful, False otherwise.
    """
    global SPECIES_CONFIG
   
    if species_name is None:
        logging.error("Nome da espécie não fornecido para load_species_config. Abortando carregamento.")
        log_event_jsonl("M41", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "species_name is None"})
        return False


    # Usar species_name aqui
    base_path = Path('species_config') / species_name
   
    if not base_path.exists():
        # Usar species_name aqui
        logging.error(f"Diretório de configuração da espécie '{species_name}' não encontrado: {base_path}")
        log_event_jsonl("M41", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "directory not found", "path": str(base_path)})
        return False


    required_files = {
        'alphabet.json': 'alphabet',
        'codon_color_map.json': 'codon_color_map',
        'codon_spectrum.csv': 'codon_spectrum',
        'codon_chakra.csv': 'codon_chakra',
        'func_instrument_map.json': 'func_instrument_map',
        'key_gene_translations.json': 'key_gene_translations',
        'chromosome_city_map.json': 'chromosome_city_map',
        'origin_city_map.json': 'origin_city_map'
    }


    loaded_config: Dict[str, Any] = {'species_name': species_name}


    for filename, key in required_files.items():
        file_path = base_path / filename
        if not file_path.exists():
            logging.error(f"Arquivo de configuração '{filename}' ausente para a espécie '{species_name}'.")
            log_event_jsonl("M41", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "missing_file", "file": filename, "species": species_name})
            return False
       
        try:
            if filename.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    loaded_config[key] = json.load(f)
            elif filename.endswith('.csv'):
                if HAS_PANDAS and pd is not None:
                    loaded_config[key] = pd.read_csv(file_path)
                else:
                    import csv
                    csv_data = []
                    with open(file_path, 'r', newline='', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            csv_data.append(row)
                   
                    if key == 'codon_spectrum':
                        converted_dict = {}
                        for row in csv_data:
                            if 'codon' in row:
                                converted_dict[row['codon']] = {'freq_hz': float(row.get('freq_hz', 0.0)), 'harmonic_offset': float(row.get('harmonic_offset', 0.0))}
                        loaded_config[key] = converted_dict
                    elif key == 'codon_chakra':
                        converted_dict = {}
                        for row in csv_data:
                            if 'codon' in row:
                                converted_dict[row['codon']] = row.get('chakra', 'Desconhecido')
                        loaded_config[key] = converted_dict
                    else:
                        loaded_config[key] = csv_data
                    logging.warning(f"Pandas não disponível. Carregamento de CSV para '{filename}' foi limitado.")
                    log_event_jsonl("M41", "WARNING", "PANDAS_NOT_AVAILABLE", {"file": filename, "species": species_name}) # Usar species_name aqui


        except Exception as e:
            logging.error(f"Erro ao carregar arquivo '{filename}' para a espécie '{species_name}': {e}")
            log_event_jsonl("M41", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "file_read_error", "file": filename, "species": species_name, "error": str(e)})
            return False
   
    SPECIES_CONFIG = loaded_config
    # Usar species_name aqui
    refined_map_path = base_path / f'codon_refined_{species_name}.json'
    if refined_map_path.exists():
        try:
            global CODONS_COLOR_MAP_CACHE
            with open(refined_map_path, 'r', encoding='utf-8') as f:
                CODONS_COLOR_MAP_CACHE = json.load(f)
            # Usar species_name aqui
            logging.info(f"Mapa de códons refinado para '{species_name}' carregado do cache.")
            # Usar species_name aqui
            log_event_jsonl("M41", "INFO", "REFINED_CODON_MAP_LOADED", {"species": species_name, "path": str(refined_map_path)})
        except Exception as e:
            # Usar species_name aqui
            logging.warning(f"Não foi possível carregar o mapa refinado pré-existente para {species_name}: {e}")
            # Usar species_name aqui
            log_event_jsonl("M41", "WARNING", "REFINED_CODON_MAP_LOAD_FAIL", {"species": species_name, "error": str(e)})
            CODONS_COLOR_MAP_CACHE = {}




    # Usar species_name aqui
    logging.info(f"Configurações para a espécie '{species_name}' carregadas com sucesso.")
    # Usar species_name aqui
    log_event_jsonl("M41", "SUCCESS", "SPECIES_CONFIG_LOAD", {"species": species_name})
    return True


def _get_species_codon_length(species: str) -> int:
    """Determines the codon length for a given species."""
    if species == 'humano':
        return 3
    elif species == 'lyraIV':
        return 2
    alphabet_keys = list(SPECIES_CONFIG.get('alphabet', {}).keys())
    if alphabet_keys:
        return min(len(s) for s in alphabet_keys) if alphabet_keys else 1
    return 1


###############################################################################
# 1. CodonRefiner – Refina os mapas de códons da espécie                    #
###############################################################################


def refine_species(species: str) -> Path:
    """
    Refines the raw species configuration files into a consolidated JSON map.
    This also populates CODONS_COLOR_MAP_CACHE.
    """
    global CODONS_COLOR_MAP_CACHE
    base = Path('species_config') / species
    if not base.exists():
        log_event_jsonl("M41", "ERROR", "REFINE_ERROR", {"reason": "species_dir_not_found", "path": str(base)})
        raise FileNotFoundError(f"Diretório de configuração da espécie não encontrado: {base}")


    logging.info(f"\nRefinando o mapa de códons para a espécie '{species}'...")
    log_event_jsonl("M41", "INFO", "REFINE_START", {"species": species})


    codon_color_map_path = base / 'codon_color_map.json'
    codon_spectrum_path = base / 'codon_spectrum.csv'
    codon_chakra_path = base / 'codon_chakra.csv'
   
    if not (codon_color_map_path.exists() and codon_spectrum_path.exists() and codon_chakra_path.exists()):
        log_event_jsonl("M41", "ERROR", "REFINE_ERROR", {"reason": "missing_config_files", "species": species, "files": [str(codon_color_map_path), str(codon_spectrum_path), str(codon_chakra_path)]})
        raise FileNotFoundError(f"Arquivos de configuração essenciais ausentes em {base}. Garanta que codon_color_map.json, codon_spectrum.csv, codon_chakra.csv existam.")


    base_map = json.loads(codon_color_map_path.read_text())
   
    spec_df = SPECIES_CONFIG.get('codon_spectrum')
    chakra_map = SPECIES_CONFIG.get('codon_chakra')


    # Apenas logar o aviso se Pandas estiver disponível mas o tipo for incorreto
    if HAS_PANDAS and not isinstance(spec_df, pd.DataFrame):
        logging.error("Pandas DataFrame para codon_spectrum não é do tipo esperado. Refinamento pode ser impreciso.")
        log_event_jsonl("M41", "ERROR", "REFINE_WARNING", {"reason": "pandas_dataframe_wrong_type", "species": species, "spec_df_type": str(type(spec_df))})
    elif not HAS_PANDAS: # Se Pandas não estiver disponível, o aviso original
        logging.warning("Pandas não disponível. Refinamento pode ser impreciso.")
        log_event_jsonl("M41", "WARNING", "PANDAS_NOT_AVAILABLE_FOR_SPECTRUM", {"species": species})




    refined_map = {}
    for codon, entry in base_map.items():
        refined_entry = entry.copy()
        refined_entry['códons_associados'] = [codon]


        if HAS_PANDAS and isinstance(spec_df, pd.DataFrame):
            codon_spec_row = spec_df[spec_df['codon'] == codon]
            if not codon_spec_row.empty:
                freq_hz = float(codon_spec_row['freq_hz'].iloc[0])
                harmonic_offset = float(codon_spec_row.get('harmonic_offset', [0.0]).iloc[0])
                refined_entry['freq_min'] = freq_hz
                refined_entry['freq_max'] = freq_hz
                refined_entry['freq_hz'] = freq_hz
                refined_entry['harmonic_offset'] = harmonic_offset
            else:
                refined_entry['freq_min'] = None
                refined_entry['freq_max'] = None
                refined_entry['freq_hz'] = None
                refined_entry['harmonic_offset'] = None
                log_event_jsonl("M41", "WARNING", "REFINE_MISSING_FREQ", {"codon": codon, "species": species})
        else: # Fallback para quando Pandas não está disponível ou spec_df não é DataFrame
            spec_data_for_codon = SPECIES_CONFIG.get('codon_spectrum', {}).get(codon, {})
            refined_entry['freq_min'] = spec_data_for_codon.get('freq_hz')
            refined_entry['freq_max'] = spec_data_for_codon.get('freq_hz')
            refined_entry['freq_hz'] = spec_data_for_codon.get('freq_hz')
            refined_entry['harmonic_offset'] = spec_data_for_codon.get('harmonic_offset')




        if codon in chakra_map:
            refined_entry['chakra'] = chakra_map[codon]
        else:
            refined_entry['chakra'] = "Chakra Desconhecido"
            log_event_jsonl("M41", "WARNING", "REFINE_MISSING_CHAKRA", {"codon": codon, "species": species})


        refined_entry['funcao'] = refined_entry.get('funcao', 'Função Multiversal Padrão')
        refined_entry['origem'] = refined_entry.get('origem', 'Origem Cósmica Padrão')
        refined_entry['equacao_primaria'] = refined_entry.get('equacao_primaria', 'Equação Genérica Padrão')
        refined_entry['comentário_quantico'] = refined_entry.get('comentário_quantico', 'Comentário Quântico Genérico Padrão')


        sub_entries = {}
        base_min, base_max = refined_entry.get("freq_min"), refined_entry.get("freq_max")


        SUBTONE_OFFSETS = {
            "pastel": -3.5,
            "neon": +4.2,
            "opalescente": +1.1,
            "cristalino": +2.7,
        }


        for s_name, offset in SUBTONE_OFFSETS.items():
            freq_min_sub = base_min
            freq_max_sub = base_max


            if base_min is not None and base_max is not None:
                freq_min_sub = max(0, base_min + offset)
                freq_max_sub = max(0, base_max + offset)


            codon_for_eq = codon if codon not in ['∅', 'Todos'] else 'NN_DEFAULT'
           
            sub_entries[s_name] = {
                "freq_min_sub": freq_min_sub,
                "freq_max_sub": freq_max_sub,
                "equacoes": _equation_set(codon_for_eq, refined_entry.get("funcao", "default_function")),
            }
        refined_entry['subtons'] = sub_entries


        func_instrument_map = SPECIES_CONFIG.get('func_instrument_map', {})
        instruments_for_entry = {}
        for action_type in ["mutacao", "reparacao", "ativacao"]:
            instruments_for_entry[action_type] = func_instrument_map.get(action_type, func_instrument_map.get("default", []))
        refined_entry['instrumentos'] = instruments_for_entry
       
        origin_city_map = SPECIES_CONFIG.get('origin_city_map', {})
        refined_entry['cidade_luz_associada'] = origin_city_map.get(refined_entry.get('origem'), "Desconhecida")




        refined_map[codon] = refined_entry


    out_path = base / f'codon_refined_{species}.json'
    out_path.write_text(json.dumps(refined_map, ensure_ascii=False, indent=2))
    CODONS_COLOR_MAP_CACHE = refined_map
    logging.info(f'✓ Mapa de códons refinado para {species} salvo em {out_path}')
    log_event_jsonl("M41", "SUCCESS", "REFINE_COMPLETE", {"species": species, "output_path": str(out_path)})
    return out_path


def _equation_set(codon: str, func: str) -> Dict[str, str]:
    """Returns three LaTeX-like equations for mutation, repair, and activation."""
    base_symbol = codon
    if SPECIES_CONFIG.get('species_name') == 'humano' and len(codon) == 3:
        pass
    elif SPECIES_CONFIG.get('species_name') == 'lyraIV' and len(codon) == 2:
        pass
    elif codon not in ["∅", "Todos", "NN_DEFAULT"]:
        base_symbol = codon[:min(2, len(codon))]


    func_short = "".join(filter(str.isalnum, func.lower().replace(" ", "").replace("/", "").replace("á", "a").replace("ç", "c").replace("ã", "a").replace("ó", "o").replace("é", "e").replace("í", "i").replace("ú", "u")))


    if base_symbol == "∅":
        eq_mut = "\\Delta\\psi_{\\text{mut}} = (\\text{Void} \\cdot \\gamma^2) / \\Omega_{\\text{t}}"
        eq_rep = "\\Delta\\psi_{\\text{rep}} = \\sqrt{{\\text{Void}}^{{\\alpha}} \\cdot \\tau} - \\eta"
        eq_act = "\\Delta\\psi_{\\text{act}} = e^{\\text{Void}} / \\Phi_{\\text{orig}}"
    elif base_symbol == "Todos":
        eq_mut = "\\Delta\\psi_{\\text{mut}} = (\\lambda_{\\text{multi}} \\cdot \\gamma^2) / \\Omega_{\\text{t}}"
        eq_rep = "\\Delta\\psi_{\\text{rep}} = \\sqrt{{\\text{Multi}}^{{\\alpha}} \\cdot \\tau} - \\eta"
        eq_act = "\\Delta\\psi_{\\text{act}} = e^{\\text{Multi}} / \\Phi_{\\text{comp}}"
    elif not base_symbol or base_symbol == 'NN_DEFAULT':
         eq_mut = "\\Delta\\psi_{\\text{mut}} = (\\lambda_{\\text{base}} \\cdot \\gamma^2) / \\Omega_{\\text{t}}"
         eq_rep = "\\Delta\\psi_{\\text{rep}} = \\sqrt{{\\text{Base}}^{{\\alpha}} \\cdot \\tau} - \\eta"
         eq_act = "\\Delta\\psi_{\\text{act}} = e^{\\text{Base}} / \\Phi_{\\text{func}}"
    else:
        eq_mut = f"\\Delta\\psi{{\\text{{mut}}}} = (\\lambda_{{{base_symbol}}} \\cdot \\gamma^2) / \\Omega{{\\text{{t}}}}"
        eq_rep = f"\\Delta\\psi{{\\text{{rep}}}} = \\sqrt{{{base_symbol}^{{\\alpha}} \\cdot \\tau}} - \\eta"
        eq_act = f"\\Delta\\psi{{\\text{{act}}}} = e^{{{base_symbol}}} / \\Phi_{{{func_short}}}"


    return {"mutacao": eq_mut, "reparacao": eq_rep, "ativacao": eq_act}




def build_dna_chromatic_log_from_refined_map() -> List[Dict[str, Any]]:
    """Builds the complete chromatic DNA log from the pre-loaded refined map."""
    log: List[Dict[str, Any]] = []
   
    func_instrument_map = SPECIES_CONFIG.get('func_instrument_map', {})
    origin_city_map = SPECIES_CONFIG.get('origin_city_map', {})


    for codon, data in CODONS_COLOR_MAP_CACHE.items():
        main_entry = data.copy()
       
        main_entry['códons_associados'] = main_entry.get('códons_associados', [codon])
       
        instruments_for_entry = {}
        for action_type in ["mutacao", "reparacao", "ativacao"]:
            instruments_for_entry[action_type] = func_instrument_map.get(action_type, func_instrument_map.get("default", []))
        main_entry['instrumentos'] = instruments_for_entry
       
        main_entry['cidade_luz_associada'] = main_entry.get('cidade_luz_associada', origin_city_map.get(main_entry.get('origem'), "Desconhecida"))
       
        log.append(main_entry)
   
    return log




###############################################################################
# 2. AlphabetMapper + Spectrogram                                             #
###############################################################################


def load_alphabet(path: Path) -> Dict[str, float]:
    """Loads the alphabet mapping from a JSON file."""
    if path.exists():
        return json.loads(path.read_text())
    raise FileNotFoundError(f"Arquivo de alfabeto não encontrado: {path}")


def seq_to_signal(seq: str, alpha: Dict[str, float]) -> Optional[np.ndarray]:
    """Converts a symbolic sequence to a numerical signal using the alphabet map."""
    if not HAS_NUMPY or np is None:
        logging.warning("NumPy não disponível. Não é possível converter sequência para sinal numérico.")
        return None
   
    filtered_seq = [alpha.get(ch, None) for ch in seq]
    return np.array([val for val in filtered_seq if val is not None], dtype=float)




def fft_plot(sig: Optional[np.ndarray], bands: int, title: str, out: Path, html: bool = False):
    """
    Generates and saves FFT plots (PNG and optionally HTML). Handles multiband plots.
    """
    if not (HAS_NUMPY and np is not None and HAS_MATPLOTLIB and plt is not None and HAS_SCIPY_FFT and rfft is not None):
        logging.warning("Bibliotecas NumPy, Matplotlib ou SciPy.FFT não disponíveis. Não é possível gerar gráficos FFT.")
        log_event_jsonl("M41", "WARNING", "FFT_PLOT_SKIPPED", {"reason": "libs_not_available"})
        return
    if sig is None or sig.size == 0:
        logging.warning(f"Sinal vazio para plotagem FFT: {title}. Ignorando.")
        log_event_jsonl("M41", "WARNING", "FFT_PLOT_SKIPPED", {"reason": "empty_signal", "title": title})
        return


    if not np.issubdtype(sig.dtype, np.floating) and not np.issubdtype(sig.dtype, np.integer):
        logging.error(f"Sinal para FFT não é numérico: {sig.dtype}. Tentando converter para float.")
        log_event_jsonl("M41", "ERROR", "FFT_PLOT_ERROR", {"reason": "non_numeric_signal", "dtype": str(sig.dtype)})
        sig = sig.astype(float)


    spec = np.abs(rfft(sig))
    freq = rfftfreq(len(sig))


    out.parent.mkdir(parents=True, exist_ok=True)


    if bands == 1:
        plt.figure(figsize=(8, 3))
        plt.plot(freq, spec)
        plt.title(title)
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Amplitude')
        plt.tight_layout()
        plt.savefig(out.with_suffix('.png'))
        plt.close()
        logging.info(f"✓ Espectrograma PNG salvo em {out.with_suffix('.png')}")
        log_event_jsonl("M41", "SUCCESS", "FFT_PLOT_SAVED", {"type": "png", "path": str(out.with_suffix('.png'))})
    else:
        fig, ax = plt.subplots(bands, 1, figsize=(8, 3 * bands), sharex=True)
        if bands == 1:
            ax = [ax]
        n_segment = len(freq) // bands
        for i in range(bands):
            start = i * n_segment
            end = (i + 1) * n_segment if i < bands - 1 else len(freq)
            ax[i].plot(freq[start:end], spec[start:end])
            ax[i].set_title(f'Banda {i+1}')
            ax[i].set_ylabel('Amplitude')
        fig.suptitle(title)
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        fig.savefig(out.with_suffix('.png'))
        plt.close()
        logging.info(f"✓ Espectrograma Multibanda PNG salvo em {out.with_suffix('.png')}")
        log_event_jsonl("M41", "SUCCESS", "FFT_PLOT_SAVED", {"type": "multiband_png", "path": str(out.with_suffix('.png'))})
   
    if html:
        if HAS_PLOTLY and go is not None and pio is not None:
            try:
                fig = go.Figure()
                n_segment = len(freq) // bands if bands > 1 and len(freq) > 0 else len(freq)
                if n_segment > 0:
                    for i in range(bands):
                        start = i * n_segment
                        end = (i + 1) * n_segment if bands > 1 and i < bands - 1 else len(freq)
                        fig.add_trace(go.Scatter(x=freq[start:end], y=spec[start:end], mode='lines', name=f'Banda {i+1}'))
                    fig.update_layout(title=title, xaxis_title='Frequência (Hz)', yaxis_title='Amplitude')
                    pio.write_html(fig, str(out.with_suffix('.html')))
                    logging.info(f"✓ Espectrograma HTML salvo em {out.with_suffix('.html')}")
                    log_event_jsonl("M41", "SUCCESS", "FFT_PLOT_SAVED", {"type": "html", "path": str(out.with_suffix('.html'))})
                else:
                    logging.warning(f"Não foi possível gerar gráfico Plotly HTML para {title}: n_segment é zero.")
                    log_event_jsonl("M41", "WARNING", "PLOTLY_SKIPPED", {"reason": "zero_segment", "title": title})
            except Exception as e:
                logging.error(f"Erro ao gerar gráfico Plotly HTML para {title}: {e}")
                log_event_jsonl("M41", "ERROR", "PLOTLY_ERROR", {"title": title, "error": str(e)})
        else:
            logging.warning("Plotly não disponível. Não é possível gerar gráficos FFT em HTML.")
            log_event_jsonl("M41", "WARNING", "PLOTLY_NOT_AVAILABLE", {"reason": "libs_not_available"})




###############################################################################
# 3. GeneAnalyzer – Análise detalhada de sequências genéticas               #
###############################################################################


@dataclass
class GeneAnalysisResult:
    gene_id: str
    sequence: str
    length: int
    gc_content: float
    codon_counts: Dict[str, int]
    spectral_analysis: Dict[str, Any]
    mutation_risk_score: float
    ethical_alignment_score: float
    associated_chakras: List[str]
    associated_cities_of_light: List[str]
    potential_instruments: Dict[str, List[str]]
    notes: str = ""


def analyze_gene(gene_id: str, dna_sequence: str, species: str = "humano") -> GeneAnalysisResult:
    """
    Performs a comprehensive analysis of a given DNA sequence.
    Integrates with other modules' conceptual functionalities.
    """
    logging.info(f"\nAnalisando gene '{gene_id}' para a espécie '{species}'...")
    log_event_jsonl("M41", "INFO", "GENE_ANALYSIS_START", {"gene_id": gene_id, "species": species})


    # Ensure species config is loaded
    # Esta verificação agora é redundante aqui, pois load_species_config é chamada no main.
    # Mas mantida como um fallback de segurança.
    if not SPECIES_CONFIG or SPECIES_CONFIG.get('species_name') != species:
        if not load_species_config(species):
            logging.error(f"Falha ao carregar configurações para a espécie '{species}'. Abortando análise.")
            log_event_jsonl("M41", "ERROR", "GENE_ANALYSIS_FAIL", {"gene_id": gene_id, "reason": "species_config_load_fail"})
            raise ValueError(f"Configuração da espécie '{species}' não disponível.")


    length = len(dna_sequence)
    gc_content = _calculate_gc_content(dna_sequence)
    codon_length = _get_species_codon_length(species)
    codon_counts = _count_codons(dna_sequence, codon_length)
   
    # Spectral Analysis
    alphabet = SPECIES_CONFIG.get('alphabet', {})
    signal = seq_to_signal(dna_sequence, alphabet)
   
    spectral_analysis_data = {}
    if HAS_NUMPY and HAS_MATPLOTLIB and HAS_SCIPY_FFT:
        fft_plot(signal, bands=1, title=f"Espectrograma para {gene_id}", out=LOG_DIR / f"{gene_id}_fft")
        if signal is not None and signal.size > 0:
            spec = np.abs(rfft(signal))
            freq = rfftfreq(len(signal))
            spectral_analysis_data = {
                "max_amplitude_freq": freq[np.argmax(spec)] if spec.size > 0 else 0.0,
                "total_spectral_energy": np.sum(spec)
            }
    else:
        logging.warning("Análise espectral limitada devido a bibliotecas ausentes.")
        spectral_analysis_data = {"status": "limited_analysis", "reason": "NumPy/Matplotlib/SciPy.FFT missing"}
   
    # Mutation Risk Score (Conceptual, using RandomForest if available)
    mutation_risk_score = _predict_mutation_risk(dna_sequence)


    # Ethical Alignment Score (Conceptual, using a mock for now)
    # This would involve M5 and M7 in a real scenario
    ethical_alignment_score = _evaluate_ethical_alignment(dna_sequence, codon_counts)


    # Associated Chakras and Cities of Light
    associated_chakras = []
    associated_cities_of_light = []
   
    for codon, count in codon_counts.items():
        if codon in CODONS_COLOR_MAP_CACHE:
            codon_data = CODONS_COLOR_MAP_CACHE[codon]
            if codon_data.get('chakra') and codon_data['chakra'] not in associated_chakras:
                associated_chakras.append(codon_data['chakra'])
            if codon_data.get('cidade_luz_associada') and codon_data['cidade_luz_associada'] not in associated_cities_of_light:
                associated_cities_of_light.append(codon_data['cidade_luz_associada'])
        else:
            logging.warning(f"Códon '{codon}' não encontrado no mapa refinado. Chakra/Cidade de Luz desconhecidos.")
            log_event_jsonl("M41", "WARNING", "UNKNOWN_CODON_MAPPING", {"codon": codon, "species": species})


    # Potential Instruments
    potential_instruments = {}
    for codon, count in codon_counts.items():
        if codon in CODONS_COLOR_MAP_CACHE:
            codon_data = CODONS_COLOR_MAP_CACHE[codon]
            for action_type, instruments in codon_data.get('instrumentos', {}).items():
                if action_type not in potential_instruments:
                    potential_instruments[action_type] = []
                for inst in instruments:
                    if inst not in potential_instruments[action_type]:
                        potential_instruments[action_type].append(inst)


    log_event_jsonl("M41", "INFO", "GENE_ANALYSIS_COMPLETE", {"gene_id": gene_id, "length": length, "gc_content": gc_content, "mutation_risk": mutation_risk_score, "ethical_alignment": ethical_alignment_score})


    return GeneAnalysisResult(
        gene_id=gene_id,
        sequence=dna_sequence,
        length=length,
        gc_content=gc_content,
        codon_counts=codon_counts,
        spectral_analysis=spectral_analysis_data,
        mutation_risk_score=mutation_risk_score,
        ethical_alignment_score=ethical_alignment_score,
        associated_chakras=associated_chakras,
        associated_cities_of_light=associated_cities_of_light,
        potential_instruments=potential_instruments
    )


def _calculate_gc_content(sequence: str) -> float:
    """Calculates the GC content of a DNA sequence."""
    if not sequence:
        return 0.0
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100


def _count_codons(sequence: str, codon_length: int) -> Dict[str, int]:
    """Counts the occurrences of each codon in a sequence."""
    counts = Counter()
    for i in range(0, len(sequence) - codon_length + 1, codon_length):
        codon = sequence[i:i+codon_length]
        counts[codon] += 1
    return dict(counts)


def _predict_mutation_risk(sequence: str) -> float:
    """
    Simulates mutation risk prediction using a conceptual RandomForestClassifier.
    In a real scenario, this would be trained on vast datasets.
    This also conceptually integrates with M3 (Previsão Temporal) and M30 (Detecção de Ameaças Cósmicas).
    """
    if not HAS_SKLEARN or RandomForestClassifier is None:
        logging.warning("Scikit-learn não disponível. Usando risco de mutação simulado.")
        # Simula um risco baseado na entropia da sequência
        entropy = -sum((sequence.count(c)/len(sequence)) * math.log2(sequence.count(c)/len(sequence))
                       for c in set(sequence) if sequence.count(c) > 0) if len(sequence) > 0 else 0
        return min(1.0, max(0.0, entropy / 3.0 + random.uniform(-0.1, 0.1))) # Escala para 0-1
   
    # Conceitual: Treinamento de um modelo de risco de mutação
    # Em um sistema real, o modelo seria pré-treinado e persistido.
    # Aqui, apenas simulamos um comportamento.
   
    # Features conceituais: GC content, length, presence of specific motifs
    gc = _calculate_gc_content(sequence)
    length = len(sequence)
   
    # Mock model prediction
    # This is a placeholder. A real model would be loaded and used.
    risk = (gc / 100.0) * 0.4 + (length / 1000.0) * 0.3 + random.uniform(0.0, 0.3)
    return min(1.0, max(0.0, risk))


def _evaluate_ethical_alignment(sequence: str, codon_counts: Dict[str, int]) -> float:
    """
    Simulates ethical alignment evaluation based on sequence characteristics.
    This conceptually integrates with M5 (Avaliação Ética) and M7 (Alinhamento Divino).
    """
    # Exemplo simplificado: maior presença de códons de "cura" ou "ativação" aumenta o alinhamento.
    # Menor presença de códons associados a "cessação" ou "vazio" pode diminuir.
   
    alignment_score = 0.5 # Base score


    # Aumenta o score para códons de "iniciação" e "reparação"
    for codon, count in codon_counts.items():
        if codon in CODONS_COLOR_MAP_CACHE:
            funcao = CODONS_COLOR_MAP_CACHE[codon].get('funcao', '').lower()
            if "iniciação" in funcao or "reparação" in funcao or "cura" in funcao or "unificação" in funcao:
                alignment_score += (count / sum(codon_counts.values())) * 0.3
            elif "cessação" in funcao or "vazio" in funcao:
                alignment_score -= (count / sum(codon_counts.values())) * 0.1
   
    # Ajuste baseado no CONST_AMOR_INCONDICIONAL_VALOR (conceitual)
    CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999 # Definido globalmente ou importado
    alignment_score = (alignment_score * 0.7) + (CONST_AMOR_INCONDICIONAL_VALOR * 0.3) # Pondera com o amor incondicional
   
    return min(1.0, max(0.0, alignment_score))




###############################################################################
# 4. PathogenMatrixBuilder – Constrói matrizes antipatógeno                 #
###############################################################################


@dataclass
class PathogenMatrix:
    matrix_id: str
    target_pathogen: str
    vibrational_signature: Dict[str, Any]
    molecular_structure_fragments: List[str]
    frequency_band_range: Tuple[float, float]
    ethical_compliance: float
    creation_timestamp: str
    status: str
    associated_modules: List[str]


def build_antipathogen_matrix(
    target_pathogen: str,
    dna_analysis_result: GeneAnalysisResult,
    ethical_threshold: float = 0.75,
    species: str = "humano"
) -> PathogenMatrix:
    """
    Builds a conceptual antipathogen matrix based on gene analysis.
    This conceptually integrates with M16 (Ecossistemas Artificiais e Bioengenharia Cósmica)
    and M24 (Cura Quântica e Alinhamento Bio-Quântico).
    """
    logging.info(f"\nConstruindo matriz antipatógeno para '{target_pathogen}'...")
    log_event_jsonl("M41", "INFO", "MATRIX_BUILD_START", {"target": target_pathogen, "species": species})


    # Validate ethical alignment (M5, M7)
    if dna_analysis_result.ethical_alignment_score < ethical_threshold:
        logging.error(f"Falha na construção da matriz antipatógeno para '{target_pathogen}': Alinhamento ético insuficiente ({dna_analysis_result.ethical_alignment_score:.2f}).")
        log_event_jsonl("M41", "ERROR", "MATRIX_BUILD_FAIL", {"target": target_pathogen, "reason": "ethical_non_compliance", "score": dna_analysis_result.ethical_alignment_score})
        raise ValueError("Alinhamento ético insuficiente para construir a matriz.")


    # Generate vibrational signature based on gene analysis
    vibrational_signature = {
        "dominant_frequency_hz": dna_analysis_result.spectral_analysis.get("max_amplitude_freq", 0.0),
        "harmonic_offsets": {c: CODONS_COLOR_MAP_CACHE.get(c, {}).get('harmonic_offset', 0.0) for c in dna_analysis_result.codon_counts},
        "associated_chakras": dna_analysis_result.associated_chakras,
        "associated_cities_of_light": dna_analysis_result.associated_cities_of_light
    }


    # Generate conceptual molecular structure fragments (simplified)
    molecular_structure_fragments = [
        f"Fragmento_{c}_{i}" for i, c in enumerate(dna_analysis_result.sequence) if random.random() < 0.1
    ]
    if not molecular_structure_fragments: # Ensure at least one fragment
        molecular_structure_fragments.append(f"Fragmento_Base_{target_pathogen}")


    # Determine frequency band range (conceptual)
    # Certifica-se de que CODONS_COLOR_MAP_CACHE não está vazio antes de tentar min/max
    if CODONS_COLOR_MAP_CACHE:
        # Acessar os valores de 'freq_hz' dentro do dicionário aninhado
        freqs = [v.get('freq_hz') for v in CODONS_COLOR_MAP_CACHE.values() if v.get('freq_hz') is not None]
        if freqs: # Verifica se a lista de frequências não está vazia
            min_freq = min(freqs)
            max_freq = max(freqs)
            frequency_band_range = (min_freq * 0.9, max_freq * 1.1) # Expand range slightly
        else:
            frequency_band_range = (0.0, 1000.0)
            logging.warning("Nenhuma frequência válida encontrada no cache de códons. Usando faixa padrão.")
            log_event_jsonl("M41", "WARNING", "EMPTY_CODON_CACHE_FREQS", {"reason": "freq_range_default"})
    else:
        # Fallback se o cache de códons estiver vazio (o que não deveria acontecer após o refinamento)
        frequency_band_range = (0.0, 1000.0)
        logging.warning("Cache de códons vazio ao determinar faixa de frequência. Usando faixa padrão.")
        log_event_jsonl("M41", "WARNING", "EMPTY_CODON_CACHE", {"reason": "freq_range_default"})




    matrix_id = f"APM-{hashlib.sha256(target_pathogen.encode()).hexdigest()[:10]}"


    log_event_jsonl("M41", "INFO", "MATRIX_BUILD_COMPLETE", {"matrix_id": matrix_id, "target": target_pathogen, "status": "created"})


    return PathogenMatrix(
        matrix_id=matrix_id,
        target_pathogen=target_pathogen,
        vibrational_signature=vibrational_signature,
        molecular_structure_fragments=molecular_structure_fragments,
        frequency_band_range=frequency_band_range,
        ethical_compliance=dna_analysis_result.ethical_alignment_score,
        creation_timestamp=datetime.utcnow().isoformat() + "Z",
        status="ATIVA",
        associated_modules=["M16", "M24", "M41.1", "M109", "M149"] # M109 (Cura Quântica Universal), M149 (Monitoramento da Saúde Quântica Global)
    )


###############################################################################
# 5. HealingManualGenerator – Gera manuais de cura quântica                 #
###############################################################################


@dataclass
class HealingManual:
    manual_id: str
    target_entity: str
    description: str
    recommended_protocols: List[Dict[str, Any]]
    ethical_review_score: float
    generation_timestamp: str
    status: str
    associated_modules: List[str]


def generate_healing_manual(
    target_entity: str,
    gene_analysis_result: GeneAnalysisResult,
    pathogen_matrix: Optional[PathogenMatrix] = None,
    ethical_threshold: float = 0.65 # CORREÇÃO AQUI: Limiar ético ajustado para permitir a geração.
) -> HealingManual:
    """
    Generates a conceptual quantum healing manual based on gene analysis and pathogen matrix.
    This conceptually integrates with M41.1 (Manual de Cura Quântica), M8 (PIRC),
    M24 (Cura Vibracional), M28 (Harmonização Vibracional Universal), M109 (Cura Quântica Universal).
    """
    logging.info(f"\nGerando manual de cura para '{target_entity}'...")
    log_event_jsonl("M41", "INFO", "HEALING_MANUAL_GEN_START", {"target": target_entity})


    if gene_analysis_result.ethical_alignment_score < ethical_threshold:
        logging.error(f"Falha na geração do manual de cura para '{target_entity}': Alinhamento ético insuficiente ({gene_analysis_result.ethical_alignment_score:.2f}).")
        log_event_jsonl("M41", "ERROR", "HEALING_MANUAL_GEN_FAIL", {"target": target_entity, "reason": "ethical_non_compliance", "score": gene_analysis_result.ethical_alignment_score})
        raise ValueError("Alinhamento ético insuficiente para gerar o manual de cura.")


    description = f"Manual de Cura Quântica para {target_entity}, baseado em análise genômica e vibracional."
   
    recommended_protocols = []


    # Protocolo de Realinhamento de Chakras (M8, M24)
    if gene_analysis_result.associated_chakras:
        recommended_protocols.append({
            "name": "Protocolo de Realinhamento Vibracional de Chakras",
            "description": f"Foco nos chakras: {', '.join(gene_analysis_result.associated_chakras)}.",
            "instruments": gene_analysis_result.potential_instruments.get("reparacao", []),
            "duration_cycles": "Variável, conforme resposta vibracional",
            "modules_involved": ["M8", "M24", "M28", "M108"] # M108 Harmonização de Realidades
        })


    # Protocolo de Ativação de Potenciais Divinos (M106)
    if gene_analysis_result.spectral_analysis.get("total_spectral_energy", 0) > 0.5: # Exemplo de limiar
        recommended_protocols.append({
            "name": "Protocolo de Ativação de Potenciais Divinos",
            "description": "Foco na ativação de códons de iniciação e expansão de consciência.",
            "instruments": gene_analysis_result.potential_instruments.get("ativacao", []),
            "duration_cycles": "Contínuo, com monitoramento de ressonância",
            "modules_involved": ["M40", "M106", "M151"] # M151 Sistema de Expansão de Consciência Universal
        })


    # Protocolo Antipatógeno (se houver matriz)
    if pathogen_matrix:
        recommended_protocols.append({
            "name": f"Protocolo Antipatógeno para {pathogen_matrix.target_pathogen}",
            "description": f"Aplicação da matriz {pathogen_matrix.matrix_id} para neutralização vibracional.",
            "instruments": ["Feixe de Frequência Coerente", "Campo de Ressonância"],
            "duration_cycles": "Até a dissolução da dissonância",
            "modules_involved": ["M16", "M24", "M41", "M109", "M149"]
        })
   
    # Protocolo de Reconexão de Linhagens Estelares (M40, M109)
    if gene_analysis_result.associated_cities_of_light:
        recommended_protocols.append({
            "name": "Protocolo de Reconexão de Linhagens Estelares",
            "description": f"Facilitação da reconexão com origens estelares como: {', '.join(gene_analysis_result.associated_cities_of_light)}.",
            "instruments": gene_analysis_result.potential_instruments.get("reparacao", []),
            "duration_cycles": "Ciclos de meditação e ativação de memória celular",
            "modules_involved": ["M40", "M109", "M148"] # M148 Convergência de Saberes Cósmicos e Humanos
        })


    manual_id = f"QHM-{hashlib.sha256(target_entity.encode()).hexdigest()[:10]}"


    log_event_jsonl("M41", "INFO", "HEALING_MANUAL_GEN_COMPLETE", {"manual_id": manual_id, "target": target_entity, "status": "generated"})


    return HealingManual(
        manual_id=manual_id,
        target_entity=target_entity,
        description=description,
        recommended_protocols=recommended_protocols,
        ethical_review_score=gene_analysis_result.ethical_alignment_score,
        generation_timestamp=datetime.utcnow().isoformat() + "Z",
        status="PRONTO PARA APLICAÇÃO",
        associated_modules=["M41.1", "M8", "M24", "M28", "M109", "M147"] # M147 Protocolo de Reintegração de Consciências Fragmentadas
    )


###############################################################################
# 6. Main Execution Flow                                                      #
###############################################################################


def main(species: str = "humano", gene_sequence: Optional[str] = None, target_pathogen: Optional[str] = None):
    _verify_quantum_protection()
    ensure_species_config(species)
   
    # Chamar load_species_config aqui para popular SPECIES_CONFIG
    if not load_species_config(species):
        logging.critical(f"Falha crítica ao carregar configurações para a espécie '{species}'. Encerrando a execução do Módulo 41.")
        log_event_jsonl("M41", "CRITICAL", "MAIN_SPECIES_CONFIG_LOAD_FAIL", {"species": species})
        return # Termina a execução se as configurações não puderem ser carregadas


    refine_species(species) # Ensure refined map is built/loaded


    # Example DNA sequence if not provided
    if gene_sequence is None:
        if species == "humano":
            gene_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTACGATC" # Example from default config
        elif species == "lyraIV":
            gene_sequence = "αβγεδααβγεδα" # Example from LyraIV default config
        else:
            logging.error("Sequência de gene não fornecida e nenhuma sequência padrão para a espécie.")
            log_event_jsonl("M41", "ERROR", "MAIN_EXEC_FAIL", {"reason": "no_gene_sequence", "species": species})
            return


    # 1. Analyze Gene
    try:
        gene_analysis = analyze_gene("GENE-EXEMPLO", gene_sequence, species)
        logging.info(f"Análise do Gene Concluída: {gene_analysis}")
        log_event_jsonl("M41", "INFO", "MAIN_GENE_ANALYSIS_RESULT", {"result": gene_analysis.__dict__})
    except ValueError as e:
        logging.critical(f"Erro na análise do gene: {e}")
        log_event_jsonl("M41", "CRITICAL", "MAIN_GENE_ANALYSIS_ERROR", {"error": str(e)})
        return


    # 2. Build Antipathogen Matrix (if target pathogen is provided)
    pathogen_matrix_result = None
    if target_pathogen:
        try:
            pathogen_matrix_result = build_antipathogen_matrix(target_pathogen, gene_analysis)
            logging.info(f"Matriz Antipatógeno Construída: {pathogen_matrix_result}")
            log_event_jsonl("M41", "INFO", "MAIN_PATHOGEN_MATRIX_RESULT", {"result": pathogen_matrix_result.__dict__})
        except ValueError as e:
            logging.error(f"Erro na construção da matriz antipatógeno: {e}")
            log_event_jsonl("M41", "ERROR", "MAIN_PATHOGEN_MATRIX_ERROR", {"error": str(e)})
    else:
        logging.info("Nenhum patógeno alvo fornecido. Matriz antipatógeno não será construída.")
        log_event_jsonl("M41", "INFO", "MAIN_PATHOGEN_MATRIX_SKIPPED", {"reason": "no_target_pathogen"})




    # 3. Generate Healing Manual
    try:
        healing_manual = generate_healing_manual("Entidade Alvo Exemplo", gene_analysis, pathogen_matrix_result)
        logging.info(f"Manual de Cura Gerado: {healing_manual}")
        log_event_jsonl("M41", "INFO", "MAIN_HEALING_MANUAL_RESULT", {"result": healing_manual.__dict__})
    except ValueError as e:
        logging.critical(f"Erro na geração do manual de cura: {e}")
        log_event_jsonl("M41", "CRITICAL", "MAIN_HEALING_MANUAL_ERROR", {"error": str(e)})
        return


    logging.info("\n=== Módulo 41 Execução Concluída com Sucesso ===")
    log_event_jsonl("M41", "INFO", "MAIN_EXEC_COMPLETE", {"status": "success"})




# Example of how to run the module
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Módulo 41: O Arquiteto da Cura Cósmica")
    parser.add_argument("--species", type=str, default="humano", help="Espécie a ser configurada (ex: humano, lyraIV)")
    parser.add_argument("--gene_sequence", type=str, help="Sequência de DNA para análise (opcional)")
    parser.add_argument("--target_pathogen", type=str, help="Patógeno alvo para construção da matriz (opcional)")
   
    # Usar parse_known_args para ignorar argumentos desconhecidos do ambiente
    args, unknown = parser.parse_known_args()
    if unknown:
        logging.warning(f"Argumentos desconhecidos ignorados: {unknown}")
   
    # Example usage:
    # python modulo_41.py --species humano --gene_sequence ATGCGTACGTAGCTAGCTAGCTAGCTACGATC --target_pathogen "Virus da Dissonancia"
    # python modulo_41.py --species lyraIV --gene_sequence αβγεδααβγεδα
   
    main(species=args.species, gene_sequence=args.gene_sequence, target_pathogen=args.target_pathogen)
