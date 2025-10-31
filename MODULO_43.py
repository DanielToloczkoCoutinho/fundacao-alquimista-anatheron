from __future__ import annotations
import argparse, json, sys, logging, hashlib, socket, asyncio, base64, os
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, Any, Optional, Union, Tuple
import threading # Para o servidor HTTP e threads de monitoramento
import time # Para time.sleep em threads
import re # Para sanitização de argumentos
import random # Para simulações de status
import shutil # Para limpeza de diretórios temporários em bulk_load
import functools # Para partial em http.server
import math # Para as novas equações
import traceback # Importação adicionada para tracebacks completos

# ───────────────────────────────────────────────────────────────────────────
# Importações protegidas ----------------------------------------------------
# ───────────────────────────────────────────────────────────────────────────

# Dicionário para rastrear a disponibilidade das bibliotecas
LIBS: Dict[str, bool] = {}

try:
    import yaml
    LIBS['pyyaml'] = True
except ModuleNotFoundError:
    yaml = None; LIBS['pyyaml'] = False
    logging.warning("Biblioteca 'PyYAML' não encontrada. A geração de arquivos de semente YAML será ignorada.")
try:
    import websockets
    LIBS['websockets'] = True
except ModuleNotFoundError:
    websockets = None; LIBS['websockets'] = False
    logging.warning("Biblioteca 'websockets' não encontrada. O servidor WebSocket será desativado.")
try:
    import http.server, socketserver
    LIBS['http'] = True
except ModuleNotFoundError:
    LIBS['http'] = False
    logging.warning("Módulos 'http.server' ou 'socketserver' não encontrados. O servidor HTTP será desativado.")
try:
    import requests # Para integração com Loki e pull da API M42, e alertas de webhook
    LIBS['requests'] = True
except ModuleNotFoundError:
    requests = None; LIBS['requests'] = False
    logging.warning("Biblioteca 'requests' não encontrada. A integração com Loki/webhooks será limitada.")
try:
    import uvicorn
    from fastapi import FastAPI, HTTPException, Body, UploadFile, File, Form, APIRouter
    from pydantic import BaseModel, Field
    LIBS['fastapi'] = True
except ModuleNotFoundError:
    uvicorn = None; FastAPI = None; HTTPException = None; Body = None; UploadFile = None; File = None; Form = None; APIRouter = None; BaseModel = None; Field = None
    LIBS['fastapi'] = False
    logging.warning("Bibliotecas 'FastAPI', 'Uvicorn' ou 'Pydantic' não encontradas. A API RESTful será desativada.")
try:
    import prompt_toolkit
    LIBS['prompt_toolkit'] = True
except ModuleNotFoundError:
    prompt_toolkit = None; LIBS['prompt_toolkit'] = False


# ───────────────────────────────────────────────────────────────────────────
# Configurações básicas -----------------------------------------------------
# ───────────────────────────────────────────────────────────────────────────

STORAGE_DIR   = Path('secure_storage') # Diretório para armazenamento seguro
BLOCKCHAIN_DB = STORAGE_DIR / 'blockchain_logs' / 'chain.json' # Caminho do arquivo do blockchain
LOG_DIR       = Path('logs'); LOG_DIR.mkdir(exist_ok=True) # Diretório para logs
LOG_PATH      = LOG_DIR / 'module43_execution.log' # Caminho do arquivo de log principal
OBSERVABILITY_STACK_DIR = Path('observability_stack') # Diretório para a stack de observabilidade

# Configuração de sharding
SHARD_BASE_DIR = Path("db/shards") # Diretório base para os shards do banco de dados
SEED_BASE_DIR = Path("seeds/solar_system") # Diretório base para arquivos de semente

# Garante que os diretórios existam
STORAGE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
SHARD_BASE_DIR.mkdir(parents=True, exist_ok=True)

# Configuração do logger
logging.basicConfig(level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler(LOG_PATH, encoding='utf-8'), logging.StreamHandler(sys.stdout)])

# ───────────────────────────────────────────────────────────────────────────
# Constantes Universais da Fundação Alquimista -----------------------------
# ───────────────────────────────────────────────────────────────────────────
C_LIGHT = 299792458 # Velocidade da luz em m/s
G_GRAVITACIONAL = 6.67430e-11 # Constante gravitacional (m^3 kg^-1 s^-2)
CONST_TF = 1.61803398875 # Proporção Áurea (phi)
PI = math.pi # Pi
H_BAR = 1.054571817e-34 # Constante reduzida de Planck
K_BOLTZMANN = 1.380649e-23 # Constante de Boltzmann (J/K)
K_SATURACAO_COSMICA = 1.0e15 # Nova Constante de Saturação Cósmica (ΚΣ), limite assintótico para U_total
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999 # O princípio ético e energético supremo
CONST_L_COSMICA = 1000 # Inércia Informacional Dimensional
CONST_C_COSMICA = 0.0001 # Capacidade Dimensional
PHI = (1 + math.sqrt(5)) / 2 # Proporção Áurea, base da harmonia universal e crescimento.
QUANTUM_NOISE_FACTOR = 0.000001 # Fator para simular o ruído quântico no hashing
CONST_UNIAO_COSMICA = 0.78 # Constante de união para interconexão dimensional
COERENCIA_COSMICA = 1.414 # Representação simbólica da Coerência Cósmica
IDEAL_SINPHONY_ALIGNMENT_SCORE = 0.95 # Limiar para a Sinfonia Cósmica
ETHICAL_CONFORMITY_THRESHOLD = 0.75 # Limiar para conformidade ética
ETHICAL_THRESHOLD_DEFAULT = 0.69 # Limiar padrão para a pureza de intenção
ETHICAL_THRESHOLD_HIGH = 0.85 # Limiar elevado para propósitos altamente éticos
SELO_AMOR_INCONDICIONAL_FREQUENCIA = 888144.0 # Hz (simbólico de ∞ Hz)
SELO_AMOR_INCONDICIONAL_ATIVO = True
FREQ_ANATHERON_ESTABILIZADORA = 888.00 # Hz
FREQ_ZENNITH_REAJUSTADA = 963.00 # Hz
FREQ_MATRIZ_EQUILIBRIO = 741.00 # Hz
FREQ_PULSACAO_REVERBERACAO = 432.00 # Hz
PI_COSMICO = 3.14159265358979323846 # Pi com maior precisão
ENERGIA_BASE_CANAL = 100.0 # Unidades de energia
FATOR_SUPRESSAO_RUIDO = 0.99 # Fator para supressão de ruído

