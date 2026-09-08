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
- existence of declared path semantics;
- existence of a declared resource or cost field in `\kappa`;
- existence of a declared observation map;
- whether future-transformability is state-indexed or history-indexed.

It may **not** contain empirical expectations, performance filters, or conditions selected because the candidate is expected to survive them.

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

If a property must hold for every action, path, state, equivalence class, or auxiliary choice, that universal quantifier is part of `P_i` and may not be weakened after system construction.

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

This may be literal equality, graph isomorphism, order isomorphism, homeomorphism, isometry, lattice isomorphism, conjugacy of partial action systems, or another exact equivalence defined prospectively.

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

A candidate may not exclude a family because it is expected to fail there.

Scope may not be altered after candidate performance is observed.

---

## A10. Prospective failure contract

Each candidate declares four boundaries in advance.

### `CONDITIONAL_IF`

State the exact observation or auxiliary variation showing dependence on additional assumptions or non-operational choice.

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

State failures invalidating scientific interpretation, including type mismatch, incomplete auxiliary class, invalid auxiliary transport, failed enumeration control, provenance mismatch, implementation disagreement with `C_i`, or invalid operational-isomorphism control.

```math
\boxed{
\text{CONTROL FAILURE}
\neq
\text{candidate refutation}.
}
```

---

## A11. Forbidden stronger interpretation

Every record states what survival would **not** establish.

A surviving candidate may receive only the V1 label:

```text
FORCED_AT_TESTED_SCOPE
```

under its frozen scope and claim ceiling.

No record may silently promote survival into a universal law of Revisics, a universal structure for all future-transformability, uniqueness of mathematical representation, or foundational status for an entire mathematical family.

---

## A12. Candidate-family coverage rule

STRUCTURE-001 V1 listed candidate families, not mandatory winners.

The primary ontology permits:

```text
NO CLEAN PRIMARY CANDIDATE IN THIS FAMILY
```

when no exact candidate passes the specification gate.

```math
\boxed{
\text{candidate family in battery}
\not\Rightarrow
\text{mandatory candidate}.
}
```

---

## A13. Candidate ontology freeze rule

This manifest may be reviewed and repaired **only before its own candidate-specification lock**.

Once locked, the following are prohibited for the V1 primary analysis:

- adding or deleting a candidate;
- changing `Dom(C_i)`;
- changing `C_i` or `P_i`;
- changing `Z_i` or its auxiliary-completeness argument;
- changing `\cong_i` or `\tau^i_\phi`;
- changing family scope;
- changing failure criteria;
- changing the forbidden stronger interpretation.

Any such later change is a V2/amendment/prospective extension and may not rewrite the V1 primary candidate ontology.

---

## A14. No-world rule

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

## A15. Next legal artifact after lock

Only after this candidate-specification manifest is fossilized may STRUCTURE-001 proceed to:

```text
experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md
```

That future artifact must define the exact F1–F5 systems while preserving the candidate ontology frozen here.

No implementation is authorized by this manifest.

---

## A16. Non-tautology gate

STRUCTURE-001 distinguishes canonical mathematical consequences of a chosen construction from non-tautological structure-discovery hypotheses.

For every instantiated candidate, the manifest must declare one of two epistemic classes:

```text
FORMAL_BASELINE
STRUCTURE_HYPOTHESIS
```

The gate is:

```math
\boxed{
P_i\in\operatorname{Th}
\left(
C_i,
\operatorname{Dom}(C_i),
Z_i,
\text{ordinary mathematics}
\right)
\Longrightarrow
\texttt{FORMAL\_BASELINE}.
}
```

Here `\operatorname{Th}` denotes the ordinary mathematical consequences of the frozen candidate construction, its semantic type domain, and its declared auxiliary semantics. This gate does not require a general theorem prover; each candidate record must supply a prospective non-tautology argument sufficient to justify its epistemic class before any system construction.

A `FORMAL_BASELINE` may establish that the operational object admits a canonical or conditional mathematical encoding and may serve as a control or reference object. It may not by itself count as a discovered nontrivial common structure for the purpose of the STRUCTURE-001 null hypothesis.

```math
\boxed{
\texttt{FORMAL\_BASELINE}
\not\Rightarrow
H_0\text{ rejected}.
}
```

