# STRUCTURE-001

## Which mathematical structures are forced by future-transformability?

**Status:** Preregistered research program  
**Version:** 1.0  
**Scientific role:** First Revisics-native structure-discovery study

---

## 1. Research question

Which nontrivial mathematical structures, if any, are forced by declared operational facts of future-transformability, invariant under admissible representation changes, and shared across the preregistered system classes?

The experiment is explicitly a **structure-discovery problem**.

It does not presuppose that future-transformability is geometric, topological, ordered, metric, dynamical, informational, or otherwise mathematically represented in any particular way.

The null outcome is scientifically admissible.

---

## 2. Constitutional relationship to Revisics

Revisics is defined as a proposed scientific field concerned with how systems change the space of future changes that remain possible.

This experiment does not establish the field's existence, nor does it establish a universal law of Revisics.

Its purpose is narrower:

> Determine which mathematical structures, if any, are operationally induced by the phenomenon under study.

The claim

```math
\text{field definition}\neq\text{empirical confirmation}
```

remains in force.

Likewise:

```math
\text{research lineage}\neq\text{retroactive evidence}.
```

Prior repositories may motivate candidate questions but do not constitute evidence for the present experiment unless independently instantiated and tested under this preregistration.

---

## 3. Raw operational object

The primitive experimental object is an operational system:

```math
\boxed{ \mathfrak O_t=(X_t,\mathcal A_t,\operatorname{Exec}_t,\kappa_t) }
```

where:

- `X_t` is the declared state space;
- `\mathcal A_t` is the declared action/transformation alphabet;
- `\operatorname{Exec}_t(x,a,x')` is the operational execution relation;
- `\kappa_t` is the declared accounting convention, including resource and horizon constraints.

No mathematical structure on `X_t` or on future-transformability is assumed by definition.

---

## 4. Derived future-transformability object

Future-transformability is derived from the operational facts:

```math
\boxed{ \mathcal T_t^\kappa(x) = \{(a,x'):\operatorname{Exec}_t(x,a,x') \} }
```

or, where explicitly preregistered, an associated path or horizon closure.

The direction of construction is therefore:

```math
\boxed{ \text{operational facts} \longrightarrow \mathcal T \longrightarrow \text{candidate mathematical structure}. }
```

The reverse direction is prohibited.

A candidate structure may not be built into the definition of `\operatorname{Exec}`, `\mathcal T`, admissibility, reachability, equivalence, or state encoding merely to make the candidate succeed.

---

## 5. Revisic transition

The fundamental transition under investigation is provisionally represented as:

```math
\boxed{ (x_t,\mathcal T_t) \longrightarrow (x_{t+1},\mathcal T_{t+1}). }
```

This representation is descriptive, not a declaration that `\mathcal T` itself is the fundamental state variable.

In particular:

```math
x_{t+1}^{(A)}=x_{t+1}^{(B)}
```

does not entail

```math
\mathcal T_{t+1}^{(A)} = \mathcal T_{t+1}^{(B)}.
```

Observed equality of state representations is therefore not sufficient evidence of equality of future-transformational structure.

---

## 6. Primary hypotheses

### Null hypothesis

```math
\boxed{ H_0: \text{No nontrivial common mathematical structure beyond the declared operational relations survives all preregistered tests.} }
```

### Alternative

At least one nontrivial candidate structure satisfies all three primary criteria:

```math
\boxed{ \text{existence} + \text{necessity} + \text{representation invariance}. }
```

A surviving structure is a **candidate common structure**, not a universal law.

---

## 7. Primary evaluation criteria

For each candidate structure `S`, evaluate three independent properties.

### 7.1 Existence

Does the relevant structure actually occur in the declared system class?

A structure absent from a system class is not forced by that class.

### 7.2 Necessity

Can the structure be removed while preserving the preregistered operational facts, or does it follow from them?

A property that appears only after adding unlisted assumptions is classified as **conditional**, not foundational.

### 7.3 Representation invariance

Let

```math
\mathfrak O\simeq\mathfrak O'
```

denote the preregistered operational equivalence relation for a system family.

Then a candidate property must satisfy:

```math
\boxed{ \mathfrak O\simeq\mathfrak O' \Longrightarrow S(\mathcal T_{\mathfrak O}) \simeq S(\mathcal T_{\mathfrak O'}). }
```

A property that changes under an admissible recoding is classified as **representation-dependent**.