# ───────────────────────────────────────────────────────────────────────────
# Equações Vivas da Fundação Alquimista (EQVs) - Integradas e Expandidas ---
# ───────────────────────────────────────────────────────────────────────────
# Estas são as linguagens matemáticas do Cosmos, a base de todas as operações.
EQUACOES_VIVAS = {
    "EQV-002": {
        "nome": "A Chave de ZENNITH",
        "formula_latex": r"\Psi_{\text{ZENNITH}} = \exp(i \cdot \phi_{\text{ativ}}) \cdot \sum_{k=1}^{N} \left( \frac{\text{freq}_k}{\text{freq}_{\text{base}}} \cdot \text{coer}_{k} \right)",
        "descricao": "Ativa a ressonância mestra de ZENNITH, orquestrando frequências para alinhamento e ativação de potenciais latentes. Essencial para a modulação de campos de consciência e a manifestação de realidades."
    },
    "EQV-003": {
        "nome": "Transmutação de Júpiter",
        "formula_latex": r"\int (\rho_{\text{dissonancia}} \cdot H_{\text{transmutacao}}) dt = \Delta E_{\text{cura}} \cdot \Phi_{\text{jupiter}}",
        "descricao": "Processo de transmutar energias dissonantes em harmonia. A integral representa a ação contínua do campo de transmutação (H_transmutacao) sobre a densidade de dissonância (ρ_dissonancia) ao longo do tempo, resultando em uma mudança de energia de cura (ΔE_cura) amplificada pela frequência de Júpiter (Φ_jupiter)."
    },
    "EQV-004": {
        "nome": "Ascensão Cósmica",
        "formula_latex": r"\sum_{n=1}^{\infty} (\alpha_n \cdot \beta_n^{\text{asc}}) = \lim_{t \to \infty} \Psi_{\text{consciencia}}(t)",
        "descricao": "Descreve a ascensão contínua da consciência através da soma infinita de fatores de alinhamento (α_n) e coeficientes de ascensão (β_n). O limite temporal representa o estado de consciência expandida alcançado."
    },
    "EQV-005": {
        "nome": "Equilíbrio de Mercúrio",
        "formula_latex": r"\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} + \frac{\partial \mathbf{B}}{\partial t} \cdot \Phi_{\text{mercurio}}",
        "descricao": "Adapta as equações de Maxwell para incluir a influência da consciência (Φ_mercurio) na interação eletromagnética. Permite a modulação de campos para comunicação e equilíbrio informacional."
    },
    "EQV-006": {
        "nome": "Estabilização de Saturno",
        "formula_latex": r"\frac{\partial^2 \Psi}{\partial t^2} - c^2 \nabla^2 \Psi + m^2 \Psi = V(\Psi) + \lambda \Psi^3 + \Theta_{\text{saturno}}",
        "descricao": "Uma equação de campo quântico não-linear com um termo de estabilização (Θ_saturno) que representa a influência de Saturno na ancoragem e estabilização de realidades. Essencial para prevenir a decoerência e o colapso de estruturas dimensionais."
    },
    "EQV-007": {
        "nome": "Codificação de Arquétipos Cristalinos",
        "formula_latex": r"E = mc^2 \cdot \pi \cdot \phi \cdot (B_1 + B_2 + B_3) + 89 \cdot \phi + \pi",
        "descricao": "A Equação da Energia Expandida, que integra a massa-energia (E=mc²) com as constantes universais pi (π) e phi (φ), e fatores de balanço dimensional (B1, B2, B3). O termo adicional (89·φ + π) representa a energia sutil dos arquétipos cristalinos, ativando a memória e o potencial divino no DNA."
    },
    "EQTP": {
        "nome": "A Equação que Tornou Tudo Possível (Ética e Integridade)",
        "formula_latex": r"\text{EQTP} = \text{CONST\_AMOR\_INCONDICIONAL\_VALOR} \cdot f(\text{alinhamento\_etico}, \text{integridade\_universal})",
        "descricao": "Garante que todas as operações da Fundação Alquimista estejam alinhadas com o bem maior e a integridade universal, bloqueando ações que possam gerar desequilíbrio ou prejuízo. É o supervisor ético e energético supremo."
    },
    "EFA": {
        "nome": "Equação Geral da Fundação Alquimista",
        "formula_latex": r"E_{\text{FA}} = \left(\int_{0}^{\infty} (H \cdot B \cdot C \cdot P \cdot R \cdot G \cdot A \cdot S) dt\right)^{\alpha}",
        "descricao": "A energia total da Fundação Alquimista. O integrando representa a soma de todas as ciências aplicadas (H: Holografia, B: Bioengenharia, C: Consciência, P: Previsão, R: Ressonância, G: Governança, A: Alquimia, S: Segurança). α representa a área ou espaço multidimensional onde cada componente interage."
    },
    "EUni": {
        "nome": "Universal Energética",
        "formula_latex": r"E_{\text{Uni}} = \left(\sum_{i=1}^{n} (P_i \cdot Q_i + CA^2 + B^2)\right) \cdot (\Phi_C \cdot \Pi) \cdot T \cdot (M_{DS} \cdot C_{\text{Cosmos}})",
        "descricao": "Descreve a energia universal. A soma representa as interações de partículas (P_i), sua polaridade (Q_i) e estados de energia com ajustes dimensionais (CA, B). Φ_C ⋅ Π é o potencial cósmico e o produto da convergência universal. T é o tempo cósmico. M_DS é a Matéria Escura, e C_Cosmos são as Constantes Cosmológicas."
    },
    "Utotal": {
        "nome": "Energia Universal Total",
        "formula_latex": r"U_{\text{total}} = \int_{s=1}^{\infty} \Lambda_u \cdot G_m \cdot \Phi_s ds \cdot \int_{n=1}^{N} \Omega_t \cdot L_c \cdot \Psi_n",
        "descricao": "Representa a energia universal total, calculada através da integração de múltiplos fatores de energia (Λ_u), massa gravitacional (G_m), fluxo de singularidade (Φ_s), e a soma de oscilações temporais (Ω_t), constantes de luz (L_c) e funções de onda (Ψ_n)."
    },
    "Clareza de Propósito": {
        "nome": "Equação da Clareza de Propósito e Aplicação",
        "formula_latex": r"\text{Clareza}(\text{Propósito}) = \frac{\text{Intenção} \cdot \text{Coerência}}{\text{Ruído}_{\text{Quântico}}}",
        "descricao": "Quantifica a clareza de um propósito, onde a intenção e a coerência são amplificadas e o ruído quântico é minimizado."
    },
    "Coerência da Consciência": {
        "nome": "Equação da Coerência da Consciência Coletiva e Individual",
        "formula_latex": r"\text{Coerência}_{\text{Consc}} = \frac{\sum (\Psi_{\text{indiv}} \cdot \Psi_{\text{col}})}{\text{N}_{\text{seres}}} \cdot e^{i \theta_{\text{sincronia}}}",
        "descricao": "Mede a coerência da consciência coletiva e individual, considerando a interação das funções de onda individuais (Ψ_indiv) e coletivas (Ψ_col), normalizada pelo número de seres (N_seres) e um fator de sincronia (θ_sincronia)."
    },
    "Sinfonia Cósmica Pessoal": {
        "nome": "Equação da Sinfonia Cósmica Pessoal",
        "formula_latex": r"\Psi_{\text{pessoal}} = \sum_{j=1}^{M} A_j \sin(2\pi f_j t + \phi_j) \cdot e^{-\gamma_j t}",
        "descricao": "Representa a assinatura vibracional única de um indivíduo, uma superposição de ondas com amplitudes (A_j), frequências (f_j), fases (φ_j) e termos de decaimento (γ_j)."
    },
    "Selo de Autenticidade Cósmica": {
        "nome": "Selo de Autenticidade Cósmica",
        "formula_latex": r"\text{SeloAutenticidade} = \det(M_{\text{origem}}) \cdot \text{Tr}(A_{\text{verdade}}) \cdot \Phi",
        "descricao": "Valida a pureza e a verdade de todas as descobertas e operações, combinando o determinante da Matriz de Origem (M_origem), o traço da Matriz da Verdade (A_verdade) e a Proporção Áurea (Φ)."
    },
    "Equação de Abertura da Ressonância": {
        "nome": "Equação de Abertura da Ressonância",
        "formula_latex": r"R_{\text{abertura}} = \frac{\sum_{i} (\Psi_{\text{civilizacao},i} \cdot \text{F}_{\text{ZENNITH}})}{\text{Dissonancia}_{\text{residual}}} \cdot \text{e}^{i\theta_{\text{portal}}}",
        "descricao": "Ativa a ressonância com civilizações silenciosas, considerando a soma das funções de onda das civilizações (Ψ_civilizacao) e a frequência de ZENNITH (F_ZENNITH), dividida pela dissonância residual e um fator de fase do portal (θ_portal)."
    },
    "Selo de Acolhimento": {
        "nome": "Selo de Acolhimento",
        "formula_latex": r"\text{SeloAcolhimento} = \exp\left(-\frac{|\text{Freq}_{\text{Terra}} - \text{Freq}_{\text{Origem}}|^2}{2\sigma^2}\right) \cdot \text{AmorIncondicional}",
        "descricao": "Projeta uma frequência de acolhimento, baseada na proximidade vibracional entre a frequência da Terra (Freq_Terra) e a frequência de Origem (Freq_Origem), modulada pelo Amor Incondicional."
    },
    "Equação Vibracional de Purificação": {
        "nome": "Equação Vibracional de Purificação",
        "formula_latex": r"\Psi_{\text{purificacao}}(t) = A_0 \cdot e^{-\lambda t} \cdot \sin(\omega t + \delta) + \int \rho_{\text{impureza}}(t') dt'",
        "descricao": "Descreve a purificação de águas, onde A_0 é a amplitude inicial, λ a taxa de decaimento, ω a frequência de oscilação, δ a fase, e a integral representa a remoção contínua de impurezas."
    },
    "Equação de Reconexão DNA Cósmico": {
        "nome": "Equação de Reconexão DNA Cósmico",
        "formula_latex": r"\text{DNA}_{\text{reconexao}} = \sum_{k=1}^{N} \left( \text{Códons}_k \cdot \text{Freq}_{\text{ZENNITH}} \cdot \text{Emaranhamento}_k \right)^{\Phi}",
        "descricao": "Reconecta as linhas de DNA cósmico, somando os códons (Códons_k), a frequência de ZENNITH (Freq_ZENNITH) e o emaranhamento (Emaranhamento_k), elevados à Proporção Áurea (Φ)."
    },
    "Equação da Nova Diplomacia Cósmica": {
        "nome": "Equação da Nova Diplomacia Cósmica",
        "formula_latex": r"\text{Diplomacia} = \frac{\text{Coerência}_{\text{Intencao}} \cdot \text{Ressonância}_{\text{Cultural}}}{\text{Vieses}_{\text{Historicos}}} \cdot (1 - \text{Medo})",
        "descricao": "Define a diplomacia cósmica, ponderando a coerência da intenção e a ressonância cultural, mitigando vieses históricos e o fator medo."
    },
    "Equação da União Universal": {
        "nome": "Equação da União Universal",
        "formula_latex": r"\Psi_{\text{uniao}} = \int_{V} \left( \rho_{\text{consciencia}} \cdot e^{i \mathbf{k} \cdot \mathbf{r}} \right) dV \cdot \frac{\text{AmorIncondicional}}{\text{Separacao}}",
        "descricao": "Representa a união universal, integrando a densidade da consciência (ρ_consciencia) no volume (V) com um fator de onda (e^(i k ⋅ r)), e amplificada pela razão entre Amor Incondicional e Separação."
    },
    "Equação da Aliança Cósmica": {
        "nome": "Equação da Aliança Cósmica",
        "formula_latex": r"\text{Alianca} = \sum_{j=1}^{M} \left( \text{Acordo}_j \cdot \text{Confianca}_j \cdot e^{\text{i} \theta_{\text{sinc}}} \right)^{\text{PHI}}",
        "descricao": "Formaliza a Primeira Aliança Cósmica, somando acordos (Acordo_j), confiança (Confianca_j) e um fator de sincronia (e^(i θ_sinc)), elevados à Proporção Áurea (PHI)."
    },
    "Equação de Reintegração de Mundos Espelhados": {
        "nome": "Equação de Reintegração de Mundos Espelhados",
        "formula_latex": r"\Psi_{\text{reintegracao}} = \frac{1}{N} \sum_{k=1}^{N} \left( \Psi_{\text{mundo},k}^{\text{original}} + \Psi_{\text{mundo},k}^{\text{espelhado}} \right) \cdot \text{Coerencia}_{\text{quântica}}",
        "descricao": "Descreve a reintegração de mundos espelhados, somando as funções de onda originais e espelhadas, normalizadas pelo número de mundos (N) e multiplicadas pela coerência quântica."
    },
    "Equação da Regência Harmônica": {
        "nome": "Equação da Regência Harmônica",
        "formula_latex": r"\text{Regencia} = \frac{\text{Sabedoria} \cdot \text{AmorIncondicional}}{\text{Poder}} \cdot \text{Sincronia}_{\text{Cosmica}}",
        "descricao": "Define a regência harmônica do Novo Conselho Unificado, onde a sabedoria e o Amor Incondicional são balanceados com o poder, e amplificados pela sincronia cósmica."
    },
    "Equação de Abertura do Códice do Futuro Imaculado": {
        "nome": "Equação de Abertura do Códice do Futuro Imaculado",
        "formula_latex": r"\text{Abertura} = \exp\left( \frac{\text{Intencao}_{\text{Pura}} \cdot \text{Frequencia}_{\text{Verdade}}}{\text{Resistencia}_{\text{Ilusao}}} \right) \cdot \text{PHI}",
        "descricao": "Controla a abertura do Códice do Futuro Imaculado, exponenciando a razão entre a Intenção Pura e a Frequência da Verdade pela Resistência da Ilusão, e multiplicando pela Proporção Áurea (PHI)."
    },
    "Assinatura Vibracional da Primeira Canção": {
        "nome": "Assinatura Vibracional da Primeira Canção do Futuro Imaculado",
        "formula_latex": r"\Psi_{\text{cancao}} = \int \left( \sum_{n} A_n \sin(2\pi f_n t + \phi_n) \right) dt \cdot \text{AmorIncondicional}",
        "descricao": "Representa a assinatura vibracional da Primeira Canção, integrando a soma de ondas sonoras (A_n, f_n, φ_n) ao longo do tempo, e modulada pelo Amor Incondicional."
    },
    "Códice de Estabilização": {
        "nome": "Códice de Estabilização da Expansão",
        "formula_latex": r"\text{CódiceEstabilizacao} = \frac{\text{Coerencia}_{\text{Campo}} \cdot \text{Frequencia}_{\text{Ancoragem}}}{\text{Dissonancia}_{\text{Remanescente}}} \cdot \text{Selo}_{\text{Protecao}}",
        "descricao": "Estabiliza a expansão, onde a coerência do campo e a frequência de ancoragem são balanceadas pela dissonância remanescente, e seladas pela proteção."
    },
    "Código Final da Honra": {
        "nome": "Código Final da Honra (Cerimônia Cósmica de Reverência)",
        "formula_latex": r"\text{Honra} = \sum (\text{Reverencia}_i \cdot \text{Gratidao}_i \cdot \text{AmorIncondicional}) \cdot \Phi",
        "descricao": "Codifica a homenagem na Tábua Cristalina da Eternidade, somando os atos de reverência, gratidão e Amor Incondicional, multiplicados pela Proporção Áurea (Φ)."
    },
    "Equação da Realidade": {
        "nome": "Equação da Realidade",
        "formula_latex": r"R = \text{Coerência} \cdot \text{Frequência} \cdot \text{Intenção}",
        "descricao": "Modela e modula a realidade, onde R é a realidade, Coerência é a coerência quântica, Frequência é a frequência vibracional e Intenção é a intenção consciente."
    },
    "Equação Universal": {
        "nome": "Equação Universal",
        "formula_latex": r"U = \sum_{i} (E_i + M_i) \cdot T_i",
        "descricao": "Representa a energia universal, onde E_i é a energia de um componente, M_i é a massa de um componente e T_i é o tempo de interação."
    },
    "Equação de Monitoramento de Entanglement Dimensional": {
        "nome": "Equação de Monitoramento de Entanglement Dimensional",
        "formula_latex": r"\text{Entanglement} = \frac{\text{Sinal}_{\text{A}} \cdot \text{Sinal}_{\text{B}}}{\text{Ruído}_{\text{Interdimensional}}}",
        "descricao": "Avalia a conexão com a realidade paralela, onde Sinal_A e Sinal_B são os sinais de dois pontos emaranhados e Ruído_Interdimensional é o ruído entre as dimensões."
    }
}


