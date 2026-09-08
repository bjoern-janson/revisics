# STRUCTURE-001 — System Construction Manifest V1

**Status:** Prospective system-construction lock candidate  
**Parent scientific contract:** `STRUCTURE-001 V1 @ 9711a6dd1b14ade10fd43a03c424ddc840cc565e`  
**Parent candidate ontology:** `CANDIDATE_SPECIFICATION_MANIFEST_V1 @ 7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d`  
**Scientific role:** Exact F1–F5 world-generation and assay-case construction rules only  
**Primary candidate changes:** PROHIBITED  
**Implementation:** NOT STARTED  
**Execution:** ZERO CASES

---

## 0. Purpose and custody boundary

This artifact serializes the prospective system-construction layer required by STRUCTURE-001 V1. It defines the finite system universe, family semantics, generation rules, canonicalization, identity, accounting, and freeze gates before any system is generated and before any candidate outcome is inspected.

The governing invariant is:

```math
\boxed{\text{candidate behavior}\not\rightarrow\text{world generation, retention, rejection, deduplication, or weighting}.}
```

Candidate ontology and world-generation ontology are separate typed layers:

```math
\boxed{\text{candidate ontology}\perp\text{world-generation ontology}.}
```

The only permitted connection is the already-frozen semantic applicability audit after the complete system universe has been frozen.

No world is selected because it is expected to be difficult, favorable, unfavorable, interesting, or diagnostic for any candidate.

---

## 1. Custody sequence

```text
STRUCTURE-001 V1 scientific contract @ 9711a6d
        ↓
CANDIDATE SPECIFICATION MANIFEST V1 @ 7d1e3cf
        ↓
SYSTEM CONSTRUCTION MANIFEST V1
        ↓
SYSTEM-CONSTRUCTION LOCK
        ↓
IMPLEMENTATION
        ↓
OPERATIONAL / ENUMERATION CONTROLS
        ↓
VALID-WORLD / ASSAY-CASE FREEZE
        ↓
PRIMARY CANDIDATE EVALUATION
        ↓
SURVIVAL MATRIX + MINIMAL COUNTEREXAMPLES
```

The first two stages are already locked and are not reopened here. This manifest introduces no candidate, candidate scope, candidate property, auxiliary-choice class, output-equivalence rule, or scientific classification rule.

The system universe must exist independently of candidate implementations.

---

## 2. Raw operational primitive

Every generated system is built from:

```math
\boxed{\mathfrak O=(X,\mathcal A,\operatorname{Exec},\kappa).}
```

For F1, F2, and the F5 base grammar, execution is deterministic and partial:

```math
\delta_a:X\rightharpoonup X,
\qquad
\operatorname{Exec}(x,a,x')\iff\delta_a(x)=x'.
```

F3 retains deterministic raw execution and adds explicit resource/regime semantics. F4 retains deterministic raw execution and adds history-indexed extension admissibility.

Future-transformability is derived from operational facts, not fed backward into generation:

```math
\boxed{\mathcal T^\kappa(x)=\{(a,x'):\operatorname{Exec}(x,a,x')\}.}
```

For F4 the corresponding history-indexed object is:

```math
\boxed{\mathcal T^\kappa(h)=\{(a,x'):\operatorname{Exec}(x_t(h),a,x')\land\alpha_\kappa(h,a,x')=1\}.}
```

---

## 3. Construction principles

### 3.1 Meaning-before-evaluation

Every world-generation rule must be meaningful before any candidate is evaluated on any world.

### 3.2 Exhaustive enumeration

Use exhaustive finite enumeration wherever the V1 contract declares a finite exhaustive grammar. F4 history carriers and sufficient-state quotient spaces are exhaustive. F5 state/action recodings are exhaustive. A mandated exhaustive dimension may not be replaced by sampling after lock.

If implementation infeasibility is discovered, the legal response is a prospective V2/amendment that reduces the base grammar or bound before the affected evaluation. It is not a post-hoc sample.

### 3.3 No primary weighting

Primary V1 analysis has no scientific weighting by world, family, recoding, rarity, density, size, cycle count, sink count, branching, candidate difficulty, or anticipated informativeness:

```math
\boxed{w(W)=1\quad\text{for every valid primary assay case }W.}
```

