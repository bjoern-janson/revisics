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

This artifact serializes the prospective system-construction layer required by STRUCTURE-001 V1.

Its purpose is to define the finite system universe, family semantics, generation rules, canonicalization, identity rules, accounting, and freeze gates **before any system is generated and before any candidate outcome is inspected**.

The governing invariant is:

```math
\boxed{
\text{world generation is independent of candidate behavior.}
}
```

Equivalently:

```math
\boxed{
\text{candidate behavior}
\not\rightarrow
\text{world generation, retention, rejection, deduplication, or weighting}.
}
```

This manifest therefore treats the candidate ontology and system-construction ontology as separate typed layers:

```math
\boxed{
\text{candidate ontology}\perp\text{world-generation ontology}
}
```

Their only permitted connection is through the already-frozen candidate applicability interface after the system universe has been frozen.

No world is selected because it is expected to be interesting, difficult, favorable, or unfavorable to any candidate.

No candidate is removed, repaired, rescoped, or redefined using generated-world behavior.

---

## 1. Frozen scientific sequence

The V1 custody sequence is:

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

The first two stages are already locked and are not reopened by this artifact.

This manifest introduces no new primary candidate, candidate scope, candidate property, auxiliary-choice class, output-equivalence rule, or scientific classification rule.

---

## 2. Raw operational object

Every generated system is built from the declared operational primitive:

```math
\boxed{
\mathfrak O=(X,\mathcal A,\operatorname{Exec},\kappa).
}
```

The construction layer does not assume a mathematical structure on `X` or on future-transformability beyond the family semantics explicitly declared below.

For F1, F2, and the F5 base grammar, execution is deterministic and partial:

```math
\boxed{
\delta_a:X\rightharpoonup X
}
```

with

```math
\operatorname{Exec}(x,a,x')
\iff
\delta_a(x)=x'.
```

F3 and F4 retain deterministic raw execution while adding family-native accounting or history-indexed admissibility semantics as specified below.

Future-transformability is derived only after the operational object has been generated:

```math
\boxed{
\mathcal T^\kappa(x)=\{(a,x'):\operatorname{Exec}(x,a,x')\}
}
```

or, for F4, the corresponding history-indexed admissible extension set.

The construction direction is therefore fixed as:

```math
\boxed{
\text{operational facts}
\longrightarrow
\mathcal T
\longrightarrow
\text{candidate evaluation}.
}
```

---

## 3. Terminology and accounting classes

STRUCTURE-001 V1 uses four distinct accounting levels. They must not be conflated.

### 3.1 Raw construction

A raw construction is one syntactic member of the declared finite generation grammar before quotienting by the family-specific canonicalization relation.

Raw construction counts are provenance and sizing quantities. They are not the number of canonical worlds.

### 3.2 Canonical base world

A canonical base world is an equivalence-class representative obtained by the frozen family canonicalization rule. Canonicalization removes only representation redundancy explicitly declared by the family ontology.

Canonicalization may use state/action relabeling symmetry where explicitly specified. It may not remove F5 recoding assay cases, because those recodings are themselves the representation-invariance test.

### 3.3 Assay case

An assay case is the unit actually presented to the candidate-analysis pipeline.

For F1–F4, the assay case is the canonical family instance unless a family-specific substructure is explicitly part of the assay unit.

For F5, the assay unit is **not merely a destination representation**. It is the complete tuple:

```math
\boxed{
(\mathfrak O,\phi_X,\phi_A).
}
```

Distinct recodings remain distinct assay cases even when two recoding maps happen to serialize to the same destination labels.

### 3.4 Candidate/case evaluation

A candidate/case evaluation is a typed pair of one frozen candidate and one valid frozen assay case.

Thus candidate/case evaluations are not world counts.

The V1 frozen sizing values below are reported with these distinctions preserved.

---

## 4. Family-independent generation rules

### 4.1 Candidate-independence firewall

The following inputs are forbidden during world construction:

- candidate outcome;
- candidate pass/fail state;
- candidate ranking or score;
- candidate-specific counterexample status;
- candidate-specific implementation difficulty;
- candidate-specific performance prediction;
- candidate-specific applicability beyond the semantic domains already frozen in the candidate manifest.

No generator branch may inspect candidate identifiers or candidate values.

The generator is a function only of this manifest's frozen grammar, family semantics, finite bounds, and deterministic canonicalization rules.