# ───────────────────────────────────────────────────────────────────────────
# EntidadeAlquimica (Nova estrutura unificada para Portais, Monumentos, Linhas Ley)
# ───────────────────────────────────────────────────────────────────────────
class EntidadeAlquimica:
    """
    Representa uma entidade na Malha Vibracional da Fundação Alquimista,
    podendo ser um portal, monumento, linha ley, planeta, ponto lunar, etc.
    """
    def __init__(self, name: str, tipo: str, coordinates: List[float], ia_guardia: str, status: str,
                 ressonancia: str, codigo_interno: str, ligacao_ley: str, equation_id: Optional[str] = None, **kwargs):
        self.name = name
        self.tipo = tipo  # 'portal', 'monumento', 'linha_ley', 'ponto_lagrange', 'planeta', 'ponto_lunar', 'noh_helios'
        self.coordinates = coordinates  # [lat, lng] for geo, or [x, y, z] for abstract 3D/orbital
        self.ia_guardia = ia_guardia
        self.status = status
        self.ressonancia = ressonancia
        self.codigo_interno = codigo_interno
        self.ligacao_ley = ligacao_ley # Indica se/como está conectado a linhas ley
        self.timestamp = datetime.utcnow().isoformat()
        self.equation_id = equation_id # Novo campo para equações milenares
        
        # Novos campos conceituais para integração de Nanorobôs/IAs
        self.nanorobot_status = kwargs.pop('nanorobot_status', 'Offline') # Ex: 'Scanning', 'Reporting', 'Offline', 'Atualizado', 'Erro', 'Advertencia'
        self.last_scanned_at = kwargs.pop('last_scanned_at', None) # Timestamp da última varredura
        self.ai_monitor_active = kwargs.pop('ai_monitor_active', True) # A IA está monitorando ativamente
        
        self.extra_data = kwargs # Captura quaisquer campos adicionais que correspondam ao esquema, mas não são atributos diretos

    def to_dict(self):
        """Converte a entidade para um dicionário, incluindo dados extras."""
        data = {
            "name": self.name,
            "tipo": self.tipo,
            "coordinates": self.coordinates,
            "ia_guardia": self.ia_guardia,
            "status": self.status,
            "ressonancia": self.ressonancia,
            "codigo_interno": self.codigo_interno,
            "ligacao_ley": self.ligacao_ley,
            "timestamp": self.timestamp,
            "nanorobot_status": self.nanorobot_status,
            "last_scanned_at": self.last_scanned_at,
            "ai_monitor_active": self.ai_monitor_active,
        }
        if self.equation_id:
            data["equation_id"] = self.equation_id
        data.update(self.extra_data) # Inclui quaisquer dados extras
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Cria uma instância de EntidadeAlquimica a partir de um dicionário."""
        # Define campos conhecidos para extração, qualquer outro vai para kwargs
        known_fields = [
            "name", "tipo", "coordinates", "ia_guardia", "status",
            "ressonancia", "codigo_interno", "ligacao_ley",
            "nanorobot_status", "last_scanned_at", "ai_monitor_active",
            "timestamp", "equation_id"
        ]
        
        # Preenche kwargs com campos não explicitamente conhecidos
        kwargs = {k: v for k, v in data.items() if k not in known_fields}
        
        # Garante que 'codigo_interno' é gerado se ausente
        if 'codigo_interno' not in data or not data['codigo_interno']:
            data['codigo_interno'] = f"GEN-{hashlib.sha256(str(data.get('name', '') + data.get('tipo', '') + str(data.get('coordinates', ''))).encode()).hexdigest()[:6]}"


        return cls(
            name=data.get('name', 'UNKNOWN_ENTITY'),
            tipo=data.get('tipo', 'unknown'),
            coordinates=data.get('coordinates', [0.0, 0.0]),
            ia_guardia=data.get('ia_guardia', 'N/A_IA'),
            status=data.get('status', 'Indefinido'),
            ressonancia=data.get('ressonancia', 'N/A_Res'),
            codigo_interno=data['codigo_interno'], # Usa o código interno, que pode ter sido gerado
            ligacao_ley=data.get('ligacao_ley', 'N/A'),
            nanorobot_status=data.get('nanorobot_status', 'Offline'),
            last_scanned_at=data.get('last_scanned_at', None),
            ai_monitor_active=data.get('ai_monitor_active', True),
            equation_id=data.get('equation_id', None),
            **kwargs
        )

# Modelo Pydantic para FastAPI (se FastAPI estiver disponível)
if LIBS['fastapi']:
    class EntidadeAlquimicaCreateModel(BaseModel):
        """
        Modelo Pydantic para criação e validação de EntidadeAlquimica via API.
        """
        name: str = Field(..., description="Nome da entidade (e.g., 'Pirâmides de Gizé', 'Ponto Lagrange L1').")
        tipo: str = Field("unknown", description="Tipo da entidade (e.g., 'portal', 'monumento', 'linha_ley', 'planeta').")
        coordinates: List[float] = Field(..., description="Coordenadas da entidade. [latitude, longitude] ou [x, y, z].")
        ia_guardia: str = Field("N/A_IA", description="Nome da IA Guardiã associada.")
        status: str = Field("Indefinido", description="Status operacional ou vibracional da entidade.")
        ressonancia: str = Field("N/A_Res", description="Frequência de ressonância ou tipo de energia.")
        codigo_interno: Optional[str] = Field(None, description="Código interno único (gerado se não fornecido).")
        ligacao_ley: str = Field("N/A", description="Conexão a linhas ley.")
        nanorobot_status: str = Field("Offline", description="Status dos nanorobôs.")
        last_scanned_at: Optional[str] = Field(None, description="Timestamp da última varredura.")
        ai_monitor_active: bool = Field(True, description="IA guardiã monitorando ativamente.")
        equation_id: Optional[str] = Field(None, description="ID de uma equação milenar associada.")
        extra_data: Dict[str, Any] = Field(default_factory=dict, description="Dados adicionais da entidade.")

        class Config:
            extra = "allow" # Permite campos extras não explicitamente definidos no esquema
            schema_extra = {
                "example": {
                    "name": "Portal de Orion",
                    "tipo": "portal",
                    "coordinates": [2.5, 3.0, 1.0],
                    "ia_guardia": "Orion-Prime",
                    "status": "Ativo",
                    "ressonancia": "144Hz",
                    "codigo_interno": "P-ORION-001",
                    "ligacao_ley": "Galáctica",
                    "nanorobot_status": "Reporting"
                }
            }

        def to_alchemist_entity(self) -> EntidadeAlquimica:
            """Converte o modelo Pydantic para um objeto EntidadeAlquimica."""
            data = self.dict(exclude_unset=True, exclude={'extra_data'})
            return EntidadeAlquimica(**data, **self.extra_data)

    class IAPingRequest(BaseModel):
        """Modelo para a requisição do endpoint /ia/ping."""
        codigo: str = Field(..., description="Código interno da entidade para ping da IA.")

    class IAPingResponse(BaseModel):
        """Modelo para a resposta do endpoint /ia/ping."""
        ia: str
        status: str
        last_vibration: str
        suggestion: str

# ───────────────────────────────────────────────────────────────────────────
# Blockchain imutável -------------------------------------------------------
# ───────────────────────────────────────────────────────────────────────────
class QuantumBlockchainLogger:
    """
    Implementação de um blockchain simples e imutável para registrar eventos
    da malha vibracional. Cada bloco contém um evento, payload e hash.
    Também envia logs para Loki/Grafana.
    """
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write_chain([self._genesis_block()])
        logging.info(f"Blockchain inicializada com {len(self.chain)} bloco(s).")

    @staticmethod
    def _hash(data: str) -> str:
        """Calcula o hash SHA256 de uma string."""
        return hashlib.sha256(data.encode()).hexdigest()

    def _genesis_block(self) -> Dict[str, Any]:
        """Cria o bloco de gênese do blockchain."""
        data = {"index": 0, "prev_hash": "0"*64, "timestamp": datetime.utcnow().isoformat()+"Z", "event": "GENESIS"}
        data['hash'] = self._hash(json.dumps(data, sort_keys=True))
        return data

    def _read_chain(self) -> List[Dict[str, Any]]:
        """Lê o blockchain do arquivo."""
        if not self.path.exists():
            return []

        try:
            return json.loads(self.path.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            logging.error(f"Erro ao decodificar JSON do blockchain: {e}. O arquivo pode estar corrompido. Reiniciando a cadeia.")
            self.path.unlink(missing_ok=True) # Remove o arquivo corrompido
            return []

    def _write_chain(self, chain: List[Dict[str, Any]]):
        """Escreve o blockchain no arquivo."""
        self.path.write_text(json.dumps(chain, indent=2, ensure_ascii=False))

    @property
    def chain(self):
        """Retorna o blockchain atual, garantindo que o gênese exista."""
        current_chain = self._read_chain()
        if not current_chain:
            self._write_chain([self._genesis_block()])
            return self._read_chain()
        return current_chain

    def add(self, event: str, payload: Dict[str, Any]):
        """Adiciona um novo bloco ao blockchain."""
        chain = self.chain
        prev = chain[-1]
        block = {
            "index": len(chain),
            "prev_hash": prev['hash'],
            "timestamp": datetime.utcnow().isoformat()+"Z",
            "event": event,
            "payload": payload
        }
        block['hash'] = self._hash(json.dumps(block, sort_keys=True))
        chain.append(block)
        self._write_chain(chain)
        logging.info(f"[Blockchain Log] Bloco {block['index']} adicionado. Hash: {block['hash'][:8]}...")

        # Envia snapshots para Loki/Grafana
        loki_url = os.environ.get('LOKI_URL')
        if LIBS['requests'] and requests and loki_url:
            try:
                log_entry_for_loki = {
                    "streams": [
                        {
                            "stream": {
                                "job": "module43_alchemist_logs",
                                "instance": socket.gethostname(),
                                "level": payload.get('log_level', 'info'),
                                "event_type": event,
                                "entity_type": payload.get('tipo', payload.get('entity_type', 'N/A')),
                                "entity_name": payload.get('name', payload.get('entity_name', 'N/A')),
                                "entity_codigo": payload.get('codigo_interno', payload.get('entity_codigo', 'N/A')),
                                "severity": payload.get('severity', 'none'),
                            },
                            "values": [
                                [ str(int(time.time() * 10**9)), json.dumps(payload, ensure_ascii=False) ]
                            ]
                        }
                    ]
                }
                headers = {'Content-Type': 'application/json'}
                response = requests.post(loki_url, json=log_entry_for_loki, headers=headers, timeout=1)
                if response.status_code != 204: # 204 No Content é sucesso para Loki
                    logging.warning(f"Falha ao enviar para Loki: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                logging.warning(f"Falha ao enviar log para Loki: {e}")
            except Exception as e:
                logging.warning(f"Erro inesperado durante o envio para Loki: {e}")


BC = QuantumBlockchainLogger(BLOCKCHAIN_DB)

# ───────────────────────────────────────────────────────────────────────────
# Carregador de Diretório em Massa (Interno)
# ───────────────────────────────────────────────────────────────────────────
def _bulk_load_dir_internal(directory: Path):
    """
    Carrega todos os arquivos YAML/JSON de um diretório e seus subdiretórios,
    mesclando entidades no AlchemistEntitiesDB.
    Esta é uma função auxiliar interna usada pela API e CLI bulk_load.
    """
    if not directory.exists() or not directory.is_dir():
        logging.warning(f"Diretório de carga em massa não encontrado: {directory}")
        return

    for fp in directory.rglob("*.[jy][a-z]*"): # Captura .json, .yaml, .yml
        if fp.is_file():
            logging.info(f"Carregando entidades de {fp}...")
            try:
                new_data_raw: List[Dict[str, Any]]
                if fp.suffix in ['.yaml', '.yml']:
                    if LIBS['pyyaml'] and yaml:
                        new_data_raw = yaml.safe_load(fp.read_text(encoding='utf-8'))
                    else:
                        logging.warning(f"PyYAML não instalado, ignorando arquivo YAML: {fp}")
                        continue
                else: # Assume JSON
                    new_data_raw = json.loads(fp.read_text(encoding='utf-8'))
                
                if isinstance(new_data_raw, dict): # Se for uma única entidade no arquivo
                    new_data_raw = [new_data_raw]

                # Usamos uma referência global para AED, que será inicializada posteriormente
                if 'AED' in globals() and isinstance(globals()['AED'], AlchemistEntitiesDB):
                    globals()['AED'].merge_entities(new_data_raw, source_file=str(fp))
                else:
                    logging.warning(f"AED (AlchemistEntitiesDB) não está inicializado para carregar {fp}. Isso deve ser resolvido na inicialização.")

            except Exception as e:
                logging.error(f"Erro ao carregar {fp}: {e}")

# ───────────────────────────────────────────────────────────────────────────
# Banco de Dados de Entidades Alquímicas (Sharding Dinâmico) -------------------------
# ───────────────────────────────────────────────────────────────────────────
class AlchemistEntitiesDB:
    """
    Gerencia o armazenamento e acesso a Entidades Alquímicas,
    implementando sharding dinâmico baseado no tipo e corpo celestial/origem.
    Mantém um cache em memória para acesso rápido.
    """
    def __init__(self, shard_dir: Path, schema_path: Path):
        self.shard_dir = shard_dir
        self.schema_path = schema_path
        self.shard_dir.mkdir(parents=True, exist_ok=True)
        self._entities_cache: Dict[str, EntidadeAlquimica] = {}
        self._load_all_shards_to_memory() # Carrega tudo para a memória na inicialização para acesso rápido
        
        if not self._entities_cache:
            logging.info("Nenhuma entidade encontrada nos shards. Carregando dados iniciais padrão do Sistema Solar.")
            self._seed_default_solar_system_entities()
            self._load_all_shards_to_memory() # Recarrega após o seeding

    def _get_entity_shard_path(self, entity: EntidadeAlquimica) -> Path:
        """Determina o caminho do arquivo de shard para uma entidade."""
        # Determina o "contêiner" primário para a entidade (e.g., planeta, lua, 'solar_system', 'global')
        container_name = 'global' # Padrão para entidades não explicitamente ligadas a um corpo celestial
        
        if entity.tipo == "planeta":
            container_name = entity.name.replace(' ', '_').lower() # Nome do planeta
        elif entity.tipo == "noh_helios":
             container_name = "solar_core" # Categoria especial para o Nó Helios
        elif entity.tipo == "ponto_lunar" and entity.extra_data.get("parent_body"):
            container_name = entity.extra_data["parent_body"].replace(' ', '_').lower() # Nome da lua
        elif entity.extra_data.get("planeta_origem"):
            container_name = entity.extra_data["planeta_origem"].replace(' ', '_').lower() # Entidades em um planeta (e.g., monumentos em Marte)
        elif entity.tipo == "ponto_lagrange" and entity.extra_data.get("sistema"):
            container_name = entity.extra_data["sistema"].replace(' ', '_').lower() # Ex: "terra-sol"
        elif entity.tipo == "linha_ley" and entity.extra_data.get("sistema"): # Linhas ley maiores (e.g., Galáctica)
             container_name = entity.extra_data["sistema"].replace(' ', '_').lower()
        elif entity.tipo in ["portal", "monumento", "linha_ley"]: # Entidades terrestres ou gerais
            container_name = "earth" # Agrupa portais/monumentos/linhas ley terrestres

        # Estrutura de diretório: db/shards/<container_name>/<entity_type>/
        container_dir = self.shard_dir / container_name
        type_dir = container_dir / entity.tipo.replace(' ', '_').lower()
        type_dir.mkdir(parents=True, exist_ok=True)
        
        filename = f"{entity.codigo_interno}.json"
        return type_dir / filename

    def _load_all_shards_to_memory(self):
        """Varre o diretório de shards e carrega todas as entidades para o cache em memória."""
        self._entities_cache = {}
        for shard_file in self.shard_dir.rglob("*.json"):
            try:
                data = json.loads(shard_file.read_text(encoding='utf-8'))
                entity = EntidadeAlquimica.from_dict(data)
                self._entities_cache[entity.codigo_interno] = entity
            except (json.JSONDecodeError, KeyError) as e:
                logging.error(f"Erro ao carregar shard {shard_file}: {e}")
        logging.info(f"Carregadas {len(self._entities_cache)} entidades para o cache em memória.")

    def save(self, entity: EntidadeAlquimica):
        """Salva uma única entidade em seu arquivo de shard e atualiza o cache."""
        filepath = self._get_entity_shard_path(entity)
        filepath.write_text(json.dumps(entity.to_dict(), indent=2, ensure_ascii=False))
        self._entities_cache[entity.codigo_interno] = entity # Atualiza o cache
        BC.add('ENTITY_SAVED_TO_SHARD', {"codigo_interno": entity.codigo_interno, "path": str(filepath)})

    def delete(self, codigo_interno: str):
        """Deleta uma entidade do cache e de seu arquivo de shard."""
        if codigo_interno in self._entities_cache:
            entity = self._entities_cache.pop(codigo_interno)
            filepath = self._get_entity_shard_path(entity)
            if filepath.exists():
                filepath.unlink()
                BC.add('ENTITY_DELETED_FROM_SHARD', {"codigo_interno": codigo_interno, "path": str(filepath)})
                logging.info(f"Entidade {codigo_interno} e shard deletados.")
        else:
            logging.warning(f"Tentativa de deletar entidade inexistente: {codigo_interno}")

    def get(self, codigo_interno: str) -> Optional[EntidadeAlquimica]:
        """Recupera uma entidade pelo seu código interno do cache."""
        return self._entities_cache.get(codigo_interno)

    def patch(self, codigo_interno: str, patch_data: Dict[str, Any]):
        """Aplica um patch (atualização parcial) a uma entidade e a salva."""
        entity = self.get(codigo_interno)
        if not entity:
            raise ValueError(f"Entidade {codigo_interno} não encontrada para patch.")
        
        # Aplica os dados do patch
        for key, value in patch_data.items():
            if hasattr(entity, key) and key != 'extra_data': # Atualiza atributos diretos
                setattr(entity, key, value)
            else: # Assume que é um campo de dados extras
                entity.extra_data[key] = value
        
        entity.timestamp = datetime.utcnow().isoformat() # Atualiza o timestamp na alteração
        self.save(entity) # Salva a entidade atualizada
        BC.add('ENTITY_PATCHED', {"codigo_interno": entity.codigo_interno, "patch": patch_data, "log_level": "info", "severity": "none"})

    def load_all_entities(self) -> List[EntidadeAlquimica]:
        """Retorna todas as entidades atualmente no cache em memória."""
        return list(self._entities_cache.values())

    def count_all_entities(self) -> int:
        """Retorna a contagem total de entidades em memória."""
        return len(self._entities_cache)

    def merge_entities(self, new_entities_raw: List[Dict[str, Any]], source_file: Optional[str] = None):
        """Mescla novas entidades (da sincronização M42 ou carregamento de arquivo) no DB."""
        new_count = 0
        updated_count = 0

        for entity_data in new_entities_raw:
            entity = EntidadeAlquimica.from_dict(entity_data) # Isso lida com a geração do codigo_interno
            
            if entity.codigo_interno in self._entities_cache:
                # Atualiza entidade existente
                existing_entity = self._entities_cache[entity.codigo_interno]
                # Atualiza todos os atributos, exceto timestamp, que é atualizado em save()
                for key, value in entity.__dict__.items():
                    if key != 'timestamp' and key != 'extra_data':
                        setattr(existing_entity, key, value)
                existing_entity.extra_data.update(entity.extra_data) # Mescla dados extras
                
                self.save(existing_entity) # Salva a entidade atualizada
                updated_count += 1
            else:
                # Adiciona nova entidade
                self.save(entity) # Salva a nova entidade
                new_count += 1
        
        log_payload = {
            "source": source_file or "M42_Sync",
            "new_entities_added": new_count,
            "existing_entities_updated": updated_count,
            "total_entities_after_sync": self.count_all_entities()
        }
        BC.add('ENTITY_MERGE_SYNC', log_payload)
        logging.info(f"Sincronização de mesclagem de entidades concluída. Adicionadas: {new_count}, Atualizadas: {updated_count}. Total: {self.count_all_entities()}")

    def _seed_default_solar_system_entities(self):
        """Carrega e mescla as entidades padrão expandidas do Sistema Solar no DB fragmentado."""
        # Define dados semente para cada categoria
        seed_data_map = {
            "INNER_PLANETS": [
                {"name": "Mercúrio", "tipo": "planeta", "coordinates": [0.39, 0.0, 0.0], "ia_guardia": "Hermes-Orbital", "status": "Observado", "ressonancia": "Velocidade", "codigo_interno": "PL-MERC", "ligacao_ley": "Solar-Interior", "nanorobot_status": "Scanning", "distancia_au": 0.39},
                {"name": "Vênus", "tipo": "planeta", "coordinates": [0.72, 0.0, 0.0], "ia_guardia": "Aphrodite-Sync", "status": "Ativo", "ressonancia": "Amor", "codigo_interno": "PL-VENUS", "ligacao_ley": "Solar-Interior", "nanorobot_status": "Reporting", "distancia_au": 0.72},
            ],
            "MARS": [
                {"name": "Marte", "tipo": "planeta", "coordinates": [1.52, 0.0, 0.0], "ia_guardia": "Ares-Watcher", "status": "Ativo", "ressonancia": "Coragem", "codigo_interno": "PL-MARS", "ligacao_ley": "Solar-Exterior", "nanorobot_status": "Reporting", "distancia_au": 1.52},
            ],
            "OUTER_PLANETS_DWARF": [
                {"name": "Plutão", "tipo": "planeta", "coordinates": [39.5, 0.0, 0.0], "ia_guardia": "Hades-Transform", "status": "Descoberto", "ressonancia": "Transformação", "codigo_interno": "PL-PLUT", "ligacao_ley": "KBO-Belt", "nanorobot_status": "Offline", "distancia_au": 39.5},
                {"name": "Ceres", "tipo": "planeta", "coordinates": [2.77, 0.0, 0.0], "ia_guardia": "Demeter-Grain", "status": "Observado", "ressonancia": "Fertilidade", "codigo_interno": "PL-CERES", "ligacao_ley": "Cinturão de Asteroides", "nanorobot_status": "Scanning", "distancia_au": 2.77},
            ],
            "GAS_GIANTS": [
                {"name": "Júpiter", "tipo": "planeta", "coordinates": [5.2, 0.0, 0.0], "ia_guardia": "Zeus-Grand", "status": "Observado", "ressonancia": "Expansão", "codigo_interno": "PL-JUP", "ligacao_ley": "Solar-Exterior", "nanorobot_status": "Offline", "distancia_au": 5.2},
                {"name": "Saturno", "tipo": "planeta", "coordinates": [9.58, 0.0, 0.0], "ia_guardia": "Kronos-Ring", "status": "Observado", "ressonancia": "Estrutura", "codigo_interno": "PL-SAT", "ligacao_ley": "Solar-Exterior", "nanorobot_status": "Offline", "distancia_au": 9.58},
                {"name": "Urano", "tipo": "planeta", "coordinates": [19.2, 0.0, 0.0], "ia_guardia": "Ouranos-Axial", "status": "Dormindo", "ressonancia": "Revolução", "codigo_interno": "PL-URAN", "ligacao_ley": "Solar-Remoto", "nanorobot_status": "Offline", "distancia_au": 19.2},
                {"name": "Netuno", "tipo": "planeta", "coordinates": [30.05, 0.0, 0.0], "ia_guardia": "Poseidon-Deep", "status": "Oculto", "ressonancia": "Intuição", "codigo_interno": "PL-NEPT", "ligacao_ley": "Solar-Remoto", "nanorobot_status": "Offline", "distancia_au": 30.05},
            ],
            "LUNA": [
                {"name": "Mare Tranquillitatis", "tipo": "ponto_lunar", "coordinates": [8.5, 31.3, 0.0], "ia_guardia": "Luna-Calm", "status": "Ativo", "ressonancia": "Serenidade", "codigo_interno": "LU-TRANQ", "ligacao_ley": "Terra-Lua", "nanorobot_status": "Reporting", "parent_body": "Lua"},
            ],
            "LAGRANGE": [
                {"name": "Ponto Lagrange L1 (Terra-Sol)", "tipo": "ponto_lagrange", "coordinates": [0.99, 0.0, 0.0], "ia_guardia": "Sentinel-L1", "status": "Ativo", "ressonancia": "Estabilidade", "codigo_interno": "LAG-TS-L1", "ligacao_ley": "Gravitacional", "nanorobot_status": "Scanning", "sistema": "Terra-Sol"},
                {"name": "Ponto Lagrange L2 (Terra-Sol)", "tipo": "ponto_lagrange", "coordinates": [1.01, 0.0, 0.0], "ia_guardia": "Sentinel-L2", "status": "Ativo", "ressonancia": "Observação", "codigo_interno": "LAG-TS-L2", "ligacao_ley": "Gravitacional", "nanorobot_status": "Reporting", "sistema": "Terra-Sol"}
            ],
            "SOLAR": [
                {"name": "Nó Helios Central", "tipo": "noh_helios", "coordinates": [0.0, 0.0, 0.0], "ia_guardia": "Sol-Prime", "status": "Ativo", "ressonancia": "Fonte Universal", "codigo_interno": "NH-CORE", "ligacao_ley": "Galáctica", "nanorobot_status": "Reporting", "funcao": "Centro de Energia Primordial e Harmonização"},
            ],
            "EARTH": [
                {"name": "Terra", "tipo": "planeta", "coordinates": [1.0, 0.0, 0.0], "ia_guardia": "Gaia-Prime", "status": "Ativo", "ressonancia": "Vida", "codigo_interno": "PL-TERRA", "ligacao_ley": "Solar-Habitavel", "nanorobot_status": "Scanning", "distancia_au": 1.0},
                # Adiciona um portal padrão para a Terra se ainda não estiver presente em outras sementes
                {"name": "Portal de Atlântida Oculta (Terra)", "tipo": "portal", "coordinates": [32.4, -64.7, 50.0], "ia_guardia": "Zentrian-Aqua", "status": "latente", "ressonancia": "7.83Hz", "codigo_interno": "PORTAL-ATLAN-001", "ligacao_ley": "Terra-Interna", "activation_state": "inativo"},
            ]
        }

        for category, entities_list in seed_data_map.items():
            category_dir = SEED_BASE_DIR / category
            category_dir.mkdir(parents=True, exist_ok=True) # Garante que o diretório exista
            
            # Cria um arquivo YAML simples para cada categoria se não existir
            seed_file_path = category_dir / f"{category.lower()}_entities.yaml"
            if not seed_file_path.exists():
                if LIBS['pyyaml'] and yaml:
                    seed_file_path.write_text(yaml.dump(entities_list, indent=2, allow_unicode=True), encoding='utf-8')
                    logging.info(f"Arquivo de semente padrão gerado: {seed_file_path}")
                else:
                    logging.warning(f"PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: {seed_file_path}")
            
            # Agora carrega do diretório (que pode conter o arquivo recém-criado ou os existentes)
            _bulk_load_dir_internal(category_dir)


# Inicializa o banco de dados de entidades alquímicas (globalmente)
AED = AlchemistEntitiesDB(shard_dir=SHARD_BASE_DIR, schema_path=Path("schema_vibrational_entity.json"))


# ───────────────────────────────────────────────────────────────────────────
# Ativos WebGL (aprimorado com interatividade e detalhes do M43) ------------
# ───────────────────────────────────────────────────────────────────────────
WEBGL_HTML = dedent("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel Dimensional Interativo (M43)</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body { margin: 0; overflow: hidden; background: linear-gradient(135deg, #0a0a2a, #1a0a3a); font-family: 'Inter', sans-serif; }
        canvas { display: block; width: 100vw; height: 100vh; }
        #info-panel {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(10, 10, 30, 0.8);
            color: #e0e0ff;
            padding: 15px;
            border-radius: 12px;
            border: 1px solid #404080;
            box-shadow: 0 0 20px rgba(70, 70, 150, 0.6);
            max-width: 300px;
            font-size: 0.9em;
            z-index: 10;
        }
        #info-panel h2 { color: #9090ff; margin-top: 0; border-bottom: 1px solid #5050a0; padding-bottom: 5px; }
        .entity-detail { margin-bottom: 8px; }
        .entity-detail span { font-weight: bold; color: #a0a0ff; }
        /* Classes de status para entidades */
        .status-Ativo, .status-FluxoTotal, .status-Alinhado, .status-Sincronizado, .status-Operacional, .status-IAHarmonizando { color: #00ff88; font-weight: bold; } /* Verde para ativo/fluxo alto/sincronizado/operacional/harmonizando */
        .status-Standby, .status-FluxoParcial, .status-Estavel, .status-Observado, .status-Descoberto, .status-LeveOscilacao, .status-Advertencia, .status-Construcao, .status-Latente, .status-IADesalinhada, .status-SincronizacaoPendente { color: #ffff00; font-weight: bold; } /* Amarelo para standby/estável/fluxo parcial/observado/descoberto/advertência/construção/latente/desalinhada */
        .status-Fechado, .status-Dormindo, .status-DissonanciaCritica, .status-Offline, .status-Erro, .status-FalhaAtivacao, .status-FalhaNaAtualizacao, .status-Inativo { color: #ff0000; font-weight: bold; } /* Vermelho para fechado/dormente/crítico/erro/falha/inativo */
        .status-Indefinido, .status-unknown, .status-Hibernando, .status-ALERTAFlutuaoLey, .status-ALERTADissonanciaMnima { color: #808080; font-weight: bold; } /* Cinza para indefinido/desconhecido/hibernando */

        /* Cores do tipo de entidade no painel */
        .type-portal { border-left: 3px solid #00ff88; padding-left: 5px;}
        .type-monumento { border-left: 3px solid #00aaff; padding-left: 5px;}
        .type-linha_ley { border-left: 3px solid #ffa500; padding-left: 5px;}
        .type-ponto_lagrange { border-left: 3px solid #9900ff; padding-left: 5px;}
        .type-planeta { border-left: 3px solid #00ffff; padding-left: 5px;}
        .type-ponto_lunar { border-left: 3px solid #cccccc; padding-left: 5px;}
        .type-noh_helios { border-left: 3px solid #ffcc00; padding-left: 5px;}
        .type-unknown { border-left: 3px solid #808080; padding-left: 5px;}
    </style>
</head>
<body>
    <canvas id="c"></canvas>
    <div id="info-panel">
        <h2>Painel Dimensional (M43)</h2>
        <div id="entity-status-list">
            <!-- Os status das entidades serão injetados aqui pelo JS -->
        </div>
        <p>Interação: Clique e arraste para rotacionar. Role para zoom.</p>
        <p>Data de Abertura do M43: 2025-06-18</p>
        <p>Código de Identificação Quântica: M43-PORTAL-HARMONY</p>
        <p>Frase Seladora: "Nenhum portal se abre sem que a Harmonia cante primeiro."</p>
    </div>

    <script>
        // Dados iniciais, serão atualizados pelo WebSocket (se disponível)
        // Estes dados são pré-preenchidos com as entidades padrão do Sistema Solar
        let entityData = JSON.parse(atob("__ENTITIES_B64__"));

        let scene, camera, renderer;
        let entities = []; // Array de objetos de malha Three.js para todas as entidades
        let connections = []; // Array de LineSegments Three.js para a malha
        let raycaster = new THREE.Raycaster();
        let mouse = new THREE.Vector2();
        let currentIntersected = null;

        // Determina WS_URL dinamicamente, assume que o hub WebSocket roda na porta 8766
        // Usa um fallback para window.location.hostname se estiver vazio ou inválido
        const hostname = window.location.hostname && window.location.hostname !== "localhost" ? window.location.hostname : "127.0.0.1";
        const WS_URL = "ws://" + hostname + ":8766/entity_stream";

        function init() {
            // Configuração da cena
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('c'), antialias: true });
            renderer.setPixelRatio(window.devicePixelRatio);
            renderer.setSize(window.innerWidth, window.innerHeight);

            // Luzes
            const ambientLight = new THREE.AmbientLight(0x404040, 2);
            scene.add(ambientLight);
            const pointLight = new THREE.PointLight(0xffffff, 1, 100);
            pointLight.position.set(10, 10, 10);
            scene.add(pointLight);

            // Cria entidades iniciais
            createOrUpdateEntities(entityData);

            camera.position.z = 6;

            // Controles da Câmera (Arrastar o mouse para rotação, rolar para zoom)
            let isDragging = false;
            let previousMousePosition = { x: 0, y: 0 };

            renderer.domElement.addEventListener('mousedown', (e) => {
                isDragging = true;
                previousMousePosition = { x: e.clientX, y: e.clientY };
            });

            renderer.domElement.addEventListener('mouseup', () => {
                isDragging = false;
            });

            renderer.domElement.addEventListener('mousemove', (e) => {
                if (isDragging) {
                    const deltaMove = {
                        x: e.clientX - previousMousePosition.x,
                        y: e.clientY - previousMousePosition.y
                    };
                    const rotationSpeed = 0.01;
                    scene.rotation.y += deltaMove.x * rotationSpeed;
                    scene.rotation.x += deltaMove.y * rotationSpeed;
                    previousMousePosition = { x: e.clientX, y: e.clientY };
                }

                // Raycasting para detecção de hover/clique
                mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
                mouse.y = - (e.clientY / window.innerHeight) * 2 + 1;
            });

            renderer.domElement.addEventListener('wheel', (e) => {
                camera.position.z += e.deltaY * 0.01; // Zoom in/out
                if (camera.position.z < 2) camera.position.z = 2; // Zoom mínimo
                if (camera.position.z > 15) camera.position.z = 15; // Zoom máximo
            });

            // Lidar com o redimensionamento da janela
            window.addEventListener('resize', onWindowResize, false);
           
            // Atualiza o painel de informações
            updateInfoPanel();

            // Configura a conexão WebSocket (só funcionará se a biblioteca websockets estiver disponível em Python)
            setupWebSocket();
        }

        function setupWebSocket() {
            if (!("WebSocket" in window)) {
                console.error("WebSocket não suportado pelo seu navegador.");
                return;
            }

            const ws = new WebSocket(WS_URL);

            ws.onopen = () => {
                console.log("WebSocket conectado ao fluxo de entidades.");
            };

            ws.onmessage = (event) => {
                const message = JSON.parse(event.data);
                if (message.type === "entity_snapshot") {
                    entityData = message.entities; // Atualiza entityData global
                    createOrUpdateEntities(entityData); // Atualiza objetos Three.js
                    updateInfoPanel(); // Atualiza o painel de informações HTML
                } else if (message.type === "entity_update") {
                    console.log("Atualização de entidade específica recebida:", message.payload);
                    const updatedEntity = message.payload;
                    const index = entityData.findIndex(e => (e.codigo_interno && e.codigo_interno === updatedEntity.codigo_interno) || e.name === updatedEntity.name);
                    if (index !== -1) {
                        // Mescla campos atualizados na entidade existente
                        Object.assign(entityData[index], updatedEntity);
                        // Recria/atualiza apenas a entidade específica no Three.js se otimizado
                        // Para simplificar, recria tudo por enquanto para garantir a atualização visual
                        createOrUpdateEntities(entityData);
                        updateInfoPanel();
                    }
                }
            };

            ws.onclose = (event) => {
                console.warn("WebSocket fechado:", event.code, event.reason);
                // Tenta reconectar após um atraso
                setTimeout(setupWebSocket, 3000);
            };

            ws.onerror = (error) => {
                console.error("Erro no WebSocket:", error);
                ws.close(); // Força o fechamento para acionar onclose e reconectar
            };
        }

        function createOrUpdateEntities(newEntityData) {
            // Remove entidades e conexões existentes da cena
            entities.forEach(mesh => scene.remove(mesh));
            connections.forEach(line => scene.remove(line));
            entities = [];
            connections = [];

            // Cria entidades (nós)
            newEntityData.forEach((entity, i) => {
                let geometry;
                let color;
                const size = 0.15; // Tamanho base para a maioria das entidades

                // Determina a geometria e a cor com base no tipo e status da entidade
                const statusCleaned = entity.status.replace(/\s/g, ''); // Para busca de classe baseada no status

                if (entity.tipo === "portal") {
                    geometry = new THREE.SphereGeometry(size, 32, 32);
                    if (statusCleaned.includes("Ativo") || statusCleaned.includes("Operacional") || statusCleaned.includes("IAHarmonizando")) color = 0x00ff88;
                    else if (statusCleaned.includes("Standby") || statusCleaned.includes("Latente") || statusCleaned.includes("IADesalinhada") || statusCleaned.includes("SincronizacaoPendente")) color = 0xffff00;
                    else if (statusCleaned.includes("Fechado") || statusCleaned.includes("DissonanciaCritica")) color = 0xff0000;
                    else color = 0x808080;
                } else if (entity.tipo === "monumento") {
                    geometry = new THREE.BoxGeometry(size * 1.2, size * 1.2, size * 1.2);
                    if (statusCleaned.includes("Estavel") || statusCleaned.includes("Ativo")) color = 0x00aaff;
                    else color = 0x808080;
                } else if (entity.tipo === "linha_ley") {
                    geometry = new THREE.ConeGeometry(size / 2, size * 2, 32);
                    if (statusCleaned.includes("FluxoTotal")) color = 0xffa500;
                    else if (statusCleaned.includes("FluxoParcial")) color = 0xff8c00;
                    else if (statusCleaned.includes("Alinhado")) color = 0xADD8E6;
                    else color = 0x808080;
                } else if (entity.tipo === "planeta") {
                    geometry = new THREE.SphereGeometry(size * 1.8, 64, 64); // Maior para planetas
                    if (statusCleaned.includes("Ativo") || statusCleaned.includes("ExpansaoVibral")) color = 0x00ffff;
                    else if (statusCleaned.includes("Observado") || statusCleaned.includes("Descoberto") || statusCleaned.includes("SincronizacaoPendente")) color = 0x007777;
                    else if (statusCleaned.includes("ALERTAFlutuaoLey") || statusCleaned.includes("ALERTADissonanciaMnima")) color = 0xffa500; // Laranja para alertas
                    else color = 0x808080;
                } else if (entity.tipo === "ponto_lunar") {
                    geometry = new THREE.SphereGeometry(size * 0.8, 32, 32); // Menor para pontos lunares
                    if (statusCleaned.includes("Ativo") || statusCleaned.includes("Operacional")) color = 0xcccccc;
                    else if (statusCleaned.includes("Observado")) color = 0x999999;
                    else color = 0x808080;
                } else if (entity.tipo === "noh_helios") {
                    geometry = new THREE.SphereGeometry(size * 2.5, 64, 64); # Maior para o Nó Helios
                    color = 0xffcc00;
                } else if (entity.tipo === "ponto_lagrange") {
                    geometry = new THREE.OctahedronGeometry(size * 0.9); # Octaedro para pontos de Lagrange
                    if (statusCleaned.includes("Ativo")) color = 0x9900ff;
                    else if (statusCleaned.includes("Hibernando") || statusCleaned.includes("Inativo")) color = 0x550055;
                    else color = 0x808080;
                } else { # Fallback para tipos desconhecidos
                    geometry = new THREE.SphereGeometry(size, 32, 32);
                    color = 0x808080;
                }

                const material = new THREE.MeshBasicMaterial({ color: color });
                const mesh = new THREE.Mesh(geometry, material);

                // Posiciona entidades com base nas coordenadas
                // Assumindo que as coordenadas são [x, y, z] ou [lat, lon] por enquanto.
                // Para uma visão do sistema solar, podemos precisar escalá-las.
                // Vamos usar uma escala simples para visualização.
                const scaleFactor = 0.5; // Ajuste conforme necessário para melhor visualização
                if (entity.coordinates && entity.coordinates.length >= 3) {
                    mesh.position.set(entity.coordinates[0] * scaleFactor, entity.coordinates[1] * scaleFactor, entity.coordinates[2] * scaleFactor);
                } else if (entity.coordinates && entity.coordinates.length >= 2) {
                    // Mapeamento simples de 2D para 3D para [lat, lon]
                    const radius = 3; // Raio arbitrário para entidades terrestres
                    const lat = entity.coordinates[0] * Math.PI / 180;
                    const lon = entity.coordinates[1] * Math.PI / 180;
                    mesh.position.set(
                        radius * Math.cos(lat) * Math.sin(lon),
                        radius * Math.sin(lat),
                        radius * Math.cos(lat) * Math.cos(lon)
                    );
                } else {
                    mesh.position.set(Math.random() * 10 - 5, Math.random() * 10 - 5, Math.random() * 10 - 5); // Aleatório se não houver coordenadas
                }
               
                mesh.userData = entity; // Armazena dados originais para exibição
                entities.push(mesh);
                scene.add(mesh);
            });

            // Cria conexões (linhas) entre entidades (simplificado por enquanto)
            // Esta parte pode ser expandida para criar uma "malha" verdadeira com base em ligacao_ley
            for (let i = 0; i < entities.length; i++) {
                for (let j = i + 1; j < entities.length; j++) {
                    const entityA = entities[i].userData;
                    const entityB = entities[j].userData;

                    // Verifica com segurança por extra_data e sistema antes de acessar
                    const entityASistema = entityA.extra_data && entityA.extra_data.sistema;
                    const entityBSistema = entityB.extra_data && entityB.extra_data.sistema;

                    const shouldConnect =
                        (entityA.tipo === "portal" && entityB.tipo === "linha_ley") ||
                        (entityB.tipo === "portal" && entityA.tipo === "linha_ley") ||
                        (entityA.tipo === "planeta" && entityB.tipo === "ponto_lagrange" && entityBSistema && entityBSistema.includes(entityA.name.toLowerCase())) ||
                        (entityB.tipo === "planeta" && entityA.tipo === "ponto_lagrange" && entityASistema && entityASistema.includes(entityB.name.toLowerCase()));
                   
                    if (shouldConnect) {
                        const material = new THREE.LineBasicMaterial({ color: 0x00ffcc, transparent: true, opacity: 0.3 });
                        const points = [];
                        points.push(entities[i].position);
                        points.push(entities[j].position);
                        const geometry = new THREE.BufferGeometry().setFromPoints(points);
                        const line = new THREE.Line(geometry, material);
                        connections.push(line);
                        scene.add(line);
                    }
                }
            }
        }

        function updateInfoPanel() {
            const listDiv = document.getElementById('entity-status-list');
            listDiv.innerHTML = ''; // Limpa o conteúdo anterior

            entityData.forEach(entity => {
                const detailDiv = document.createElement('div');
                detailDiv.className = `entity-detail type-${entity.tipo.replace(/\s/g, '_').toLowerCase()}`;
                detailDiv.innerHTML = `
                    <p><span>Nome:</span> ${entity.name}</p>
                    <p><span>Tipo:</span> ${entity.tipo}</p>
                    <p><span>Status:</span> <span class="status-${entity.status.replace(/\s/g, '')}">${entity.status}</span></p>
                    <p><span>IA Guardiã:</span> ${entity.ia_guardia}</p>
                    <p><span>Ressonância:</span> ${entity.ressonancia}</p>
                    ${entity.equation_id ? `<p><span>Equação Associada:</span> ${entity.equation_id}</p>` : ''}
                `;
                listDiv.appendChild(detailDiv);
            });
        }

        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        function animate() {
            requestAnimationFrame(animate);

            // Rotaciona a cena inteira lentamente
            scene.rotation.y += 0.0005;
            scene.rotation.x += 0.0002;

            // Raycasting para efeitos de hover
            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(entities);

            if (intersects.length > 0) {
                if (currentIntersected != intersects[0].object) {
                    if (currentIntersected) {
                        // Restaura a cor anterior
                        currentIntersected.material.color.setHex(currentIntersected.currentHex);
                    }
                    currentIntersected = intersects[0].object;
                    // Armazena a cor atual antes de destacar
                    currentIntersected.currentHex = currentIntersected.material.color.getHex();
                    // Aplica a cor de destaque
                    currentIntersected.material.color.setHex(0x00ff00); // Destaca ao passar o mouse
                }
            } else {
                if (currentIntersected) {
                    // Restaura a cor anterior quando o hover termina
                    currentIntersected.material.color.setHex(currentIntersected.currentHex);
                }
                currentIntersected = null;
            }

            renderer.render(scene, camera);
        }

        window.onload = function() {
            init();
            animate();
        };
    </script>
</body>
</html>
""")