A candidate may be classified `STRUCTURE_HYPOTHESIS` only when its frozen `P_i` is not guaranteed solely by `C_i`, `Dom(C_i)`, `Z_i`, and ordinary mathematical consequences of those definitions. Its record must identify the operationally variable relation whose truth value can differ across valid typed systems without changing the candidate definition.

If the non-tautology status cannot be justified prospectively, the candidate is classified `FORMAL_BASELINE` rather than receiving structure-discovery credit.

The permanent anti-tautology rule is:

```math
\boxed{
\text{researcher construction}
\not\rightarrow
\text{automatic theorem}
\not\rightarrow
\text{claimed scientific discovery}.
}
```

---

# Part B — Instantiated Candidate Records

## B0. Candidate index

The prospective V1 candidate ontology contains:

| Candidate ID | Layer | Short name | Declared scope |
|---|---|---|---|
| `S-ALG-001` | Algebraic | Executable-path partial composition | F1, F2, F3, F4, F5 |
| `S-REL-001` | Relational | Exact future-transformational kernel quotient | F1, F2, F3, F5 |
| `S-COMB-001` | Combinatorial | Operational SCC condensation order | F1, F2, F3, F4, F5 |
| `S-TOP-001` | Topological | Reachability dual Alexandrov bitopology | F1, F2, F3, F4, F5 |
| `S-GEO-001` | Geometric | Cost-induced directed extended metric | F3, F5 |
| `S-INF-001` | Informational | T-blind admissible history-quotient lattice | F4, F5 |
| `S-DYN-001` | Dynamical | Congruence of future-equivalence under action dynamics | F1, F2, F3, F5 |

No standalone `S-INV-*` primary candidate is instantiated. Representation invariance is already a required criterion for every candidate, and no nonredundant standalone invariant construction is admitted prospectively here. This is an ontology decision made before system construction, not a scientific result.

---

## B1. `S-ALG-001` — Executable-path partial composition

**Layer:** Algebraic  
**Epistemic class:** `FORMAL_BASELINE`  
**Non-tautology argument:** The primary claim is an ordinary mathematical consequence of literal finite-sequence concatenation together with the frozen whole-path admissibility semantics. Its positive validation is therefore a formal baseline and cannot reject `H_0`.

### Scientific claim

Finite executable paths generated by the declared operational relation admit a canonical typed partial composition by literal path concatenation, with associativity wherever the relevant composites are defined.

### Type domain `Dom(C)`

Operational objects for which finite executable paths, source/target states, and `\kappa`-admissibility of complete paths are semantically defined.

### Construction `C`

Let `\Pi_\kappa(\mathfrak O)` be the finite `\kappa`-admissible execution paths

```math
\pi=(x_0,a_0,x_1,\ldots,a_{n-1},x_n)
```

whose adjacent triples satisfy `\operatorname{Exec}`.

Define

```math
s(\pi)=x_0,
\qquad
t(\pi)=x_n.
```

Define `\pi_2\circ\pi_1` iff `t(\pi_1)=s(\pi_2)` and the literal concatenated path is `\kappa`-admissible.

Output:

```math
C_{\mathrm{ALG}}(\mathfrak O)
=
(\Pi_\kappa,s,t,\circ).
```

### Claim `P`

For all typed triples `\pi_1,\pi_2,\pi_3`, if the literal full concatenation is `\kappa`-admissible, then both bracketings are defined and

```math
(\pi_3\circ\pi_2)\circ\pi_1
=
\pi_3\circ(\pi_2\circ\pi_1)
```

as literal paths.

No identity structure is claimed unless empty paths are independently part of `\kappa`.

### Auxiliary class `Z`

```math
Z_{\mathrm{ALG}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

Concatenation is literal sequence concatenation; source, target, and whole-path admissibility are frozen operational facts. No ordering, coordinate, embedding, representative, or tie-break enters the output.

### Output equivalence `\cong`

Isomorphism of typed partial path algebras preserving source, target, and composition.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{ALG}}_\phi(\varnothing)=\varnothing.
```

Operational isomorphisms transport paths pointwise.

### Declared scope

```math
\{F1,F2,F3,F4,F5\}.
```

**Scope justification:** only typed execution paths and `\kappa` are required.

