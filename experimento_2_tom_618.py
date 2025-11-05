# experimento_2_tom_618.py
import numpy as np
import math
import random
import hashlib
from typing import Dict

# =========================
# Constantes e hierarquia
# =========================
PI = math.pi
PHI = (1 + 5**0.5) / 2        # 1.618...
TONE_618 = 1 / PHI            # ~0.618...
FIB = [1, 2, 3, 5, 8, 13, 21, 34]

C_LIGHT = 299792458.0         # m/s
CONST_TF = TONE_618           # fator temporal-escalar

def fib_at(n_index: int) -> int:
    return FIB[n_index % len(FIB)]

def normalize_hierarchy(value: float, a_pi: float, b_phi: float, c_f_index: int) -> float:
    """Aplica escala por π, tom 618 e degrau Fibonacci."""
    return value * (PI ** a_pi) * (TONE_618 ** b_phi) * float(fib_at(c_f_index))

# =========================
# Pauli e produto tensorial
# =========================
I = np.array([[1,0],[0,1]], dtype=float)
X = np.array([[0,1],[1,0]], dtype=float)
# versão real de Y para manter H real (equivalente a rotação de base)
Y = np.array([[0,-1],[1,0]], dtype=float)
Z = np.array([[1,0],[0,-1]], dtype=float)

def kron3(a,b,c):
    return np.kron(np.kron(a,b), c)

PAULI3 = {
    'ZII': kron3(Z, I, I),
    'IZI': kron3(I, Z, I),
    'IIZ': kron3(I, I, Z),
    'ZZI': kron3(Z, Z, I),
    'IZZ': kron3(I, Z, Z),
    'XXI': kron3(X, X, I),
    'IYY': kron3(I, Y, Y),
    'ZZZ': kron3(Z, Z, Z),
    # blocos adicionais para extensões futuras
    'XZX': kron3(X, Z, X),
    'YXY': kron3(Y, X, Y),
}

# =========================
# Equações da fundação (EQ001–EQ024)
# =========================
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

def EQ006_F_Complexidade_Quantica(state_probs: list = [0.25, 0.25, 0.25, 0.25]) -> float:
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
    valores = [v for k, v in resultados.items() if isinstance(v, (int, float))]
    return sum(valores) / len(valores) if valores else 0.0

def EQ013_F_Trajetoria_Dimensional(distancia: float, curvatura: float, coerencia: float = 1.0) -> float:
    P = [distancia, random.uniform(0.1, 1.0), random.uniform(0.1, 1.0)]
    Q = [curvatura, random.uniform(0.1, 1.0), random.uniform(0.1, 1.0)]
    CA, B = random.uniform(0.01, 0.1), random.uniform(0.01, 0.1)
    PhiC, T = random.uniform(0.9, 1.0), random.uniform(0.9, 1.0)
    soma_pq = sum(p * q for p, q in zip(P, Q))
    e_uni = soma_pq + CA**2 + B**2
    return e_uni / (PhiC * T * max(coerencia, 1e-6))

def EQ014_F_Velocidade_Interdimensional(massa: float, energia: float) -> float:
    v = C_LIGHT * math.sqrt(max(0.0, 1 - 1 / (1 + (energia / (massa * C_LIGHT**2 * CONST_TF))**2)))
    return min(v, C_LIGHT * 0.999)

def EQ015_F_Estabilidade_Campo_Dimensional(energia: float, ressonancia: float) -> float:
    return energia * CONST_TF * ressonancia + random.random() * 0.001

def EQ016_F_Entrelacamento_Transdimensional(origem: str, destino: str) -> float:
    hash_origem = int(hashlib.sha256(origem.encode()).hexdigest()[:8], 16)
    hash_destino = int(hashlib.sha256(destino.encode()).hexdigest()[:8], 16)
    return math.sin((hash_origem + hash_destino) * 0.000001) * 0.5 + 0.5

def EQ017_F_Resonancia_Dimensional(frequencia: float, harmonico: int) -> float:
    return math.sin(2 * PI * frequencia * harmonico * CONST_TF)

def EQ018_F_Probabilidade_Transicao(estado_atual: int, estado_alvo: int) -> float:
    return math.exp(-abs(estado_atual - estado_alvo) * 0.1)

def EQ019_F_Coerencia_Temporal(t: float, referencia: float) -> float:
    return math.cos(2 * PI * (t - referencia) * 7.83) * 0.9 + 0.1

