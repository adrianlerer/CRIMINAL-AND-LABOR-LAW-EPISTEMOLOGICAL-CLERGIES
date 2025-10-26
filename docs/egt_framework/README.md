# Evolutionary Game Theory Framework for Constitutional Law

## Overview

This framework implements the **Darwinian Dynamics** approach from Vince (2005) *"Evolutionary Game Theory, Natural Selection, and Darwinian Dynamics"* (Cambridge University Press) applied to constitutional law evolution.

**Core Insight**: Constitutional doctrines evolve as **Evolutionarily Stable Strategies (ESS)** that resist legislative reforms through judicial precedent accumulation.

---

## 🎯 Reality Filter: Proven vs Hypothetical

### ✅ PROVEN (Rigorous Mathematical Theory from Vince 2005)

1. **G-Function Framework** (Chapter 4)
   - Fitness-Generating Function: G(v, u, x)
   - Per capita growth rate for strategy v in population (u, x)
   - **Status**: Mathematically proven, peer-reviewed

2. **ESS Maximum Principle** (Theorem 7.1.1)
   - ESS requires: max G(v, u, x*) = G(u_i, u, x*) = 0
   - Invasion resistance: ∂²G/∂v² < 0 (peak)
   - **Status**: Proven theorem, rigorously implemented

3. **Darwinian Dynamics** (Chapter 5)
   - Coupled population-strategy evolution
   - Timescale separation: T_evo >> T_eco
   - **Status**: Established theoretical framework

4. **Disruptive Selection → Speciation** (Chapter 8)
   - ∂²G/∂v² > 0 (valley) → evolutionary branching
   - Mechanism for doctrinal subdivision
   - **Status**: Proven mathematical result

5. **Coevolution Framework** (Chapter 10)
   - Multiple G-functions for interacting populations
   - Predator-prey analogue (legislative-judicial)
   - **Status**: Peer-reviewed theory

### ⚠️ HYPOTHETICAL (Requires Empirical Validation)

1. **CLI → sigma_k Mapping**
   - Hypothesis: High CLI → low sigma_k → speciation
   - **Status**: Testable hypothesis, NOT proven
   - **Method**: Linear inverse mapping (conservative)
   - **Validation Needed**: Empirical calibration with 60-case dataset

2. **Reform Success Prediction**
   - Hypothesis: G(u_reform, u_ess, x*) predicts success probability
   - **Status**: Logical extension, NOT validated
   - **Validation Needed**: Out-of-sample prediction accuracy

3. **Frequency-Wave Effects**
   - Hypothesis: Reform waves change adaptive landscape topology
   - **Status**: Plausible from theory, NOT empirically tested
   - **Validation Needed**: Time-series analysis of reform clustering

4. **Coevolutionary Red Queen**
   - Hypothesis: Legislative-judicial arms race strengthens lock-in
   - **Status**: Theoretical prediction, NOT observed
   - **Validation Needed**: Historical case studies with time dynamics

### ❌ SPECULATIVE (Explicitly Avoided in Implementation)

1. **Invented Coefficients**
   - ❌ NOT used: β_reform, ε_critical, τ_convergence with arbitrary values
   - ✅ USED: Parameters from Vince's worked examples (r=0.25, K_max=100, sigma ∈ [0.5, 4])

2. **Predictive Claims Without Data**
   - ❌ NOT claimed: "Reforms will fail with 93.4% probability"
   - ✅ CLAIMED: "ESS theory predicts high CLI → low reform success"

3. **Untestable Mechanisms**
   - ❌ NOT invoked: "Judicial neurons fire in ESS patterns"
   - ✅ INVOKED: "Precedent accumulation follows Darwinian selection gradient"

---

## 📊 Empirical Validation Status

### Dataset: 62 Labor Law Reforms (1991-2025)
- **Argentina**: CLI=0.87, N=23, Success=0% ✓ (Validates strong lock-in prediction)
- **Chile**: CLI=0.15, N=17, Success=88% ✓ (Validates weak lock-in prediction)
- **Brazil**: CLI=0.40, N=12, Success=67% ⚠️ (Moderate CLI, moderate success)
- **Spain**: CLI=0.35, N=10, Success=60% ⚠️ (Moderate CLI, moderate success)