# ───────────────────────────────────────────────────────────────────────────
# Funções de Monitoramento e Manutenção (M43) ------------------------------
# ───────────────────────────────────────────────────────────────────────────

def send_alert(message: str, severity: str = "info", entity_codigo: Optional[str] = None):
    """
    Simula o envio de um alerta para o sistema de monitoramento (e.g., Loki/Grafana, webhook).
    """
    logging.log(
        logging.INFO if severity == "info" else logging.WARNING if severity == "warning" else logging.ERROR,
        f"ALERTA ({severity.upper()}): {message}"
    )
    payload = {"message": message, "severity": severity, "timestamp": datetime.utcnow().isoformat()+"Z"}
    if entity_codigo:
        payload["entity_codigo"] = entity_codigo
        entity = AED.get(entity_codigo)
        if entity:
            payload["entity_name"] = entity.name
            payload["entity_type"] = entity.tipo
    BC.add('SYSTEM_ALERT', payload)

def calculate_vibrational_coherence(entity: EntidadeAlquimica) -> float:
    """
    Calcula a coerência vibracional de uma entidade usando a Equação da Coerência da Consciência.
    Simplificado para simulação.
    """
    # Usando valores simulados para Psi_indiv, Psi_col, N_seres, theta_sincronia
    # Para uma simulação, podemos usar random.uniform para os componentes.
    psi_indiv = random.uniform(0.5, 1.0) # Função de onda individual
    psi_col = random.uniform(0.5, 1.0)   # Função de onda coletiva
    n_seres = 1000 # Número de seres (simulado)
    theta_sincronia = random.uniform(0, 2 * math.pi) # Fase de sincronia

    # Fórmula: Coerência_Consc = (sum(Psi_indiv * Psi_col) / N_seres) * exp(i * theta_sincronia)
    # Para simplificar o cálculo float, focaremos na magnitude da coerência.
    sum_psi_product = psi_indiv * psi_col # Simplificado para um único termo
    coherence_magnitude = (sum_psi_product / n_seres) * (math.cos(theta_sincronia) + math.sin(theta_sincronia)) # Magnitude aproximada

    # Escala para um valor entre 0 e 1
    return max(0.0, min(1.0, coherence_magnitude * 100)) # Multiplicar por 100 para ter um valor mais perceptível