### 4.2 Meaning-before-evaluation rule

Every world-generation rule must be meaningful before any candidate is evaluated on any world.

```math
\boxed{
\text{generation rule}
\text{ must be semantically defined independently of candidate outcomes.}
}
```

### 4.3 Enumeration priority

For each family, generation uses the strongest complete method required by V1:

1. exhaustive finite grammar;
2. exhaustive enumeration within the frozen finite bound;
3. deterministic generation only where exhaustive enumeration is not separately mandated by the scientific contract.

F4 history carriers and sufficient-state quotient spaces are required to be exhaustively enumerated.

F5 state/action recodings are required to be exhaustively enumerated.

Therefore neither F4 nor F5 may replace a mandated exhaustive dimension with post-lock sampling.

If a mandated exhaustive dimension proves infeasible in implementation, the legal response is a prospective reduction of the **base-world grammar or frozen bound** in a V2/amendment before execution of that dimension. Sampling is not a V1 substitute for a declared exhaustive requirement.

### 4.4 No primary weighting

The V1 primary assay assigns no statistical or scientific weighting to worlds, families, or recodings.

```math
\boxed{
w(W)=1
\quad\text{for every valid primary assay case }W.
}
```

Equivalently, no primary case is upweighted or downweighted according to density, rarity, size, cycle count, sink count, branching, candidate difficulty, or anticipated informativeness.

Derived metadata may be reported descriptively but is not a V1 world-generation control and is not a primary weighting variable.

### 4.5 Separation of construction and minimality

The frozen construction bound and any later minimal counterexample search are different objects.

Construction uses a prospectively frozen family bound:

```math
\boxed{\chi_F(W)\le K_F.}
```

A post-hoc minimal counterexample, when requested by the candidate failure contract, is then selected only from the already frozen valid universe:

```math
W^*
=
\arg\min_{W\in\mathcal U_F:\ P_i(W)=\mathrm{false}}
\chi_F(W).
```

No `K_F` may be increased, decreased, or otherwise chosen from observed candidate behavior during V1 primary evaluation.

---

## 5. World identity, canonicalization, and provenance

### 5.1 F1–F4 family identity

For family-valid instances, the primary canonical-world identity is computed only after application of the frozen family canonicalization rule.

A world identity is a content-derived digest of the canonical operational/family object. It is not a sequential generation index.

### 5.2 F5 identity

For an F5 base world, define a representation-independent base identifier:

```math
\boxed{
\mathrm{BaseID}=H(\mathrm{Canon}(W_{base})).
}
```

For a particular canonical-preserving serialization of that base:

```math
\boxed{
\mathrm{InstanceID}=H(\mathrm{Normalize}_{labels\ preserved}(\mathfrak O)).
}
```

For a specific recoding pair:

```math
\boxed{
\mathrm{RecodingID}
=
H(\mathrm{BaseID},\phi_X,\phi_A).
}
```

`H` denotes the repository's fixed cryptographic digest procedure as implemented under the execution controls. No digest algorithm may be substituted after primary cases are generated.

### 5.3 Deduplication rule

Base-world deduplication is permitted only where required by the declared family canonicalization relation.

F5 recodings are never deduplicated merely because the resulting serialized destination representation is identical.

In particular:

```math
\boxed{
\text{deduplicate base worlds; never deduplicate required F5 recodings.}
}
```

Distinct automorphisms remain distinct F5 assay cases.

### 5.4 Provenance ledger

Every raw construction, canonical world, and F5 recoding case must retain sufficient provenance to reconstruct:

- source family;
- raw grammar coordinates;
- canonicalization result;
- world identity;
- for F5, `BaseID`, `\phi_X`, `\phi_A`, and `RecodingID`;
- generator version and manifest identity;
- and validation status.

A provenance mismatch is a control failure, not a candidate result.

---

# Part A — Frozen numerical universe

## 6. Primary family bounds

The V1 primary construction bounds are:

```math
\boxed{
\begin{array}{lll}
F1 & 1\le n,m\le3 & \text{all deterministic partial-action tables}\\[2mm]
F2 & 1\le n,m\le3 & \text{F1 + every observation partition}\\[2mm]
F3 & 1\le n,m\le3,\quad nm\le4 & |\mathcal B|=2,\ 0\prec_B1,\ c\in\{0,1\},\ H\in\{1,2\}\\[2mm]
F4 & 1\le n,m\le2,\quad H\in\{1,2\} & \text{exhaustive history-extension semantics}\\[2mm]
F5_{\mathrm{primary}} & 2\le n,m\le3,\quad nm\le6 & c\in\{0,1\},\ H=2,\ \text{all }n!m!\text{ recodings}
\end{array}
}
```