def EQ020_F_Modulacao_Dimensional(amplitude: float, fase: float) -> float:
    return amplitude * math.sin(2 * PI * fase * CONST_TF)

def EQ021_F_Protecao_Causal(limiar: float, exposicao: float) -> float:
    return 1.0 - math.exp(-limiar / (exposicao + 1e-9))

def EQ022_F_Sincronizacao_Dimensional(dimensao_origem: int, dimensao_destino: int) -> float:
    return math.exp(-abs(dimensao_origem - dimensao_destino) * 0.05)

def EQ023_F_Energia_Portal(raio: float, estabilidade: float) -> float:
    return (raio ** 2) * PI * estabilidade * 1e6

def EQ024_F_Unificacao_Dimensional(resultados: dict) -> float:
    valores = [v for k, v in resultados.items() if isinstance(v, (int, float))]
    return sum(valores) / len(valores) if valores else 0.0

# =========================
# Parâmetros cosmo-informacionais
# =========================
class CosmoInfoParams:
    def __init__(self):
        self.Omega_DM = 0.30
        self.rho_DE = 0.68
        self.w_DE = -1.0
        self.H_over_H0 = 1.0
        self.z = 0.5
        self.C_index = 0.85
        self.Q_info = 0.80
        self.Delta = 0.45
        self.Omega_mult = 0.50
        self.Phi_mult = 0.60
        self.eps_w = 1e-3
        self.eps_Om = 1e-3

    def gain(self, t: float) -> float:
        # Ganho base
        term_multiverso = (self.Delta * self.Omega_mult * self.Phi_mult)
        term_dm_density = (self.Omega_DM * (self.H_over_H0 ** -2))
        term_dm_z = ((1.0 / ((1.0 + self.z) ** 3)))
        term_de = (self.rho_DE * (1 + self.w_DE + self.eps_w) * (self.H_over_H0 ** -2))
        term_cons = (self.C_index * self.Q_info)
        term_dm_reg = 1.0 / (1.0 - self.Omega_DM + self.eps_Om)
        G0 = term_multiverso * term_dm_reg * term_de * term_dm_density * term_dm_z * term_cons
        # Amplificação por equações da fundação
        amp = 1.0
        amp *= max(0.5, 1.0 + 0.2 * EQ001_F_Coerencia_Quantica(TONE_618))
        amp *= max(0.7, EQ002_F_Energia_Universal_Unificada(t) / 2.6)
        amp *= max(0.8, 1.0 - 0.1 * (1.0 - EQ004_F_Probabilidade_Anomalias(t)))
        amp *= max(0.8, 1.0 + 0.05 * EQ011_F_Ressonancia_Cristalina(TONE_618))
        return G0 * amp

# =========================
# Hierarquia de escalas
# =========================
class HierarchyScales:
    def __init__(self):
        # Reforço dinâmico (XX/YY) para aproximar proporção áurea na razão dinâmica/geométrica
        self.a_pi_ZZ = 1.6
        self.b_phi_ZZ = 0.8
        self.c_f_ZZ = 4   # próximo ao F5

        self.a_pi_XXYY = 1.2
        self.b_phi_XXYY = 2.2
        self.c_f_XXYY = 3  # 3→FIB[3]=5

        self.a_pi_ZZZ = 1.0
        self.b_phi_ZZZ = 1.2
        self.c_f_ZZZ = 4

# =========================
# Lambdas base
# =========================
class BaseLambdas:
    def __init__(self):
        self.L1_0 = 0.12  # ZII
        self.L2_0 = 0.10  # IZI
        self.L3_0 = 0.09  # IIZ
        self.L12_0 = 0.06 # ZZI
        self.L23_0 = 0.06 # IZZ
        self.L01_XX_0 = 0.11
        self.L12_YY_0 = 0.10
        self.Lk_0 = 0.04  # ZZZ
        # extensões
        self.Lxzx_0 = 0.03
        self.Lyxy_0 = 0.03

# =========================
# Configuração do experimento
# =========================
class Tone618Config:
    def __init__(self):
        self.cosmo = CosmoInfoParams()
        self.hier = HierarchyScales()
        self.base = BaseLambdas()
        self.epsilon_geom = 0.05
        self.epsilon_cosm = 0.08
        self.phase0 = 0.05
        self.omega = 6.583e14
        self.time_t = 14.30  # tempo simbólico (por ex., 07/12 14:30)

