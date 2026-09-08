# Formal Primitives V0

**Status:** provisional notation for organizing questions, not an established theory.

## 1. State

Let

\[
x_t\in X_t
\]

be a system state at time \(t\).

No assumption is made that the state space is fixed over time.

## 2. Reachable transformation structure

Define

\[
\boxed{\mathcal T_t(x)=\{\text{transformations declared reachable from state }x\text{ at time }t\}.}
\]

The word “reachable” is protocol-relative. A study must specify what counts as a transformation, what resources are available, and what constraints define reachability.

\(\mathcal T_t(x)\) need not be represented as a plain set. Depending on the assay it may carry cost, topology, geometry, probability, authority, timing, provenance, or other declared structure.

## 3. System transformation

A realized transformation may be written

\[
\tau_t:x_t\mapsto x_{t+1}.
\]

The distinctively revisic object is the associated change

\[
\boxed{\mathcal T_t(x_t)\longrightarrow\mathcal T_{t+1}(x_{t+1}).}
\]

No monotonicity is presumed. Future transformability may expand, contract, rotate, fragment, merge, become more costly, become easier, or change in ways not captured by a scalar order.

## 4. Transformation-relative comparison

Given two realized or counterfactual transformations \(\tau\) and \(\tau'\), a revisic assay may compare the resulting future transformation structures:

\[
\mathcal T_{t+1}^{(\tau)}(x_{t+1})
\qquad\text{and}\qquad
\mathcal T_{t+1}^{(\tau')}(x'_{t+1}).
\]

A metric, divergence, partial order, equivalence relation, or invariant may be introduced only when defined and justified for that assay.

## 5. Corrective transformations

When a study declares a corrective class,

\[
\mathcal C_t(x)\subseteq\mathcal T_t(x),
\]

it must state what makes a transformation corrective and relative to which error, contract, objective, or evidence condition.

Correction is not identical to generic transformability.

## 6. Response maps

Some experiments may represent the effect of interventions with a response map

\[
\mathsf M_t:U_t\rightarrow Y_t.
\]

This is an assay-specific representation of transformation response, not the constitutional definition of Revisics.

Local linearizations such as

\[
D\mathsf M_t
\]

and quantities such as rank, singular values, condition numbers, or tangent-space geometry are likewise local tools unless a stronger result is established.

## 7. Quotients

A quotient \(q\) compresses or identifies distinctions in a richer object.

A revisic quotient question asks whether the quotient preserves the future transformations relevant to a declared task:

\[
\boxed{\text{current equivalence does not automatically imply future-transformational equivalence}.}
\]

No quotient is called safe without a declared future-operation criterion.

## 8. Optional viability functional

A study may introduce

\[
V_t:X_t\rightarrow\mathbb R
\]

or another viability object to evaluate outcomes. Revisics does not constitutionally identify greater transformability with greater value or viability.

Useful change and preserved revisability are separate questions.

## 9. Minimal research form

A minimal revisic experiment therefore specifies:

1. a state or system object;
2. a declared transformation structure \(\mathcal T\);
3. an intervention or realized transformation;
4. the resulting change in \(\mathcal T\);
5. the measurement or equivalence criterion;
6. the claim ceiling.

Anything stronger is assay-specific.