These are construction bounds, not performance-derived filters.

### 6.1 F1 bound

State and action cardinalities satisfy:

```math
1\le n\le3,
\qquad
1\le m\le3.
```

Every deterministic partial-action table is generated:

```math
\delta_a:X\to X\cup\{\bot\}.
```

The raw grammar varies transition entries exhaustively. Density, cycle structure, sink count, branching, and related graph statistics are derived metadata only.

### 6.2 F2 bound

F2 uses the complete F1 bound and attaches every observation partition:

```math
\Pi_O\in\operatorname{Part}(X).
```

Observation structure is therefore generated from partitions of the state carrier rather than from a candidate-specific relation pattern.

The following relation pattern is derived only after construction:

```math
R(x,y)
=
\bigl(
1[x=y],
1[O(x)=O(y)],
1[\mathcal T(x)=\mathcal T(y)]
\bigr).
```

The three coordinates are not direct world-generation knobs.

### 6.3 F3 bound

F3 uses:

```math
1\le n,m\le3,
\qquad nm\le4,
```

with exactly two finite resource configurations:

```math
\mathcal B=\{0,1\},
\qquad 0\prec_B1.
```

Edge costs satisfy:

```math
c(e)\in\{0,1\}.
```

Regime horizons satisfy:

```math
H\in\{1,2\}.
```

All declared finite resource-update semantics and regime-bundle combinations in the frozen grammar are exhaustively generated as defined in Section 9.

### 6.4 F4 bound

F4 uses:

```math
1\le n,m\le2,
\qquad H\in\{1,2\}.
```

The history-extension table is exhaustive over the finite raw history carrier defined in Section 10.

The V1 choice `H_{max}=2` is deliberate and prospective. At horizon 2, the maximum terminal history-carrier size is 8 and the unrestricted partition ceiling is:

```math
B_8=4,140.
```

At horizon 3, a terminal history carrier may reach size 16, for which the unrestricted Bell-number partition ceiling is:

```math
B_{16}=10,480,142,147.
```

These Bell numbers are **unrestricted partition ceilings only**. They do not assert that the actual admissible quotient class has that many elements, nor that `H=3` is intrinsically impossible. V1 adopts `H_{max}=2` because exhaustive admissible-quotient generation is prospectively guaranteed feasible under a simple complete-partition enumeration strategy at this declared horizon. A larger horizon requires a separately preregistered exhaustive V2 extension.

### 6.5 F5 primary bound

The primary F5 grammar satisfies:

```math
2\le n,m\le3,
\qquad nm\le6.
```

Raw edge costs:

```math
c(e)\in\{0,1\}.
```

Base history horizon:

```math
H=2.
```

For every canonical F5 base, all state and action bijections are enumerated:

```math
\mathcal R(W)
=
\{(W,\phi_X,\phi_A):
\phi_X\in\operatorname{Bij}(X),\ 
\phi_A\in\operatorname{Bij}(\mathcal A)
\}.
```

The identity recoding is included.

One-dimensional F5 controls with `n=1` or `m=1` are excluded from the primary F5 scope but may be retained as construction controls. Their exclusion is a prospective typed design choice, not an observed-performance filter.

---

## 7. Frozen sizing results

The declared grammars yield the following verified V1 sizing values:

| Family | Raw constructions / normalized specifications | Canonical primary worlds / bundles | F5 assay cases |
|---|---:|---:|---:|
| F1 | 267,137 raw | 8,344 canonical | — |
| F2 | 1,333,172 raw | 40,839 canonical | — |
| F3 | 2,049,144 raw | 500,079 canonical regime bundles | — |
| F4 | 13,056 normalized specifications; 10,886 family-valid labeled | 2,862 valid canonical | — |
| F5 primary | 133,899 labeled bases | 11,718 canonical bases | 139,216 exhaustive recoding cases |

F4's largest declared construction cell is `(n,m,H)=(2,2,2)`:

```text
12,311 normalized specifications
10,886 valid labeled instances
2,784 valid canonical instances
```