**Validation Metrics** (from `empirical_validation.py`):
- Accuracy: TBD (to be computed)
- AUC: TBD
- Cross-validation: TBD

**Status**: Preliminary validation supports core predictions (high CLI → low success), but precise quantitative predictions require further calibration.

---

## 🔬 Mathematical Rigor: Implementation Details

### 1. G-Function (src/egt/g_function.py)

**Lotka-Volterra Model** (Example 4.1.1):
```
G(v, u, x) = r * [K(v) - sum_j x_j * a(v, u_j)] / K(v)

where:
  K(v) = K_max * exp(-v²/(2*sigma_k²))
  a(v, u_j) = exp(-(v - u_j - beta)²/(2*sigma_alpha²))
```

**Parameters**:
- `r = 0.25`: Intrinsic growth rate (from Vince Example 5.4.1)
- `K_max = 100.0`: Maximum carrying capacity (normalized units)
- `sigma_k`: Resource niche width (mapped from CLI)
- `sigma_alpha = 2.0`: Competition niche width
- `beta = 0.0`: Asymmetry (symmetric competition baseline)

**Legal Interpretation**:
- `v`: Doctrinal rigidity (strategy)
- `K(v)`: Maximum sustainable doctrine strength
- `a(v, u_j)`: Conflict between reform v and doctrine u_j
- `r * (K - competition) / K`: Net fitness of doctrine v

### 2. ESS Solver (src/egt/ess_solver.py)

**ESS Maximum Principle** (Theorem 7.1.1):
```
If u_c is ESS, then:
  1. max G(v, u, x*) = G(u_i, u, x*) = 0
  2. ∂²G/∂v² < 0 (negative curvature = peak)
```

**Implementation**:
- Darwinian Dynamics integration until convergence
- Hessian analysis for invasion resistance (IR)
- Convergent stability (CS) via perturbed simulations
- Classification: ESS (peak), CSS (valley → speciation), Repellor (saddle)

### 3. Darwinian Dynamics (src/egt/darwinian_dynamics.py)

**Coupled Equations**:
```
Population (fast):  dx_i/dt = x_i * G(u_i, u, x)
Strategy (slow):    du_i/dt = sigma² * ∂G/∂v|_{v=u_i}
```

**Quasi-Equilibrium Assumption**:
- If `T_evo >> T_eco` (separation ratio > 10), then x ≈ x*(u) always
- Allows ESS analysis on fixed adaptive landscape G*(v) = G(v, u, x*(u))
- **Legal interpretation**: Legislative activity (fast) reaches equilibrium before judicial doctrine (slow) changes

### 4. Bifurcation Analysis (src/egt/adaptive_landscape.py)

**CLI as Bifurcation Parameter**:
- Low CLI → Wide niche (sigma_k large) → Single ESS (doctrinal unity)
- High CLI → Narrow niche (sigma_k small) → Multiple ESS (doctrinal pluralism)

**Mechanism**: As CLI increases, competition intensifies → disruptive selection → speciation

---

## 🧬 Legal Analogy Table

| **Biology (Vince 2005)** | **Constitutional Law (Our Framework)** |
|--------------------------|---------------------------------------|
| Species strategy `u` | Judicial doctrine (level of rigidity) |
| Population density `x` | Doctrine strength (precedent weight) |
| Fitness `G(v, u, x)` | Reform viability (success probability) |
| ESS (peak) | Constitutional lock-in (núcleo irreductible) |
| CSS (valley) | Unstable doctrine → speciation |
| Speciation | Doctrinal subdivision (conflicting precedents) |
| Predation `b(v, u_j)` | Judicial blocking of reform v by doctrine u_j |
| Harvesting | Legislative reforms (external pressure) |
| ESOHS | Optimal reform strategy (incremental, not shock) |
| Chemotherapy resistance | Lock-in strengthens under reform pressure |
| Red Queen dynamics | Legislative-judicial arms race |
| Timescale separation | Reforms fast, precedent evolution slow |

---

## 📚 Integration with Existing Tools