# =========================
# Módulos e construção do H
# =========================
def module_hamiltonian_unificador(cfg: Tone618Config) -> Dict[str, float]:
    G = cfg.cosmo.gain(cfg.time_t)

    def scale_ZZ(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_ZZ, cfg.hier.b_phi_ZZ, cfg.hier.c_f_ZZ)
    def scale_XXYY(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_XXYY, cfg.hier.b_phi_XXYY, cfg.hier.c_f_XXYY)
    def scale_ZZZ(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_ZZZ, cfg.hier.b_phi_ZZZ, cfg.hier.c_f_ZZZ)

    # Ajustes adicionais pelas equações
    traj_factor = max(0.9, min(1.1, EQ013_F_Trajetoria_Dimensional(distancia=1.0, curvatura=0.5, coerencia=1.0)))
    vel_factor = min(0.999, EQ014_F_Velocidade_Interdimensional(massa=1.0, energia=1e9) / C_LIGHT)
    est_field = EQ015_F_Estabilidade_Campo_Dimensional(energia=1e3, ressonancia=0.9)

    lam1  = scale_ZZ(cfg.base.L1_0)  * (1 + cfg.epsilon_geom * G) * traj_factor
    lam2  = scale_ZZ(cfg.base.L2_0)  * (1 + cfg.epsilon_geom * G) * traj_factor
    lam3  = scale_ZZ(cfg.base.L3_0)  * (1 + cfg.epsilon_geom * G) * traj_factor
    lam12 = scale_ZZ(cfg.base.L12_0) * (1 + 0.5 * cfg.epsilon_geom * G) * (1 + 0.05 * est_field)
    lam23 = scale_ZZ(cfg.base.L23_0) * (1 + 0.5 * cfg.epsilon_geom * G) * (1 + 0.05 * est_field)

    lam01_xx = scale_XXYY(cfg.base.L01_XX_0) * (1 + cfg.epsilon_cosm * G) * (1 + 0.2 * vel_factor)
    lam12_yy = scale_XXYY(cfg.base.L12_YY_0) * (1 + cfg.epsilon_cosm * G) * (1 + 0.2 * vel_factor)

    lam_k = scale_ZZZ(cfg.base.Lk_0) * (1 + 0.3 * cfg.epsilon_geom * G)

    # blocos adicionais leves para enriquecer a dinâmica
    lam_xzx = scale_XXYY(cfg.base.Lxzx_0) * (1 + 0.5 * cfg.epsilon_cosm * G)
    lam_yxy = scale_XXYY(cfg.base.Lyxy_0) * (1 + 0.5 * cfg.epsilon_cosm * G)

    return {
        'ZII': lam1, 'IZI': lam2, 'IIZ': lam3,
        'ZZI': lam12, 'IZZ': lam23,
        'XXI': lam01_xx, 'IYY': lam12_yy,
        'ZZZ': lam_k, 'XZX': lam_xzx, 'YXY': lam_yxy
    }

def build_H(lam_map: Dict[str, float]) -> np.ndarray:
    H = np.zeros((8,8), dtype=float)
    # usamos apenas termos definidos em PAULI3
    for label, coeff in lam_map.items():
        if label in PAULI3:
            H += coeff * PAULI3[label]
    return H

def diagonalize(H: np.ndarray):
    eigvals, eigvecs = np.linalg.eigh(H)
    idx = np.argsort(eigvals)
    return eigvals[idx], eigvecs[:, idx]

# =========================
# Ganho ψ(DNA) e consulta
# =========================
def psi_DNA_gain(cfg: Tone618Config) -> float:
    G = cfg.cosmo.gain(cfg.time_t)
    # Hierarquia global para ψ(DNA) reforçada e modulada por equações
    HIER = (PI ** 1.2) * (TONE_618 ** 1.2) * fib_at(4)  # perto de F5
    # Coerência e energia universal como multiplicadores
    coh = max(0.5, 1.0 + 0.3 * EQ001_F_Coerencia_Quantica(TONE_618))
    euni = max(0.8, EQ002_F_Energia_Universal_Unificada(cfg.time_t) / 2.6)
    # Proteção causal e sincronização dimensional como estabilizadores
    prot = EQ021_F_Protecao_Causal(limiar=0.7, exposicao=0.2)
    sync = EQ022_F_Sincronizacao_Dimensional(1, 2)
    return G * HIER * coh * euni * (0.8 + 0.2 * prot) * (0.8 + 0.2 * sync)