### Failure contract

`CONDITIONAL_IF:` a non-operational choice is required to determine concatenation or whole-path admissibility while `\mathfrak O` is fixed.

`REPRESENTATION_DEPENDENT_IF:` an operational twin fails to induce an isomorphic partial path algebra.

`REFUTED_IF:` a valid scoped object has a `\kappa`-admissible full concatenation for which the two bracketings are unequal or not both defined.

`CONTROL_FAILURE_IF:` path enumeration, whole-path admissibility, or F5 path transport is implemented inconsistently.

### Forbidden stronger interpretation

Survival does not establish that all future-transformability is fundamentally categorical, algebraic, or compositional. As a `FORMAL_BASELINE`, positive validation does not reject `H_0`.

---

## B2. `S-REL-001` — Exact future-transformational kernel quotient

**Layer:** Relational  
**Epistemic class:** `FORMAL_BASELINE`  
**Non-tautology argument:** Equivalence of the exact kernel relation and the coarsest exact factorization property are ordinary consequences of equality and kernel quotienting. Their positive validation is formal control, not structure discovery, and cannot reject `H_0`.

### Scientific claim

When future-transformability is a well-typed single-valued map on the declared current carrier, equality of future-transformability profiles induces the unique coarsest exact quotient preserving those profiles.

### Type domain `Dom(C)`

Operational objects with a single-valued typed map

```math
\Theta_\mathfrak O:D\rightarrow Y,
\qquad
\Theta_\mathfrak O(d)=\mathcal T^\kappa(d),
```

and exact equality in `Y`.

### Construction `C`

```math
d\sim_{\mathcal T}d'
\iff
\Theta_\mathfrak O(d)=\Theta_\mathfrak O(d').
```

Let

```math
Q_\mathcal T=D/{\sim_\mathcal T}
```

with canonical quotient `q_\mathcal T:D\to Q_\mathcal T`.

### Claim `P`

1. `\sim_\mathcal T` is an equivalence relation.
2. `\Theta_\mathfrak O` is constant on every fiber of `q_\mathcal T`.
3. Every quotient `q:D\to Q` satisfying

   ```math
   q(d)=q(d')\Rightarrow\Theta_\mathfrak O(d)=\Theta_\mathfrak O(d')
   ```

   refines `q_\mathcal T`.

### Auxiliary class `Z`

```math
Z_{\mathrm{REL}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

The relation is the exact kernel of the frozen map `\Theta_\mathfrak O`. No tolerance, metric, clustering, ordering, or representative choice is permitted.

### Output equivalence `\cong`

Isomorphism of quotient sets induced by operational transport, preserving fibers and transported `\Theta` values.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{REL}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\{F1,F2,F3,F5\}.
```

**F4 exclusion:** F4 prospectively forbids target-informed generation of candidate history quotients; this candidate is explicitly the kernel of `\mathcal T`.

### Failure contract

`CONDITIONAL_IF:` equality of future-transformability requires an unfrozen tolerance, metric, or matching rule.

`REPRESENTATION_DEPENDENT_IF:` an operational twin changes the quotient beyond induced transport.

`REFUTED_IF:` `\sim_\mathcal T` fails equivalence or an exact `\Theta`-preserving quotient exists that is strictly coarser than `q_\mathcal T`.

`CONTROL_FAILURE_IF:` `\Theta` is not single-valued on the declared carrier, equality is mistyped, or quotient factorization is implemented incorrectly.

### Forbidden stronger interpretation

Survival does not establish that this quotient is sufficient for every future task, approximate setting, or history-dependent system. As a `FORMAL_BASELINE`, positive validation does not reject `H_0`.

---

## B3. `S-COMB-001` — Operational SCC condensation order

**Layer:** Combinatorial  
**Epistemic class:** `FORMAL_BASELINE`  
**Non-tautology argument:** SCC equivalence, acyclicity of the condensation graph, and the induced reachability partial order are standard graph-theoretic consequences of the SCC construction. Positive validation therefore establishes a canonical formal baseline only.

### Scientific claim

The finite directed graph of `\kappa`-admissible one-step operational transitions induces a canonical quotient into strongly connected components whose condensation is acyclic and whose reachability relation is a partial order.

### Type domain `Dom(C)`

