# Active_Schema V1 Root and Identity Contract

```yaml
schema_version: "1.0.0"
document_role: ROOT_AND_GENESIS_BINDING_CONTRACT
```

## 1. Canonical Vocabulary

```yaml
conceptual_root:
  value: Hash_Relation_Track_DB
  meaning: theory direction and system origin

publication_root:
  value: Zenodo_DOI
  meaning: permanent publication resolution origin

package_identity:
  value: Active_Schema_ZIP_SHA256
  representation: ZIP_FILENAME_ONLY
  meaning: exact ZIP byte identity

content_identity:
  value: Manifest_Digest
  meaning: canonical internal content relation identity

deployment_set:
  value: D0
  meaning: first unfolded GitHub payload state

genesis_binding_record:
  meaning: immutable Relation object binding independent identities

runtime_storage_commit:
  value: G1
  meaning: Git commit storing the Genesis Binding Record
```

The following terms are not canonical V1 vocabulary:

```text
Object Root
Content Root
Deployment Root
Runtime Root
Genesis Root Hash
```

## 2. Identity Separation

```text
Conceptual Root
≠
Publication Root

Publication Root
≠
Package Identity

Package Identity
≠
Content Identity

Content Identity
≠
Deployment Set

Genesis Binding Record
≠
Runtime Storage Commit
```

## 3. Genesis Binding

The Genesis Binding Record is not a new single Root value.

```text
Genesis Binding Record
=
Conceptual Root reference
+
Publication Root
+
Package Identity
+
Content Identity
+
Deployment Set D0
```

Each identity remains independently verifiable.

The canonical Genesis Binding Record belongs to:

```yaml
repository: SeungeFlow/Relation
branch: main
path: 05_hash_relation_track_registry/
record_type: HASH_RELATION_TRACK_DB_GENESIS
```

`Bridge` holds the theory projection and an optional post-Genesis pointer.

`for_instance` holds the alignment binding and an optional post-Genesis reference.

Neither duplicates the canonical Genesis Binding Record.

## 4. Self-Reference Guard

The package does not contain:

```text
its final ZIP SHA-256 value
an unissued DOI
future deployment commits
future Genesis Binding Record IDs
the unknown commit that will contain a record itself
```

The ZIP SHA-256 exists only as the ZIP filename.

The manifest does not contain its own final digest.

A Position Binding Record refers only to a pre-existing Git state and never to its own unknown storage commit.

## 5. Formation Direction

```text
Canonical content
→ Payload hashes
→ Manifest
→ External Manifest Digest
→ Deterministic ZIP
→ ZIP SHA-256 Filename
→ Final Review
→ Zenodo DOI
→ Deployment Set D0
→ Genesis Binding Record
→ Runtime Storage Commit G1
→ Observable C
```

## 6. Resolution Directions

Publication resolution:

```text
DOI
→ Zenodo Record
→ ZIP
→ ZIP Filename Digest Verification
→ Manifest Digest Verification
→ Payload Verification
```

Runtime resolution:

```text
Relation Registry Commit
→ Genesis Binding Record
→ Independent Identities
→ Deployment Set D0
→ Current Git State
→ Current Relation Tracks
→ Observable C
```

## 7. Historical Relation Closure

The historical closed scope and the closure-record state are distinct Git states.

```yaml
verified_closed_scope_base:
  commit: ff624832e5be2b195b8916113753b8b709574cfe
  tree: 6ac428f2f8e1f57f0a55d3b86e8a76415eb01a05

closure_record_state:
  commit: cc4adf6891b53db0ec2e02ef4db8a1c9a9b41256
  tree_resolution: FROM_GIT_COMMIT_OBJECT_AT_GATE_0B
```

They must not be represented as one mixed commit-tree pair.

## 8. Crystallization and Review

Round 10 crystallization freezes the content bytes and ZIP bytes.

The later `gpt.logi` final review approves or rejects the exact frozen object; it does not edit it.

A failed review requires a new package identity.

## 9. Guard

```text
A hash identifies bytes.
A DOI identifies publication.
A manifest digest identifies canonical content relation.
A deployment set identifies unfolded payload state.
A binding record relates them.
The relation does not merge them.
```