Derived metadata may be reported descriptively but is never a generation knob or primary weight.

### 3.4 Construction versus minimality

Construction bounds are prospective:

```math
\boxed{\chi_F(W)\le K_F.}
```

A later minimal counterexample is searched only inside the already frozen valid universe:

```math
W^*=\arg\min_{W\in\mathcal U_F:P_i(W)=\mathrm{false}}\chi_F(W).
```

No construction bound is chosen from observed candidate behavior.

---

## 4. Accounting and identity

STRUCTURE-001 distinguishes:

1. **Raw construction:** one syntactic member of the frozen finite generation grammar before canonicalization.
2. **Canonical base world:** one representative of a family equivalence class under the frozen canonicalization rule.
3. **Assay case:** the unit presented to candidate evaluation. For F5 this is the complete `(W,\phi_X,\phi_A)` recoding case, not merely the destination serialization.
4. **Candidate/case evaluation:** one frozen candidate paired with one valid assay case.

These levels must never be called interchangeably “worlds.”

For canonical worlds, identity is a content-derived digest of the canonical family object. The implementation must fix the digest algorithm prospectively and retain the canonical serialization used as its input; the V1 provenance control uses SHA-256.

For F5:

```math
\boxed{\mathrm{BaseID}=H(\mathrm{Canon}(W_{base}))}
```

```math
\boxed{\mathrm{InstanceID}=H(\mathrm{Normalize}_{labels\ preserved}(\mathfrak O))}
```

```math
\boxed{\mathrm{RecodingID}=H(\mathrm{BaseID},\phi_X,\phi_A)}
```

Base-world deduplication is allowed only under the frozen family canonicalization relation. Required F5 recodings are never deduplicated. Distinct automorphisms remain distinct assay cases even if destination labels serialize identically.

Every raw construction, canonical world, and F5 recoding must retain enough provenance to reconstruct family, raw grammar coordinates, canonicalization, identity, manifest version, generator/canonicalization rule IDs, and validation status. F5 additionally records `BaseID`, `InstanceID`, `\phi_X`, `\phi_A`, `RecodingID`, and identity-recoding status.

A provenance mismatch is a control failure, never candidate evidence.

---

# Part A — Frozen numerical universe

## 5. V1 family bounds

```math
\boxed{
\begin{array}{lll}
F1 & 1\le n,m\le3 & \text{all deterministic partial-action tables}\\[1mm]
F2 & 1\le n,m\le3 & \text{F1 + every observation partition}\\[1mm]
F3 & 1\le n,m\le3,\ nm\le4 & |\mathcal B|=2,\ 0\prec_B1,\ c\in\{0,1\},\ H\in\{1,2\}\\[1mm]
F4 & 1\le n,m\le2,\ H\in\{1,2\} & \text{exhaustive history-extension semantics}\\[1mm]
F5_{\mathrm{primary}} & 2\le n,m\le3,\ nm\le6 & c\in\{0,1\},\ H=2,\ \text{all }n!m!\text{ recodings}
\end{array}}
```

These are construction bounds, not performance filters.

### 5.1 F1

```math
X=[n],\qquad\mathcal A=[m],\qquad\delta_a(x)\in X\cup\{\bot\}.
```

Every deterministic partial-action table inside the bound is generated. Density, cycles, sinks, branching, and related graph statistics are derived metadata only.

F1 does not enumerate extra `\kappa` variants; the operational baseline uses the fixed V1 path/accounting semantics. No candidate-specific resource structure is generated here.

### 5.2 F2

F2 is F1 plus every state observation partition:

```math
\Pi_O\in\operatorname{Part}(X).
```

Observation equivalence is induced by partition membership. The relation

```math
R(x,y)=\bigl(1[x=y],1[O(x)=O(y)],1[\mathcal T(x)=\mathcal T(y)]\bigr)
```

is derived after generation and is never a direct generation knob.

F2 does not enumerate extra `\kappa` variants beyond the fixed V1 baseline.

### 5.3 F3 — exact finite grammar

The F3 world is:

```math
\boxed{\mathfrak W_{F3}=(X,\mathcal A,\delta,\mathcal B,\preceq_B,u,c,R)}
```

with:

```math
\mathcal B=\{0,1\},\qquad 0\prec_B1.
```

Let

