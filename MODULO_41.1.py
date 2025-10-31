# -*- coding: utf-8 -*-
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
from dataclasses import dataclass  # Para estruturas de dados

# =============================================================================
# 2. LOGGER GLOBAL: Garante que o log sempre funcione
# =============================================================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_PATH = LOG_DIR / "report_module_41_1_execution.log"

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_PATH, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info(f"\n=== Módulo 41.1 Iniciado ({datetime.now().isoformat()}) ===\n")

# =============================================================================
# 1. IMPORTS OPCIONAIS – substituídos por flags (todas as libs externas indisponíveis)
# =============================================================================

HAS_NUMPY = False
HAS_PANDAS = False
HAS_MATPLOTLIB = False
HAS_SCIPY_FFT = False
HAS_SKLEARN = False
HAS_WEBSOCKETS = False
HAS_BIOPYTHON = False
HAS_SEABORN = False
HAS_PLOTLY = False
HAS_PYYAML = False

# Colocar None para referências de APIs externas
np = None
pd = None
plt = None
rfft = None
rfftfreq = None
PCA = None
LinearRegression = None
RandomForestClassifier = None
StandardScaler = None
websockets = None
asyncio = None
SeqIO = None
Seq = None
SeqRecord = None
Entrez = None
sns = None
go = None
pio = None
yaml = None

BCBIO_GFF_AVAILABLE = False

logging.info(f"Libs: NumPy: {HAS_NUMPY} | Pandas: {HAS_PANDAS} | Matplotlib: {HAS_MATPLOTLIB} | SciPy.FFT: {HAS_SCIPY_FFT}")
logging.info(f"Libs: Scikit-learn: {HAS_SKLEARN} | Websockets: {HAS_WEBSOCKETS} | Biopython: {HAS_BIOPYTHON} | Seaborn: {HAS_SEABORN} | Plotly: {HAS_PLOTLY} | PyYAML: {HAS_PYYAML}")

# =============================================================================
# 0. Z-Header: Assinatura de Proteção ZENNITH (conceitual)
# =============================================================================

ZENNITH_HEADER_ACTIVE = True
ANATHERON_FINGERPRINT = "d998b8211382f83927beaed6641a5edaa74aaceb419b3b14"  # Hash simbólico
COUNCIL_KEY_ACTIVE = True
QUANTUM_ECHO_ID = f"M41.1-QEC-{hashlib.sha256(str(datetime.utcnow()).encode()).hexdigest()[:8]}"
SELF_SEALING_PROTOCOL_ACTIVE = True

def _verify_quantum_protection():
    if ZENNITH_HEADER_ACTIVE:
        logging.info("🛡️ Z-Header (Assinatura ZENNITH) Ativo.")
    else:
        logging.critical("🚨 ERRO CRÍTICO: Z-Header Inativo. Encerrando.")
        sys.exit(1)

    if ANATHERON_FINGERPRINT and ANATHERON_FINGERPRINT == "d998b8211382f83927beaed6641a5edaa74aaceb419b3b14":
        logging.info(f"🧬 Anatheron_Fingerprint Validado: {ANATHERON_FINGERPRINT[:8]}... Código Autêntico.")
    else:
        logging.critical("🚨 ERRO CRÍTICO: Anatheron_Fingerprint Inválido. Encerrando.")
        sys.exit(1)

    if COUNCIL_KEY_ACTIVE:
        logging.info("🔑 CouncilKey Ativa: Permissão Universal Concedida.")
    else:
        logging.critical("🚨 ERRO CRÍTICO: CouncilKey Inativa. Encerrando.")
        sys.exit(1)

    logging.info(f"📡 Quantum Echo ID Ativado: {QUANTUM_ECHO_ID}")
    if SELF_SEALING_PROTOCOL_ACTIVE:
        logging.info("🌈 Self-Sealing Protocol Ativo: Proteção Contra Uso Indevido.")
    logging.info("✅ Proteções Quânticas Verificadas e Ativadas.")

def log_event_jsonl(module_name: str, level: str, event_type: str, data: Dict[str, Any]):
    entry = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "module": module_name,
        "level": level.upper(),
        "event": event_type,
        "data": data
    }
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    getattr(logging, level.lower(), logging.info)(f"JSONL Event [{event_type}]: {json.dumps(data)}")

# =============================================================================
# Seeds e configuração de espécies
# =============================================================================

