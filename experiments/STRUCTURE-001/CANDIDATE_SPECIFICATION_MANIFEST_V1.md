# STRUCTURE-001 — Candidate Specification Manifest V1

**Status:** Prospective candidate-specification draft  
**Parent scientific contract:** `STRUCTURE-001 V1 @ 9711a6dd1b14ade10fd43a03c424ddc840cc565e`  
**Scientific role:** Candidate ontology and candidate contracts only  
**System construction:** NOT STARTED  
**Implementation:** NOT STARTED  
**Execution:** NOT STARTED

---

## 0. Purpose and custody boundary

This artifact is the candidate-specification layer required by STRUCTURE-001 V1.

Its only scientific purpose is to define, prospectively and independently of candidate behavior, the exact mathematical candidates that may enter the V1 primary analysis.

The governing invariant is:

```math
\boxed{ \text{candidate ontology is fixed independently of candidate behavior}. }
```

The custody order is:

```text
STRUCTURE-001 V1 @ 9711a6d
        ↓
CANDIDATE SPECIFICATION SCHEMA
        ↓
INSTANTIATED CANDIDATE RECORDS
        ↓
CANDIDATE SPECIFICATION LOCK
        ↓
SYSTEM-CONSTRUCTION MANIFEST
        ↓
IMPLEMENTATION
        ↓
CONTROLS
        ↓
EXECUTION
```

This file contains **no F1–F5 system instance**, no hand-designed adversarial world, no implementation decision, and no outcome.

No candidate may be added, removed, repaired, narrowed, broadened, re-scoped, or redefined in the V1 primary analysis after the candidate-specification lock. Any later candidate is a prospective extension and is reported separately.

The critical causal prohibition is:

```math
\boxed{ \text{candidate outcomes} \not\rightarrow \text{candidate ontology}. }
```

---

# Part A — Candidate Specification Schema

## A1. Hard semantic-completeness rule

Every primary candidate must be completely meaningful before any exact F1–F5 instance exists.

For candidate `S_i`, the frozen contract is:

```math
\boxed{
S_i=
\left(
C_i,
P_i,
Z_i,
\cong_i,
\tau^i_\phi,
\operatorname{Scope}(S_i)
\right).
}
```

The construction direction is always:

```math
\boxed{
\mathfrak O
\overset{C_i}{\longmapsto}
S_{i,\mathfrak O,z},
\qquad z\in Z_i(\mathfrak O).
}
```

No candidate definition may refer to the behavior of an eventual test instance.

---

## A2. Candidate definition is not candidate success

For every candidate:

```math
\boxed{ \text{candidate definition} \neq \text{candidate success criterion}. }
```

`C_i` defines what mathematical object is constructed from the frozen operational object and declared auxiliary choice.

`P_i` defines the exact candidate claim tested on that object.

`C_i` may not contain a branch such as “choose the construction that satisfies `P_i`,” and `P_i` may not be defined as “whatever property the constructed object has.”

The construction and claim must be independently inspectable.

---

## A3. Semantic type domain

Every candidate declares a semantic applicability domain:

```math
\boxed{ \operatorname{Dom}(C_i). }
```

`Dom(C_i)` may state only semantic or typing conditions required for the construction to be meaningful.

It may refer to facts such as:

- finiteness of a carrier;
- determinism or nondeterminism of an execution relation;
- existence of a declared path semantics;
- existence of a declared resource or cost field in `\kappa`;
- existence of a declared observation map;
- whether future-transformability is state-indexed or history-indexed.

It may **not** contain empirical expectations, performance filters, or conditions selected because the candidate is expected to survive them.

Formally:

```math
\boxed{
\operatorname{Dom}(C_i)
\text{ may state semantic applicability conditions, never empirical expectations.}
}
```

A condition whose only justification is that the candidate is likely to pass under that condition is prohibited.

---

## A4. Construction map `C_i`

The construction map must be exact and deterministic conditional on `z`:

```math
C_i:(\mathfrak O,z)\mapsto S_{i,\mathfrak O,z}.
```

The record must specify:

1. input type;
2. output type;
3. exact mathematical construction;
4. whether the construction uses one-step `\mathcal T`, a declared path/horizon closure, histories, resources, or another object already permitted by V1;
5. all explicit auxiliary inputs.

No exact F1–F5 instance may appear in the definition.

---

## A5. Candidate property `P_i`

`P_i` is the exact primary claim made about `C_i(\mathfrak O,z)`.

The quantifier structure must be explicit.

For example, if a property must hold for every action, path, state, equivalence class, or auxiliary choice, that universal quantifier is part of `P_i` and may not be weakened after system construction.