The family-level canonical assay-case total is therefore:

```math
8,344+40,839+500,079+2,862+139,216
=
\boxed{691,340}
```

This total must be described as a mixed **assay-case count**, not generically as “691,340 worlds,” because F3 units are regime bundles and F5 units are recoding cases.

The locked V1 candidate scopes imply the following candidate/case evaluation counts:

```math
F1:8,344\times5
```

```math
F2:40,839\times5
```

```math
F3:500,079\times6
```

```math
F4:2,862\times4
```

```math
F5:139,216\times7
```

for a total of:

```math
\boxed{4,232,349}
```

candidate/case evaluations if every applicable primary candidate is evaluated on every valid corresponding assay case.

These counts are bookkeeping consequences of the already frozen candidate scopes and system grammar. They are not effect sizes and carry no scientific weighting by themselves.

---

# Part B — Family-native semantic contracts

## 8. F1 — Finite deterministic partial-action systems

### 8.1 World type

```math
\boxed{
\mathfrak W_{F1}
=(X,\mathcal A,\delta,\kappa)
}
```

with:

```math
X=[n],
\qquad
\mathcal A=[m],
\qquad
\delta_a:X\rightharpoonup X.
```

`\kappa` carries only the declared path/horizon/accounting semantics required by the operational baseline. It may not inject candidate-specific structure.

### 8.2 Generation

Every deterministic partial-action transition table inside the Section 6.1 bound is generated.

Each action `a` independently has an entry for every state:

```math
\delta_a(x)\in X\cup\{\bot\}.
```

No generator knob is provided for “interesting” density, cycles, sinks, or branching. Those properties emerge from the exhaustive grammar.

### 8.3 Canonicalization

F1 labeled transition tables are quotiented by the frozen simultaneous state/action relabeling isomorphism:

```math
\phi_X:X\to X',
\qquad
\phi_A:\mathcal A\to\mathcal A'.
```

Canonicalization chooses one deterministic representative per isomorphism class.

### 8.4 Derived metadata

After generation, but before candidate evaluation, the following may be computed as descriptive metadata:

- number of executable edges;
- branching counts;
- sinks;
- strongly connected components;
- cycles;
- raw path counts within declared horizons;
- and other deterministic functions of the operational object.

None is a primary generation or weighting variable.

---

## 9. F2 — State / observation / future-equivalence separation

### 9.1 World type

```math
\boxed{
\mathfrak W_{F2}
=(X,\mathcal A,\delta,\Pi_O,\kappa)
}
```

where `(X,\mathcal A,\delta,\kappa)` obeys F1 semantics and

```math
\Pi_O\in\operatorname{Part}(X)
```

is an observation partition.

### 9.2 Observation semantics

The partition induces observation equivalence:

```math
x\equiv_O y
\iff
x,y\text{ lie in the same block of }\Pi_O.
```

No arbitrary numerical observation labels are used as a scientific degree of freedom.

### 9.3 Generation order

The exact order is:

```text
F1 operational table
      ↓
all state partitions Pi_O
      ↓
F2 canonicalization
      ↓
derived relation comparisons
```

Future-transformational equivalence is never used to choose the observation partition.

### 9.4 Required distinction

The family must preserve the possibility of distinct relationships among:

```math
x=y,
\qquad
x\equiv_Oy,
\qquad
\mathcal T(x)=\mathcal T(y).
```

The generator does not preselect relation patterns. They emerge from the completed operational and observation data.

---

## 10. F3 — Regime bundle with finite resource automaton

### 10.1 World type

```math
\boxed{
\mathfrak W_{F3}
=
(X,\mathcal A,\delta,\mathcal B,\preceq_B,u,c,R)
}
```

with:

- finite state set `X` and action set `\mathcal A`;
- deterministic partial action maps `\delta_a`;
- finite resource configuration set `\mathcal B=\{0,1\}`;
- strict resource order `0\prec_B1`;
- deterministic resource update/admissibility map
  
  ```math
  u:\mathcal B\times E\to\mathcal B\cup\{\bot\};
  ```
- edge cost
  
  ```math
  c:E\to\{0,1\};
  ```
  extended additively to raw executable paths;
- finite regime bundle `R` whose elements are pairs
  
  ```math
  r=(B_r,H_r);
  ```
  with `H_r\in\{1,2\}`.

Each regime induces the ordinary operational object:

