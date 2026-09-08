# STRUCTURE-001

## Which mathematical structures are forced by future-transformability?

**Status:** Preregistered research program  
**Version:** 1.0  
**Scientific role:** First Revisics-native structure-discovery study

---

## 1. Research question

Which nontrivial mathematical structures, if any, are forced by declared operational facts of future-transformability, invariant under admissible representation changes, and shared across their prospectively declared family scopes?

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
\boxed{ H_0: \text{No nontrivial additional mathematical structure is forced at tested scope across its prospectively declared family scope.} }
```

Here “additional” excludes the operational relations and objects explicitly derived by definition in Section 4.

### Alternative

At least one nontrivial additional candidate structure satisfies all three primary criteria at its prospectively declared scope:

```math
\boxed{ \text{existence} + \text{operational necessity} + \text{representation invariance}. }
```

A surviving structure is a **candidate common structure at the tested scope**, not a universal law.

---

## 7. Candidate construction contract and primary evaluation criteria

A broad mathematical family such as “topology” or “geometry” is not itself a testable candidate. Every primary candidate must first be converted into an exact prospective construction contract.

### 7.1 Candidate specification gate

For each primary candidate `S`, a prospective candidate-specification record must freeze, before exact system instances are selected or constructed:

```math
\boxed{ \operatorname{Scope}(S)\subseteq\{F1,F2,F3,F4,F5\} }
```

and an exact construction map

```math
\boxed{ C_S:(\mathfrak O,z)\mapsto S_{\mathfrak O,z},\qquad z\in Z_S(\mathfrak O). }
```

The record must also freeze:

- the defining candidate property `P_S` being tested;
- the admissible auxiliary-choice set `Z_S(\mathfrak O)`;
- the equality or isomorphism criterion `\cong_S` for candidate outputs;
- the exact family scope `\operatorname{Scope}(S)`;
- any applicability restrictions;
- and all auxiliary assumptions.

If no auxiliary choice is required, then prospectively:

```math
Z_S(\mathfrak O)=\{\varnothing\}.
```

A singleton auxiliary class is valid only if the auxiliary-completeness rule in Section 7.2 is satisfied.

A candidate without a frozen `C_S`, `P_S`, `Z_S`, `\cong_S`, and family scope is **not testable under v1**.

The same candidate construction may not be changed by family after results are known. Family-specific substitutes are different candidates and require different candidate IDs.

### 7.2 Auxiliary completeness

The auxiliary-choice class is part of the scientific contract, not a convenience chosen to make a candidate pass.

For each frozen operational object `\mathfrak O`, `Z_S(\mathfrak O)` must expose every admissible candidate-relevant degree of freedom that is not uniquely determined by `\mathfrak O`.

In particular, every construction choice that can change either

```math
P_S\!\left(C_S(\mathfrak O,z)\right)
```

or the `\cong_S`-isomorphism class of `C_S(\mathfrak O,z)` while leaving `\mathfrak O` unchanged must appear explicitly as part of `z\in Z_S(\mathfrak O)`.

Equivalently:

```math
\boxed{ \text{No auxiliary freedom capable of changing the candidate claim may be hidden inside }C_S,P_S,\cong_S,\text{ or the implementation}. }
```

A coordinate convention, ordering, tie-break, embedding, weighting, neighborhood rule, basis, normalization, initialization, serialization-dependent choice, canonical-label choice, or other non-operational convention may not be made implicit merely by placing it inside the definition or code of `C_S`.

A degree of freedom may be omitted from `Z_S` only if the candidate specification prospectively establishes one of the following:

1. it is uniquely determined by the frozen operational object; or
2. all admissible alternatives are proven to leave both `P_S` and the `\cong_S`-class unchanged.

Thus

```math
Z_S(\mathfrak O)=\{\varnothing\}
```

is permitted only when the candidate-specification record prospectively demonstrates that no candidate-relevant non-operational freedom remains.

Auxiliary completeness must be established before system construction by either:

1. exhaustive enumeration of a finite declared construction-choice space together with a proof that it is complete; or
2. a prospective formal argument characterizing the complete admissible choice class and proving that every candidate-relevant non-operational degree of freedom is represented in `Z_S`.

If auxiliary completeness cannot be established, the candidate specification is incomplete and primary evaluation must stop before system construction.

### 7.3 Existence

Does the exact preregistered construction `C_S` produce the claimed candidate object or property in every tested instance within its declared scope?

A candidate absent from a tested instance within its claimed scope is not forced at that scope.

Merely showing that a mathematical structure *can* be placed on the underlying carrier is not evidence of operational induction.

### 7.4 Operational necessity

“Necessity” is given a counterfactual operational meaning.

For a frozen operational object `\mathfrak O`, the candidate property is necessary only if it survives every admissible auxiliary completion that leaves the operational object unchanged:

```math
\boxed{ \forall z\in Z_S(\mathfrak O),\quad P_S\!\left(C_S(\mathfrak O,z)\right)=\text{true}. }
```

If the claim concerns a particular induced structure rather than merely a property, then every admissible completion must additionally yield the same structure up to the preregistered output equivalence:

```math
\boxed{ \forall z,z'\in Z_S(\mathfrak O),\quad C_S(\mathfrak O,z)\cong_S C_S(\mathfrak O,z'). }
```

Thus a candidate can be **toggled while the operational object is held fixed** iff there exist admissible `z,z'` for which its defining property or claimed isomorphism class changes. Such a candidate is classified **conditional**, not forced at tested scope.