A candidate is refuted only when its exact frozen `P_i` fails within its prospectively declared scope under valid controls.

Failure of `P_i` does not refute the surrounding mathematical family unless that stronger claim was itself preregistered.

---

## A6. Auxiliary-choice class `Z_i`

The candidate must freeze the complete admissible candidate-relevant auxiliary-choice class:

```math
Z_i(\mathfrak O).
```

Every non-operational degree of freedom capable of changing either `P_i` or the `\cong_i`-class of the output while leaving `\mathfrak O` unchanged must appear explicitly in `Z_i`.

No such freedom may be hidden in:

- the prose definition of `C_i`;
- a coordinate convention;
- an ordering;
- a tie-break rule;
- a basis;
- a normalization;
- an embedding;
- a neighborhood rule;
- serialization order;
- an implementation default;
- or the definition of `P_i` or `\cong_i`.

If

```math
Z_i(\mathfrak O)=\{\varnothing\},
```

the record must include a prospective auxiliary-completeness argument showing that no candidate-relevant non-operational freedom remains.

---

## A7. Output equivalence `\cong_i`

Every candidate declares what counts as the same mathematical output.

This may be, depending on type:

- literal equality;
- equality of scalar invariants;
- graph isomorphism;
- order isomorphism;
- homeomorphism induced by operational transport;
- isometry;
- lattice isomorphism;
- conjugacy of partial action systems;
- or another exact equivalence defined prospectively.

Raw state names, action names, serialization order, and arbitrary coordinates are never evidence of inequivalence unless the operational contract gives them semantic meaning.

---

## A8. Operational isomorphism and auxiliary transport

For each admissible operational isomorphism

```math
\phi:\mathfrak O\simeq\mathfrak O',
```

the candidate must define an exact auxiliary transport when its representation-invariance scope requires one:

```math
\boxed{
\tau^i_\phi:
Z_i(\mathfrak O)
\leftrightarrow
Z_i(\mathfrak O').
}
```

It must satisfy:

```math
\tau^i_{\mathrm{id}}=\mathrm{id}
```

and, whenever the operational maps compose,

```math
\tau^i_{\psi\circ\phi}
=
\tau^i_\psi\circ\tau^i_\phi.
```

Representation invariance is tested by:

```math
\boxed{
\forall z\in Z_i(\mathfrak O),\quad
C_i(\mathfrak O,z)
\cong_i
C_i(\mathfrak O',\tau^i_\phi(z)).
}
```

If `Z_i={\varnothing}`, then `\tau^i_\phi(\varnothing)=\varnothing`.

---

## A9. Prospectively declared family scope

Each candidate declares:

```math
\boxed{
\operatorname{Scope}(S_i)
\subseteq
\{F1,F2,F3,F4,F5\}.
}
```

Scope is frozen before system construction.

Each included family must have a semantic reason for inclusion. Each excluded family must have a typed or applicability reason for exclusion.

The following is prohibited:

> “F3 excluded because this candidate is unlikely to work there.”

The following kind of statement is permitted:

> “F4 excluded because this candidate requires construction from current-state future-transformability, while the F4 primary sufficient-state lane prohibits target-informed quotient generation.”

Scope may not be altered after candidate performance is observed.

---

## A10. Prospective failure contract

Each candidate must declare all four outcome boundaries in advance.

### `CONDITIONAL_IF`

State the exact observation or counterfactual auxiliary variation that would show the candidate depends on additional assumptions or non-operational choice.

### `REPRESENTATION_DEPENDENT_IF`

State the exact failure of transport invariance:

```math
\exists\phi,z:\quad
C_i(\mathfrak O,z)
\not\cong_i
C_i(\mathfrak O',\tau^i_\phi(z)).
```

### `REFUTED_IF`

State the exact failure of `P_i` within declared scope under valid controls.

### `CONTROL_FAILURE_IF`

State failures that invalidate scientific interpretation, including:

- type mismatch;
- incomplete auxiliary class;
- invalid auxiliary transport;
- failed enumeration control;
- provenance mismatch;
- implementation disagreement with `C_i`;
- or invalid operational-isomorphism control.

The permanent distinction is:

```math
\boxed{
\text{CONTROL FAILURE}
\neq
\text{candidate refutation}.
}
```

---

## A11. Forbidden stronger interpretation

Every record includes a statement of what survival would **not** establish.

A surviving candidate may receive only the V1 label:

```text
FORCED_AT_TESTED_SCOPE
```

under its frozen scope and claim ceiling.

No record may silently promote survival into:

- a universal law of Revisics;
- a universal structure for all future-transformability;
- uniqueness of the mathematical representation;
- or foundational status for an entire mathematical family.

---

## A12. Candidate-family coverage rule

STRUCTURE-001 V1 listed candidate families, not mandatory winners.

The primary ontology therefore permits:

```text
NO CLEAN PRIMARY CANDIDATE IN THIS FAMILY
```

when no exact candidate passes the specification gate.

A family is not populated merely for aesthetic completeness.

```math
\boxed{
\text{candidate family in battery}
\not\Rightarrow
\text{mandatory candidate}.
}
```

---

# Part B — Instantiated Candidate Records

## B0. Candidate index

The V1 candidate ontology contains the following primary candidates:

| Candidate ID | Layer | Short name | Declared scope |
|---|---|---|---|
| `S-ALG-001` | Algebraic | Executable-path partial composition | F1, F2, F3, F4, F5 |
| `S-REL-001` | Relational | Exact future-transformational kernel quotient | F1, F2, F3, F5 |
| `S-COMB-001` | Combinatorial | Mutual-reachability condensation order | F1, F2, F3, F4, F5 |
| `S-TOP-001` | Topological | Reachability Alexandrov topology on the condensation quotient | F1, F2, F3, F4, F5 |
| `S-GEO-001` | Geometric | Cost-induced directed extended metric | F3, F5 |
| `S-INF-001` | Informational | T-blind admissible history-quotient lattice | F4, F5 |
| `S-DYN-001` | Dynamical | Descent of action dynamics to future-equivalence classes | F1, F2, F3, F5 |

No standalone `S-INV-*` primary candidate is instantiated in this manifest.

Reason: representation invariance is already a required criterion for every candidate, and no nonredundant standalone invariant construction has yet met the candidate-specification standard without collapsing into another listed candidate. This is an ontology decision made before system construction, not an observed failure.

---

# `S-ALG-001` — Executable-path partial composition

**Layer:** Algebraic  
**Name:** Executable-path partial composition

### Scientific claim

Finite executable paths generated by the declared operational relation admit a canonical typed partial composition by path concatenation, with associativity wherever the relevant composites are defined.

### Type domain `Dom(C)`

Operational objects for which:

1. finite executable paths are semantically defined from `\operatorname{Exec}`;
2. source and target state of each path are defined;
3. `\kappa` determines whether a concatenated path is admissible.

These are semantic typing conditions only.

### Construction `C`

Let `\Pi_\kappa(\mathfrak O)` be the set of all finite `\kappa`-admissible execution paths

```math
\pi=(x_0,a_0,x_1,\ldots,a_{n-1},x_n)
```

whose adjacent triples satisfy `\operatorname{Exec}`.

Define source and target:

```math
s(\pi)=x_0,
\qquad
t(\pi)=x_n.
```

For paths `\pi_1,\pi_2`, define

```math
\pi_2\circ\pi_1
```

iff:

1. `t(\pi_1)=s(\pi_2)`; and
2. the literal concatenated path is `\kappa`-admissible.

The output is the typed partial algebra

```math
C_{\mathrm{ALG}}(\mathfrak O)
=
(\Pi_\kappa,s,t,\circ).
```

### Claim `P`

For all composable triples `\pi_1,\pi_2,\pi_3`, whenever either side is defined under the frozen partial-operation semantics, both sides are defined together and

```math
(\pi_3\circ\pi_2)\circ\pi_1
=
\pi_3\circ(\pi_2\circ\pi_1)
```

as literal paths.

No identity element is claimed unless empty paths are separately declared admissible by `\kappa`; identity structure is not part of the primary claim.

### Auxiliary class `Z`

```math
Z_{\mathrm{ALG}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

Path concatenation is literal sequence concatenation. Source, target, and admissibility are read from the frozen operational object. No ordering, basis, coordinate, embedding, tie-break, or other non-operational choice enters the construction.

### Output equivalence `\cong`

Isomorphism of typed partial path algebras preserving source, target, and partial composition.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{ALG}}_\phi(\varnothing)=\varnothing.
```

An operational isomorphism transports each path pointwise through the induced state/action maps.

### Declared scope

```math
\operatorname{Scope}(S\text{-ALG-001})
=
\{F1,F2,F3,F4,F5\}.
```

**Scope justification:** the construction depends only on typed executable paths and `\kappa`, not on observation semantics, history compression, or representation labels.

### Failure contract

`CONDITIONAL_IF:` a candidate-relevant non-operational choice is required to determine path concatenation, source/target typing, or admissibility while `\mathfrak O` is fixed.