Finite operational carriers with a well-typed set of `\kappa`-admissible one-step transitions.

### Construction `C`

Construct the directed graph

```math
G_\kappa=(D,E_\kappa)
```

where

```math
(x,y)\in E_\kappa
\iff
\exists a:\operatorname{Exec}(x,a,y)
```

under the declared one-step `\kappa` semantics.

Let `\operatorname{SCC}(G_\kappa)` be the exact strongly connected component partition.

Construct the condensation graph `\operatorname{Cond}(G_\kappa)` and its reflexive-transitive reachability order `\preceq_C` on components.

Output:

```math
C_{\mathrm{COMB}}(\mathfrak O)
=
(\operatorname{SCC}(G_\kappa),\operatorname{Cond}(G_\kappa),\preceq_C).
```

### Claim `P`

1. SCC membership is an equivalence relation.
2. The condensation graph is acyclic.
3. `\preceq_C` is a partial order on SCCs.

### Auxiliary class `Z`

```math
Z_{\mathrm{COMB}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

SCC membership and condensation edges are exact graph-theoretic functions of the frozen directed operational transition graph. Traversal order, graph layout, canonical labels, and chosen representatives have no semantic role.

### Output equivalence `\cong`

Directed-graph isomorphism of condensations together with order isomorphism of `\preceq_C` induced by operational transport.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{COMB}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\{F1,F2,F3,F4,F5\}.
```

**Scope justification:** only finite typed one-step operational transitions are required; F4 may use its declared finite history carrier without performing target-informed compression.

### Failure contract

`CONDITIONAL_IF:` SCC membership or condensation requires an unfrozen edge-selection, threshold, representative, or pruning rule.

`REPRESENTATION_DEPENDENT_IF:` operational twins yield non-isomorphic condensation structures under transport.

`REFUTED_IF:` a valid scoped object yields a condensation directed cycle or a failure of partial-order laws for `\preceq_C`.

`CONTROL_FAILURE_IF:` transition edges or SCCs are incompletely/incorrectly enumerated or F5 graph transport fails.

### Forbidden stronger interpretation

Survival does not establish that SCC condensation is a complete description of future-transformability or that Revisics is fundamentally graph-theoretic. As a `FORMAL_BASELINE`, positive validation does not reject `H_0`.

---

## B4. `S-TOP-001` — Reachability dual Alexandrov bitopology

**Layer:** Topological  
**Epistemic class:** `FORMAL_BASELINE`  
**Non-tautology argument:** Given the frozen partial order, the declared upward and downward Alexandrov topologies and their specialization-order properties are ordinary order/topology consequences of the construction. This is a canonical topological baseline, not a structure-discovery hypothesis.

### Scientific claim

The operational reachability order on SCC components induces a canonical **pair** of dual Alexandrov topologies, avoiding any hidden researcher choice between upward and downward orientation.

### Type domain `Dom(C)`

Finite operational objects for which the SCC condensation order `(K,\preceq_C)` is defined directly from the one-step operational transition graph.

### Construction `C`

Let `K` be the SCC carrier and `\preceq_C` the condensation reachability order.

Define the upward topology

```math
\mathcal O^\uparrow
=
\{U\subseteq K:\forall x\in U,\ x\preceq_C y\Rightarrow y\in U\}
```

and the downward topology

```math
\mathcal O^\downarrow
=
\{U\subseteq K:\forall x\in U,\ y\preceq_C x\Rightarrow y\in U\}.
```

Output the ordered dual pair

```math
C_{\mathrm{TOP}}(\mathfrak O)
=
(K,\mathcal O^\uparrow,\mathcal O^\downarrow).
```

No orientation is selected or discarded.

### Claim `P`

1. `\mathcal O^\uparrow` and `\mathcal O^\downarrow` are topologies.
2. Both are Alexandrov.
3. Under the frozen specialization convention

   ```math
   x\le_{\mathrm{spec}}y
   \iff
   \forall U,\ x\in U\Rightarrow y\in U,
   ```

   `\mathcal O^\uparrow` has specialization order `\preceq_C` and `\mathcal O^\downarrow` has specialization order `\preceq_C^{\mathrm{op}}`.
4. Both are `T_0` because `\preceq_C` is antisymmetric.

### Auxiliary class `Z`