Necessity may be established only by:

1. exhaustive evaluation of the frozen finite auxiliary-choice set; or
2. a prospective formal proof quantifying over the complete frozen auxiliary-choice class.

Sampling auxiliary choices is insufficient.

A structure that requires an unfrozen neighborhood rule, coordinate system, embedding, weighting, smoothness assumption, composition law, metric choice, or other extra object is therefore not called forced unless that extra object is itself mechanically derived from the frozen operational facts under its own declared contract.

### 7.5 Representation invariance and auxiliary transport

Let

```math
\phi:\mathfrak O\simeq\mathfrak O'
```

denote a preregistered admissible operational isomorphism for a system family.

The candidate specification must prospectively freeze the induced auxiliary transport

```math
\boxed{ \tau_\phi:Z_S(\mathfrak O)\leftrightarrow Z_S(\mathfrak O'). }
```

For finite auxiliary classes this transport must be an exact bijection. It may not be chosen after candidate outcomes are inspected.

The transport must satisfy the coherence controls

```math
\boxed{ \tau_{\mathrm{id}}=\mathrm{id} }
```

and, whenever admissible operational isomorphisms compose,

```math
\boxed{ \tau_{\psi\circ\phi}=\tau_\psi\circ\tau_\phi. }
```

Representation invariance is then tested by the exact rule

```math
\boxed{ \forall z\in Z_S(\mathfrak O),\quad C_S(\mathfrak O,z)\cong_S C_S(\mathfrak O',\tau_\phi(z)). }
```

This replaces analyst judgment about which auxiliary choice in the recoded system “corresponds” to `z`.

If no exact prospective transport can be specified, the candidate specification is incomplete for that representation-invariance scope.

A candidate that changes under an admissible recoding and its frozen auxiliary transport is classified **representation-dependent** at the claimed scope.

### 7.6 Cross-family quantifier

“Shared across system classes” is quantified prospectively.

A candidate `S` is **shared across its declared family scope** iff:

1. `\operatorname{Scope}(S)` was frozen before system construction;
2. the same preregistered candidate construction `C_S`, property `P_S`, auxiliary semantics `Z_S`, output-equivalence rule `\cong_S`, and applicable transport rules `\tau_\phi` are used in every family in that scope; and
3. the candidate passes its required criteria in every preregistered instance of every family in that scope.

If

```math
|\operatorname{Scope}(S)|=1,
```

the result is **family-local** and may not be described as cross-family common.

If

```math
|\operatorname{Scope}(S)|\ge2,
```

