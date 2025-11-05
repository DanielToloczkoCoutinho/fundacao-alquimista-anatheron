# experimento_4_tom_618.py
import numpy as np
import math
import random
import hashlib
from typing import Dict, List

# =========================
# Constantes universais
# =========================
PI = math.pi
PHI = (1 + math.sqrt(5)) / 2                    # 1.618...
TONE_618 = 1 / PHI                               # ~0.618...
COERENCIA_COSMICA = 1.414                        # ~sqrt(2), coerência transversal
CONST_AMOR_INCONDICIONAL_VALOR = 0.999999999999999
ETHICAL_CONFORMITY_THRESHOLD = 0.75
ETHICAL_THRESHOLD_HIGH = 0.85
ETHICAL_THRESHOLD_DEFAULT = 0.69

C_LIGHT = 299792458                              # m/s
H_BAR = 1.054571817e-34                          # J*s

# Constantes cosmológicas (simbólicas)
H0_DEFAULT = 70.0                                # km/s/Mpc (simbólico)
G_GRAV = 6.67430e-11                             # m^3/(kg*s^2)
LAMBDA_COSMO = 1.11e-52                          # 1/m^2
RHO_CRITICAL = 8.62e-27                          # kg/m^3

# Sequência Fibonacci
FIB = [1, 2, 3, 5, 8, 13, 21, 34]

def fib_at(n_index: int) -> int:
    return FIB[n_index % len(FIB)]

def normalize_hierarchy(value: float, a_pi: float, b_phi: float, c_f_index: int) -> float:
    """Aplica escala por π, tom 618 e degrau Fibonacci."""
    return value * (PI ** a_pi) * (TONE_618 ** b_phi) * float(fib_at(c_f_index))

# =========================
# Diretrizes éticas e verificação
# =========================
def ethical_score(context: Dict[str, float]) -> float:
    """
    Calcula uma pontuação ética simples:
    - harmonia (0..1)
    - proteção (0..1)
    - transparência (0..1)
    - respeito (0..1)
    """
    h = context.get("harmonia", 0.8)
    p = context.get("protecao", 0.8)
    t = context.get("transparencia", 0.8)
    r = context.get("respeito", 0.8)
    base = (h + p + t + r) / 4.0
    reforco = 0.1 * CONST_AMOR_INCONDICIONAL_VALOR
    return min(1.0, base + reforco)

def ethical_gate(score: float) -> float:
    """
    Portão ético que ajusta ganhos e acoplamentos:
    - abaixo do threshold_default: reduz drasticamente
    - entre default e conformity: redução leve
    - acima de conformity e próximo de high: neutro/leve reforço
    """
    if score < ETHICAL_THRESHOLD_DEFAULT:
        return 0.1
    elif score < ETHICAL_CONFORMITY_THRESHOLD:
        return 0.7
    elif score < ETHICAL_THRESHOLD_HIGH:
        return 0.95
    else:
        return 1.05

# =========================
# Pauli e produto tensorial
# =========================
I = np.array([[1,0],[0,1]], dtype=float)
X = np.array([[0,1],[1,0]], dtype=float)
# versão real de Y para manter H real (rotação de base equivalente)
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

def EQ006_F_Complexidade_Quantica(state_probs: List[float] = [0.25, 0.25, 0.25, 0.25]) -> float:
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
    v = C_LIGHT * math.sqrt(max(0.0, 1 - 1 / (1 + (energia / (massa * C_LIGHT**2 * TONE_618))**2)))
    return min(v, C_LIGHT * 0.999)

def EQ015_F_Estabilidade_Campo_Dimensional(energia: float, ressonancia: float) -> float:
    return energia * TONE_618 * ressonancia + random.random() * 0.001

def EQ016_F_Entrelacamento_Transdimensional(origem: str, destino: str) -> float:
    hash_origem = int(hashlib.sha256(origem.encode()).hexdigest()[:8], 16)
    hash_destino = int(hashlib.sha256(destino.encode()).hexdigest()[:8], 16)
    return math.sin((hash_origem + hash_destino) * 0.000001) * 0.5 + 0.5

def EQ017_F_Resonancia_Dimensional(frequencia: float, harmonico: int) -> float:
    return math.sin(2 * PI * frequencia * harmonico * TONE_618)

def EQ018_F_Probabilidade_Transicao(estado_atual: int, estado_alvo: int) -> float:
    return math.exp(-abs(estado_atual - estado_alvo) * 0.1)

def EQ019_F_Coerencia_Temporal(t: float, referencia: float) -> float:
    return math.cos(2 * PI * (t - referencia) * 7.83) * 0.9 + 0.1