```math
\mathfrak O_r=(X,\mathcal A,\operatorname{Exec},\kappa_r)
```

with:

```math
\kappa_r=(B_r,H_r,u,c).
```

The primary F3 assay unit is the **regime bundle**, not a single selected regime, because the family is defined by the coexistence of the declared resource/horizon regimes.

### 10.2 Raw paths and regime admissibility

For a raw executable path

```math
\pi=e_1\cdots e_k,
```

with initial resource configuration `b_0=B_r`, define:

```math
b_j=u(b_{j-1},e_j).
```

A path is regime-admissible iff:

```math
k\le H_r
```

and no resource update returns `\bot`.

The raw-path cost is additive:

```math
c(\pi)=\sum_{j=1}^{k}c(e_j).
```

### 10.3 No monotonicity assumption

The resource update is **not** required to be monotone under `\preceq_B`:

```math
\boxed{
u\text{ is not required to be monotone under }\preceq_B.}
```

No monotone and non-monotone cases are preselected. Any such relation is an empirical/structural result of the frozen grammar.

### 10.4 Generation and deduplication

All F3 operational tables, resource-update choices, costs, horizons, and regime-bundle configurations allowed by the frozen grammar are generated before candidate applicability is considered.

The canonicalization unit is the complete regime bundle under the declared typed isomorphisms, including resource and regime transport. Candidate-specific properties may not be used to collapse regime bundles.

---

## 11. F4 — Deterministic raw core with exact history-indexed extension semantics

### 11.1 World type

F4 begins from a deterministic raw core:

```math
\boxed{
\mathfrak W_{F4}
=(X,\mathcal A,\delta,\alpha_\kappa,H)
}
```

with `1\le n,m\le2` and `H\in\{1,2\}`.

Unlike F3, F4 has no candidate-designed memory mechanism and no resource policy intended to guarantee a particular compressed state.

### 11.2 Exhaustive raw histories

Generate all raw histories through the frozen horizon:

```math
h_t=(x_0,a_0,x_1,a_1,\ldots,a_{t-1},x_t).
```

Let

```math
\mathcal H_{\le H}^{raw}
```

be the complete finite raw history carrier generated by the deterministic raw core.

Only histories that satisfy the raw operational relation are eligible to generate continuation decisions.

This normalization convention removes inert decisions occurring after already-inadmissible prefixes; it does not add a candidate-specific semantic criterion.

### 11.3 History-indexed extension table

For every raw history `h` of length `<H` and every raw executable transition

```math
\operatorname{Exec}(x_t(h),a,x'),
```

freeze a binary extension-admissibility bit:

```math
\boxed{
\alpha_\kappa(h,a,x')\in\{0,1\}.
}
```

The extension `hax'` is admissible iff:

1. `h` is admissible;
2. `Exec(x_t(h),a,x')` holds;
3. `\alpha_\kappa(h,a,x')=1`.

The history-indexed future-transformability set is therefore:

```math
\boxed{
\mathcal T^\kappa(h)
=
\{(a,x'):
\operatorname{Exec}(x_t(h),a,x')
\land
\alpha_\kappa(h,a,x')=1
\}.
}
```

This construction allows histories with the same current state to have either equal or unequal future-transformability sets. Neither outcome is preselected.

### 11.4 Family-validity condition

A primary F4 instance must contain a nonvacuous current-state collision:

```math
\boxed{
\exists t\le H,\ \exists h\ne h'\in\mathcal H_t:
 x_t(h)=x_t(h').
}
```

The collision itself is a family-validity requirement, not a candidate-specific filter.

The future-transformability sets for the colliding histories may be equal or unequal.

### 11.5 F4 quotient construction is separate from world generation

The exact T-blind sufficient-state quotient machinery is defined by the frozen candidate specification and is executed only after the F4 world itself is frozen.

During world generation, candidate quotient outcomes are never inspected.

After world freeze, all admissible finite history quotients required by the candidate specification are exhaustively generated subject only to:

- current-state refinement;
- deterministic causal updateability.

The construction may not inspect `\mathcal T`, candidate outcomes, or future-transformational distinctness while proposing, ranking, filtering, or editing quotient candidates.

Sufficiency is then tested as a separate property:

```math
f(h)=f(h')
\Rightarrow
\mathcal T^\kappa(h)=\mathcal T^\kappa(h').
```

The identity on complete histories is retained only as a terminal control.