`REPRESENTATION_DEPENDENT_IF:` an admissible operational isomorphism fails to induce an isomorphism of the partial path algebra.

`REFUTED_IF:` a valid scoped operational object contains a composable triple for which the two bracketings differ or one bracketing is defined while the other is not under the frozen path semantics.

`CONTROL_FAILURE_IF:` path enumeration is incomplete, `\kappa` admissibility is implemented inconsistently, or path transport under an operational twin fails validation.

### Forbidden stronger interpretation

Survival does not establish that all future-transformability is fundamentally algebraic, categorical, or compositional.

---

# `S-REL-001` — Exact future-transformational kernel quotient

**Layer:** Relational  
**Name:** Exact future-transformational kernel quotient

### Scientific claim

Whenever future-transformability is a well-typed single-valued map on the declared current carrier, equality of future-transformability profiles induces the unique coarsest exact quotient that preserves those profiles.

### Type domain `Dom(C)`

Operational objects for which the V1-derived future-transformability object is a single-valued map

```math
\Theta_\mathfrak O:D\rightarrow Y,
\qquad
\Theta_\mathfrak O(d)=\mathcal T^\kappa(d),
```

on a declared current carrier `D`, with equality in `Y` prospectively typed.

The construction is not applicable in the F4 primary sufficient-state lane because F4 prohibits target-informed generation of candidate history quotients.

### Construction `C`

Define

```math
d\sim_{\mathcal T}d'
\iff
\Theta_\mathfrak O(d)=\Theta_\mathfrak O(d').
```

Let

```math
Q_\mathcal T=D/{\sim_\mathcal T}
```

and let

```math
q_\mathcal T:D\rightarrow Q_\mathcal T
```

be the canonical quotient map.

### Claim `P`

1. `\sim_\mathcal T` is an equivalence relation.
2. `\Theta_\mathfrak O` is constant on every fiber of `q_\mathcal T`.
3. For every quotient `q:D\rightarrow Q` satisfying

   ```math
   q(d)=q(d')\Rightarrow \Theta_\mathfrak O(d)=\Theta_\mathfrak O(d'),
   ```

   `q` refines `q_\mathcal T`.

Thus `q_\mathcal T` is the coarsest exact quotient preserving the declared future-transformability profile.

### Auxiliary class `Z`

```math
Z_{\mathrm{REL}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

The relation is the kernel equivalence of the frozen map `\Theta_\mathfrak O`. No clustering threshold, metric, ordering, tie-break, embedding, or approximate equality is permitted.

### Output equivalence `\cong`

Isomorphism of quotient sets induced by operational transport, preserving quotient fibers and transported `\Theta` values.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{REL}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\operatorname{Scope}(S\text{-REL-001})
=
\{F1,F2,F3,F5\}.
```

**F4 exclusion:** semantic/methodological. The F4 primary sufficient-state construction must be generated without inspection of `\mathcal T`; this candidate is explicitly defined as the kernel of `\mathcal T` and therefore cannot serve as an F4 candidate-generation mechanism under V1.

### Failure contract

`CONDITIONAL_IF:` equality of future-transformability requires an unfrozen tolerance, metric, matching rule, or other non-operational choice.

`REPRESENTATION_DEPENDENT_IF:` an admissible operational isomorphism changes the quotient partition beyond the induced transport.

`REFUTED_IF:` `\sim_\mathcal T` fails equivalence or there exists an exact `\Theta`-preserving quotient strictly coarser than `q_\mathcal T`.

`CONTROL_FAILURE_IF:` `\Theta` is not single-valued on the declared carrier, future-transformability equality is mistyped, or quotient enumeration/factorization is implemented incorrectly.

### Forbidden stronger interpretation

Survival does not establish that future-transformational equivalence is the uniquely useful quotient for all future tasks, approximate settings, or history-dependent systems.

---

# `S-COMB-001` — Mutual-reachability condensation order

**Layer:** Combinatorial  
**Name:** Mutual-reachability condensation order

### Scientific claim

Finite operational reachability induces a quotient into mutually reachable components whose inter-component reachability is acyclic and forms a partial order.

### Type domain `Dom(C)`

Finite operational carriers with a declared finite-path reachability relation

```math
R_\kappa\subseteq D\times D
```

derived from `\operatorname{Exec}` and the frozen path/horizon semantics.

### Construction `C`

Define mutual reachability:

```math
x\approx_R y
\iff
R_\kappa(x,y)\land R_\kappa(y,x).
```

Let

```math
K=D/{\approx_R}.
```

Define the component relation

```math
[A]\preceq_R[B]
\iff
R_\kappa(a,b)
```

