# Hash Relation Track DB — Canonical Theory

```yaml
schema_version: "1.0.0"
document_role: CANONICAL_THEORY
```

## 1. Definition

```text
Hash Relation Track DB
=
a logical distributed DB.System that identifies bounded Object States by Hash,
binds Object States to Positions,
records boundary-preserving Relations,
reconstructs physical and semantic Tracks,
and exposes a verifiable observable state C.
```

It is not one repository, one file, one hash, one table, or one global center object.

```text
Hash Relation Track DB
=
Zenodo
+
Active_Schema
+
Bridge
+
for_instance
+
Relation
+
Git History
+
Observable C
```

## 2. Object State and Hash

An Object State is one exact immutable byte state.

```text
Object State
→ SHA-256
```

Its canonical identity key is `algorithm + digest`; `byte_length` and `media_type` are verification fields.

```text
Hash
=
Object State Key

Hash
≠
Truth
≠
Meaning
≠
Semantic Identity
≠
Position
```

## 3. Semantic Identity

Semantic Identity expresses what an object participates as inside an explicit semantic scope.

```text
Object State
≠
Semantic Identity
```

One Object State may relate to multiple Semantic Identities, and one Semantic Identity may relate to multiple Object States.

The binding is represented by a Semantic Relation.

## 4. Position

```text
Position
=
a binding between an Object State and a physical or logical field
```

```text
identity is not position.
position binds identity to a field.
```

The same Object State may have multiple Position Bindings.

A Position Binding does not change Object State bytes.

## 5. Relation

```text
Relation
=
a boundary-preserving semantic connection between independently identified references
```

```text
relation is not merge.
relation is interconnecting.
```

A Relation identifies its source, target, type, semantic scope, boundary state, declared state, and evidence.

Conflicting Relations remain independently observable until resolved by later valid records.

## 6. Track

```text
Track
=
an append-only logical lineage inside an explicit track scope
```

A Track Event stores predecessor references.

It does not predeclare an unknown future `next` event.

```text
E0
← E1
← E2
```

Multiple current tips represent a branch.

```text
Multiple Tips
≠
Automatic Conflict
≠
Automatic Merge
```

## 7. Physical and Semantic Lineage

Git preserves physical lineage:

```text
Blob
Tree
Commit
Parent
Ref
Diff
```

Relation preserves semantic and logical lineage:

```text
Semantic Identity
Object State Reference
Position Binding
Semantic Relation
Track Event
Seat Occupation
Declared State
Derived Effective State
Evidence
Closure Snapshot
```

```text
Git Physical Lineage
≠
Relation Semantic Lineage
```

The lineages are related and reconstructed together without duplication.

## 8. Declared and Effective State

An append-only record stores immutable declared state at creation.

```yaml
declared_state:
  validation:
  lifecycle:
  closure:
```

Current effective state is derived from later valid records and Relations.

```text
Append-only
≠
State cannot change

Append-only
=
State change is represented by a new object
```

A historical record is not rewritten from `CURRENT` to `SUPERSEDED`.

A later valid record points to it through `supersedes_refs`.

## 9. Seat, Instance, and Occupation

```text
Seat
≠
Instance

Seat Definition
≠
Seat Occupation
```

A Seat Definition is an operational Position Contract.

An Instance may occupy one or more Seats over time.

A new Seat Occupation is a Runtime Record in the Relation extension.

Existing `for_instance` Assignment History remains at its existing position and is not silently converted.

## 10. Result and Handoff

```text
Result
→ validated output Object State

Result to Next Data
→ Track Event
```

A Handoff Event connects one Occupation result to a target Seat Definition without merging either identity.

## 11. Observable C

```text
C
=
generated observable projection of canonical Relation records and Git state
```

C is not another source of truth.

Live C is generated on demand.

A Closure C Snapshot may be preserved as immutable evidence.

C separates:

```text
Object State change
Position change
Semantic Identity change
Semantic Relation change
Track change
Seat Occupation change
Git reference change
```

## 12. Repository Identities

### Bridge

```text
Bridge/start_position
=
new canonical theory and restart field
```

Projection position:

```text
start_position/01_active_schema/
```

### for_instance

```text
for_instance
=
existing AI Instance Alignment Repository
```

It already contains Seat, Instance Registry, Assignment, Handoff, Operation, Test, and History structures.

Binding extension:

```text
main/09_active_schema_binding/
```

### Relation

```text
Relation
=
existing integrated Relation System–DB Repository
```

Append-only runtime and semantic registry extension:

```text
main/05_hash_relation_track_registry/
```

The extension does not rewrite the closed initial structure.

## 13. Open.Mind

```text
Open.Mind
=
independent structural verification without automatic submission to authority
```

Existing theories, 승이's theory, AI outputs, and implementation results are all verification targets.

```text
Position is defined.
Internal method remains adaptive.
External result remains observable.
```

## 14. System Guard

```text
Hash is not meaning.
Meaning is related through records.

Structure is not isolate.
Structure is relation processing.
```
