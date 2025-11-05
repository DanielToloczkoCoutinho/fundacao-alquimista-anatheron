# experimento_tom_618.py
import numpy as np
import math
from dataclasses import dataclass, field
from typing import List, Dict, Callable

# =========================
# Utilitários matemáticos
# =========================
PI = math.pi
PHI = (1 + 5**0.5) / 2   # 1.618...
TONE_618 = 1 / PHI       # ~0.618...

FIB = [1, 2, 3, 5, 8, 13]

def fib_at(n_index: int) -> int:
    return FIB[n_index % len(FIB)]

def normalize_hierarchy(value: float, a_pi: float, b_phi: float, c_f: int) -> float:
    return value * (PI ** a_pi) * (TONE_618 ** b_phi) * (fib_at(c_f) ** 1.0)

# =========================
# Pauli e produto tensorial
# =========================
I = np.array([[1,0],[0,1]], dtype=float)
X = np.array([[0,1],[1,0]], dtype=float)
Y = np.array([[0,-1],[1,0]], dtype=float)  # usaremos uma versão sem i para manter H real (efeito YY ajustado)
Z = np.array([[1,0],[0,-1]], dtype=float)

def kron3(a,b,c):
    return np.kron(np.kron(a,b), c)

# Mapeamento de strings Pauli
PAULI3 = {
    'ZII': kron3(Z, I, I),
    'IZI': kron3(I, Z, I),
    'IIZ': kron3(I, I, Z),
    'ZZI': kron3(Z, Z, I),
    'IZZ': kron3(I, Z, Z),
    'XXI': kron3(X, X, I),
    'IYY': kron3(I, Y, Y),
    'ZZZ': kron3(Z, Z, Z)
}

# =========================
# Estruturas de configuração
# =========================
@dataclass
class CosmoInfoParams:
    Omega_DM: float = 0.28
    rho_DE: float = 0.70
    w_DE: float = -1.0
    H_over_H0: float = 1.0
    z: float = 0.5
    C_index: float = 0.6  # consciência quântica
    Q_info: float = 0.7   # entrelaçamento x superposição
    Delta: float = 0.3
    Omega_mult: float = 0.4
    Phi_mult: float = 0.5
    eps_w: float = 1e-3   # regularização (1 + w_DE)
    eps_Om: float = 1e-3  # regularização (1 - Omega_DM)

    def gain(self) -> float:
        # Ganho cosmo-informacional lapidado
        term_multiverso = (self.Delta * self.Omega_mult * self.Phi_mult)
        term_dm_density = (self.Omega_DM * (self.H_over_H0 ** -2))
        term_dm_z = ((1.0 / ((1.0 + self.z) ** 3)))
        term_de = (self.rho_DE * (1 + self.w_DE + self.eps_w) * (self.H_over_H0 ** -2))
        term_cons = (self.C_index * self.Q_info)
        # Evita singularidades em (1 - Omega_DM)
        term_dm_reg = 1.0 / (1.0 - self.Omega_DM + self.eps_Om)
        G = term_multiverso * term_dm_reg * term_de * term_dm_density * term_dm_z * term_cons
        return G

@dataclass
class HierarchyScales:
    # Exponentes de hierarquia para cada bloco
    a_pi_ZZ: float = 2.0
    b_phi_ZZ: float = 1.0
    c_f_ZZ: int = 4  # preferir F5 como vale -> índice 4 (FIB[4] = 8); usaremos ajuste adiante

    a_pi_XXYY: float = 1.0
    b_phi_XXYY: float = 2.0
    c_f_XXYY: int = 3  # próximo ao F5

    a_pi_ZZZ: float = 1.0
    b_phi_ZZZ: float = 1.0
    c_f_ZZZ: int = 4  # alvo de ressonância em torno de F5

@dataclass
class BaseLambdas:
    L1_0: float = 0.15  # ZII
    L2_0: float = 0.10  # IZI
    L3_0: float = 0.08  # IIZ
    L12_0: float = 0.05 # ZZI
    L23_0: float = 0.05 # IZZ
    L01_XX_0: float = 0.07
    L12_YY_0: float = 0.06
    Lk_0: float = 0.03  # ZZZ

@dataclass
class Tone618Config:
    cosmo: CosmoInfoParams = field(default_factory=CosmoInfoParams)
    hier: HierarchyScales = field(default_factory=HierarchyScales)
    base: BaseLambdas = field(default_factory=BaseLambdas)
    epsilon_geom: float = 0.05
    epsilon_cosm: float = 0.05
    phase0: float = 0.05  # deslocamento de fase e^{i*0.05}
    omega: float = 6.583e14  # frequência (E/hbar) simbólica