### 1. IusMorfos (CLI Calculator)
- **Integration**: CLI score → sigma_k via `LotkaVolterraGFunction(params, cli)`
- **Enhancement**: ESS strength predicts CLI effectiveness
- **Status**: Ready for integration

### 2. JurisRank (Precedent Network)
- **Integration**: Precedent centrality → strategy u_i in G-function
- **Enhancement**: Network topology predicts ESS stability
- **Status**: Requires module development

### 3. RootFinder (Genealogy Tracer)
- **Integration**: Citation network → phylogenetic tree = strategy evolution trajectory
- **Enhancement**: Darwinian Dynamics models precedent accumulation paths
- **Status**: Requires module development

### 4. Peralta Network Analysis (Coalition Clusters)
- **Integration**: Voting clusters → multi-strategy coalition ESS
- **Enhancement**: Coalition ESS theory (Section 6.2) predicts cluster stability
- **Status**: Requires empirical validation

---

## 🚀 Usage Example

```python
from src.egt import (
    LotkaVolterraGFunction,
    GFunctionParams,
    ESSSolver,
    TimescaleParams,
    AdaptiveLandscape,
    LandscapeVisualizer
)

# 1. Define parameters
base_params = GFunctionParams(
    r=0.25,
    K_max=100.0,
    sigma_k=2.0,
    sigma_alpha=2.0,
    beta=0.0
)

# 2. Create G-function for Argentina (CLI=0.87)
g_func = LotkaVolterraGFunction(base_params, cli_score=0.87)

# 3. Solve for ESS
timescale_params = TimescaleParams(sigma_sq=1.0, tau_eco=10.0, tau_evo=1000.0)
solver = ESSSolver(g_func, timescale_params)
result = solver.solve(u0=[0.0], t_max=10000.0)

print(f"ESS Strategy: {result.u_ess}")
print(f"Stability Type: {result.stability_type.value}")
print(f"Invasion Resistant: {result.invasion_resistant}")

# 4. Visualize adaptive landscape
landscape_obj = AdaptiveLandscape(g_func)
landscape = landscape_obj.compute(result.u_ess, result.x_ess)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 6))
LandscapeVisualizer.plot_single(landscape, ax=ax, show_ess=True)
plt.savefig('argentina_adaptive_landscape.png')
```

---

## 📖 References

### Primary Source
Vince, T.L. (2005). *Evolutionary Game Theory, Natural Selection, and Darwinian Dynamics*. Cambridge University Press. ISBN: 978-0-521-84170-2

### Application to Law
Lerer, I.A. (2025). *Constitutional Paleontology: Tracing the Ancestor's Tale of Legal Doctrines*. SSRN: https://ssrn.com/abstract=5660770

### Key Theorems Implemented
- **Theorem 7.1.1**: ESS Maximum Principle
- **Theorem 9.1.2**: Matrix-ESS for frequency-dependent selection
- **Equation 5.25**: First-order strategy dynamics
- **Chapter 8**: Evolutionary branching and speciation

---

## ⚠️ Limitations and Future Work

### Current Limitations
1. **Parameter Calibration**: CLI → sigma_k mapping is linear (conservative but not optimal)
2. **Reform Strategy Estimation**: Assumes reforms target u=0 (neutral point)
3. **Single-Trait Model**: Does not capture multi-dimensional doctrinal trade-offs
4. **Static ESS**: Does not model time-varying lock-in (requires coevolution module)

### Future Enhancements
1. **Empirical Calibration**: Maximum likelihood estimation of G-function parameters
2. **Multi-Trait Strategies**: Vector strategies for complex doctrinal dimensions
3. **Resource-Explicit Models**: Explicit resource dynamics (political capital, public support)
4. **Temporal Analysis**: Time-series of reform waves and precedent evolution
5. **Coalition ESS**: Multi-strategy equilibria for Peralta network clusters

---

## 📧 Contact

Ignacio A. Lerer  
SSRN: https://ssrn.com/abstract=5660770  
GitHub: https://github.com/[your-repo]/legal-evolution-unified

---

**Last Updated**: October 26, 2025  
**Framework Version**: 1.0.0  
**Status**: Core modules complete, empirical validation in progress