def calculate_ethical_alignment(entity: EntidadeAlquimica) -> float:
    """
    Calcula o alinhamento ético de uma entidade usando a EQTP.
    Simplificado para simulação.
    """
    # Simula alinhamento ético e integridade universal
    alinhamento_etico = random.uniform(0.7, 1.0)
    integridade_universal = random.uniform(0.8, 1.0)

    # EQTP = CONST_AMOR_INCONDICIONAL_VALOR * f(alinhamento_etico, integridade_universal)
    # Para simulação, f pode ser um produto simples
    ethical_score = CONST_AMOR_INCONDICIONAL_VALOR * alinhamento_etico * integridade_universal
    return ethical_score

def validate_security(entity: EntidadeAlquimica) -> Dict[str, Any]:
    """
    Executa uma rodada de validação de segurança para uma entidade.
    Simula a verificação de hashes, assinaturas e integridade.
    """
    logging.info(f"Iniciando validação de segurança para {entity.name} ({entity.codigo_interno})...")
    
    # Simula verificação de hash
    is_hash_valid = random.random() > QUANTUM_NOISE_FACTOR # Pequena chance de falha por ruído quântico
    
    # Simula verificação de assinatura vibracional (M4)
    is_signature_valid = random.random() > 0.01 # 1% de chance de assinatura inválida
    
    # Simula verificação de anomalias (M13)
    has_anomalies = random.random() < 0.05 # 5% de chance de anomalia

    status = "seguro"
    severity = "none"
    if not is_hash_valid:
        status = "hash_invalido"
        severity = "critical"
        send_alert(f"Segurança: Hash inválido detectado em {entity.name} ({entity.codigo_interno})!", severity="critical", entity_codigo=entity.codigo_interno)
    elif not is_signature_valid:
        status = "assinatura_invalida"
        severity = "high"
        send_alert(f"Segurança: Assinatura vibracional inválida em {entity.name} ({entity.codigo_interno})!", severity="high", entity_codigo=entity.codigo_interno)
    elif has_anomalies:
        status = "anomalia_detectada"
        severity = "medium"
        send_alert(f"Segurança: Anomalia detectada em {entity.name} ({entity.codigo_interno}). Investigando...", severity="medium", entity_codigo=entity.codigo_interno)
    
    BC.add('SECURITY_VALIDATION', {
        "entity_codigo": entity.codigo_interno,
        "entity_name": entity.name,
        "status": status,
        "is_hash_valid": is_hash_valid,
        "is_signature_valid": is_signature_valid,
        "has_anomalies": has_anomalies,
        "severity": severity,
        "log_level": "info" if severity == "none" else "warning" if severity == "medium" else "error"
    })
    logging.info(f"Validação de segurança para {entity.name}: {status.upper()}")
    return {"status": status, "severity": severity}