# =========================
# Módulos de equações
# =========================
def module_hamiltonian_unificador(cfg: Tone618Config) -> Dict[str, float]:
    """Aplica hierarquia π–φ–Fibonacci ao Hamiltoniano base e escala por ganho cosmo-informacional."""
    G = cfg.cosmo.gain()

    # Hierarquia para blocos
    def scale_ZZ(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_ZZ, cfg.hier.b_phi_ZZ, cfg.hier.c_f_ZZ)
    def scale_XXYY(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_XXYY, cfg.hier.b_phi_XXYY, cfg.hier.c_f_XXYY)
    def scale_ZZZ(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_ZZZ, cfg.hier.b_phi_ZZZ, cfg.hier.c_f_ZZZ)

    lam1 = scale_ZZ(cfg.base.L1_0) * (1 + cfg.epsilon_geom * G)
    lam2 = scale_ZZ(cfg.base.L2_0) * (1 + cfg.epsilon_geom * G)
    lam3 = scale_ZZ(cfg.base.L3_0) * (1 + cfg.epsilon_geom * G)
    lam12 = scale_ZZ(cfg.base.L12_0) * (1 + 0.5 * cfg.epsilon_geom * G)
    lam23 = scale_ZZ(cfg.base.L23_0) * (1 + 0.5 * cfg.epsilon_geom * G)

    lam01_xx = scale_XXYY(cfg.base.L01_XX_0) * (1 + cfg.epsilon_cosm * G)
    lam12_yy = scale_XXYY(cfg.base.L12_YY_0) * (1 + cfg.epsilon_cosm * G)

    lam_k = scale_ZZZ(cfg.base.Lk_0) * (1 + 0.3 * cfg.epsilon_geom * G)

    return {
        'ZII': lam1, 'IZI': lam2, 'IIZ': lam3,
        'ZZI': lam12, 'IZZ': lam23, 'XXI': lam01_xx,
        'IYY': lam12_yy, 'ZZZ': lam_k
    }

def module_psi_DNA_gain(cfg: Tone618Config) -> float:
    """Retorna o ganho cosmo-informacional total para ψ(DNA), já hierarquizado."""
    G = cfg.cosmo.gain()
    # Aplicamos uma camada de hierarquia global para ψ(DNA)
    G_h = G * (PI ** 1.0) * (TONE_618 ** 1.0) * fib_at(4)  # em torno do F5 (índice próximo), reforçando ressonância
    return G_h

def module_query_operator(kappa: float, info_index: float) -> float:
    """Operador de consulta estrutural: retorno é um fator de fase efetiva."""
    # e^{i*kappa*I(S)} ~ fase; aqui retornamos o ângulo para interpretação
    return kappa * info_index

# =========================
# Construção do Hamiltoniano 3-qubit
# =========================
def build_H(lam_map: Dict[str, float]) -> np.ndarray:
    H = np.zeros((8,8), dtype=float)
    for label, coeff in lam_map.items():
        H += coeff * PAULI3[label]
    return H

def diagonalize(H: np.ndarray):
    eigvals, eigvecs = np.linalg.eigh(H)  # Hermitiano real
    idx = np.argsort(eigvals)
    return eigvals[idx], eigvecs[:, idx]

# =========================
# Métricas e assinaturas
# =========================
def energy_min_signature(eigvals: np.ndarray) -> float:
    return float(eigvals[0])

def fidelity_with_basis(eigvec: np.ndarray, basis_index: int = 0) -> float:
    # Fidelidade com |000> por simplicidade (index 0)
    amp = eigvec[basis_index]
    return float(abs(amp)**2)

def phi_plateau_check(lam_map: Dict[str, float]) -> float:
    # Relação dinâmica:geométrica aproximada
    dyn = lam_map['XXI'] + lam_map['IYY']
    geom = lam_map['ZII'] + lam_map['IZI'] + lam_map['IIZ']
    ratio = dyn / max(geom, 1e-9)
    return ratio  # esperamos ~TONE_618..PHI regime estável

def fibonacci_valley_confirm(cfg: Tone618Config, base: BaseLambdas) -> Dict[int, float]:
    # Varre F_n movimentando c_f_ZZZ, medindo energia mínima
    energies = {}
    for idx, Fn in enumerate(FIB):
        cfg.hier.c_f_ZZZ = idx
        lam_map = module_hamiltonian_unificador(cfg)
        H = build_H(lam_map)
        evals, evecs = diagonalize(H)
        energies[Fn] = energy_min_signature(evals)
    return energies

# =========================
# Execução de testes
# =========================
def run_all_tests():
    cfg = Tone618Config()
    # 1) Construção dos lambdas com hierarquia e ganho
    lam_map = module_hamiltonian_unificador(cfg)
    H = build_H(lam_map)
    evals, evecs = diagonalize(H)
    Emin = energy_min_signature(evals)
    vmin = evecs[:,0]
    fid000 = fidelity_with_basis(vmin, 0)
    ratio_phi_geom = phi_plateau_check(lam_map)

    # 2) Ganho ψ(DNA)
    G_psiDNA = module_psi_DNA_gain(cfg)

    # 3) Operador de consulta (acesso remoto), com índice informacional simples:
    # InfoIndex = C * Q_info * TONE_618
    info_index = cfg.cosmo.C_index * cfg.cosmo.Q_info * TONE_618
    theta_query = module_query_operator(kappa=0.2, info_index=info_index)  # fator de fase efetiva

    # 4) Varredura Fibonacci para confirmar vale ~F5
    energies_fib = fibonacci_valley_confirm(cfg, cfg.base)
    fib_valley_F = min(energies_fib, key=lambda Fn: energies_fib[Fn])

    # 5) Reprodutibilidade: N=50 execuções (determinísticas aqui, variação mínima simulada)
    # Introduziremos microvariações numéricas controladas no mapeamento para verificar estabilidade.
    np.random.seed(42)
    repeats = []
    for n in range(50):
        jitter = 1e-6 * np.random.randn()
        lam_map_rep = {k: v*(1+jitter) for k,v in lam_map.items()}
        H_rep = build_H(lam_map_rep)
        ev_rep, _ = diagonalize(H_rep)
        repeats.append(energy_min_signature(ev_rep))
    mean_rep = float(np.mean(repeats))
    std_rep = float(np.std(repeats))

    # Resultado agregado
    return {
        'Emin': Emin,
        'fid_000': fid000,
        'ratio_dyn_geom': ratio_phi_geom,
        'G_psiDNA': G_psiDNA,
        'theta_query': theta_query,
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
    print("=== Experiência TOM 618 ===")
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