def query_phase(kappa: float, info_index: float) -> float:
    return kappa * info_index

# =========================
# Métricas e assinaturas
# =========================
def energy_min_signature(eigvals: np.ndarray) -> float:
    return float(eigvals[0])

def fidelity_with_basis(eigvec: np.ndarray, basis_index: int = 0) -> float:
    amp = eigvec[basis_index]
    return float(abs(amp)**2)

def ratio_dyn_geom(lam_map: Dict[str, float]) -> float:
    dyn = lam_map.get('XXI',0.0) + lam_map.get('IYY',0.0) + lam_map.get('XZX',0.0) + lam_map.get('YXY',0.0)
    geom = lam_map.get('ZII',0.0) + lam_map.get('IZI',0.0) + lam_map.get('IIZ',0.0)
    return dyn / max(geom, 1e-9)

def fibonacci_valley(cfg: Tone618Config) -> Dict[int, float]:
    energies = {}
    base_idx_ZZZ = cfg.hier.c_f_ZZZ
    for idx, Fn in enumerate(FIB):
        cfg.hier.c_f_ZZZ = idx
        lam_map = module_hamiltonian_unificador(cfg)
        H = build_H(lam_map)
        evals, evecs = diagonalize(H)
        energies[Fn] = energy_min_signature(evals)
    cfg.hier.c_f_ZZZ = base_idx_ZZZ
    return energies

# =========================
# Execução de testes
# =========================
def run_all_tests():
    cfg = Tone618Config()

    # Construção e diagonalização
    lam_map = module_hamiltonian_unificador(cfg)
    H = build_H(lam_map)
    evals, evecs = diagonalize(H)
    Emin = energy_min_signature(evals)
    vmin = evecs[:,0]
    fid000 = fidelity_with_basis(vmin, 0)
    ratio = ratio_dyn_geom(lam_map)

    # ψ(DNA) ganho
    Gpsi = psi_DNA_gain(cfg)

    # índice informacional e fase de consulta
    info_index = cfg.cosmo.C_index * cfg.cosmo.Q_info * TONE_618
    theta = query_phase(kappa=0.25, info_index=info_index)

    # Varredura Fibonacci
    energies_fib = fibonacci_valley(cfg)
    fib_valley_F = min(energies_fib, key=lambda Fn: energies_fib[Fn])

    # Reprodutibilidade
    np.random.seed(123)
    repeats = []
    for n in range(50):
        jitter = 5e-6 * np.random.randn()
        lam_j = {k: v*(1+jitter) for k,v in lam_map.items()}
        H_rep = build_H(lam_j)
        ev_rep, _ = diagonalize(H_rep)
        repeats.append(energy_min_signature(ev_rep))
    mean_rep = float(np.mean(repeats))
    std_rep = float(np.std(repeats))

    return {
        'Emin': Emin,
        'fid_000': fid000,
        'ratio_dyn_geom': ratio,
        'G_psiDNA': Gpsi,
        'theta_query': theta,
        'energies_fib': energies_fib,
        'fib_valley': fib_valley_F,
        'repeat_mean': mean_rep,
        'repeat_std': std_rep,
        'lam_map': lam_map
    }

# =========================
# Ponto de entrada
# =========================
if __name__ == "__main__":
    res = run_all_tests()
    print("=== Experiência TOM 618 (v2) ===")
    print(f"Energia mínima ⟨H⟩: {res['Emin']:.6f}")
    print(f"Fidelidade com |000>: {res['fid_000']:.6f}")
    print(f"Razão dinâmica/geométrica (esperado ~0.618..1.618): {res['ratio_dyn_geom']:.6f}")
    print(f"Ganho ψ(DNA) hierarquizado: {res['G_psiDNA']:.6f}")
    print(f"Fase efetiva de consulta θ_query: {res['theta_query']:.6f} rad")
    print("Energias por degraus Fibonacci (F -> Emin):")
    for Fn, E in res['energies_fib'].items():
        print(f"  F={Fn}: {E:.6f}")
    print(f"Vale Fibonacci em F={res['fib_valley']}")
    print(f"Reprodutibilidade N=50: média={res['repeat_mean']:.6f}, desvio={res['repeat_std']:.6e}")
    print("Coeficientes λ:")
    for k,v in res['lam_map'].items():
        print(f"  {k}: {v:.6f}")