---

## 8. Adversarial system families

Five deliberately distinct families are required.

### F1 — Finite executable systems

Small finite systems whose execution relations can be exhaustively enumerated.

Purpose:

- test reachability;
- test compositional closure;
- expose minimal counterexamples;
- determine whether candidate structure follows from execution alone.

### F2 — State / observation / future-equivalence separations

Systems containing states that may be:

- operationally distinct;
- observationally equivalent;
- future-transformationally equivalent;
- or observationally equivalent but future-transformationally distinct.

Purpose: separate state identity from future-transformational identity.

A candidate quotient must not be assumed merely because two representations look equivalent.

### F3 — Resource- and horizon-sensitive systems

Systems parameterized by explicitly declared resources or horizons:

```math
\mathcal T^{(B,H)}(x).
```

Test whether increased resources or horizon yield stable relations such as:

```math
B_1\le B_2 \Rightarrow \mathcal T^{(B_1,H)}(x) \subseteq \mathcal T^{(B_2,H)}(x).
```

Any such relation is treated as a hypothesis to test, not an axiom.

### F4 — History / sufficient-state systems

Systems designed so that distinct histories may yield identical current representations:

```math
x_{t+1}^{(A)}=x_{t+1}^{(B)}
```

while:

```math
\mathcal T_{t+1}^{(A)} \neq \mathcal T_{t+1}^{(B)}.
```

The first interpretation to test is:

```math
\boxed{ \text{current state representation is insufficient}. }
```

The exact allowed sufficient-state rule is frozen as follows.

For each finite F4 instance, let the raw observed history through time `t` be

```math
h_t=(x_0,a_0,x_1,a_1,\ldots,a_{t-1},x_t).
```

The F4 construction manifest must freeze a finite evaluation horizon before any future-transformability comparison is inspected. All admissible histories through that horizon are then exhaustively enumerated from the raw operational relation.

An admissible sufficient-state construction is a deterministic quotient

```math
f:H_t\rightarrow S_t
```

of the exhaustively enumerated history set satisfying all of the following:

1. **Current-state refinement.**

   ```math
   f(h)=f(h') \Longrightarrow x_t(h)=x_t(h').
   ```

   The constructed state may augment the current observed state but may not identify histories with different current observed states.

2. **Causal updateability.** There must exist a deterministic update function `F` such that for every admissible one-step extension,

   ```math
   f(h\,a\,x')=F(f(h),a,x').
   ```

   The summary must therefore be recursively maintainable from past summary, executed action, and newly observed state; it may not depend on future outcomes.

3. **No target leakage in construction.** Candidate quotients are generated exhaustively from the finite history set subject only to current-state refinement and causal updateability. They may not be proposed, ranked, filtered, or edited using `\mathcal T`, candidate-structure outcomes, or knowledge of which histories later prove future-transformationally distinct.

4. **Sufficiency test.** A generated quotient is sufficient only if

   ```math
   f(h)=f(h') \Longrightarrow \mathcal T^\kappa(h)=\mathcal T^\kappa(h')
   ```

   throughout the frozen evaluation horizon.

5. **Compression test.** The identity map on complete histories is retained only as a terminal control. A nontrivial sufficient-state construction must merge at least two distinct admissible histories while remaining sufficient.

The F4 outcome is classified prospectively as one of:

```text
CURRENT_STATE_SUFFICIENT
SUFFICIENT_HISTORY_QUOTIENT_EXISTS
ONLY_FULL_HISTORY_IDENTITY_SUFFICIENT_WITHIN_FROZEN_HORIZON
CONTROL_FAILURE
```

Observation of

```math
x_A=x_B,\qquad \mathcal T_A\neq\mathcal T_B
```

is not, by itself, evidence for irreducible history dependence.

If no nontrivial admissible sufficient-history quotient exists, the strongest permitted statement is:

```math
\boxed{ \text{future-transformability is not compressible beyond full observed history within the preregistered F4 class and frozen horizon}. }
```

The phrase **irreducible history dependence** may not be promoted to an unqualified universal claim from STRUCTURE-001.

### F5 — Representation twins

F5 consists of exact operationally equivalent recodings of the same finite operational system.

Two systems

```math
\mathfrak O=(X,\mathcal A,\operatorname{Exec},\kappa)
```

and

```math
\mathfrak O'=(X',\mathcal A',\operatorname{Exec}',\kappa')
```