and all scoped families pass, the candidate may be described as **cross-family at the tested scope**.

Only if

```math
\operatorname{Scope}(S)=\{F1,F2,F3,F4,F5\}
```

and all tests pass may the candidate be described as **study-wide shared across the preregistered families**.

Any family exclusion must be justified prospectively by a type or applicability argument, not by observed candidate performance.

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

The F4 system-construction manifest must freeze a finite evaluation horizon before any future-transformability comparison is inspected. All admissible histories through that horizon are then exhaustively enumerated from the raw operational relation.

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

5. **Frozen auxiliary transport.** For every F5 operational twin isomorphism `\phi=(\phi_X,\phi_A)` and every primary candidate whose scope includes F5, the candidate specification must provide the exact prospective map

   ```math
   \tau_\phi:Z_S(\mathfrak O)\leftrightarrow Z_S(\mathfrak O')
   ```

   satisfying the Section 7.5 identity and composition controls.

A candidate structure `S` passes F5 representation invariance only if, for every admissible twin recoding and every admissible auxiliary choice,

```math
\boxed{ \forall z\in Z_S(\mathfrak O),\quad C_S(\mathfrak O,z)\cong_S C_S(\mathfrak O',\tau_\phi(z)). }
```

For scalar or discrete invariants, equality must be exact. For structured outputs, preservation means isomorphism under the mapping induced by `\phi_X`, `\phi_A`, and the frozen candidate output rule; raw labels themselves are ignored.

Any primary candidate that changes under an admissible F5 recoding and its frozen auxiliary transport is classified **representation-dependent** at the claimed scope.

Continuous-coordinate recodings are not part of the primary F5 v1 control. Any such extension requires a prospective preregistration amendment before inspection of the added candidate's outcomes.

---

## 9. Structure layers and candidate battery

The study separates structures that are **derived by the operational definition** from additional mathematical structures that must earn evidentiary status.

### 9.1 Derived operational baseline

The following are derived operational objects or lossless representations of them:

- the execution relation `\operatorname{Exec}`;
- one-step reachability represented by `\mathcal T^\kappa`;
- any path or horizon closure explicitly specified by `\kappa`;
- and a raw transition graph when it is only a lossless recoding of the execution relation.

These objects are controls and prerequisites. Their existence does **not** count as discovery of a nontrivial additional mathematical structure and cannot by itself reject `H_0`.

In particular:

```math
\boxed{ \operatorname{Exec}\rightarrow\mathcal T \text{ is derivation, not discovery}. }
```

### 9.2 Additional candidate structure battery

The primary additional battery is organized by ontological level:

| Layer | Primary candidate family |
|---|---|
| Algebraic | composition / partial composition |
| Relational | future-transformational equivalence; inclusion / preorder |
| Combinatorial | graph-theoretic structure beyond the raw transition encoding |
| Topological | topology / connectedness constructions |
| Geometric | metric / pseudometric / local geometric structure |
| Informational | reconstruction / sufficient-statistic / information-preservation structure |
| Dynamical | transition operators / evolution of transformability |
| Invariant | invariants under specified transformation classes |

The labels in this table are **candidate families**, not claims that the family as a whole is testable or present.

For every primary candidate actually evaluated, the candidate-specification record must instantiate an exact `C_S`, `P_S`, complete `Z_S`, `\cong_S`, applicable auxiliary transports `\tau_\phi`, and prospectively declared scope as required by Section 7.

Thus, for example, “topology” is not a test. A specific topology construction from frozen operational data is a testable candidate. “Geometry” is not a test. A specific metric, pseudometric, or local-response construction with a frozen derivation rule is a testable candidate.

A failure of one such construction does not refute every topology or geometry. A success of one such construction does not establish topology or geometry as universally foundational.

No primary candidate family may be removed or replaced after primary evaluation begins.

A new candidate requires a separately committed prospective extension record created before evaluating that candidate. Extension candidates are reported separately and may not alter the preregistered classifications of the v1 primary battery.

---

## 10. Classification of outcomes