for representatives `a\in[A]`, `b\in[B]`.

The output is

```math
C_{\mathrm{COMB}}(\mathfrak O)
=(K,\preceq_R).
```

### Claim `P`

1. `\approx_R` is an equivalence relation.
2. `\preceq_R` is well-defined on equivalence classes.
3. `\preceq_R` is a partial order.
4. The directed graph of strict inter-component reachability is acyclic.

### Auxiliary class `Z`

```math
Z_{\mathrm{COMB}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

The quotient uses exact mutual reachability and exact reachability between quotient classes. No graph layout, node ordering, traversal order, representative choice, or canonical-label convention contributes to the mathematical output.

### Output equivalence `\cong`

Order isomorphism of condensation quotients; equivalently, directed-acyclic-graph isomorphism preserving the reachability order.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{COMB}}_\phi(\varnothing)=\varnothing.
```

Operational transport maps a component to the component containing the transported states.

### Declared scope

```math
\operatorname{Scope}(S\text{-COMB-001})
=
\{F1,F2,F3,F4,F5\}.
```

**Scope justification:** the construction requires only finite typed reachability. For F4, the carrier may be the prospectively declared finite history carrier used by that family; this does not perform target-informed history compression.

### Failure contract

`CONDITIONAL_IF:` reachability itself requires an unfrozen path convention or representative-dependent rule.

`REPRESENTATION_DEPENDENT_IF:` operational twins yield non-isomorphic condensation orders under the induced transport.

`REFUTED_IF:` the quotient relation is not well-defined, antisymmetry fails between distinct components, or the strict condensation graph contains a directed cycle.

`CONTROL_FAILURE_IF:` reachability closure is incomplete, mutual-reachability components are enumerated incorrectly, or F5 transport fails validation.

### Forbidden stronger interpretation

Survival does not establish that the condensation order is a complete description of future-transformability or that all revisic structure is graph-theoretic.

---

# `S-TOP-001` — Reachability Alexandrov topology

**Layer:** Topological  
**Name:** Reachability Alexandrov topology on the condensation quotient

### Scientific claim

The exact operational reachability order on mutually reachable components induces a canonical Alexandrov topology whose specialization order recovers the operational reachability order under the frozen convention.

### Type domain `Dom(C)`

Finite operational objects satisfying the semantic typing needed to construct the quotient order `(K,\preceq_R)` directly from finite-path reachability.

### Construction `C`

Let `(K,\preceq_R)` be the mutual-reachability quotient order constructed directly from `\mathfrak O`.

Define

```math
\mathcal O_R
=
\{U\subseteq K:\forall x\in U,\ x\preceq_R y\Rightarrow y\in U\}.
```

That is, `\mathcal O_R` is the family of upward-closed sets in the operational reachability order.

The output is

```math
C_{\mathrm{TOP}}(\mathfrak O)
=(K,\mathcal O_R).
```

The upward-closed convention is part of this candidate definition; the claim concerns this exact construction and not “topology in general.”

### Claim `P`

1. `\mathcal O_R` is a topology on `K`.
2. It is Alexandrov: arbitrary intersections of open sets are open.
3. Under the frozen specialization-order convention

   ```math
   x\le_{\mathrm{spec}}y
   \iff
   \forall U\in\mathcal O_R,\ x\in U\Rightarrow y\in U,
   ```

   the specialization order equals `\preceq_R` exactly.
4. Because `K` is a partial order quotient, the topology is `T_0`.

### Auxiliary class `Z`

```math
Z_{\mathrm{TOP}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

This candidate is **not** the class of all topologies that could be placed on `K`. It is the single exact construction “upward-closed Alexandrov topology of operational reachability.” No neighborhood radius, metric, embedding, basis selection, graph layout, coordinate, or orientation is left free: orientation is frozen in the candidate definition and the claim is correspondingly narrow.

Any alternative topology construction is a different candidate and cannot be substituted into this record.

### Output equivalence `\cong`

Homeomorphism induced by the operationally transported order isomorphism on `K`; equivalently, isomorphism of the corresponding Alexandrov ordered spaces.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{TOP}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\operatorname{Scope}(S\text{-TOP-001})
=
\{F1,F2,F3,F4,F5\}.
```

**Scope justification:** the candidate requires finite operational reachability and its mutual-reachability quotient; it does not require geometric coordinates or observation semantics.

### Failure contract

`CONDITIONAL_IF:` this exact topology construction requires any additional unfrozen neighborhood, orientation, basis, weighting, or embedding choice beyond the frozen upward-closure rule.