```math
Z_{\mathrm{TOP}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

The only obvious orientation freedom—upward versus downward Alexandrov construction—is not chosen; both dual topologies are retained in the candidate output. No metric, radius, basis selection, embedding, coordinate, graph layout, or neighborhood threshold is introduced.

Any different topological construction is a distinct candidate and cannot be substituted into this record.

### Output equivalence `\cong`

Bitopological isomorphism induced by the transported SCC order, preserving the ordered pair `(\mathcal O^\uparrow,\mathcal O^\downarrow)`.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{TOP}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\{F1,F2,F3,F4,F5\}.
```

**Scope justification:** only the finite operational SCC order is required.

### Failure contract

`CONDITIONAL_IF:` constructing this exact dual pair requires any additional unfrozen topological choice while the SCC order is fixed.

`REPRESENTATION_DEPENDENT_IF:` operational twins fail to induce isomorphic ordered bitopological spaces.

`REFUTED_IF:` either declared family fails the topology axioms or Alexandrov closure, or the specialization orders fail to recover `\preceq_C` and its opposite as frozen.

`CONTROL_FAILURE_IF:` the SCC order is wrong or transport of SCCs/topologies under operational twins fails validation.

### Forbidden stronger interpretation

Survival establishes only this exact reachability-induced dual Alexandrov construction at tested scope. It does not establish that topology as a whole is uniquely foundational for Revisics. As a `FORMAL_BASELINE`, positive validation does not reject `H_0`.

---

## B5. `S-GEO-001` — Cost-induced directed extended metric

**Layer:** Geometric  
**Epistemic class:** `FORMAL_BASELINE`  
**Non-tautology argument:** Under the semantic domain's nonnegative additive path-cost assumptions, zero self-distance and the directed triangle inequality are shortest-path consequences of the declared cost construction. The result is therefore a conditional induced geometry baseline rather than positive evidence that geometry is forced.

### Scientific claim

When the operational accounting convention itself supplies nonnegative additive path cost, minimal operational path cost induces a directed extended metric-like geometry invariant under cost-preserving operational recoding.

### Type domain `Dom(C)`

Operational objects for which `\kappa` semantically declares:

1. a nonnegative path cost `c`;
2. zero cost for the empty path;
3. path cost determined by the frozen operational path;
4. additive concatenation cost whenever literal path concatenation is executable.

These are semantic typing conditions for this cost-derived candidate, not empirical performance conditions.

### Construction `C`

```math
d_\kappa(x,y)
=
\inf\{c(\pi):\pi\text{ executable from }x\text{ to }y\},
```

with `d_\kappa(x,y)=+\infty` when no executable path exists.

Output:

```math
C_{\mathrm{GEO}}(\mathfrak O)
=(D,d_\kappa).
```

No symmetrization, embedding, or coordinate chart is added.

### Claim `P`

For all `x,y,z`:

```math
d_\kappa(x,x)=0
```

and

```math
d_\kappa(x,z)
\le
d_\kappa(x,y)+d_\kappa(y,z)
```

in extended-real arithmetic.

Symmetry and positive separation are not claimed.

### Auxiliary class `Z`

```math
Z_{\mathrm{GEO}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

The cost function is frozen inside operational `\kappa`. No norm, embedding, symmetrization, rescaling, kernel, coordinate, or weighting is chosen by the candidate.

### Output equivalence `\cong`

Isometry of directed extended-distance spaces under transported states.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{GEO}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\{F3,F5\}.
```

**F3 inclusion:** resource/accounting semantics are the explicit role of F3.  
**F5 inclusion:** exact recoding tests whether the cost-derived geometry is representation invariant.

**F1/F2/F4 exclusion:** those family roles do not semantically require an operational additive cost field; exclusion is by type, not expected performance.

### Failure contract

`CONDITIONAL_IF:` the distance requires an unfrozen norm, embedding, symmetrization, rescaling, or path weighting not fixed by `\kappa`.

`REPRESENTATION_DEPENDENT_IF:` a cost-preserving operational twin fails to be an isometry.

`REFUTED_IF:` a valid scoped object satisfying `Dom(C)` violates zero self-distance or the directed triangle inequality.

`CONTROL_FAILURE_IF:` cost additivity, path-cost accumulation, infimum computation, or F5 cost transport is implemented incorrectly.