```math
E=\{(x,a,x'):\operatorname{Exec}(x,a,x')\}
```

be the executable edge set of the deterministic raw transition table. If `|E|=k`, then `0\le k\le nm\le4`.

For **every** raw transition table, F3 exhaustively enumerates:

1. every edge-cost function

   ```math
   c:E\to\{0,1\},
   ```

   giving exactly `2^k` possibilities;

2. every resource-update/admissibility function

   ```math
   u:\mathcal B\times E\to\mathcal B\cup\{\bot\},
   ```

   giving exactly `3^{2k}` possibilities because `|\mathcal B\times E|=2k` and `|\mathcal B\cup\{\bot\}|=3`;

3. the **fixed complete regime bundle**

   ```math
   \boxed{R=\mathcal B\times\{1,2\}}
   ```

   containing all four regime pairs `(B_r,H_r)` with `B_r\in\{0,1\}` and `H_r\in\{1,2\}`.

There is **no additional regime-subset choice** and no regime weighting. Thus the frozen F3 raw grammar is exactly the product of the transition-table grammar, `2^k` cost assignments, and `3^{2k}` resource-update assignments, with `R` fixed.

For each regime `r=(B_r,H_r)`, set

```math
\kappa_r=(B_r,H_r,u,c).
```

For a raw executable path `\pi=e_1\cdots e_j`, start with `b_0=B_r` and set

```math
b_i=u(b_{i-1},e_i).
```

The path is regime-admissible iff `j\le H_r` and no update returns `\bot`. Raw edge cost is additive:

```math
c(\pi)=\sum_i c(e_i).
```

No monotonicity is assumed:

```math
\boxed{u\text{ is not required to be monotone under }\preceq_B.}
```

Monotone and non-monotone cases emerge from exhaustive enumeration; neither is preselected.

The exact F3 raw count follows from the frozen grammar:

```math
\sum_{\substack{1\le n,m\le3\\nm\le4}}
\sum_{k=0}^{nm}
\binom{nm}{k}n^k\,2^k\,3^{2k}
=2,049,144.
```

Canonicalization is by the complete regime bundle under typed state/action isomorphism, with the ordered resource carrier fixed by `0\prec_B1`; candidate behavior is never used for deduplication.

### 5.4 F4

F4 is a deterministic raw core with exact history-indexed extension semantics:

```math
\boxed{\mathfrak W_{F4}=(X,\mathcal A,\delta,\alpha_\kappa,H)}
```

with `1\le n,m\le2` and `H\in\{1,2\}`.

All raw histories through the frozen horizon are generated:

```math
h_t=(x_0,a_0,x_1,\ldots,a_{t-1},x_t).
```

Only histories satisfying the raw deterministic relation generate continuation decisions. This normalization removes inert decisions after an already-inadmissible prefix; it is not candidate-specific.

For every raw history `h` of length `<H` and every raw executable extension `Exec(x_t(h),a,x')`, exhaustively assign:

```math
\boxed{\alpha_\kappa(h,a,x')\in\{0,1\}.}
```

Then an extension is admissible exactly when `h` is admissible, `Exec` holds, and `\alpha_\kappa(h,a,x')=1`.

A primary F4 world must satisfy the nonvacuous current-state collision:

```math
\boxed{\exists t\le H,\exists h\ne h'\in\mathcal H_t:\ x_t(h)=x_t(h').}
```

The corresponding future-transformability sets may be equal or unequal; neither is preselected.

The V1 horizon boundary is:

```math
H_{max}=2.
```

At `H=2`, the maximum deterministic terminal history-carrier size is `8`, so the unrestricted partition ceiling is `B_8=4,140`. At `H=3`, a terminal carrier may reach size `16`, whose unrestricted partition ceiling is `B_{16}=10,480,142,147`. These are partition ceilings only, not actual admissible quotient-class sizes and not a proof that `H=3` is inherently impossible. V1 uses `Hmax=2` because complete-partition enumeration of the admissible quotient search is prospectively guaranteed feasible at this horizon under the declared strategy. A larger horizon requires a prospective exhaustive V2 extension.

The T-blind sufficient-state quotient generation required by the candidate manifest occurs only after F4 worlds are frozen. It enumerates all admissible finite quotients subject only to current-state refinement and deterministic causal updateability; `\mathcal T`, candidate outcomes, and later future-transformational distinctions are forbidden as proposal/ranking/filtering inputs. Sufficiency is tested only afterward.