### 11.6 F4 Bell-number boundary

The V1 horizon statement is exactly:

> F4 V1 adopts `Hmax=2` because it is the largest declared horizon for which exhaustive admissible-quotient generation is prospectively guaranteed feasible under a simple complete-partition enumeration strategy.

The number `B_8=4,140` is the unrestricted partition ceiling for the maximum terminal carrier at `H=2`.

The number `B_{16}=10,480,142,147` is the unrestricted partition ceiling for a possible terminal carrier at `H=3`.

Neither number is the number of admissible quotient candidates in the actual assay.

---

## 12. F5 — Dedicated intersection-typed representation-twin grammar

### 12.1 Base-world type

F5 begins from the intersection-typed base grammar:

```math
\boxed{
W_{base}=(X,\mathcal A,\delta,c,H)
}
```

with:

- deterministic partial action maps `\delta_a`;
- nonnegative raw edge cost `c` extended additively over executable paths;
- frozen finite history horizon `H=2`;
- no history-dependent admissibility in the base world.

The base grammar is intentionally strong enough to type every primary F5-scoped candidate without candidate filtering:

```text
ALG  executable paths
REL  state-indexed T / exact kernel quotient
COMB operational graph
TOP  SCC reachability order
GEO  raw-path additive cost
INF  finite history carrier
DYN  deterministic partial action dynamics
```

A candidate does not cause a base world to enter or leave F5 because the base lacks a field the candidate happens to want. Type validity is determined by the frozen intersection grammar itself.

### 12.2 Base bounds

Primary bases satisfy:

```math
2\le n,m\le3,
\qquad
nm\le6,
\qquad
c(e)\in\{0,1\},
\qquad
H=2.
```

### 12.3 Base canonicalization

All labeled bases are canonicalized first under the frozen state/action relabeling relation.

The canonical base-world set is the F5 base universe.

### 12.4 Exhaustive recoding ledger

For each canonical base `W`, construct:

```math
\boxed{
\mathcal R(W)
=
\{(W,\phi_X,\phi_A):
\phi_X\in\operatorname{Bij}(X),
\phi_A\in\operatorname{Bij}(\mathcal A)
\}.
}
```

The identity map is included.

All state bijections and all action bijections are enumerated exhaustively.

No F5 recoding is discarded because another recoding looks equivalent.

The reason is methodological: F5 is itself the representation-invariance assay, so the recoding dimension is the tested representation change and must remain visible in the provenance ledger.

### 12.5 Recoding semantics

For

```math
\phi=(\phi_X,\phi_A),
```

the recoded execution relation satisfies exactly:

```math
\boxed{
\operatorname{Exec}(x,a,y)
\iff
\operatorname{Exec}'(\phi_X(x),\phi_A(a),\phi_X(y)).
}
```

All operational accounting semantics are transported exactly, including:

- path horizon;
- budget semantics;
- transition costs;
- admissibility rules;
- and any other operationally declared resource quantities.

Numeric labels, lexical names, serialization order, memory addresses, and coordinates have no operational meaning unless explicitly included in the frozen operational contract.

### 12.6 Continuous-coordinate boundary

Continuous-coordinate recodings are not part of F5 primary V1.

Any such extension requires a separate prospective preregistration amendment before inspection of the added outcomes.

---

# Part C — Candidate applicability firewall

## 13. Applicability audit occurs after world freeze

Once the complete family universe has been generated, canonicalized, validated, and frozen, candidate applicability is computed as:

```math
\boxed{
A_{iW}
=
1[W\in\operatorname{Dom}(C_i)].
}
```

This audit is semantic typing only.

It cannot:

- delete a generated world;
- repair an invalid world;
- change a world bound;
- alter canonicalization;
- alter F5 recoding coverage;
- assign scientific weights;
- or choose a more favorable representation.

An inapplicable candidate/world pair is a typed non-assay pair, not a failed candidate result.

Candidate applicability is therefore conceptually downstream of world construction:

```text
WORLD UNIVERSE FROZEN
        ↓
APPLICABILITY AUDIT
        ↓
VALID TYPED CANDIDATE/CASE PAIRS
```

---

## 14. Candidate-scope consistency check

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

Therefore the expected primary candidate/case evaluation arithmetic is:

```math
F1: 5
F2: 5
F3: 6
F4: 4
F5: 7
```

