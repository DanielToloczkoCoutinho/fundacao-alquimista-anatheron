# experimento_7_tom_618.py
import numpy as np
import MODULO_41_2_orquestrador as orch

class Tone618Config:
    def __init__(self):
        self.cosmo = orch.CosmoInfoParams()
        self.hier = orch.HierarchyScales()
        self.base = orch.BaseLambdas()
        self.epsilon_geom = 0.05
        self.epsilon_cosm = 0.08
        self.phase0 = 0.05
        self.omega = 6.583e14
        self.time_t = 14.30
        self.eth_context = {
            "harmonia": 0.93,
            "protecao": 0.91,
            "transparencia": 0.89,
            "respeito": 0.96
        }

def run_all_tests():
    cfg = Tone618Config()

    lam_map = orch.module_hamiltonian_unificador(cfg)
    H = orch.build_H(lam_map)
    evals, evecs = orch.diagonalize(H)

    Emin = orch.energy_min_signature(evals)
    fid000 = orch.fidelity_with_basis(evecs[:,0], 0)
    ratio = orch.ratio_dyn_geom(lam_map)

    Gpsi = orch.psi_DNA_gain(cfg)

    info_index = cfg.cosmo.C_index * cfg.cosmo.Q_info * orch.TONE_618
    theta = orch.query_phase(kappa=0.36, info_index=info_index)

    energies_fib = orch.fibonacci_valley(cfg)
    fib_valley_F = min(energies_fib, key=lambda Fn: energies_fib[Fn])

    # Reprodutibilidade
    np.random.seed(7777)
    repeats = []
    for n in range(50):
        jitter = 5e-6 * np.random.randn()
        lam_j = {k: v*(1+jitter) for k,v in lam_map.items()}
        H_rep = orch.build_H(lam_j)
        ev_rep, _ = orch.diagonalize(H_rep)
        repeats.append(orch.energy_min_signature(ev_rep))
    mean_rep = float(np.mean(repeats))
    std_rep = float(np.std(repeats))

    e_score = orch.ethical_score(cfg.eth_context)
    e_gate = orch.ethical_gate(e_score)

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

if __name__ == "__main__":
    res = run_all_tests()
    print("=== Experiência TOM 618 (v7) ===")
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