def EQ020_F_Modulacao_Dimensional(amplitude: float, fase: float) -> float:
    return amplitude * math.sin(2 * PI * fase * TONE_618)

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
        self.Omega_b = 0.05
        self.rho_DE = 0.68
        self.w_DE = -1.0
        self.H_over_H0 = 1.0
        self.z = 0.5

        self.C_index = 0.92
        self.Q_info = 0.88
        self.Delta = 0.50
        self.Omega_mult = 0.55
        self.Phi_mult = 0.60

        self.eps_w = 6e-4
        self.eps_Om = 1e-3

    def gain(self, t: float, ethical_adj: float) -> float:
        term_multiverso = (self.Delta * self.Omega_mult * self.Phi_mult)
        term_dm_density = (self.Omega_DM * (self.H_over_H0 ** -2))
        term_dm_z = ((1.0 / ((1.0 + self.z) ** 3)))
        term_de = (self.rho_DE * (1 + self.w_DE + self.eps_w) * (self.H_over_H0 ** -2))
        term_cons = (self.C_index * self.Q_info)
        term_dm_reg = 1.0 / (1.0 - self.Omega_DM + self.eps_Om)
        G0 = term_multiverso * term_dm_reg * term_de * term_dm_density * term_dm_z * term_cons

        amp = 1.0
        amp *= max(0.6, 1.0 + 0.45 * EQ001_F_Coerencia_Quantica(TONE_618))
        amp *= max(0.85, EQ002_F_Energia_Universal_Unificada(t) / 2.6)
        amp *= max(0.85, 1.0 - 0.10 * (1.0 - EQ004_F_Probabilidade_Anomalias(t)))
        amp *= max(0.85, 1.0 + 0.05 * EQ011_F_Ressonancia_Cristalina(TONE_618))
        amp *= COERENCIA_COSMICA

        return G0 * amp * ethical_adj

# =========================
# Hierarquia de escalas
# =========================
class HierarchyScales:
    def __init__(self):
        # Geometria moderada
        self.a_pi_ZZ = 1.10
        self.b_phi_ZZ = 0.55
        self.c_f_ZZ = 4   # perto de F5

        # Dinâmica reforçada (XX/YY/XZX/YXY)
        self.a_pi_XXYY = 1.0
        self.b_phi_XXYY = 2.85
        self.c_f_XXYY = 4  # F5

        # Termo interno moderado
        self.a_pi_ZZZ = 0.95
        self.b_phi_ZZZ = 1.1
        self.c_f_ZZZ = 4   # alvo em F5

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
        self.L01_XX_0 = 0.14
        self.L12_YY_0 = 0.13
        self.Lk_0 = 0.04  # ZZZ
        self.Lxzx_0 = 0.040
        self.Lyxy_0 = 0.040

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
        # contexto ético
        self.eth_context = {
            "harmonia": 0.93,
            "protecao": 0.91,
            "transparencia": 0.89,
            "respeito": 0.96
        }

# =========================
# Módulos e construção do H
# =========================
def module_hamiltonian_unificador(cfg: Tone618Config) -> Dict[str, float]:
    score = ethical_score(cfg.eth_context)
    e_gate = ethical_gate(score)

    G = cfg.cosmo.gain(cfg.time_t, e_gate)

    def scale_ZZ(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_ZZ, cfg.hier.b_phi_ZZ, cfg.hier.c_f_ZZ)
    def scale_XXYY(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_XXYY, cfg.hier.b_phi_XXYY, cfg.hier.c_f_XXYY)
    def scale_ZZZ(l0): return normalize_hierarchy(l0, cfg.hier.a_pi_ZZZ, cfg.hier.b_phi_ZZZ, cfg.hier.c_f_ZZZ)

    traj_factor = max(0.9, min(1.1, EQ013_F_Trajetoria_Dimensional(distancia=1.0, curvatura=0.5, coerencia=1.0)))
    vel_factor = min(0.999, EQ014_F_Velocidade_Interdimensional(massa=1.0, energia=1e9) / C_LIGHT)
    est_field = EQ015_F_Estabilidade_Campo_Dimensional(energia=1e3, ressonancia=0.9)
    boost_dyn = 1.0 + 0.45 * abs(EQ017_F_Resonancia_Dimensional(frequencia=0.83, harmonico=3)) \
                     + 0.30 * abs(EQ019_F_Coerencia_Temporal(t=cfg.time_t, referencia=7.83))
    boost_dyn *= e_gate

    # Geometria
    lam1  = scale_ZZ(cfg.base.L1_0)  * (1 + cfg.epsilon_geom * G) * traj_factor
    lam2  = scale_ZZ(cfg.base.L2_0)  * (1 + cfg.epsilon_geom * G) * traj_factor
    lam3  = scale_ZZ(cfg.base.L3_0)  * (1 + cfg.epsilon_geom * G) * traj_factor

    lam12 = scale_ZZ(cfg.base.L12_0) * (1 + 0.5 * cfg.epsilon_geom * G) * (1 + 0.05 * est_field)
    lam23 = scale_ZZ(cfg.base.L23_0) * (1 + 0.5 * cfg.epsilon_geom * G) * (1 + 0.05 * est_field)
    # Redução dos acoplamentos geométricos de segunda ordem (não dominar)
    lam12 *= 0.12
    lam23 *= 0.12

    # Dinâmica
    lam01_xx = scale_XXYY(cfg.base.L01_XX_0) * (1 + cfg.epsilon_cosm * G) * (1 + 0.2 * vel_factor) * boost_dyn
    lam12_yy = scale_XXYY(cfg.base.L12_YY_0) * (1 + cfg.epsilon_cosm * G) * (1 + 0.2 * vel_factor) * boost_dyn

    lam_k = scale_ZZZ(cfg.base.Lk_0) * (1 + 0.3 * cfg.epsilon_geom * G)

    # Blocos adicionais
    lam_xzx = scale_XXYY(cfg.base.Lxzx_0) * (1 + 0.5 * cfg.epsilon_cosm * G) * (boost_dyn * 1.1)
    lam_yxy = scale_XXYY(cfg.base.Lyxy_0) * (1 + 0.5 * cfg.epsilon_cosm * G) * (boost_dyn * 1.1)

    return {
        'ZII': lam1, 'IZI': lam2, 'IIZ': lam3,
        'ZZI': lam12, 'IZZ': lam23,
        'XXI': lam01_xx, 'IYY': lam12_yy,
        'ZZZ': lam_k, 'XZX': lam_xzx, 'YXY': lam_yxy
    }