DEFAULT_SPECIES_CONFIG = {
    "humano": {
        "metadata.json": dedent("""
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
        "alphabet.json": dedent("""
        {"A": 1.0, "T": 0.8, "C": 1.2, "G": 1.5, "N": 0.0, "X": 0.5}
        """),
        "codon_color_map.json": dedent("""
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
        "codon_spectrum.csv": dedent("""
        codon,freq_hz,harmonic_offset
        ATG,963,0.05
        TAA,432,-0.10
        TGA,741,0.02
        TGC,528,0.08
        GGC,850,0.03
        CCA,920,0.15
        AGT,780,0.07
        """),
        "codon_chakra.csv": dedent("""
        codon,chakra
        ATG,coroa
        TAA,sacro
        TGA,frontal
        TGC,coração
        GGC,plexo solar
        CCA,laríngeo
        AGT,raiz
        """),
        "func_instrument_map.json": dedent("""
        {
            "default": ["Luz Coerente", "Som de Solfeggio", "Toque Cristalino"],
            "iniciação": ["Cajado de Luz", "Harpa Arcana"],
            "cessação": ["Diapás do Silêncio", "Vórtice de Antimatéria"],
            "transmutação": ["Cristal de Obsidiana", "Gongo de Plasma"],
            "reparacao": ["Cristal Vibracional", "Canto Harmônico"],
            "ativacao": ["Reator de Phi", "Pêndulo Resonante"]
        }
        """),
        "origin_city_map.json": dedent("""
        {
            "Consciência Primordial": "Capital Universal de Aton",
            "Vazio Cósmico": "Reino de Erebus",
            "Nebulosa da Transformação": "Nexus de Andrômeda",
            "Jardim Pleiadiano": "Jardins de Alcyone",
            "Arcturus": "Nexus Arcturiano",
            "Pleiades": "Alcyone (Pleiades)",
            "Andrômeda": "Xylos (Andrômeda)",
            "Terra": "Lemuria/Atlantis (Terra)"
        }
        """)
    }
}

SPECIES_CONFIG: Dict[str, Any] = {}
CODONS_COLOR_MAP_CACHE: Dict[str, Any] = {}

def ensure_species_config(species: str = "humano") -> None:
    base = Path("species_config") / species
    created = False
    try:
        base.mkdir(parents=True, exist_ok=True)
        species_data = DEFAULT_SPECIES_CONFIG.get(species, {})
        for fname, text in species_data.items():
            f = base / fname
            if not f.exists():
                f.write_text(text.strip() + "\n", encoding="utf-8")
                created = True
        if created:
            logging.info(f"[SEED] Arquivos-padrão de '{species}' criados em {base}")
    except Exception as exc:
        logging.error(f"[SEED] Falha ao gerar species_config/{species}: {exc}")

def load_species_config(species_name: str) -> bool:
    global SPECIES_CONFIG
    if species_name is None:
        logging.error("Nome da espécie não fornecido.")
        log_event_jsonl("M41.1", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "species_name is None"})
        return False

    base_path = Path('species_config') / species_name
    if not base_path.exists():
        logging.error(f"Diretório species_config '{species_name}' não encontrado: {base_path}")
        log_event_jsonl("M41.1", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "directory not found", "path": str(base_path)})
        return False

    required_files = {
        'alphabet.json': 'alphabet',
        'codon_color_map.json': 'codon_color_map',
        'codon_spectrum.csv': 'codon_spectrum',
        'codon_chakra.csv': 'codon_chakra',
        'func_instrument_map.json': 'func_instrument_map',
        'origin_city_map.json': 'origin_city_map'
    }

    loaded_config: Dict[str, Any] = {'species_name': species_name}
    for filename, key in required_files.items():
        file_path = base_path / filename
        if not file_path.exists():
            logging.error(f"Arquivo '{filename}' ausente.")
            log_event_jsonl("M41.1", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "missing_file", "file": filename, "species": species_name})
            return False
        try:
            if filename.endswith('.json'):
                loaded_config[key] = json.loads(file_path.read_text(encoding='utf-8'))
            elif filename.endswith('.csv'):
                # Fallback sem pandas
                import csv
                csv_data = []
                with open(file_path, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        csv_data.append(row)
                if key == 'codon_spectrum':
                    converted = {}
                    for row in csv_data:
                        if 'codon' in row:
                            converted[row['codon']] = {
                                'freq_hz': float(row.get('freq_hz', 0.0)),
                                'harmonic_offset': float(row.get('harmonic_offset', 0.0))
                            }
                    loaded_config[key] = converted
                elif key == 'codon_chakra':
                    converted = {}
                    for row in csv_data:
                        if 'codon' in row:
                            converted[row['codon']] = row.get('chakra', 'Desconhecido')
                    loaded_config[key] = converted
                else:
                    loaded_config[key] = csv_data
                logging.warning(f"Pandas indisponível. Carregamento de CSV '{filename}' via fallback.")
                log_event_jsonl("M41.1", "WARNING", "PANDAS_NOT_AVAILABLE", {"file": filename, "species": species_name})
        except Exception as e:
            logging.error(f"Erro ao carregar '{filename}': {e}")
            log_event_jsonl("M41.1", "ERROR", "SPECIES_CONFIG_LOAD_FAIL", {"reason": "file_read_error", "file": filename, "species": species_name, "error": str(e)})
            return False

    SPECIES_CONFIG = loaded_config

    # Tenta carregar mapa refinado preexistente
    refined_map_path = base_path / f'codon_refined_{species_name}.json'
    global CODONS_COLOR_MAP_CACHE
    if refined_map_path.exists():
        try:
            CODONS_COLOR_MAP_CACHE = json.loads(refined_map_path.read_text(encoding='utf-8'))
            logging.info(f"Mapa de códons refinado para '{species_name}' carregado do cache.")
            log_event_jsonl("M41.1", "INFO", "REFINED_CODON_MAP_LOADED", {"species": species_name, "path": str(refined_map_path)})
        except Exception as e:
            logging.warning(f"Não foi possível carregar mapa refinado para {species_name}: {e}")
            log_event_jsonl("M41.1", "WARNING", "REFINED_CODON_MAP_LOAD_FAIL", {"species": species_name, "error": str(e)})
            CODONS_COLOR_MAP_CACHE = {}

    logging.info(f"Configurações para '{species_name}' carregadas com sucesso.")
    log_event_jsonl("M41.1", "SUCCESS", "SPECIES_CONFIG_LOAD", {"species": species_name})
    return True

def _get_species_codon_length(species: str) -> int:
    if species == 'humano':
        return 3
    alphabet_keys = list(SPECIES_CONFIG.get('alphabet', {}).keys())
    if alphabet_keys:
        return min(len(s) for s in alphabet_keys) if alphabet_keys else 1
    return 1

# =============================================================================
# 1. CodonRefiner – Refina os mapas de códons
# =============================================================================

def _equation_set(codon: str, func: str) -> Dict[str, str]:
    base_symbol = codon if codon not in ["∅", "Todos", "NN_DEFAULT"] else codon
    func_short = "".join(filter(str.isalnum, func.lower().replace(" ", "")))
    if base_symbol == "∅":
        eq_mut = "\\Delta\\psi_{\\text{mut}} = (\\text{Void} \\cdot \\gamma^2) / \\Omega_{\\text{t}}"
        eq_rep = "\\Delta\\psi_{\\text{rep}} = \\sqrt{\\text{Void}^{\\alpha} \\cdot \\tau} - \\eta"
        eq_act = "\\Delta\\psi_{\\text{act}} = e^{\\text{Void}} / \\Phi_{\\text{orig}}"
    elif base_symbol == "Todos":
        eq_mut = "\\Delta\\psi_{\\text{mut}} = (\\lambda_{\\text{multi}} \\cdot \\gamma^2) / \\Omega_{\\text{t}}"
        eq_rep = "\\Delta\\psi_{\\text{rep}} = \\sqrt{\\text{Multi}^{\\alpha} \\cdot \\tau} - \\eta"
        eq_act = "\\Delta\\psi_{\\text{act}} = e^{\\text{Multi}} / \\Phi_{\\text{comp}}"
    elif base_symbol == "NN_DEFAULT":
        eq_mut = "\\Delta\\psi_{\\text{mut}} = (\\lambda_{\\text{base}} \\cdot \\gamma^2) / \\Omega_{\\text{t}}"
        eq_rep = "\\Delta\\psi_{\\text{rep}} = \\sqrt{\\text{Base}^{\\alpha} \\cdot \\tau} - \\eta"
        eq_act = "\\Delta\\psi_{\\text{act}} = e^{\\text{Base}} / \\Phi_{\\text{func}}"
    else:
        short = base_symbol[:min(3, len(base_symbol))]
        eq_mut = f"\\Delta\\psi{{\\text{{mut}}}} = (\\lambda_{{{short}}} \\cdot \\gamma^2) / \\Omega{{\\text{{t}}}}"
        eq_rep = f"\\Delta\\psi{{\\text{{rep}}}} = \\sqrt{{{short}^{{\\alpha}} \\cdot \\tau}} - \\eta"
        eq_act = f"\\Delta\\psi{{\\text{{act}}}} = e^{{{short}}} / \\Phi_{{{func_short}}}"
    return {"mutacao": eq_mut, "reparacao": eq_rep, "ativacao": eq_act}

def refine_species(species: str) -> Path:
    global CODONS_COLOR_MAP_CACHE
    base = Path('species_config') / species
    if not base.exists():
        log_event_jsonl("M41.1", "ERROR", "REFINE_ERROR", {"reason": "species_dir_not_found", "path": str(base)})
        raise FileNotFoundError(f"Diretório species_config não encontrado: {base}")

    logging.info(f"\nRefinando o mapa de códons para a espécie '{species}'...\n")
    log_event_jsonl("M41.1", "INFO", "REFINE_START", {"species": species})

    codon_color_map = SPECIES_CONFIG.get('codon_color_map', {})
    spec_spectrum = SPECIES_CONFIG.get('codon_spectrum', {})
    chakra_map = SPECIES_CONFIG.get('codon_chakra', {})
    refined_map: Dict[str, Any] = {}

    SUBTONE_OFFSETS = {
        "pastel": -3.5,
        "neon":  4.2,
        "opalescente": 1.1,
        "cristalino":  2.7
    }

    func_instrument_map = SPECIES_CONFIG.get('func_instrument_map', {})
    origin_city_map = SPECIES_CONFIG.get('origin_city_map', {})

    for codon, entry in codon_color_map.items():
        refined_entry = entry.copy()
        refined_entry['códons_associados'] = [codon]

        # Frequências do espectro (fallback sem pandas/numpy)
        spectrum_data = spec_spectrum.get(codon, {})
        refined_entry['freq_min'] = spectrum_data.get('freq_hz')
        refined_entry['freq_max'] = spectrum_data.get('freq_hz')
        refined_entry['freq_hz'] = spectrum_data.get('freq_hz')
        refined_entry['harmonic_offset'] = spectrum_data.get('harmonic_offset')

        # Chakra
        refined_entry['chakra'] = chakra_map.get(codon, "Chakra Desconhecido")
        if refined_entry['chakra'] == "Chakra Desconhecido":
            log_event_jsonl("M41.1", "WARNING", "REFINE_MISSING_CHAKRA", {"codon": codon, "species": species})

        # Defaults
        refined_entry['funcao'] = refined_entry.get('funcao', 'Função Multiversal Padrão')
        refined_entry['origem'] = refined_entry.get('origem', 'Origem Cósmica Padrão')
        refined_entry['equacao_primaria'] = refined_entry.get('equacao_primaria', 'Equação Genérica Padrão')
        refined_entry['comentário_quantico'] = refined_entry.get('comentário_quantico', 'Comentário Quântico Genérico Padrão')

        # Subtons
        sub_entries = {}
        base_min, base_max = refined_entry.get("freq_min"), refined_entry.get("freq_max")
        for s_name, offset in SUBTONE_OFFSETS.items():
            freq_min_sub = None if base_min is None else max(0, base_min + offset)
            freq_max_sub = None if base_max is None else max(0, base_max + offset)
            sub_entries[s_name] = {
                "freq_min_sub": freq_min_sub,
                "freq_max_sub": freq_max_sub,
                "equacoes": _equation_set(codon, refined_entry.get("funcao", "default"))
            }
        refined_entry['subtons'] = sub_entries

        # Instrumentos
        instruments_for_entry = {}
        for action_type in ["mutacao", "reparacao", "ativacao"]:
            instruments_for_entry[action_type] = func_instrument_map.get(action_type, func_instrument_map.get("default", []))
        refined_entry['instrumentos'] = instruments_for_entry

        # Cidade de Luz
        refined_entry['cidade_luz_associada'] = origin_city_map.get(refined_entry.get('origem'), "Desconhecida")

        refined_map[codon] = refined_entry

    out_path = base / f'codon_refined_{species}.json'
    out_path.write_text(json.dumps(refined_map, ensure_ascii=False, indent=2), encoding='utf-8')
    CODONS_COLOR_MAP_CACHE = refined_map

    logging.info(f'✓ Mapa de códons refinado para {species} salvo em {out_path}')
    log_event_jsonl("M41.1", "SUCCESS", "REFINE_COMPLETE", {"species": species, "output_path": str(out_path)})
    return out_path

def build_dna_chromatic_log_from_refined_map() -> List[Dict[str, Any]]:
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

# =============================================================================
# 2. AlphabetMapper + Spectrogram (sem plot, com fallbacks)
# =============================================================================

def load_alphabet(path: Path) -> Dict[str, float]:
    if path.exists():
        return json.loads(path.read_text())
    raise FileNotFoundError(f"Arquivo de alfabeto não encontrado: {path}")

def seq_to_signal(seq: str, alpha: Dict[str, float]) -> Optional[List[float]]:
    if not HAS_NUMPY or np is None:
        logging.warning("NumPy indisponível. Conversão para sinal numérico limitada.")
        return [alpha.get(ch, 0.0) for ch in seq if ch in alpha]
    filtered_seq = [alpha.get(ch, None) for ch in seq]
    return [val for val in filtered_seq if val is not None]

def fft_plot(sig: Optional[List[float]], bands: int, title: str, out: Path, html: bool = False):
    logging.warning("Bibliotecas FFT/Plot indisponíveis. Pulando geração de espectrograma.")
    log_event_jsonl("M41.1", "WARNING", "FFT_PLOT_SKIPPED", {"reason": "libs_not_available", "title": title})
    return

# =============================================================================
# 3. GeneAnalyzer – Análise detalhada de sequências genéticas
# =============================================================================

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

def _calculate_gc_content(sequence: str) -> float:
    if not sequence:
        return 0.0
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def _count_codons(sequence: str, codon_length: int) -> Dict[str, int]:
    counts = Counter()
    for i in range(0, len(sequence) - codon_length + 1, codon_length):
        codon = sequence[i:i+codon_length]
        counts[codon] += 1
    return dict(counts)

def _predict_mutation_risk(sequence: str) -> float:
    # Simulação sem scikit-learn
    if len(sequence) == 0:
        return 0.0
    probs = []
    for c in set(sequence):
        p = sequence.count(c) / len(sequence)
        if p > 0:
            probs.append(p)
    entropy = -sum(p * math.log2(p) for p in probs) if probs else 0.0
    return min(1.0, max(0.0, entropy / 3.0 + random.uniform(-0.1, 0.1)))

def _evaluate_ethical_alignment(sequence: str, codon_counts: Dict[str, int]) -> float:
    alignment_score = 0.5
    total = sum(codon_counts.values()) or 1
    for codon, count in codon_counts.items():
        data = CODONS_COLOR_MAP_CACHE.get(codon, {})
        funcao = data.get('funcao', '').lower()
        frac = count / total
        if any(k in funcao for k in ["iniciação", "reparação", "cura", "unificação", "ativação"]):
            alignment_score += 0.3 * frac
        if any(k in funcao for k in ["cessação", "vazio"]):
            alignment_score -= 0.1 * frac
    CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
    alignment_score = (alignment_score * 0.7) + (CONST_AMOR_INCONDICIONAL_VALOR * 0.3)
    return min(1.0, max(0.0, alignment_score))

def analyze_gene(gene_id: str, dna_sequence: str, species: str = "humano") -> GeneAnalysisResult:
    logging.info(f"\nAnalisando gene '{gene_id}' para a espécie '{species}'...\n")
    log_event_jsonl("M41.1", "INFO", "GENE_ANALYSIS_START", {"gene_id": gene_id, "species": species})

    if not SPECIES_CONFIG or SPECIES_CONFIG.get('species_name') != species:
        if not load_species_config(species):
            logging.error(f"Falha ao carregar configs da espécie '{species}'.")
            log_event_jsonl("M41.1", "ERROR", "GENE_ANALYSIS_FAIL", {"gene_id": gene_id, "reason": "species_config_load_fail"})
            raise ValueError(f"Configuração da espécie '{species}' não disponível.")

    length = len(dna_sequence)
    gc_content = _calculate_gc_content(dna_sequence)
    codon_length = _get_species_codon_length(species)
    codon_counts = _count_codons(dna_sequence, codon_length)

    # Análise espectral (fallback)
    alphabet = SPECIES_CONFIG.get('alphabet', {})
    signal = seq_to_signal(dna_sequence, alphabet)
    spectral_analysis_data = {}
    if signal and len(signal) > 0:
        # Calcular métricas simples no fallback
        max_amp_freq = 0.0  # sem FFT real
        total_energy = sum(abs(x) for x in signal)
        spectral_analysis_data = {"max_amplitude_freq": max_amp_freq, "total_spectral_energy": total_energy}
    else:
        spectral_analysis_data = {"status": "limited_analysis", "reason": "No signal or libs missing"}

    mutation_risk_score = _predict_mutation_risk(dna_sequence)
    ethical_alignment_score = _evaluate_ethical_alignment(dna_sequence, codon_counts)

    associated_chakras: List[str] = []
    associated_cities_of_light: List[str] = []
    for codon, count in codon_counts.items():
        codon_data = CODONS_COLOR_MAP_CACHE.get(codon)
        if codon_data:
            chakra = codon_data.get('chakra')
            city = codon_data.get('cidade_luz_associada')
            if chakra and chakra not in associated_chakras:
                associated_chakras.append(chakra)
            if city and city not in associated_cities_of_light:
                associated_cities_of_light.append(city)
        else:
            logging.warning(f"Códon '{codon}' não encontrado no mapa refinado.")
            log_event_jsonl("M41.1", "WARNING", "UNKNOWN_CODON_MAPPING", {"codon": codon, "species": species})

    # Instrumentos potenciais
    potential_instruments: Dict[str, List[str]] = {}
    for codon, count in codon_counts.items():
        codon_data = CODONS_COLOR_MAP_CACHE.get(codon)
        if codon_data:
            for action_type, instruments in codon_data.get('instrumentos', {}).items():
                potential_instruments.setdefault(action_type, [])
                for inst in instruments:
                    if inst not in potential_instruments[action_type]:
                        potential_instruments[action_type].append(inst)

    log_event_jsonl("M41.1", "INFO", "GENE_ANALYSIS_COMPLETE", {
        "gene_id": gene_id,
        "length": length,
        "gc_content": gc_content,
        "mutation_risk": mutation_risk_score,
        "ethical_alignment": ethical_alignment_score
    })

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

# =============================================================================
# 4. PathogenMatrixBuilder – Matriz antipatógeno (conceitual)
# =============================================================================

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
    logging.info(f"\nConstruindo matriz antipatógeno para '{target_pathogen}'...\n")
    log_event_jsonl("M41.1", "INFO", "MATRIX_BUILD_START", {"target": target_pathogen, "species": species})

    if dna_analysis_result.ethical_alignment_score < ethical_threshold:
        msg = f"Alinhamento ético insuficiente ({dna_analysis_result.ethical_alignment_score:.2f})."
        logging.error(f"Falha na construção da matriz: {msg}")
        log_event_jsonl("M41.1", "ERROR", "MATRIX_BUILD_FAIL", {"target": target_pathogen, "reason": "ethical_non_compliance", "score": dna_analysis_result.ethical_alignment_score})
        raise ValueError("Alinhamento ético insuficiente para construir a matriz.")

    vibrational_signature = {
        "dominant_frequency_hz": dna_analysis_result.spectral_analysis.get("max_amplitude_freq", 0.0),
        "harmonic_offsets": {c: CODONS_COLOR_MAP_CACHE.get(c, {}).get('harmonic_offset', 0.0) for c in dna_analysis_result.codon_counts},
        "associated_chakras": dna_analysis_result.associated_chakras,
        "associated_cities_of_light": dna_analysis_result.associated_cities_of_light
    }

    fragments = [f"Fragmento_{c}_{i}" for i, c in enumerate(dna_analysis_result.sequence) if random.random() < 0.1]
    if not fragments:
        fragments.append(f"Fragmento_Base_{target_pathogen}")

    if CODONS_COLOR_MAP_CACHE:
        freqs = [v.get('freq_hz') for v in CODONS_COLOR_MAP_CACHE.values() if v.get('freq_hz') is not None]
        if freqs:
            min_freq = min(freqs)
            max_freq = max(freqs)
            frequency_band_range = (min_freq * 0.9, max_freq * 1.1)
        else:
            frequency_band_range = (0.0, 1000.0)
            logging.warning("Nenhuma frequência válida no cache. Usando faixa padrão.")
            log_event_jsonl("M41.1", "WARNING", "EMPTY_CODON_CACHE_FREQS", {"reason": "freq_range_default"})
    else:
        frequency_band_range = (0.0, 1000.0)
        logging.warning("Cache de códons vazio. Usando faixa padrão.")
        log_event_jsonl("M41.1", "WARNING", "EMPTY_CODON_CACHE", {"reason": "freq_range_default"})

    matrix_id = f"APM-{hashlib.sha256(target_pathogen.encode()).hexdigest()[:10]}"
    log_event_jsonl("M41.1", "INFO", "MATRIX_BUILD_COMPLETE", {"matrix_id": matrix_id, "target": target_pathogen, "status": "created"})

    return PathogenMatrix(
        matrix_id=matrix_id,
        target_pathogen=target_pathogen,
        vibrational_signature=vibrational_signature,
        molecular_structure_fragments=fragments,
        frequency_band_range=frequency_band_range,
        ethical_compliance=dna_analysis_result.ethical_alignment_score,
        creation_timestamp=datetime.utcnow().isoformat() + "Z",
        status="ATIVA",
        associated_modules=["M16", "M24", "M41.1", "M109", "M149"]
    )

# =============================================================================
# 5. HealingManualGenerator – Geração de manuais de cura quântica
# =============================================================================

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
    ethical_threshold: float = 0.65
) -> HealingManual:
    logging.info(f"\nGerando manual de cura para '{target_entity}'...\n")
    log_event_jsonl("M41.1", "INFO", "HEALING_MANUAL_GEN_START", {"target": target_entity})

    if gene_analysis_result.ethical_alignment_score < ethical_threshold:
        msg = f"Alinhamento ético insuficiente ({gene_analysis_result.ethical_alignment_score:.2f})."
        logging.error(f"Falha na geração do manual: {msg}")
        log_event_jsonl("M41.1", "ERROR", "HEALING_MANUAL_GEN_FAIL", {"target": target_entity, "reason": "ethical_non_compliance", "score": gene_analysis_result.ethical_alignment_score})
        raise ValueError("Alinhamento ético insuficiente para gerar o manual de cura.")

    description = f"Manual de Cura Quântica para {target_entity}, baseado em análise genômica e vibracional."
    recommended_protocols: List[Dict[str, Any]] = []

    if gene_analysis_result.associated_chakras:
        recommended_protocols.append({
            "name": "Protocolo de Realinhamento Vibracional de Chakras",
            "description": f"Foco nos chakras: {', '.join(gene_analysis_result.associated_chakras)}.",
            "instruments": gene_analysis_result.potential_instruments.get("reparacao", []),
            "duration_cycles": "Variável, conforme resposta vibracional",
            "modules_involved": ["M8", "M24", "M28", "M108"]
        })

    if gene_analysis_result.spectral_analysis.get("total_spectral_energy", 0) > 0.5:
        recommended_protocols.append({
            "name": "Protocolo de Ativação de Potenciais Divinos",
            "description": "Ativação de códons de iniciação e expansão de consciência.",
            "instruments": gene_analysis_result.potential_instruments.get("ativacao", []),
            "duration_cycles": "Contínuo, com monitoramento de ressonância",
            "modules_involved": ["M40", "M106", "M151"]
        })

    if pathogen_matrix:
        recommended_protocols.append({
            "name": f"Protocolo Antipatógeno para {pathogen_matrix.target_pathogen}",
            "description": f"Aplicação da matriz {pathogen_matrix.matrix_id} para neutralização vibracional.",
            "instruments": ["Feixe de Frequência Coerente", "Campo de Ressonância"],
            "duration_cycles": "Até a dissolução da dissonância",
            "modules_involved": ["M16", "M24", "M41.1", "M109", "M149"]
        })

    if gene_analysis_result.associated_cities_of_light:
        recommended_protocols.append({
            "name": "Protocolo de Reconexão de Linhagens Estelares",
            "description": f"Reconexão com origens estelares: {', '.join(gene_analysis_result.associated_cities_of_light)}.",
            "instruments": gene_analysis_result.potential_instruments.get("reparacao", []),
            "duration_cycles": "Ciclos de meditação e ativação de memória celular",
            "modules_involved": ["M40", "M109", "M148"]
        })

    manual_id = f"QHM-{hashlib.sha256(target_entity.encode()).hexdigest()[:10]}"
    log_event_jsonl("M41.1", "INFO", "HEALING_MANUAL_GEN_COMPLETE", {"manual_id": manual_id, "target": target_entity, "status": "generated"})

    return HealingManual(
        manual_id=manual_id,
        target_entity=target_entity,
        description=description,
        recommended_protocols=recommended_protocols,
        ethical_review_score=gene_analysis_result.ethical_alignment_score,
        generation_timestamp=datetime.utcnow().isoformat() + "Z",
        status="PRONTO PARA APLICAÇÃO",
        associated_modules=["M41.1", "M8", "M24", "M28", "M109", "M147"]
    )