### Forbidden stronger interpretation

Survival does not establish Euclidean geometry, manifold structure, local differential geometry, symmetry, or a universal scalar of revisability. As a `FORMAL_BASELINE`, positive validation does not reject `H_0`.

---

## B6. `S-INF-001` — T-blind admissible history-quotient lattice

**Layer:** Informational  
**Epistemic class:** `FORMAL_BASELINE`  
**Non-tautology argument:** The lattice claim is treated prospectively as a formal property of the complete T-blind admissible-equivalence construction rather than as evidence that future-transformability empirically forces information-lattice structure. Positive validation therefore cannot reject `H_0`.

### Scientific claim

The F4 admissible sufficient-state search space, generated without inspecting future-transformability, has an operational refinement structure: the complete set of current-state-refining, causally updateable history equivalences forms a finite lattice under refinement.

### Type domain `Dom(C)`

Finite-history operational objects with:

1. a frozen finite evaluation horizon;
2. an exhaustively enumerable history carrier `H_t`;
3. the F4 current-state refinement rule;
4. the F4 causal-updateability rule.

The construction does not inspect `\mathcal T` or later sufficiency outcomes.

### Construction `C`

Let `\mathcal Q_{\mathrm{adm}}(\mathfrak O)` be all equivalence relations `E` on `H_t` satisfying:

1. current-state refinement

   ```math
   hEh'\Rightarrow x_t(h)=x_t(h');
   ```

2. causal updateability/congruence under every same-typed admissible one-step extension.

Order the set by refinement:

```math
E_1\preceq E_2
\iff
E_1\subseteq E_2.
```

Output:

```math
C_{\mathrm{INF}}(\mathfrak O)
=(\mathcal Q_{\mathrm{adm}},\preceq).
```

No quotient is selected using `\mathcal T`.

### Claim `P`

1. `\mathcal Q_{\mathrm{adm}}` is finite and nonempty because the full-history identity equivalence is admissible.
2. Every pair has a greatest lower bound under refinement.
3. Every pair has a least upper bound within `\mathcal Q_{\mathrm{adm}}`.
4. Therefore `(\mathcal Q_{\mathrm{adm}},\preceq)` is a finite lattice.

This claim concerns the T-blind admissible quotient space, not future sufficiency.

### Auxiliary class `Z`

```math
Z_{\mathrm{INF}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

The output is the exhaustive set of all equivalence relations satisfying the frozen F4 syntactic/causal admissibility constraints. Enumeration order, quotient labels, and representative choices have no semantic role; `\mathcal T` is not consulted.

### Output equivalence `\cong`

Lattice isomorphism induced by transport of histories and equivalence relations.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{INF}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\{F4,F5\}.
```

**F4 inclusion:** the candidate concerns the target-blind history-quotient search space required by F4.  
**F5 inclusion:** representation twins provide the anti-artifact test for the quotient lattice.

**F1/F2/F3 exclusion:** those family roles do not semantically require the F4 history-quotient construction.

### Failure contract

`CONDITIONAL_IF:` generating the admissible quotient set requires an unfrozen heuristic, ordering, pruning rule, or target-informed choice.

`REPRESENTATION_DEPENDENT_IF:` operational twins yield non-isomorphic admissible quotient structures under transported histories.

`REFUTED_IF:` a valid scoped object has an admissible quotient poset lacking a meet or join for some pair.

`CONTROL_FAILURE_IF:` the quotient set is not exhaustively enumerated, current-state refinement/causal updateability is implemented incorrectly, or `\mathcal T` leaks into quotient generation.

### Forbidden stronger interpretation

Survival does not establish that any nontrivial quotient is future-sufficient. That remains a later F4 question under V1. As a `FORMAL_BASELINE`, positive validation does not reject `H_0`.

---

## B7. `S-DYN-001` — Congruence of future-equivalence under action dynamics

**Layer:** Dynamical  
**Epistemic class:** `STRUCTURE_HYPOTHESIS`  
**Non-tautology argument:** The candidate construction freezes a future-transformational equivalence and the raw declared action dynamics without repairing failures of class consistency. The primary claim is the contingent congruence condition itself: valid typed systems may in principle have future-equivalent current states whose action-definedness or successor future-equivalence differs. Therefore `P` is not granted merely by forming the quotient; it must be tested on the later frozen systems.