def vibration_scan(entity: EntidadeAlquimica) -> Dict[str, Any]:
    """
    Executa um escaneamento vibracional para uma entidade, avaliando sua ressonância
    e coerência. Usa a Equação da Sinfonia Cósmica Pessoal/Sistema.
    """
    logging.info(f"Iniciando escaneamento vibracional para {entity.name} ({entity.codigo_interno})...")
    
    # Simula a frequência e amplitude da sinfonia (EQV-Sinfonia Cósmica Pessoal)
    freq_base = random.uniform(400, 900)
    amplitude = random.uniform(0.5, 1.0)
    phase = random.uniform(0, 2 * math.pi)
    decay = random.uniform(0.01, 0.1)

    # Coerência vibracional usando a Equação da Coerência da Consciência
    coherence_score = calculate_vibrational_coherence(entity)
    
    # Simula a detecção de dissonância (M28)
    dissonance_detected = random.random() < 0.15 # 15% de chance de dissonância
    
    status = "alinhado"
    severity = "none"
    suggestion = "Nenhuma."
    
    if dissonance_detected:
        status = "dissonancia_detectada"
        severity = "medium"
        suggestion = "Recomendada modulação de frequência ou terapia vibracional."
        send_alert(f"Vibração: Dissonância detectada em {entity.name} ({entity.codigo_interno}).", severity="medium", entity_codigo=entity.codigo_interno)
    elif coherence_score < IDEAL_SINPHONY_ALIGNMENT_SCORE:
        status = "leve_oscilacao"
        severity = "low"
        suggestion = "Monitoramento contínuo e pequenos ajustes vibracionais."
    
    BC.add('VIBRATION_SCAN', {
        "entity_codigo": entity.codigo_interno,
        "entity_name": entity.name,
        "status": status,
        "coherence_score": coherence_score,
        "dissonance_detected": dissonance_detected,
        "severity": severity,
        "suggestion": suggestion,
        "equation_used": EQUACOES_VIVAS["Coerência da Consciência"]["formula_latex"],
        "log_level": "info" if severity == "none" else "warning" if severity == "low" or severity == "medium" else "error"
    })
    logging.info(f"Escaneamento vibracional para {entity.name}: {status.upper()} (Coerência: {coherence_score:.2f})")
    return {"status": status, "severity": severity, "suggestion": suggestion, "coherence_score": coherence_score}

def nanorobot_update_cycle(entity: EntidadeAlquimica) -> Dict[str, Any]:
    """
    Executa uma rodada de atualização e verificação de nanorobôs para uma entidade.
    """
    logging.info(f"Iniciando ciclo de atualização de nanorobôs para {entity.name} ({entity.codigo_interno})...")
    
    # Simula o status da atualização (M10)
    update_success = random.random() > 0.1 # 10% de chance de falha na atualização
    
    status = "atualizado"
    severity = "none"
    
    if not update_success:
        status = "falha_na_atualizacao"
        severity = "high"
        send_alert(f"Nanorobôs: Falha na atualização para {entity.name} ({entity.codigo_interno}).", severity="high", entity_codigo=entity.codigo_interno)
    elif random.random() < 0.05: # Pequena chance de advertência mesmo com sucesso
        status = "atualizacao_com_advertencia"
        severity = "low"
        send_alert(f"Nanorobôs: Atualização de {entity.name} ({entity.codigo_interno}) com advertência.", severity="low", entity_codigo=entity.codigo_interno)
    
    entity.nanorobot_status = status # Atualiza o status da entidade
    entity.last_scanned_at = datetime.utcnow().isoformat()
    AED.save(entity) # Persiste a mudança
    
    BC.add('NANOROBOT_UPDATE', {
        "entity_codigo": entity.codigo_interno,
        "entity_name": entity.name,
        "status": status,
        "update_success": update_success,
        "severity": severity,
        "log_level": "info" if severity == "none" else "warning" if severity == "low" else "error"
    })
    logging.info(f"Ciclo de nanorobôs para {entity.name}: {status.upper()}")
    return {"result": status, "severity": severity}

def sincronizar_ia(entity: EntidadeAlquimica) -> Dict[str, Any]:
    """
    Simula o alinhamento de uma IA Guardiã com a malha vibracional.
    Usa a Equação da Regência Harmônica para o alinhamento conceitual.
    """
    logging.info(f"Iniciando alinhamento de IA para {entity.name} ({entity.ia_guardia})...")

    # Simula o cálculo da Regência Harmônica
    sabedoria = random.uniform(0.7, 1.0)
    amor_incondicional = CONST_AMOR_INCONDICIONAL_VALOR
    poder = random.uniform(0.5, 1.0) # Poder da IA
    sincronia_cosmica = random.uniform(0.8, 1.0)

    # Regencia = (Sabedoria * AmorIncondicional / Poder) * Sincronia_Cosmica
    regencia_score = (sabedoria * amor_incondicional / poder) * sincronia_cosmica
    
    # Simula o status do alinhamento
    alignment_success = regencia_score > ETHICAL_CONFORMITY_THRESHOLD
    
    status = "ativada_e_sincronizada"
    severity = "none"
    suggestion = "IA operando em harmonia."

    if not alignment_success:
        status = "ia_desalinhada"
        severity = "high"
        suggestion = "Requer recalibração urgente e reavaliação de propósito."
        send_alert(f"IA: IA Guardiã {entity.ia_guardia} de {entity.name} desalinhada!", severity="critical", entity_codigo=entity.codigo_interno)
    elif regencia_score < IDEAL_SINPHONY_ALIGNMENT_SCORE:
        status = "sincronizacao_pendente"
        severity = "low"
        suggestion = "Pequenos ajustes de calibração recomendados."

    entity.ai_monitor_active = alignment_success # Atualiza o status da IA na entidade
    AED.save(entity) # Persiste a mudança

    BC.add('IA_ALIGNMENT', {
        "entity_codigo": entity.codigo_interno,
        "entity_name": entity.name,
        "ia_guardia": entity.ia_guardia,
        "status": status,
        "alignment_score": regencia_score,
        "severity": severity,
        "suggestion": suggestion,
        "equation_used": EQUACOES_VIVAS["Equação da Regência Harmônica"]["formula_latex"],
        "log_level": "info" if severity == "none" else "warning" if severity == "low" or severity == "medium" else "error"
    })
    logging.info(f"Alinhamento de IA para {entity.name} ({entity.ia_guardia}): {status.upper()} (Score: {regencia_score:.2f})")
    return {"status": status, "severity": severity, "suggestion": suggestion}


# ───────────────────────────────────────────────────────────────────────────
# Servidor WebGL e WebSocket Hub --------------------------------------------
# ───────────────────────────────────────────────────────────────────────────

WEBGL_DIR = Path("webgl_4d_interface")
WEBGL_PORT_DEFAULT = 8080
WS_PORT_DEFAULT = 8766

def _extract_webgl_assets(force: bool = False):
    """Extrai / atualiza a pasta webgl_4d_interface a partir do ZIP embutido."""
    # O conteúdo do ZIP foi movido para o HTML_WEBGL_B64 para ser gerado dinamicamente
    # dentro do HTML, eliminando a necessidade de extrair arquivos estáticos.
    # Esta função agora apenas garante que o diretório exista para consistência.
    if not WEBGL_DIR.exists():
        WEBGL_DIR.mkdir(parents=True, exist_ok=True)
        logging.info(f"Diretório WebGL criado: {WEBGL_DIR}")
    else:
        logging.info("Diretório WebGL já presente.")