per applicable family case, yielding the Section 7 total when multiplied by the frozen assay-case counts.

This arithmetic is a bookkeeping control, not a new scientific choice.

---

# Part D — Freeze and validation gates

## 15. Gate S0 — Manifest completeness

Before any system is generated, verify that this manifest contains, for every family in scope:

- exact semantic type;
- exact finite bounds;
- exact generation grammar;
- canonicalization rule;
- identity/provenance rule;
- any family-native validity condition;
- any exhaustive enumeration requirement;
- and the explicit candidate-independence firewall.

Missing construction semantics are a control failure.

### S0 output

```text
SYSTEM CONSTRUCTION SPECIFICATION = COMPLETE / STOP
```

---

## 16. Gate S1 — Scientific custody lock

Record:

```text
Parent scientific contract: 9711a6d
Parent candidate ontology: 7d1e3cf
System construction manifest: this exact V1 artifact
```

After S1, the following are frozen for V1 primary analysis:

- family definitions;
- construction bounds;
- enumeration requirements;
- canonicalization rules;
- world/assay-case identity rules;
- no-weighting rule;
- F3 resource semantics;
- F4 history semantics and horizon;
- F5 base/recoding distinction.

Any later change must be prospective V2/amendment work.

---

## 17. Gate S2 — Zero-world verification

Immediately before implementation begins, verify:

```text
raw constructions generated        = 0
canonical worlds generated         = 0
F5 recoding cases generated        = 0
candidate/case outcomes observed   = 0
```

The manifest must be committed and state-recorded while these quantities remain zero.

---

## 18. Gate S3 — Generator determinism

The implementation must demonstrate that a frozen generation run is a deterministic function of:

```text
manifest version
+ family
+ frozen bounds
+ frozen grammar
+ fixed canonicalization rule
```

and not of:

```text
candidate outputs
+ candidate ordering
+ model judgment
+ execution outcomes
+ post-hoc weighting
```

Repeated generation under identical inputs must reproduce identical raw construction identities and canonical world identities.

A generator disagreement is a control failure.

---

## 19. Gate S4 — Construction completeness

For every family with an exhaustive declaration, completeness must be checked against the finite grammar.

At minimum, controls must establish:

```text
no permitted raw construction omitted
no prohibited construction included
no permitted canonical class omitted
no distinct canonical class merged incorrectly
```

F4 must additionally establish complete raw-history coverage and complete extension-table coverage.

F5 must additionally establish all state bijections, all action bijections, and identity-recoding coverage for every canonical base.

No candidate outcome may be consulted to certify completeness.

---

## 20. Gate S5 — Family validity

Every generated object is independently tested against its family semantic contract.

Invalid objects are marked as construction failures and retain provenance explaining the failure.

They are not silently repaired, and candidate performance may not be used to decide whether an invalid object should be restored.

F4 family validity specifically requires the declared nonvacuous current-state collision.

F5 validity specifically requires exact operational equivalence of each recoding.

---

## 21. Gate S6 — Canonical-world freeze

Only after generation completeness and family validity pass may the canonical primary universe be frozen.

For F5, canonical base worlds are frozen first and the exhaustive recoding ledger is then generated from those bases without deduplication.

After this gate:

```math
\boxed{
\text{world set and required F5 recoding set are immutable for V1 primary evaluation}.
}
```

A candidate failure may not trigger insertion of a new world.

A candidate success may not trigger deletion of a world.

A candidate-specific counterexample may be minimized only inside the already frozen universe.

---

## 22. Gate S7 — Applicability freeze

After the world/assay universe is frozen, evaluate candidate semantic applicability.

Store:

```math
A_{iW}=1[W\in\operatorname{Dom}(C_i)].
```

This creates the candidate/case evaluation matrix but does not mutate the world universe.

No candidate-specific applicability rule may be added after this point.

---

## 23. Gate S8 — Implementation separation

Only after the construction lock and universe freeze are established may implementations of the candidate constructions be executed.

Implementation code must be checked against the already-frozen mathematical candidate records.

The implementation may not reinterpret:

- a world bound;
- a family definition;
- an observation partition;
- F3 resource semantics;
- F4 history normalization;
- F5 recoding maps;
- or a candidate's semantic applicability.

Implementation failure is always a control failure unless a prospective amendment explicitly changes the scientific contract before the affected evaluation is interpreted.

---

# Part E — Provenance ledger requirements