`REPRESENTATION_DEPENDENT_IF:` operational twins fail to induce homeomorphic Alexandrov spaces under the transported quotient order.

`REFUTED_IF:` `\mathcal O_R` fails the topology axioms, fails Alexandrov closure, or its frozen specialization order fails to recover `\preceq_R`.

`CONTROL_FAILURE_IF:` the underlying quotient order is computed incorrectly or operational transport does not preserve the finite reachability relation.

### Forbidden stronger interpretation

Survival establishes only this exact reachability-induced Alexandrov construction at tested scope. It does not establish that topology as a mathematical family is uniquely foundational for Revisics.

---

# `S-GEO-001` — Cost-induced directed extended metric

**Layer:** Geometric  
**Name:** Cost-induced directed extended metric

### Scientific claim

When the operational accounting convention itself supplies a nonnegative additive path cost, minimal operational path cost induces a directed extended metric-like geometry that is invariant under cost-preserving operational recoding.

### Type domain `Dom(C)`

Operational objects for which `\kappa` prospectively and semantically declares:

1. a nonnegative transition/path cost `c`;
2. zero cost for the empty path;
3. path cost determined by the frozen operational path, not by representation labels;
4. additive concatenation cost:

   ```math
   c(\pi_2\circ\pi_1)=c(\pi_1)+c(\pi_2)
   ```

   whenever literal path concatenation is executable.

These are typing conditions for this cost-derived candidate, not empirical performance conditions.

### Construction `C`

Define

```math
d_\kappa(x,y)
=
\inf\{c(\pi):\pi\text{ is an executable path from }x\text{ to }y\},
```

with

```math
d_\kappa(x,y)=+\infty
```

when no executable path exists.

The output is the directed extended-distance space

```math
C_{\mathrm{GEO}}(\mathfrak O)
=(D,d_\kappa).
```

No symmetrization is performed.

### Claim `P`

For all `x,y,z` in the declared carrier:

```math
d_\kappa(x,x)=0,
```

```math
d_\kappa(x,z)
\le
 d_\kappa(x,y)+d_\kappa(y,z),
```

using extended-real arithmetic.

Symmetry and positive separation are **not** claimed.

The exact candidate is therefore a directed extended metric / Lawvere-style distance candidate, not an ordinary Euclidean metric claim.

### Auxiliary class `Z`

```math
Z_{\mathrm{GEO}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

The cost function is part of the frozen operational accounting convention `\kappa`. The candidate does not choose an embedding, symmetrization, norm, coordinate chart, weighting, kernel, or scale normalization. Any such added construction would be a different candidate.

### Output equivalence `\cong`

Isometry of directed extended-distance spaces under the state transport induced by the operational isomorphism.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{GEO}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\operatorname{Scope}(S\text{-GEO-001})
=
\{F3,F5\}.
```

**F3 inclusion:** resource/accounting semantics are the explicit scientific focus of F3.  
**F5 inclusion:** exact recoding is required to test whether the cost-derived geometry is representation invariant.

**F1/F2/F4 exclusion:** this primary candidate requires an operationally declared additive cost field in `\kappa`; those family roles do not, by definition, require such a field. This is a semantic applicability exclusion, not a prediction of failure.

### Failure contract

`CONDITIONAL_IF:` the distance requires any unfrozen choice of norm, embedding, symmetrization, rescaling, or path weighting not fixed by `\kappa`.

`REPRESENTATION_DEPENDENT_IF:` a cost-preserving operational twin fails to be an isometry under transported states.

`REFUTED_IF:` a valid scoped object satisfying `Dom(C)` violates zero self-distance or the directed triangle inequality.

`CONTROL_FAILURE_IF:` cost additivity, path-cost accumulation, infimum/minimum computation, or F5 cost transport is implemented incorrectly.

### Forbidden stronger interpretation

Survival does not establish Euclidean geometry, manifold structure, local differential geometry, symmetry, or a universal scalar of revisability.

---

# `S-INF-001` — T-blind admissible history-quotient lattice

**Layer:** Informational  
**Name:** T-blind admissible history-quotient lattice

### Scientific claim

The F4 admissible sufficient-state search space, generated without inspecting future-transformability, has an operationally induced refinement structure: the complete set of current-state-refining, causally updateable history equivalences forms a finite lattice under refinement.

### Type domain `Dom(C)`

Finite-history operational objects with:

1. a prospectively frozen finite evaluation horizon;
2. an exhaustively enumerable history carrier `H_t`;
3. the F4 current-state refinement rule;
4. the F4 causal-updateability rule.

The construction does **not** inspect `\mathcal T` and does not use later sufficiency outcomes.