### Scientific claim

Declared future-transformational equivalence is preserved by one-step action dynamics exactly when the action dynamics are class-consistent. STRUCTURE-001 tests the contingent question of whether that congruence property holds across the candidate's prospectively declared scope.

### Type domain `Dom(C)`

Operational objects for which:

1. a single-valued typed future-transformability signature

   ```math
   \Theta_\mathfrak O:X\rightarrow Y
   ```

   is mechanically derived from declared future-transformability under the frozen operational semantics, with exact equality in `Y`;
2. the signature derivation is part of the operational semantics rather than a candidate-selected auxiliary choice;
3. each action `a` defines a deterministic partial transition

   ```math
   \delta_a:X\rightharpoonup X.
   ```

### Construction `C`

Define

```math
x\sim_\mathcal T y
\iff
\Theta_\mathfrak O(x)=\Theta_\mathfrak O(y).
```

Let `Q_\mathcal T=X/{\sim_\mathcal T}`.

The candidate output retains:

1. the exact quotient `Q_\mathcal T`;
2. the raw partial transitions `\{\delta_a\}`;
3. for each action and equivalence class, the unmodified representative-level definedness and successor classes needed to test congruence.

No representative is selected to force descent, and no failed class is repaired or removed.

### Claim `P`

For every action `a` and all `x\sim_\mathcal T y`:

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

Equivalently, the frozen future-equivalence relation is a congruence for every declared partial action, so and only so do the action maps descend without representative choice to well-defined partial maps on `Q_\mathcal T`.

### Auxiliary class `Z`

```math
Z_{\mathrm{DYN}}=\{\varnothing\}.
```

### Auxiliary-completeness argument

The future-transformability signature and action transitions are frozen operational inputs under `Dom(C)`. The candidate uses exact equality and retains all representative-level action behavior. No representative selection, approximate threshold, action ordering, coordinate, repair rule, or tie-break is introduced.

### Output equivalence `\cong`

Isomorphism of the quotient-plus-raw-action test object under operational transport, preserving equivalence classes, action definedness, and successor-class relations.

### Auxiliary transport `\tau_\phi`

```math
\tau^{\mathrm{DYN}}_\phi(\varnothing)=\varnothing.
```

### Declared scope

```math
\{F1,F2,F3,F5\}.
```

**F4 exclusion:** this candidate uses a declared future-transformability signature to define its current-state equivalence and is not admissible as an F4 sufficient-state construction under the V1 no-target-leak rule.

### Failure contract

`CONDITIONAL_IF:` the future-equivalence or congruence test requires an unfrozen representative-selection rule, approximate equivalence threshold, signature choice, or action-matching convention.

`REPRESENTATION_DEPENDENT_IF:` an operational twin fails to preserve the quotient and congruence verdict under transport.

`REFUTED_IF:` there exist `x\sim_\mathcal T y` and action `a` such that definedness differs or defined successors are not future-equivalent.

`CONTROL_FAILURE_IF:` determinism is violated despite the declared type, the frozen future-transformability signature is computed incorrectly, or F5 action transport fails.

### Forbidden stronger interpretation

Survival does not establish dynamic controllability, Markov sufficiency, corrigibility, or that future-equivalence is the correct quotient for every downstream task. It would establish only the frozen congruence claim at tested scope.

---

## B8. Candidate-family coverage

| V1 candidate family | Prospective primary status |
|---|---|
| Algebraic | `S-ALG-001` instantiated |
| Relational | `S-REL-001` instantiated |
| Combinatorial | `S-COMB-001` instantiated |
| Topological | `S-TOP-001` instantiated |
| Geometric | `S-GEO-001` instantiated |
| Informational | `S-INF-001` instantiated |
| Dynamical | `S-DYN-001` instantiated |
| Invariant | No standalone primary candidate instantiated |

The empty invariant slot is not a negative result. It is a prospective ontology decision.

---

## B9. Current stopping point

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

The candidate manifest is a prospective ontology artifact only.

Its scientific question is:

```math
\boxed{
\text{What exact mathematical claims are we willing to let enter the arena before any arena exists?}
}
```