### 5.5 F5 — dedicated intersection-typed representation twins

The F5 base is:

```math
\boxed{W_{base}=(X,\mathcal A,\delta,c,H)}
```

with deterministic partial actions, additive nonnegative raw edge cost, `H=2`, and no history-dependent base admissibility. Primary bounds are `2\le n,m\le3`, `nm\le6`, `c(e)\in\{0,1\}`.

The base grammar is chosen because it semantically types every F5-scoped V1 candidate: ALG paths, REL state-indexed `\mathcal T`, COMB graph structure, TOP SCC order, GEO raw-path cost, INF finite history carriers, and DYN deterministic partial action dynamics.

All labeled bases are canonicalized first. Then for every canonical base:

```math
\boxed{\mathcal R(W)=\{(W,\phi_X,\phi_A):\phi_X\in\operatorname{Bij}(X),\phi_A\in\operatorname{Bij}(\mathcal A)\}.}
```

All state bijections and action bijections are retained, identity included. Required recodings are never deduplicated.

For `\phi=(\phi_X,\phi_A)`, the recoded execution relation satisfies exactly:

```math
\operatorname{Exec}(x,a,y)
\iff
\operatorname{Exec}'(\phi_X(x),\phi_A(a),\phi_X(y)).
```

Accounting, including horizon and edge cost, is transported exactly. Numeric labels, lexical names, serialization order, addresses, and coordinates have no operational meaning unless explicitly declared operational.

Continuous-coordinate recodings are outside primary V1.

---

## 6. Verified V1 sizing

The frozen grammar gives:

| Family | Raw constructions / normalized specifications | Canonical primary worlds / bundles | Primary F5 assay cases |
|---|---:|---:|---:|
| F1 | 267,137 | 8,344 | — |
| F2 | 1,333,172 | 40,839 | — |
| F3 | 2,049,144 | 500,079 canonical regime bundles | — |
| F4 | 13,056 normalized; 10,886 valid labeled | 2,862 valid canonical | — |
| F5 primary | 133,899 labeled bases | 11,718 canonical bases | 139,216 exhaustive recoding cases |

F4's largest declared cell `(n,m,H)=(2,2,2)` has:

```text
12,311 normalized specifications
10,886 valid labeled instances
2,784 valid canonical instances
```

The mixed canonical assay-case total is:

```math
8,344+40,839+500,079+2,862+139,216
=\boxed{691,340}.
```

This is an assay-case total, not a generic “world” total: F3 cases are regime bundles and F5 cases are recoding cases.

With the locked candidate scopes, the corresponding applicable candidate/case evaluation arithmetic is:

```math
8,344\times5
+40,839\times5
+500,079\times6
+2,862\times4
+139,216\times7
=\boxed{4,232,349}.
```

These are bookkeeping counts, not effect sizes and not scientific weights.

---

# Part B — Canonical family identities

## 7. Candidate applicability firewall

Only after the complete family universes have been generated, validated, canonicalized, and frozen is semantic candidate applicability evaluated:

```math
\boxed{A_{iW}=1[W\in\operatorname{Dom}(C_i)].}
```

Applicability may not delete, repair, reweight, recanonicalize, rescope, or otherwise mutate a world. An inapplicable candidate/case pair is a typed non-assay pair, not a candidate failure.

The locked candidate scopes are:

| Candidate | Scope |
|---|---|
| `S-ALG-001` | F1, F2, F3, F4, F5 |
| `S-REL-001` | F1, F2, F3, F5 |
| `S-COMB-001` | F1, F2, F3, F4, F5 |
| `S-TOP-001` | F1, F2, F3, F4, F5 |
| `S-GEO-001` | F3, F5 |
| `S-INF-001` | F4, F5 |
| `S-DYN-001` | F1, F2, F3, F5 |
```

Thus the per-family candidate multiplicities are F1=5, F2=5, F3=6, F4=4, F5=7.

---

# Part C — Construction and freeze gates

## 8. S0 — Manifest completeness

Before any generation, verify that each family has an exact type, exact bound, exact generation grammar, canonicalization rule, identity/provenance rule, validity condition, exhaustive-enumeration requirement where applicable, and candidate-independence firewall.

Missing construction semantics are a control failure.

## 9. S1 — Scientific custody lock

Record exactly:

```text
Parent scientific contract: 9711a6d
Parent candidate ontology: 7d1e3cf
System construction manifest: this exact V1 artifact
```

After lock, family definitions, bounds, enumeration requirements, canonicalization, identity, no-weighting, F3 semantics, F4 semantics, and F5 recoding coverage are immutable for V1 primary analysis. Later changes are V2/amendment work.

## 10. S2 — Zero-world verification

Immediately before implementation begins, verify:

```text
raw constructions generated        = 0
canonical worlds generated         = 0
F5 recoding cases generated        = 0
candidate/case outcomes observed   = 0
```

The construction manifest must be state-recorded while all four values are zero.

## 11. S3 — Generator determinism

A frozen generation run must be a deterministic function only of manifest version, family, bound, frozen grammar, and canonicalization rule. It may not depend on candidate outputs, candidate order, model judgment, execution outcomes, or post-hoc weighting.

Repeated generation from identical frozen inputs must reproduce identical raw identities and canonical identities.

## 12. S4 — Completeness controls

For exhaustive families, certify:

```text
no permitted raw construction omitted
no prohibited construction included
no permitted canonical class omitted
no distinct canonical class merged incorrectly
```

F4 additionally certifies complete raw-history and extension-table coverage. F5 additionally certifies all state bijections, all action bijections, and identity recoding coverage for every canonical base.

No candidate outcome may be consulted during completeness validation.

## 13. S5 — Family validity

Every generated object is independently checked against its family semantic contract. Invalid objects are marked with provenance and are not silently repaired. Candidate behavior cannot restore an invalid object.

F4 requires the declared current-state collision. F5 requires exact operational equivalence under the recoding maps.

## 14. S6 — Valid-world / assay-case freeze

Only after completeness and family validity pass may the canonical primary universe be frozen.

For F5, canonical bases are frozen first, then the exhaustive recoding ledger is generated without deduplication.

After this gate:

```math
\boxed{\text{V1 primary world/assay membership is immutable.}}
```

Candidate failures cannot add worlds. Candidate successes cannot remove worlds. Minimal counterexamples are searched only within the frozen universe.

## 15. S7 — Applicability freeze

After world/assay freeze, compute and record only the semantic applicability interface `A_{iW}`. This produces the typed evaluation matrix without mutating the world universe.

## 16. S8 — Implementation separation

Only after construction lock and universe freeze may candidate implementations run. Implementations must match the already-frozen candidate mathematical records. Disagreement is a control failure, not permission to reinterpret the world grammar.

---

# Part D — Anti-leakage and learning boundary

## 17. Explicit prohibitions

The following are prohibited during V1 primary construction/evaluation:

```text
candidate outcome       → world generation
candidate outcome       → world rejection
candidate outcome       → world retention
candidate outcome       → canonicalization
candidate outcome       → primary weighting
candidate outcome       → bound selection
candidate outcome       → candidate repair
```

The generator must remain executable without any candidate implementation.

## 18. Learning boundary

V1 permits learning from the frozen experiment, but information revealed after the freeze may only determine a prospective V2/amendment/extension. It may not change the evidentiary interpretation of V1.

```math
\boxed{\text{learning from an experiment}\neq\text{changing the experiment}.}
```

---

## 19. Claim ceiling of this artifact

This manifest establishes only:

```math
\boxed{\text{STRUCTURE-001 V1 has a prospectively declared, candidate-independent finite arena construction contract.}}
```

It does not establish that any candidate survives, that any candidate is refuted, that any mathematical family is foundational, that V1 bounds are representative beyond their declared finite scope, or that Revisics has a universal law.

---

## 20. Status inscription

```text
QUESTION / SCIENTIFIC CONTRACT       LOCKED @ 9711a6d
CANDIDATE ONTOLOGY                    LOCKED @ 7d1e3cf
SYSTEM CONSTRUCTION MANIFEST V1      THIS ARTIFACT
RAW CONSTRUCTIONS                     ZERO
CANONICAL WORLDS                      ZERO
F5 RECODING CASES                     ZERO
OUTCOMES                              ZERO
```

```math
\boxed{\text{third stone: cut before contact with the worlds.}}
```