### Construction `C`

Let `\mathcal Q_{\mathrm{adm}}(\mathfrak O)` be the set of all equivalence relations `E` on the finite history carrier satisfying:

1. **current-state refinement**

   ```math
   h\,E\,h'\Rightarrow x_t(h)=x_t(h');
   ```

2. **causal updateability / congruence**: whenever `h E h'` and both histories admit the same typed one-step extension `(a,x')`, the extended histories remain equivalent under the corresponding quotient update rule.

Order `\mathcal Q_{\mathrm{adm}}` by refinement:

```math
E_1\preceq E_2
\iff
E_1\subseteq E_2.
```

The output is

```math
C_{\mathrm{INF}}(\mathfrak O)
=(\mathcal Q_{\mathrm{adm}},\preceq).
```

No element is selected using `\mathcal T`.

### Claim `P`

For every valid scoped object:

1. `\mathcal Q_{\mathrm{adm}}` is finite and nonempty because the full-history identity equivalence is present as the terminal control;
2. arbitrary finite meets are given by intersection;
3. every pair has a least admissible upper bound under refinement;
4. therefore `(\mathcal Q_{\mathrm{adm}},\preceq)` is a finite lattice.

The claim concerns the **T-blind admissible quotient space**, not whether any nontrivial quotient is later sufficient for `\mathcal T`.

### Auxiliary class `Z`

```math
Z_{\mathrm{INF}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

The candidate output is the exhaustive set of all equivalence relations satisfying the frozen F4 syntactic/causal admissibility constraints. No candidate quotient is chosen, ranked, or filtered by future-transformability. Enumeration order and quotient labels have no semantic status.

### Output equivalence `\cong`

Lattice isomorphism induced by transport of histories and equivalence relations under the operational recoding.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{INF}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\operatorname{Scope}(S\text{-INF-001})
=
\{F4,F5\}.
```

**F4 inclusion:** the candidate is exactly about the prospectively generated, target-blind history-quotient search space required by F4.  
**F5 inclusion:** representation twins provide the explicit anti-artifact test for the quotient lattice.

**F1/F2/F3 exclusion:** those family roles do not require a history-quotient construction under the F4 causal-updateability constraints.

### Failure contract

`CONDITIONAL_IF:` generating the admissible quotient set requires an unfrozen heuristic, ordering, pruning rule, or target-informed choice.

`REPRESENTATION_DEPENDENT_IF:` operational twins yield non-isomorphic admissible quotient lattices under transported histories.

`REFUTED_IF:` a valid scoped object has an admissible quotient set that fails closure under finite meet or lacks a least admissible upper bound for some pair.

`CONTROL_FAILURE_IF:` the admissible quotient set is not exhaustively enumerated, current-state refinement or causal updateability is implemented incorrectly, or future-transformability leaks into quotient generation.

### Forbidden stronger interpretation

Survival does not establish that a nontrivial future-sufficient history quotient exists. That remains a later F4 scientific question under the frozen V1 decision rule.

---

# `S-DYN-001` — Descent of action dynamics to future-equivalence classes

**Layer:** Dynamical  
**Name:** Descent of action dynamics to future-equivalence classes

### Scientific claim

Exact future-transformational equivalence is a congruence for the declared one-step action dynamics only when action execution is class-consistent. When that condition holds, the action dynamics descend to a well-defined partial dynamical system on future-equivalence classes.

### Type domain `Dom(C)`

Operational objects for which:

1. current-state future-transformability is a single-valued typed map `\Theta_\mathfrak O(x)=\mathcal T^\kappa(x)`;
2. for each action `a`, one-step execution defines a deterministic partial transition

   ```math
   \delta_a:X\rightharpoonup X.
   ```

The candidate is not used in the F4 primary history-quotient lane because its equivalence relation is target-informed.

### Construction `C`

Construct the exact future-equivalence relation

```math
x\sim_\mathcal T y
\iff
\Theta_\mathfrak O(x)=\Theta_\mathfrak O(y).
```

Let

```math
Q_\mathcal T=X/{\sim_\mathcal T}.
```

For each action `a`, define a candidate quotient transition

```math
\bar\delta_a([x])=[\delta_a(x)]
```

whenever the right-hand side is well-defined independently of the representative.

The output is the candidate partial action system

```math
C_{\mathrm{DYN}}(\mathfrak O)
=(Q_\mathcal T,\{\bar\delta_a\}_{a\in\mathcal A}).
```

### Claim `P`

For every action `a` and all `x,y` with `x\sim_\mathcal T y`:

1. definedness is class-invariant:

   ```math
   \delta_a(x)\text{ defined}
   \iff
   \delta_a(y)\text{ defined};
   ```

2. whenever defined,

   ```math
   \delta_a(x)\sim_\mathcal T\delta_a(y).
   ```

If both hold, every `\bar\delta_a` is a well-defined partial map on `Q_\mathcal T`.

### Auxiliary class `Z`

```math
Z_{\mathrm{DYN}}(\mathfrak O)=\{\varnothing\}.
```

### Auxiliary-completeness argument

The candidate uses exact equality of `\Theta`, the declared deterministic action transition, and the induced quotient. No representative choice, approximate matching threshold, action ordering, coordinate, or tie-break enters the mathematical claim.

### Output equivalence `\cong`

Conjugacy/isomorphism of the quotient partial action systems under the quotient map induced by the operational isomorphism.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{DYN}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\operatorname{Scope}(S\text{-DYN-001})
=
\{F1,F2,F3,F5\}.
```

**F4 exclusion:** the candidate is constructed from target-informed current-state future-equivalence and therefore is not admissible as an F4 sufficient-state candidate under the V1 no-target-leak rule.

### Failure contract

`CONDITIONAL_IF:` quotient dynamics require an unfrozen representative-selection rule, approximate equivalence threshold, or action matching convention.

`REPRESENTATION_DEPENDENT_IF:` an admissible operational twin fails to yield a conjugate quotient action system under transported states/actions.

`REFUTED_IF:` within valid scope there exist `x\sim_\mathcal T y` and action `a` such that definedness differs or the successors are not future-equivalent.

`CONTROL_FAILURE_IF:` determinism is violated despite the declared type, future-equivalence is computed incorrectly, or action transport under F5 fails.

### Forbidden stronger interpretation

Survival does not establish general dynamic controllability, Markov sufficiency, corrigibility, or that future-equivalence is the correct quotient for every downstream task.

---

# Part C — Candidate-family coverage and lock conditions

## C1. Coverage summary

| V1 candidate family | Primary candidate status |
|---|---|
| Algebraic | `S-ALG-001` instantiated |
| Relational | `S-REL-001` instantiated |
| Combinatorial | `S-COMB-001` instantiated |
| Topological | `S-TOP-001` instantiated |
| Geometric | `S-GEO-001` instantiated |
| Informational | `S-INF-001` instantiated |
| Dynamical | `S-DYN-001` instantiated |
| Invariant | No standalone primary candidate instantiated |

The absence of a standalone invariant candidate is not a negative scientific result. It records that no nonredundant invariant candidate is admitted to the V1 primary ontology at this prospective stage.

---

## C2. Candidate ontology freeze rule

This manifest may be reviewed and repaired **only before its own candidate-specification lock**.

Once locked, the following are prohibited for the V1 primary analysis:

- adding a candidate;
- deleting a candidate;
- changing `Dom(C_i)`;
- changing `C_i`;
- changing `P_i`;
- changing `Z_i`;
- changing the auxiliary-completeness argument;
- changing `\cong_i`;
- changing `\tau^i_\phi`;
- changing family scope;
- changing failure criteria;
- or changing the forbidden stronger interpretation.

Any such future change is a V2/amendment/prospective extension and may not rewrite the V1 primary candidate ontology.

---

## C3. No-world rule

Before candidate-specification lock, this file may be reviewed for typing, hidden auxiliary freedom, circularity, or claim inflation.

It may **not** be reviewed against a newly constructed F1–F5 world.

No exact F1–F5 system may be created in order to decide whether one of these candidates should remain in the manifest.

```math
\boxed{
\text{world behavior}
\not\rightarrow
\text{candidate retention or repair}.
}
```

---

## C4. Next legal artifact after lock

Only after this candidate-specification manifest is fossilized may STRUCTURE-001 proceed to:

```text
experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md
```

That future artifact must define the exact F1–F5 systems and adversarial constructions while preserving the candidate ontology frozen here.

No implementation is authorized by this manifest.

---

## C5. Current stopping point

```text
STRUCTURE-001 V1 @ 9711a6d            LOCKED
        ↓
CANDIDATE_SPECIFICATION_MANIFEST_V1    REVIEW STATE
        ↓
SYSTEM CONSTRUCTION                     NOT STARTED
        ↓
IMPLEMENTATION                          NOT STARTED
        ↓
EXECUTION                               NOT STARTED
```

The candidate manifest is therefore a prospective ontology artifact only.

Its scientific question is:

```math
\boxed{
\text{What exact mathematical claims are we willing to let enter the arena before any arena exists?}
}
```
