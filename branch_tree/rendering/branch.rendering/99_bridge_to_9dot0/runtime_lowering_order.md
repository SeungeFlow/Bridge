# runtime_lowering_order.md

## purpose

Define lowering order from rendering principle to Runtime candidate.

```text
1. source boundary
2. rendering branch manifest
3. existence relation rendering
4. field relation rendering
5. reverse check
6. Active_Schema bridge
7. Runtime lowering order
8. renderer_v0_1 position guard
9. Runtime placement judgment
```

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