# =============================================================================
# 6. Fluxo principal de execução (Main)
# =============================================================================

def main(species: str = "humano", gene_sequence: Optional[str] = None, target_pathogen: Optional[str] = None):
    _verify_quantum_protection()
    ensure_species_config(species)

    if not load_species_config(species):
        logging.critical(f"Falha crítica ao carregar configs para '{species}'.")
        log_event_jsonl("M41.1", "CRITICAL", "MAIN_SPECIES_CONFIG_LOAD_FAIL", {"species": species})
        return

    refine_species(species)  # garante mapa refinado

    if gene_sequence is None:
        if species == "humano":
            gene_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTACGATC"
        else:
            logging.error("Sequência de gene não fornecida e sem padrão.")
            log_event_jsonl("M41.1", "ERROR", "MAIN_EXEC_FAIL", {"reason": "no_gene_sequence", "species": species})
            return

    # 1. Analisar gene
    try:
        gene_analysis = analyze_gene("GENE-EXEMPLO", gene_sequence, species)
        logging.info(f"Análise do Gene Concluída: {gene_analysis}")
        log_event_jsonl("M41.1", "INFO", "MAIN_GENE_ANALYSIS_RESULT", {"result": gene_analysis.__dict__})
    except ValueError as e:
        logging.critical(f"Erro na análise do gene: {e}")
        log_event_jsonl("M41.1", "CRITICAL", "MAIN_GENE_ANALYSIS_ERROR", {"error": str(e)})
        return

    # 2. Construir matriz antipatógeno (opcional)
    pathogen_matrix_result = None
    if target_pathogen:
        try:
            pathogen_matrix_result = build_antipathogen_matrix(target_pathogen, gene_analysis, species=species)
            logging.info(f"Matriz Antipatógeno Construída: {pathogen_matrix_result}")
            log_event_jsonl("M41.1", "INFO", "MAIN_PATHOGEN_MATRIX_RESULT", {"result": pathogen_matrix_result.__dict__})
        except ValueError as e:
            logging.error(f"Erro na construção da matriz antipatógeno: {e}")
            log_event_jsonl("M41.1", "ERROR", "MAIN_PATHOGEN_MATRIX_ERROR", {"error": str(e)})
    else:
        logging.info("Nenhum patógeno alvo fornecido. Pulando matriz antipatógeno.")
        log_event_jsonl("M41.1", "INFO", "MAIN_PATHOGEN_MATRIX_SKIPPED", {"reason": "no_target_pathogen"})

    # 3. Gerar manual de cura
    try:
        healing_manual = generate_healing_manual("Entidade Alvo Exemplo", gene_analysis, pathogen_matrix_result)
        logging.info(f"Manual de Cura Gerado: {healing_manual}")
        log_event_jsonl("M41.1", "INFO", "MAIN_HEALING_MANUAL_RESULT", {"result": healing_manual.__dict__})
    except ValueError as e:
        logging.critical(f"Erro na geração do manual de cura: {e}")
        log_event_jsonl("M41.1", "CRITICAL", "MAIN_HEALING_MANUAL_ERROR", {"error": str(e)})
        return

    logging.info("\n=== Módulo 41.1 Execução Concluída com Sucesso ===")
    log_event_jsonl("M41.1", "INFO", "MAIN_EXEC_COMPLETE", {"status": "success"})

# =============================================================================
# Execução via CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Módulo 41.1: Manual de Cura Quântica e Alinhamento Genômico")
    parser.add_argument("--species", type=str, default="humano", help="Espécie a ser configurada (ex: humano)")
    parser.add_argument("--gene_sequence", type=str, help="Sequência de DNA para análise (opcional)")
    parser.add_argument("--target_pathogen", type=str, help="Patógeno alvo para matriz (opcional)")
    args, unknown = parser.parse_known_args()
    if unknown:
        logging.warning(f"Argumentos desconhecidos ignorados: {unknown}")
    main(species=args.species, gene_sequence=args.gene_sequence, target_pathogen=args.target_pathogen)