## 24. Minimum required provenance fields

Every generated artifact must carry or be recoverable from a ledger containing at least:

```text
family_id
raw_construction_id
canonical_world_id
manifest_version
parent_scientific_lock
parent_candidate_lock
generation_rule_id
canonicalization_rule_id
validation_status
```

F4 additionally records:

```text
history_horizon
history_normalization_rule_id
extension_table_identity
```

F5 additionally records:

```text
BaseID
InstanceID
phi_X
phi_A
RecodingID
identity_recoding_flag
```

Candidate/case evaluation records additionally reference the candidate ID and the frozen applicability bit, but candidate outcomes are written only after the system universe and applicability interfaces are frozen.

---

## 25. Primary-case immutability

Once the valid primary assay universe has been frozen, each assay case has immutable identity.

The following operations are prohibited in V1:

```text
edit a world because a candidate fails
edit a world because a candidate succeeds
change canonical labels to simplify a candidate
remove a world because it is redundant to a candidate
add a world because a candidate has no counterexample
remove an F5 recoding because another recoding looks identical
weight a world because it is unusually diagnostic
```

Any such action creates a protocol violation or prospective V2/amendment issue, not a V1 repair.

---

# Part F — Explicit anti-leakage statements

## 26. Construction must precede candidate knowledge

The system-generation logic must be executable even in a context where no candidate implementation exists.

```math
\boxed{
\text{generator meaning does not depend on candidate existence.}
}
```

## 27. Candidate ontology cannot reach backward

The locked candidate ontology may describe semantic applicability to a frozen world, but it may not determine:

```text
which worlds exist
which worlds are canonical
which recodings are retained
which worlds receive weight
which worlds are rejected
which bounds are used
```

Those decisions are fully specified here.

## 28. Candidate outcomes cannot reach backward

No result generated by `C_i`, `P_i`, or a candidate implementation may modify this manifest during V1 evaluation.

```math
\boxed{
\text{candidate outcome}
\not\rightarrow
\text{V1 arena repair}.
}
```

## 29. Learning is downstream

STRUCTURE-001 V1 permits scientific learning from the frozen experiment, but such learning may only determine:

```text
prospective V2 / amendment / extension decisions
```

and may not alter the evidentiary meaning of V1 results.

```math
\boxed{
\text{learning from an experiment}
\neq
\text{changing the experiment}.
}
```

---

# Part G — Frozen arena summary

## 30. V1 construction object

The system-construction layer is summarized as:

```math
\boxed{
\mathcal U_{V1}
=
\mathcal U_{F1}
\cup
\mathcal U_{F2}
\cup
\mathcal U_{F3}
\cup
\mathcal U_{F4}
\cup
\mathcal U_{F5}^{recoding}
}
```

where each family universe is generated without candidate knowledge, canonicalized only under its declared family identity relation, and frozen before candidate applicability or outcome is interpreted.

The five families deliberately stress different semantic dimensions:

```text
F1  finite partial execution
F2  observation / state / future-equivalence separation
F3  resources / regimes / horizons
F4  history-indexed admissibility
F5  exact representation twins
```

The resulting structure is therefore:

```text
operational grammar
      ↓
finite raw construction universe
      ↓
family validity
      ↓
canonical world / assay-case universe
      ↓
F5 exhaustive recoding ledger
      ↓
V1 world freeze
      ↓
candidate applicability
      ↓
implementation
      ↓
primary evaluation
```

The arena is not constructed to prove any candidate. It is constructed to make candidate behavior answerable against a world universe whose membership was fixed without observing that behavior.

---

## 31. Claim ceiling of this artifact

This manifest establishes only the **construction contract** for STRUCTURE-001 V1.

It does not establish:

- that any candidate survives;
- that any candidate is refuted;
- that any candidate family is foundational;
- that the numerical universe is scientifically representative beyond its declared finite bounds;
- that the V1 bounds are optimal;
- or that Revisics has a universal mathematical law.

The strongest statement justified by this artifact alone is:

```math
\boxed{
\text{STRUCTURE-001 V1 has a prospectively declared, candidate-independent finite arena construction contract.}
}
```

Scientific conclusions require valid implementation, control passage, frozen-world provenance, and candidate evaluation under the already locked contracts.

---

## 32. Status inscription

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
\boxed{
\text{third stone: cut before contact with the worlds.}
}
```
