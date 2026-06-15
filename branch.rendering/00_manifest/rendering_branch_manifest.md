# rendering_branch_manifest.md

## purpose

`branch.rendering` is a rendering-principle branch. It defines what must be rendered, what must not be merged, and how a rendered surface returns to source.

Core split:

```text
01_existence_relation_rendering = relation-definition of existence rendering
02_field_relation_rendering = relation-definition of field rendering
```

Existing rendering v0.4 tree is preserved. This draft set adds a new rendering-principle layer.

## common guards

```text
source ≠ derived
memo ≠ proof
schema ≠ source
runtime ≠ theory itself
renderer ≠ proof

existence ≠ field
grid ≠ matrix
content ≠ container
water ≠ bowl
numerator ≠ denominator

numerator_zero ≠ denominator_zero
0/1 ≠ void
0/0 ≠ single_zero
1/0 ≠ 0/0

arithmetic_value ≠ structural_containment_status
denominator_capacity >= numerator_content

field_identity ≠ runtime_state
observed_frame ≠ field_identity
visibility_state ≠ plane_identity

parent_global_frame ≠ child_tilted_local_frame
Z_G ≠ z_c
reference_plane ≠ absolute_plane

hidden ≠ nonexistent
YZ_hidden_but_existing = true

C=0 singular ≠ center_balance_criterion_point proof
candidate_not_proof = true
```