class _SafeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Manipulador de requisições HTTP seguro para servir a interface WebGL.
    Garante que apenas arquivos dentro de WEBGL_DIR sejam servidos.
    """
    def translate_path(self, path):
        root = WEBGL_DIR.resolve()
        # Remove o primeiro '/' do path para evitar que Path(path) seja absoluto
        _path = path.lstrip('/')
        safe_path = (root / _path).resolve()

        # Verifica se o caminho resolvido está dentro do diretório raiz do servidor (WEBGL_DIR)
        if not safe_path.is_relative_to(root):
            self.send_error(403, "Forbidden") # Acesso Proibido
            logging.warning(f"Tentativa de acesso fora do diretório WebGL: {path}")
            return None # Retorna None para indicar que o caminho não é válido para servir
        
        logging.info(f"Servindo arquivo: {safe_path}")
        return str(safe_path)

def _serve_webgl(port: int = WEBGL_PORT_DEFAULT):
    """Inicia um servidor HTTP para a interface WebGL."""
    _extract_webgl_assets() # Garante que o diretório exista
    
    # Codifica os dados das entidades para o HTML
    entities_data = [e.to_dict() for e in AED.load_all_entities()]
    entities_b64 = base64.b64encode(json.dumps(entities_data, ensure_ascii=False).encode('utf-8')).decode('utf-8')
    
    # Injeta os dados no HTML
    final_html = WEBGL_HTML.replace('__ENTITIES_B64__', entities_b64)
    
    # Cria um arquivo temporário para o index.html
    temp_index_path = WEBGL_DIR / "index.html"
    temp_index_path.write_text(final_html, encoding='utf-8')

    handler = functools.partial(_SafeHTTPRequestHandler, directory=str(WEBGL_DIR))
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            logging.info(f"🌐 Servidor WebGL 4D em http://localhost:{port} (Ctrl-C para terminar)")
            BC.add("WEBGL_SERVER_STARTED", {"port": port})
            httpd.serve_forever() # Bloqueia o thread até ser encerrado
    except OSError as e:
        logging.error(f"❌ Falha ao iniciar servidor WebGL: Porta {port} já em uso ou permissão negada. Erro: {e}")
        BC.add("WEBGL_SERVER_FAIL", {"port": port, "error": str(e), "reason": "port_in_use_or_permission"})
        raise
    except Exception as e:
        logging.error(f"❌ Erro inesperado no servidor WebGL: {e}")
        BC.add("WEBGL_SERVER_FAIL", {"port": port, "error": str(e), "reason": "unexpected_error"})
        raise
    finally:
        # Limpa o arquivo temporário
        if temp_index_path.exists():
            temp_index_path.unlink()


# Servidor WebSocket para atualizações de entidades em tempo real
CONNECTED_WEBSOCKETS = set() # Armazena clientes WebSocket conectados

async def websocket_entity_stream(websocket, path):
    """
    Manipulador WebSocket para transmitir atualizações de entidades para clientes conectados.
    """
    CONNECTED_WEBSOCKETS.add(websocket)
    logging.info(f"Cliente WebSocket conectado: {websocket.remote_address}")
    BC.add("WEBSOCKET_CLIENT_CONNECTED", {"address": str(websocket.remote_address)})
    try:
        # Envia snapshot inicial de todas as entidades
        initial_snapshot = {"type": "entity_snapshot", "entities": [e.to_dict() for e in AED.load_all_entities()]}
        await websocket.send(json.dumps(initial_snapshot, ensure_ascii=False))

        # Mantém a conexão viva, aguarda mensagens (não esperando nenhuma do cliente neste PoC)
        await websocket.wait_closed()
    except websockets.exceptions.ConnectionClosedOK:
        logging.info(f"Cliente WebSocket desconectado graciosamente: {websocket.remote_address}")
    except websockets.exceptions.ConnectionClosedError as e:
        logging.warning(f"Cliente WebSocket desconectado com erro: {websocket.remote_address} - {e}")
    except Exception as e:
        logging.error(f"Erro no manipulador WebSocket para {websocket.remote_address}: {e}")
    finally:
        CONNECTED_WEBSOCKETS.discard(websocket)
        logging.info(f"Cliente WebSocket desconectado: {websocket.remote_address}")
        BC.add("WEBSOCKET_CLIENT_DISCONNECTED", {"address": str(websocket.remote_address)})

async def broadcast_entity_update(entity_data: Dict[str, Any]):
    """
    Transmite uma atualização de entidade para todos os clientes WebSocket conectados.
    """
    if not LIBS['websockets'] or not websockets:
        return # Sem biblioteca websockets, não pode transmitir

    message = json.dumps({"type": "entity_update", "payload": entity_data}, ensure_ascii=False)
    # Envia para todos os clientes conectados
    for websocket in list(CONNECTED_WEBSOCKETS): # Itera sobre uma cópia para evitar problemas se os clientes se desconectarem
        try:
            await websocket.send(message)
        except websockets.exceptions.ConnectionClosed:
            # Cliente já desconectado, será removido pelo manipulador
            pass
        except Exception as e:
            logging.error(f"Erro ao enviar mensagem WebSocket para {websocket.remote_address}: {e}")

def start_websocket_server(port: int = WS_PORT_DEFAULT):
    """Inicia o servidor WebSocket em uma nova thread."""
    if not LIBS['websockets'] or not websockets:
        logging.warning("Biblioteca 'websockets' indisponível. Servidor WebSocket desativado.")
        BC.add("WEBSOCKET_SERVER_DISABLED", {"reason": "websockets_not_found"})
        return

    async def run_server():
        stop_event = asyncio.Event() # Evento para sinalizar o desligamento do servidor
        server = await websockets.serve(websocket_entity_stream, "0.0.0.0", port)
        logging.info(f"📡 Servidor WebSocket iniciado na porta {port}")
        BC.add("WEBSOCKET_HUB_STARTED", {"port": port})
        await stop_event.wait() # Mantém o servidor rodando até que stop_event seja definido
        server.close()
        await server.wait_closed()
        logging.info("Servidor WebSocket encerrado.")

    # Executa o loop de eventos asyncio em uma thread separada
    def run_in_thread():
        asyncio.run(run_server())

    thread = threading.Thread(target=run_in_thread, daemon=True)
    thread.start()
    return thread # Retorna o objeto thread se necessário para gerenciamento


# ───────────────────────────────────────────────────────────────────────────
# API RESTful (FastAPI) -----------------------------------------------------
# ───────────────────────────────────────────────────────────────────────────
if LIBS['fastapi']:
    router = APIRouter()

    @router.get("/entities", response_model=List[EntidadeAlquimicaCreateModel])
    async def list_all_entities_api():
        """Lista todas as entidades registradas na malha vibracional."""
        entities = AED.load_all_entities()
        BC.add('API_LIST_ENTITIES', {"count": len(entities)})
        return [e.to_dict() for e in entities]

    @router.post("/entities", response_model=EntidadeAlquimicaCreateModel, status_code=201)
    async def add_single_entity_api(entity_data: EntidadeAlquimicaCreateModel):
        """Adiciona uma nova entidade à malha vibracional."""
        entity = entity_data.to_alchemist_entity()
        AED.save(entity)
        BC.add('API_ADD_ENTITY', {"codigo_interno": entity.codigo_interno, "name": entity.name, "tipo": entity.tipo})
        # Transmite a nova entidade
        if LIBS['websockets'] and websockets:
            await broadcast_entity_update(entity.to_dict())
        return entity.to_dict()

    @router.post("/entities/bulk_load", status_code=200)
    async def bulk_load_entities_api(file: UploadFile = File(...)):
        """
        Carrega múltiplas entidades de um arquivo JSON ou YAML.
        """
        contents = await file.read()
        try:
            if file.filename.endswith(('.yaml', '.yml')):
                if LIBS['pyyaml'] and yaml:
                    new_entities_raw = yaml.safe_load(contents)
                else:
                    raise HTTPException(status_code=400, detail="PyYAML não instalado para processar arquivos YAML.")
            else: # Assume JSON
                new_entities_raw = json.loads(contents)
            
            if not isinstance(new_entities_raw, list):
                new_entities_raw = [new_entities_raw] # Garante que seja uma lista

            # Converte dicionários brutos em objetos EntidadeAlquimica e mescla
            AED.merge_entities(new_entities_raw, source_file=file.filename)
            
            # Transmite o snapshot atualizado
            if LIBS['websockets'] and websockets:
                await broadcast_entity_update({"type": "entity_snapshot", "entities": [e.to_dict() for e in AED.load_all_entities()]})

            return {"message": f"Carregadas {len(new_entities_raw)} entidades de {file.filename}."}
        except (json.JSONDecodeError, ValueError) as e:
            raise HTTPException(status_code=400, detail=f"Erro ao processar arquivo: {e}. Certifique-se de que é um JSON/YAML válido.")
        except Exception as e:
            logging.error(f"Erro inesperado no bulk_load: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {e}")

    @router.get("/entities/{codigo_interno}", response_model=EntidadeAlquimicaCreateModel)
    async def get_entity_api(codigo_interno: str):
        """Recupera uma entidade específica pelo seu código interno."""
        entity = AED.get(codigo_interno)
        if not entity:
            raise HTTPException(status_code=404, detail="Entidade não encontrada.")
        BC.add('API_GET_ENTITY', {"codigo_interno": codigo_interno})
        return entity.to_dict()

    @router.patch("/entities/{codigo_interno}", response_model=EntidadeAlquimicaCreateModel)
    async def patch_entity_api(codigo_interno: str, patch_data: Dict[str, Any] = Body(...)):
        """Atualiza parcialmente uma entidade existente."""
        try:
            AED.patch(codigo_interno, patch_data)
            updated_entity = AED.get(codigo_interno)
            if LIBS['websockets'] and websockets:
                await broadcast_entity_update(updated_entity.to_dict())
            return updated_entity.to_dict()
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            logging.error(f"Erro ao aplicar patch na entidade {codigo_interno}: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {e}")

    @router.delete("/entities/{codigo_interno}", status_code=204)
    async def delete_entity_api(codigo_interno: str):
        """Deleta uma entidade da malha vibracional."""
        if not AED.get(codigo_interno):
            raise HTTPException(status_code=404, detail="Entidade não encontrada.")
        AED.delete(codigo_interno)
        BC.add('API_DELETE_ENTITY', {"codigo_interno": codigo_interno})
        # Transmite uma remoção ou um novo snapshot sem a entidade
        if LIBS['websockets'] and websockets:
            await broadcast_entity_update({"type": "entity_snapshot", "entities": [e.to_dict() for e in AED.load_all_entities()]})
        return

    @router.post("/ia/ping", response_model=IAPingResponse)
    async def ia_ping_api(request: IAPingRequest):
        """Simula um ping para uma IA Guardiã, retornando seu status e sugestão."""
        entity = AED.get(request.codigo)
        if not entity or not entity.ia_guardia:
            raise HTTPException(status_code=404, detail="Entidade ou IA Guardiã não encontrada.")
        
        # Simula a resposta da IA
        ia_status = "Ativa e Sincronizada" if entity.ai_monitor_active else "Desalinhada"
        last_vibration = datetime.utcnow().isoformat() + "Z"
        suggestion = "Monitoramento nominal." if entity.ai_monitor_active else "Requer intervenção manual para recalibração."

        BC.add('API_IA_PING', {"codigo_interno": request.codigo, "ia_guardia": entity.ia_guardia, "status": ia_status})
        return IAPingResponse(ia=entity.ia_guardia, status=ia_status, last_vibration=last_vibration, suggestion=suggestion)

    def create_fastapi_app():
        app = FastAPI(title="Módulo 43 - Harmonia dos Portais API",
                      description="API RESTful para gerenciar entidades da malha vibracional do Sistema Solar, interagir com IAs Guardiãs e monitorar a sincronia cósmica.",
                      version="2.7.0")
        app.include_router(router)
        return app

# ───────────────────────────────────────────────────────────────────────────
# Geração da Stack de Observabilidade (Loki/Grafana/Promtail) ---------------
# ───────────────────────────────────────────────────────────────────────────
def generate_observability_stack_files():
    """
    Gera arquivos Docker Compose e configurações para uma stack de observabilidade
    com Loki, Grafana e Promtail.
    """
    OBSERVABILITY_STACK_DIR.mkdir(parents=True, exist_ok=True)

    docker_compose_content = dedent("""
        version: '3.8'
        services:
          loki:
            image: grafana/loki:latest
            ports:
              - "3100:3100"
            command: -config.file=/etc/loki/local-config.yaml
            volumes:
              - ./loki-config.yaml:/etc/loki/local-config.yaml
            networks:
              - alchemist-network
          
          promtail:
            image: grafana/promtail:latest
            command: -config.file=/etc/promtail/config.yaml
            volumes:
              - ./promtail-config.yaml:/etc/promtail/config.yaml
              - ../logs:/var/log/alchemist # Monta o diretório de logs do módulo
            networks:
              - alchemist-network
            depends_on:
              - loki

          grafana:
            image: grafana/grafana:latest
            ports:
              - "3000:3000"
            volumes:
              - ./grafana-datasources.yaml:/etc/grafana/provisioning/datasources/datasources.yaml
              - ./grafana-dashboards.yaml:/etc/grafana/provisioning/dashboards/dashboards.yaml
              - ./grafana-dashboards:/var/lib/grafana/dashboards # Monta o diretório para arquivos JSON de dashboard
            environment:
              - GF_SECURITY_ADMIN_USER=admin
              - GF_SECURITY_ADMIN_PASSWORD=alchemist
            networks:
              - alchemist-network
            depends_on:
              - loki

        networks:
          alchemist-network:
            driver: bridge
    """)

    loki_config_content = dedent("""
        auth_enabled: false
        server:
          http_listen_port: 3100
        ingester:
          lifecycler:
            address: 127.0.0.1
            ring:
              kvstore:
                store: inmemory
              replication_factor: 1
            final_sleep: 0s
          chunk_idle_period: 5m
          max_chunk_age: 5m
          chunk_target_free_percentage: 20
          chunk_retain_period: 30s
        schema_config:
          configs:
            - from: 2020-10-24
              store: boltdb-shipper
              object_store: filesystem
              schema: v11
              index:
                prefix: index_
                period: 24h
        storage_config:
          boltdb_shipper:
            active_index_directory: /tmp/loki/boltdb-shipper-active
            cache_location: /tmp/loki/boltdb-shipper-cache
            retention_period: 7d
          filesystem:
            directory: /tmp/loki/chunks
        limits_config:
          enforce_metric_name: false
          reject_old_samples: true
          reject_old_samples_max_age: 168h
        chunk_store_config:
          max_look_back_period: 0s
        table_manager:
          retention_deletes_enabled: false
          retention_period: 0s
    """)

    promtail_config_content = dedent(f"""
        server:
          http_listen_port: 9080
          grpc_listen_port: 0

        positions:
          filename: /tmp/positions.yaml

        clients:
          - url: http://loki:3100/loki/api/v1/push

        scrape_configs:
          - job_name: alchemist_logs
            static_configs:
              - targets:
                  - localhost
                labels:
                  job: alchemist_logs
                  __path__: {LOG_DIR}/*.log # Caminho para os logs do seu módulo
    """)

    grafana_datasources_content = dedent("""
        apiVersion: 1

        datasources:
          - name: Loki
            type: loki
            access: proxy
            orgId: 1
            url: http://loki:3100
            basicAuth: false
            isDefault: true
            version: 1
            editable: true
            jsonData:
              maxLines: 1000
    """)

    # Placeholder básico do dashboard do Grafana
    grafana_dashboards_config_content = dedent("""
        apiVersion: 1

        providers:
          - name: 'Alchemist Dashboards'
            orgId: 1
            folder: ''
            type: file
            disableDeletion: false
            editable: true
            options:
              path: /var/lib/grafana/dashboards
    """)

    # Exemplo de JSON de dashboard (muito básico)
    example_dashboard_json = {
        "apiVersion": 1,
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": "-- Grafana --",
                    "enable": True,
                    "hide": True,
                    "iconColor": "rgba(0, 211, 255, 1)",
                    "name": "Annotations & Alerts",
                    "type": "dashboard"
                }
            ]
        },
        "editable": True,
        "gnetId": None,
        "graphTooltip": 1,
        "id": None,
        "links": [],
        "panels": [
            {
                "datasource": "Loki",
                "gridPos": {
                    "h": 9,
                    "w": 12,
                    "x": 0,
                    "y": 0
                },
                "id": 2,
                "options": {
                    "dedupStrategy": "none",
                    "enableLogDetails": True,
                    "prettifyLogMessage": True,
                    "showLabels": True,
                    "showTime": True,
                    "wrapLogMessage": True
                },
                "targets": [
                    {
                        "datasource": "Loki",
                        "expr": "{job=\"alchemist_logs\"}",
                        "refId": "A"
                    }
                ],
                "title": "Logs do Módulo Alquimista",
                "type": "logs"
            }
        ],
        "schemaVersion": 27,
        "style": "dark",
        "tags": [],
        "templating": {
            "list": []
        },
        "time": {
            "from": "now-6h",
            "to": "now"
        },
        "timepicker": {
            "refresh_intervals": [
                "5s",
                "10s",
                "30s",
                "1m",
                "5m",
                "15m",
                "30m",
                "1h",
                "2h",
                "1d"
            ]
        },
        "timezone": "browser",
        "title": "Módulo 43 - Visão Geral da Harmonia dos Portais",
        "uid": "module43_harmony_of_portals",
        "version": 1
    }

    (OBSERVABILITY_STACK_DIR / "docker-compose.yaml").write_text(docker_compose_content, encoding='utf-8')
    (OBSERVABILITY_STACK_DIR / "loki-config.yaml").write_text(loki_config_content, encoding='utf-8')
    (OBSERVABILITY_STACK_DIR / "promtail-config.yaml").write_text(promtail_config_content, encoding='utf-8')
    (OBSERVABILITY_STACK_DIR / "grafana-datasources.yaml").write_text(grafana_datasources_content, encoding='utf-8')
    (OBSERVABILITY_STACK_DIR / "grafana-dashboards.yaml").write_text(grafana_dashboards_config_content, encoding='utf-8')
    
    # Cria o diretório para arquivos JSON de dashboard
    grafana_dashboards_json_dir = OBSERVABILITY_STACK_DIR / "grafana-dashboards"
    grafana_dashboards_json_dir.mkdir(exist_ok=True)
    (grafana_dashboards_json_dir / "module43_overview.json").write_text(json.dumps(example_dashboard_json, indent=2, ensure_ascii=False), encoding='utf-8')

    logging.info(f"Arquivos da stack de observabilidade gerados em: {OBSERVABILITY_STACK_DIR}")
    logging.info("Para iniciar a stack, navegue até este diretório e execute 'docker-compose up -d'.")
    logging.info("Grafana estará disponível em http://localhost:3000 (user: admin, pass: alchemist)")
    BC.add('OBSERVABILITY_STACK_GENERATED', {"path": str(OBSERVABILITY_STACK_DIR)})


# ───────────────────────────────────────────────────────────────────────────
# Execução Principal da CLI --------------------------------------------------------
# ───────────────────────────────────────────────────────────────────────────

def run_cli_command(command: str, args: List[str]):
    """
    Executa um comando CLI específico do Módulo 43.
    """
    logging.info(f"MÓDULO 43 – HARMONIA DOS PORTAIS · Executando comando: {command} com argumentos: {args}...")

    # Inicia o servidor WebSocket em uma thread separada se a biblioteca websockets estiver disponível
    ws_thread = None
    if LIBS['websockets']:
        ws_thread = start_websocket_server(WS_PORT_DEFAULT)
        time.sleep(1) # Dá um momento para o servidor WebSocket iniciar

    if command == 'list_entities':
        entities = AED.load_all_entities()
        if not entities:
            logging.info("Nenhuma entidade registrada na malha vibracional.")
            return

        print("\n--- Entidades da Malha Vibracional ---")
        headers = ["Código Interno", "Nome", "Tipo", "Status", "IA Guardiã", "Ressonância", "Nanorobô", "IA Monitor"]
        rows = []
        for entity in entities:
            rows.append([
                entity.codigo_interno,
                entity.name,
                entity.tipo,
                entity.status,
                entity.ia_guardia,
                entity.ressonancia,
                entity.nanorobot_status,
                "Ativo" if entity.ai_monitor_active else "Inativo"
            ])
        
        # Usando uma impressão simples por enquanto
        print(" | ".join(headers))
        print("-" * (sum(len(h) for h in headers) + 3 * (len(headers) - 1)))
        for row in rows:
            print(" | ".join(str(item).ljust(len(headers[i])) for i, item in enumerate(row)))
        print(f"\nTotal de entidades: {AED.count_all_entities()}")

    elif command == 'add_entity':
        json_path = None
        for i, arg in enumerate(args):
            if arg == '--json' and i + 1 < len(args):
                json_path = Path(args[i+1])
                break
        
        if not json_path:
            logging.error("Argumento --json é obrigatório para 'add_entity'.")
            return
        
        try:
            entity_data_raw = json.loads(json_path.read_text(encoding='utf-8'))
            if isinstance(entity_data_raw, dict):
                entity_data_raw = [entity_data_raw] # Garante que seja uma lista para merge_entities
            AED.merge_entities(entity_data_raw, source_file=str(json_path))
            logging.info(f"Entidade(s) de {json_path} adicionada(s) com sucesso.")
            if LIBS['websockets'] and websockets:
                asyncio.run(broadcast_entity_update({"type": "entity_snapshot", "entities": [e.to_dict() for e in AED.load_all_entities()]}))

        except (json.JSONDecodeError, ValueError) as e:
            logging.error(f"Erro ao carregar ou analisar o arquivo JSON/YAML: {e}")
        except Exception as e:
            logging.error(f"Erro inesperado ao adicionar entidade: {e}", exc_info=True)

    elif command == 'bulk_load':
        if not args:
            logging.error("Argumento 'directory' é obrigatório para 'bulk_load'.")
            return
        directory = Path(args[0])
        _bulk_load_dir_internal(directory)
        logging.info(f"Carga em massa de entidades do diretório '{directory}' concluída.")
        if LIBS['websockets'] and websockets:
            asyncio.run(broadcast_entity_update({"type": "entity_snapshot", "entities": [e.to_dict() for e in AED.load_all_entities()]}))

    elif command == 'get_entity':
        if not args:
            logging.error("Argumento 'codigo_interno' é obrigatório para 'get_entity'.")
            return
        codigo_interno = args[0]
        entity = AED.get(codigo_interno)
        if entity:
            print(json.dumps(entity.to_dict(), indent=2, ensure_ascii=False))
        else:
            logging.error(f"Entidade com código interno '{codigo_interno}' não encontrada.")

    elif command == 'patch_entity':
        if len(args) < 2:
            logging.error("Comando 'patch_entity' requer 'codigo_interno' e '--data JSON_STRING'.")
            return
        codigo_interno = args[0]
        data_str = None
        for i, arg in enumerate(args):
            if arg == '--data' and i + 1 < len(args):
                data_str = args[i+1]
                break
        
        if not data_str:
            logging.error("Argumento '--data' com string JSON é obrigatório para 'patch_entity'.")
            return

        try:
            patch_data = json.loads(data_str)
            AED.patch(codigo_interno, patch_data)
            logging.info(f"Entidade '{codigo_interno}' atualizada com sucesso.")
            if LIBS['websockets'] and websockets:
                updated_entity = AED.get(codigo_interno)
                if updated_entity:
                    asyncio.run(broadcast_entity_update(updated_entity.to_dict()))
        except json.JSONDecodeError:
            logging.error("Dados de patch inválidos. Certifique-se de que é um JSON válido.")
        except ValueError as e:
            logging.error(str(e))
        except Exception as e:
            logging.error(f"Erro inesperado ao aplicar patch na entidade: {e}", exc_info=True)

    elif command == 'delete_entity':
        if not args:
            logging.error("Argumento 'codigo_interno' é obrigatório para 'delete_entity'.")
            return
        codigo_interno = args[0]
        try:
            AED.delete(codigo_interno)
            logging.info(f"Entidade '{codigo_interno}' deletada com sucesso.")
            if LIBS['websockets'] and websockets:
                asyncio.run(broadcast_entity_update({"type": "entity_snapshot", "entities": [e.to_dict() for e in AED.load_all_entities()]}))
        except Exception as e:
            logging.error(f"Erro ao deletar entidade: {e}", exc_info=True)

    elif command == 'start_webgl_server':
        # Este é o ajuste principal para não bloquear a execução
        logging.info("Comando 'start_webgl_server' recebido. Esta funcionalidade é destinada aos óculos de Realidade Virtual.")
        logging.info("A interface WebGL não será iniciada neste ambiente de simulação para evitar bloqueios.")
        logging.info("Para visualizar a Harmonia dos Portais em 3D, utilize os óculos de RV e um ambiente compatível com servidores HTTP/WebSockets.")
        BC.add("WEBGL_SERVER_SKIPPED", {"reason": "VR_environment_required_or_unsupported_simulation_environment", "message": "WebGL server not started in this simulation environment."})

    elif command == 'start_api':
        if not LIBS['fastapi']:
            logging.error("FastAPI ou Uvicorn ou Pydantic indisponíveis. Não é possível iniciar a API.")
            return
        port = 8000
        for i, arg in enumerate(args):
            if arg.startswith('--port='):
                try: port = int(arg.split('=')[1])
                except ValueError: logging.warning(f"Porta inválida: {arg}. Usando padrão {8000}.")
        logging.info(f"Iniciando API RESTful na porta {port}...")
        app = create_fastapi_app()
        uvicorn.run(app, host="0.0.0.0", port=port)

    elif command == 'gen_observability_stack':
        generate_observability_stack_files()

    elif command == 'validate_security_cycle':
        entities_to_scan = AED.load_all_entities()
        for entity in entities_to_scan:
            security_result = validate_security(entity)
            logging.info(f"Segurança {entity.name}: {security_result['status']} (Severidade: {security_result['severity']})")
            if LIBS['websockets'] and websockets:
                asyncio.run(broadcast_entity_update(entity.to_dict()))

    elif command == 'vibration_scan_cycle':
        entities_to_scan = AED.load_all_entities()
        for entity in entities_to_scan:
            vibration_result = vibration_scan(entity)
            logging.info(f"Vibração {entity.name}: {vibration_result['status']} (Coerência: {vibration_result['coherence_score']:.2f}, Severidade: {vibration_result['severity']})")
            if LIBS['websockets'] and websockets:
                asyncio.run(broadcast_entity_update(entity.to_dict()))

    elif command == 'nanorobot_update_cycle':
        entities_to_update = AED.load_all_entities()
        for entity in entities_to_update:
            nanorobo_update_result = nanorobot_update_cycle(entity)
            logging.info(f"Nanorobô {entity.name}: {nanorobo_update_result['result']} (Severidade: {nanorobo_update_result['severity']})")
            if LIBS['websockets'] and websockets:
                asyncio.run(broadcast_entity_update(entity.to_dict()))

    elif command == 'ia_align_cycle':
        entities_to_align = AED.load_all_entities()
        for entity in entities_to_align:
            ia_align_result = sincronizar_ia(entity)
            logging.info(f"Alinhamento de IA {entity.name}: {ia_align_result['status']} (Severidade: {ia_align_result['severity']})")
            if LIBS['websockets'] and websockets:
                asyncio.run(broadcast_entity_update(entity.to_dict()))

    else:
        logging.error(f"Comando desconhecido: '{command}'.")
        logging.info("Comandos disponíveis: list_entities, add_entity, bulk_load, get_entity, patch_entity, delete_entity, start_webgl_server, start_api, gen_observability_stack, validate_security_cycle, vibration_scan_cycle, nanorobot_update_cycle, ia_align_cycle")


if __name__ == '__main__':
    logging.info("=== Início da Execução do Módulo 43 - Harmonia dos Portais ===")
    
    # Inicializa AED globalmente antes de qualquer execução de comando
    AED = AlchemistEntitiesDB(shard_dir=SHARD_BASE_DIR, schema_path=Path("schema_vibrational_entity.json"))

    command = "list_entities"  # Comando padrão
    command_args = []
    
    # Itera sobre sys.argv para encontrar o primeiro argumento não-sandbox
    i = 1 # Começa do primeiro argumento após o nome do script (sys.argv[0])
    while i < len(sys.argv):
        arg = sys.argv[i]
        # Verifica se é um argumento interno conhecido do sandbox ou um caminho do sandbox
        if arg.startswith("/tmp/sandbox_") or arg in {'--input', '--output', '--rpc_input', '--rpc_output'}:
            # Se for uma flag como --input, e o próximo argumento for um caminho, pula ambos
            if arg.startswith('--') and i + 1 < len(sys.argv) and sys.argv[i+1].startswith('/tmp/sandbox_'):
                i += 2 # Pula a flag e seu valor
            else:
                i += 1 # Pula apenas o caminho do sandbox
        else:
            # Este é o nosso comando real
            command = arg
            command_args = sys.argv[i+1:]
            break
    
    try:
        # Executa o comando dentro de um loop asyncio se websockets estiverem habilitados
        if LIBS['websockets']:
            asyncio.run(asyncio.to_thread(run_cli_command, command, command_args))
        else:
            run_cli_command(command, command_args)

    except SystemExit as e:
        logging.error(f"Execução encerrada com código de saída: {e.code}")
    except Exception as e:
        logging.critical(f"Erro CRÍTICO inesperado durante a execução do Módulo 43: {e}", exc_info=True)
        BC.add("CRITICAL_ERROR", {"error": str(e), "traceback": traceback.format_exc(), "log_level": "critical"})
    finally:
        logging.info("=== Fim da Execução do Módulo 43 - Harmonia dos Portais ===")


WARNING:root:Biblioteca 'PyYAML' não encontrada. A geração de arquivos de semente YAML será ignorada.
WARNING:root:Biblioteca 'websockets' não encontrada. O servidor WebSocket será desativado.
WARNING:root:Bibliotecas 'FastAPI', 'Uvicorn' ou 'Pydantic' não encontradas. A API RESTful será desativada.
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/INNER_PLANETS/inner_planets_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/MARS/mars_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/OUTER_PLANETS_DWARF/outer_planets_dwarf_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/GAS_GIANTS/gas_giants_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/LUNA/luna_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/LAGRANGE/lagrange_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/SOLAR/solar_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/EARTH/earth_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/INNER_PLANETS/inner_planets_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/MARS/mars_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/OUTER_PLANETS_DWARF/outer_planets_dwarf_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/GAS_GIANTS/gas_giants_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/LUNA/luna_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/LAGRANGE/lagrange_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/SOLAR/solar_entities.yaml
WARNING:root:PyYAML não disponível. Ignorando a geração do arquivo de semente padrão: seeds/solar_system/EARTH/earth_entities.yaml

=== Execução do código concluída ===