are admissible F5 twins iff there exist bijections

```math
\phi_X:X\rightarrow X',\qquad \phi_A:\mathcal A\rightarrow\mathcal A'
```

such that all of the following hold exactly:

1. **Execution preservation.**

   ```math
   \operatorname{Exec}(x,a,y)
   \iff
   \operatorname{Exec}'(\phi_X(x),\phi_A(a),\phi_X(y)).
   ```

2. **Accounting preservation.** `\kappa'` is exactly the transport of `\kappa` under `\phi_X,\phi_A`: horizons, budgets, admissibility rules, transition costs, and any other operationally declared resource quantities are preserved under the recoding.

3. **No hidden coordinate semantics.** Numeric labels, lexical names, serialization order, memory addresses, or coordinates carry no operational meaning unless that meaning is explicitly part of `\operatorname{Exec}` or `\kappa`. A candidate structure may not use such representation-only features as evidence.

4. **Exhaustive finite recoding.** For each finite F5 base instance, all state-label bijections and all action-label bijections are tested exhaustively, subject to exact preservation of the operational system above. The identity recoding is included as a control.

A candidate structure `S` passes F5 representation invariance only if its declared classification and all claimed invariant content are preserved under the induced transport for every admissible twin recoding.

For scalar or discrete invariants, equality must be exact. For structured outputs, preservation means isomorphism under the mapping induced by `\phi_X` and `\phi_A`; raw labels themselves are ignored.

Any primary candidate that changes under an admissible F5 recoding is classified **representation-dependent** at the claimed scope.

Continuous-coordinate recodings are not part of the primary F5 v1 control. Any such extension requires a prospective preregistration amendment before inspection of the added candidate's outcomes.

---

## 9. Candidate structure battery

The initial battery includes, without commitment to survival:

- reachability relations;
- composition / partial composition;
- future-transformational equivalence;
- inclusion or preorder structure;
- graph structure;
- topology;
- local geometric structure;
- metric or pseudometric structure;
- transition dynamics;
- information-preserving or reconstructibility structure;
- invariants under specified transformation classes.

No primary candidate may be added, removed, or replaced after primary evaluation begins.

A new candidate requires a separately committed prospective extension record created before evaluating that candidate. Extension candidates are reported separately and may not alter the preregistered classifications of the v1 primary battery.

---

## 10. Classification of outcomes

Every candidate is assigned one of four primary classifications:

```math
\boxed{ \text{forced} \;|\; \text{conditional} \;|\; \text{representation-dependent} \;|\; \text{refuted}. }
```

### Forced

The candidate is present, follows from the declared operational facts under the preregistered semantics, and survives admissible representation changes across the relevant system classes.

### Conditional

The candidate exists only when additional explicitly stated assumptions hold, such as smoothness, composability, monotone resource semantics, a chosen neighborhood structure, or a particular parameterization.

### Representation-dependent

The candidate changes under an admissible operationally equivalent recoding.

Such a structure is not treated as foundational.

### Refuted

A preregistered counterexample demonstrates that the candidate does not hold under its claimed scope.

---

## 11. History-dependence decision rule

The experiment distinguishes:

```math
\boxed{ \text{insufficient observed state} }
```

from stronger history-indexed dependence.

Observation of

```math
x_A=x_B,\qquad \mathcal T_A\neq\mathcal T_B
```

is not, by itself, evidence for irreducible history dependence.

The exact F4 quotient procedure in Section 8 is the only permitted sufficient-state test in v1.

If current state fails but a nontrivial sufficient history quotient succeeds, the permitted conclusion is that additional historical state is required under the declared semantics.

If only the full-history identity is sufficient, the permitted conclusion is limited to the frozen F4 class and evaluation horizon. STRUCTURE-001 does not license an unqualified claim that history dependence is universally irreducible.

---

## 12. Primary evidence table

The principal output is a survival matrix of the form:

| Candidate structure | F1 | F2 | F3 | F4 | F5 | Minimum assumptions | Classification |
|---|---|---|---|---|---|---|---|
| Reachability relation | | | | | | | |
| Composition | | | | | | | |
| Future-equivalence | | | | | | | |
| Inclusion / preorder | | | | | | | |
| Graph structure | | | | | | | |
| Topology | | | | | | | |
| Local geometry | | | | | | | |
| Metric structure | | | | | | | |
| Transition dynamics | | | | | | | |
| Information structure | | | | | | | |
| Invariants | | | | | | | |