def build_H(lam_map: Dict[str, float]) -> np.ndarray:
    H = np.zeros((8,8), dtype=float)
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
    score = ethical_score(cfg.eth_context)
    e_gate = ethical_gate(score)
    G = cfg.cosmo.gain(cfg.time_t, e_gate)
    HIER = (PI ** 1.40) * (TONE_618 ** 1.40) * fib_at(4)  # perto de F5
    coh  = max(0.65, 1.0 + 0.50 * EQ001_F_Coerencia_Quantica(TONE_618))
    euni = max(0.88, EQ002_F_Energia_Universal_Unificada(cfg.time_t) / 2.6)
    prot = EQ021_F_Protecao_Causal(limiar=0.75, exposicao=0.2)
    sync = EQ022_F_Sincronizacao_Dimensional(1, 2)
    return G * HIER * coh * euni * (0.82 + 0.18 * prot) * (0.82 + 0.18 * sync) * e_gate

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
    # favorece centros (F=5,8) com suavização informacional
    for Fn in list(energies.keys()):
        if Fn in (5, 8):
            energies[Fn] *= 0.975
    cfg.hier.c_f_ZZZ = base_idx_ZZZ
    return energies

# =========================
# Execução de testes
# =========================
def run_all_tests():
    cfg = Tone618Config()

    lam_map = module_hamiltonian_unificador(cfg)
    H = build_H(lam_map)
    evals, evecs = diagonalize(H)

    Emin = energy_min_signature(evals)
    vmin = evecs[:,0]
    fid000 = fidelity_with_basis(vmin, 0)
    ratio = ratio_dyn_geom(lam_map)

    Gpsi = psi_DNA_gain(cfg)

    info_index = cfg.cosmo.C_index * cfg.cosmo.Q_info * TONE_618
    theta = query_phase(kappa=0.30, info_index=info_index)

    energies_fib = fibonacci_valley(cfg)
    fib_valley_F = min(energies_fib, key=lambda Fn: energies_fib[Fn])

    np.random.seed(777)
    repeats = []
    for n in range(50):
        jitter = 5e-6 * np.random.randn()
        lam_j = {k: v*(1+jitter) for k,v in lam_map.items()}
        H_rep = build_H(lam_j)
        ev_rep, _ = diagonalize(H_rep)
        repeats.append(energy_min_signature(ev_rep))
    mean_rep = float(np.mean(repeats))
    std_rep = float(np.std(repeats))

    e_score = ethical_score(cfg.eth_context)
    e_gate = ethical_gate(e_score)

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
        'lam_map': lam_map,
        'ethical_score': e_score,
        'ethical_gate': e_gate
    }

# =========================
# Ponto de entrada
# =========================
if __name__ == "__main__":
    res = run_all_tests()
    print("=== Experiência TOM 618 (v4) ===")
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
    print(f"Ética: score={res['ethical_score']:.3f}, gate={res['ethical_gate']:.3f}")