Every testable additional candidate is assigned one of four primary classifications:

```math
\boxed{ \text{FORCED_AT_TESTED_SCOPE} \;|\; \text{CONDITIONAL} \;|\; \text{REPRESENTATION_DEPENDENT} \;|\; \text{REFUTED}. }
```

A specification, provenance, enumeration, or implementation failure is a **control failure**, not a scientific classification.

### FORCED_AT_TESTED_SCOPE

The exact candidate construction is present throughout its prospectively declared scope, satisfies auxiliary completeness and the operational-necessity rule, survives admissible representation changes under the frozen auxiliary transports, and uses the same frozen candidate contract in every scoped family.

This label is always scope-indexed. It may not be shortened in interpretation to “universally forced.”

### CONDITIONAL

The candidate holds only under additional explicitly stated assumptions or auxiliary choices, such as smoothness, composability, monotone resource semantics, a chosen neighborhood rule, coordinate structure, weighting, embedding, or parameterization.

### REPRESENTATION_DEPENDENT

The candidate changes under an admissible operationally equivalent recoding at its claimed scope.

Such a structure is not treated as foundational at that scope.

### REFUTED

A preregistered counterexample demonstrates that the exact candidate claim `P_S` fails within its prospectively declared scope.

Refutation applies to the exact preregistered candidate construction and claim. It does not automatically refute the entire surrounding mathematical family.

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

## 12. Primary evidence tables

### 12.1 Derived operational baseline

The derived baseline is reported separately from structure-discovery claims.

| Derived operational object | F1 | F2 | F3 | F4 | F5 | Control status |
|---|---|---|---|---|---|---|
| Execution relation | | | | | | |
| One-step future-transformability `\mathcal T` | | | | | | |
| Declared path / horizon closure | | | | | | |
| Raw transition representation | | | | | | |

No entry in this table may be reported as a positive discovery of additional revisic structure.

### 12.2 Additional structure survival matrix

The principal scientific output is a survival matrix of the form:

| Layer | Candidate ID | Declared family scope | Construction map ID | F1 | F2 | F3 | F4 | F5 | Auxiliary choices / minimum assumptions | Classification |
|---|---|---|---|---|---|---|---|---|---|---|
| Algebraic | | | | | | | | | | |
| Relational | | | | | | | | | | |
| Combinatorial | | | | | | | | | | |
| Topological | | | | | | | | | | |
| Geometric | | | | | | | | | | |
| Informational | | | | | | | | | | |
| Dynamical | | | | | | | | | | |
| Invariant | | | | | | | | | | |

Every row must point to the exact prospectively frozen candidate contract. The table is descriptive evidence, not a scorecard intended to crown a preferred formalism.

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

```math
\text{some topology exists on }X \not\Rightarrow \text{topology is operationally induced}
```

```math
\text{one geometric construction fails} \not\Rightarrow \text{geometry as a mathematical family is refuted}
```

```math
\text{one geometric construction survives} \not\Rightarrow \text{geometry is universally foundational}
```

```math
Z_S(\mathfrak O)=\{\varnothing\} \not\Rightarrow \text{the construction is genuinely auxiliary-free}
```

unless auxiliary completeness has been established under Section 7.2.

No scalar “revisability” quantity is assumed by this preregistration.

No universal geometry is assumed.

No universal topology is assumed.

No universal order is assumed.

---

## 14. Claim ceiling

The strongest warranted positive result from STRUCTURE-001 is:

```math
\boxed{ \text{A preregistered candidate construction is forced at tested scope: it is mechanically induced from the frozen operational object, auxiliary-complete, invariant under the tested admissible representations and frozen auxiliary transports, and shared across every family in its prospectively declared scope.} }
```

If the declared scope contains only one family, the result is family-local.

If the declared scope contains multiple families and all pass, the result is cross-family **at that tested scope**.

Only a candidate whose prospectively declared scope contains all five families and passes all corresponding tests may be called study-wide shared across the preregistered families.

This does **not** establish:

- a universal law of Revisics;
- completeness of the candidate mathematical description;
- applicability to all systems;
- uniqueness of the surviving structure;
- that an entire mathematical family is foundational because one construction survived;
- or a universal scalar measure of revisability.

The experiment may instead support:

```math
\boxed{ \text{universal primitive, plural mathematical representations}. }
```

Alternatively, it may find no nontrivial common structure beyond the operational level.

Either outcome is scientifically admissible.

---

## 15. Success condition for the study

The study succeeds if it produces a reproducible, scope-indexed classification of candidate structures showing which are:

1. operationally induced and forced at tested scope;
2. assumption-dependent;
3. representation-dependent;
4. refuted;

with explicit candidate construction maps, declared scopes, auxiliary-complete choice classes, frozen auxiliary transports, and minimal counterexamples where applicable.

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

## 17. Prospective specification, construction, and evaluation freeze

This preregistration freezes the scientific question, operational direction, five family roles, F4 sufficient-state rules, F5 operational-isomorphism rules, auxiliary-completeness rule, auxiliary-transport rule, structure layers, candidate-family battery, classification system, forbidden inferences, and claim ceiling.

It does **not** yet instantiate executable system instances or exact candidate construction maps.

### 17.1 Candidate-specification manifest

Before exact F1–F5 system instances are selected or constructed, a separately committed and state-recorded candidate-specification manifest must freeze, for every primary candidate to be evaluated:

- candidate ID and ontological layer;
- exact `\operatorname{Scope}(S)`;
- exact construction map `C_S`;
- exact defining property `P_S`;
- complete admissible auxiliary-choice class `Z_S`;
- an auxiliary-completeness justification satisfying Section 7.2;
- exact equality / isomorphism criterion `\cong_S`;
- exact auxiliary transport `\tau_\phi` for every applicable admissible operational isomorphism, including identity and composition controls;
- all applicability restrictions;
- all auxiliary assumptions;
- and the deterministic procedure or formal proof used to test operational necessity.

The family scope, candidate construction, auxiliary class, auxiliary-completeness argument, and auxiliary transports must therefore be frozen **before system construction**, not after candidate performance is observed.

If a primary candidate lacks this complete specification, then:

```text
CANDIDATE SPECIFICATION INCOMPLETE -> STOP BEFORE SYSTEM CONSTRUCTION
```

No primary structure evaluation may proceed.

### 17.2 System-construction manifest

Only after the candidate-specification manifest is frozen may a prospective system-construction manifest freeze:

- the exact finite systems used in F1–F5;
- all action alphabets and execution relations;
- all accounting conventions `\kappa`;
- all F3 budgets and horizons;
- all F4 evaluation horizons;
- the exact observation maps used by F2;
- the exact enumeration procedure for F4 history quotients;
- the exact enumeration procedure for F5 twin recodings;
- and all deterministic system-level analysis procedures.

That manifest must be committed and state-recorded before implementation or any primary structure classification is inspected.

After system construction begins, no primary candidate scope, construction map, property, auxiliary-choice class, auxiliary-completeness argument, auxiliary transport, output-equivalence rule, or classification criterion may be altered.

### 17.3 Execution order

```text
PREREGISTRATION V1
        ↓
CANDIDATE-SPECIFICATION MANIFEST
        ↓
SYSTEM-CONSTRUCTION MANIFEST
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

Any failure of a preregistered candidate specification, auxiliary-completeness control, auxiliary-transport control, operational equivalence, enumeration, provenance, or implementation control is reported as a control failure and does not become evidence for or against the candidate mathematical structure.

No code is authorized by this preregistration itself.

---

## 18. Frozen scientific sequence

```math
\boxed{ \text{Constitution} \rightarrow \texttt{STRUCTURE-001}\ \text{preregistration} \rightarrow \text{candidate specification} \rightarrow \text{system construction} \rightarrow \text{implementation} \rightarrow \text{execution}. }
```

STRUCTURE-001 is therefore the first Revisics-native attempt to make the proposed object earn its mathematics rather than receive mathematics by declaration.