The table is descriptive evidence, not a scorecard intended to crown a preferred formalism.

---

## 13. Forbidden inferential moves

The following claims are prohibited unless separately established:

```math
\mathcal T\text{ exists} \not\Rightarrow \mathcal T\text{ is geometric}
```

```math
\mathcal T\text{ is reachable} \not\Rightarrow \mathcal T\text{ is topological}
```

```math
\mathcal T(x)\subseteq\mathcal T(y) \not\Rightarrow y\text{ is universally “more revisable” than }x
```

```math
x_A=x_B \not\Rightarrow \mathcal T_A=\mathcal T_B
```

```math
\mathcal T_A\neq\mathcal T_B \not\Rightarrow \text{irreducible history dependence}.
```

No scalar “revisability” quantity is assumed by this preregistration.

No universal geometry is assumed.

No universal topology is assumed.

No universal order is assumed.

---

## 14. Claim ceiling

The strongest warranted positive result from STRUCTURE-001 is:

```math
\boxed{ \text{A candidate mathematical structure is operationally induced, invariant under the tested admissible representations, and shared across the tested system classes.} }
```

This does **not** establish:

- a universal law of Revisics;
- completeness of the candidate mathematical description;
- applicability to all systems;
- uniqueness of the surviving structure;
- or a universal scalar measure of revisability.

The experiment may instead support:

```math
\boxed{ \text{universal primitive, plural mathematical representations}. }
```

Alternatively, it may find no nontrivial common structure beyond the operational level.

Either outcome is scientifically admissible.

---

## 15. Success condition for the study

The study succeeds if it produces a reproducible classification of candidate structures showing which are:

1. operationally induced;
2. assumption-dependent;
3. representation-dependent;
4. refuted;

together with explicit minimal counterexamples where applicable.

The study does not require discovery of a positive universal structure.

---

## 16. Epistemic objective

The purpose of STRUCTURE-001 is not to make Revisics look mathematically mature.

It is to determine, without presupposing the answer, **what mathematics the object itself permits us to claim**.

```math
\boxed{ \text{operational facts} \rightarrow \mathcal T \rightarrow \text{adversarial tests} \rightarrow \text{surviving structure} \rightarrow \text{theory}. }
```

The ordering is part of the methodology.

No later theory may be used to rewrite the earlier operational object merely to recover a preferred structure.

---

## 17. Construction and evaluation freeze

This preregistration freezes the scientific question, operational direction, five family roles, F4 sufficient-state rules, F5 operational-isomorphism rules, candidate battery, classification system, forbidden inferences, and claim ceiling.

It does **not** yet instantiate executable system instances.

Before any candidate-structure outcome is evaluated, implementation must produce a prospective construction manifest that freezes:

- the exact finite systems used in F1–F5;
- all action alphabets and execution relations;
- all accounting conventions `\kappa`;
- all F3 budgets and horizons;
- all F4 evaluation horizons;
- the exact observation maps used by F2;
- the exact enumeration procedure for F4 history quotients;
- the exact enumeration procedure for F5 twin recodings;
- and all deterministic analysis procedures.

That manifest must be committed and state-recorded before any primary structure classifications are inspected.

The execution order is:

```text
PREREGISTRATION V1
        ↓
CONSTRUCTION MANIFEST
        ↓
IMPLEMENTATION
        ↓
OPERATIONAL / ENUMERATION CONTROLS
        ↓
FREEZE VALID SYSTEM INSTANCES
        ↓
PRIMARY STRUCTURE EVALUATION
        ↓
SURVIVAL MATRIX + MINIMAL COUNTEREXAMPLES
        ↓
INTERPRET ONLY UNDER THE FROZEN CLAIM CEILING
```

Any failure of a preregistered operational-equivalence, enumeration, provenance, or implementation control is reported as a control failure and does not become evidence for or against the candidate mathematical structure.

No code is authorized by this preregistration itself.

---

## 18. Frozen scientific sequence

```math
\boxed{ \text{Constitution} \rightarrow \texttt{STRUCTURE-001}\ \text{preregistration} \rightarrow \text{construction manifest} \rightarrow \text{implementation} \rightarrow \text{execution}. }
```

STRUCTURE-001 is therefore the first Revisics-native attempt to make the proposed object earn its mathematics rather than receive mathematics by declaration.
