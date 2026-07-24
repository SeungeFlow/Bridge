# water_bowl_relation_states.md

## state table

| expression | grid/content | matrix/container | status |
|---|---:|---:|---|
| 1/1 | 1 | 1 | RELATION_FORMED |
| 1/0 | 1 | 0 | SINGULAR_CONTAINER_ABSENT |
| 0/1 | 0 | 1 | EMPTY_FIELD_READY |
| 0/0 | 0 | 0 | NO_RELATION_FIELD |

`0/1` is not void. `0/0` is not one undifferentiated zero.

```text
numerator_zero = content absence
denominator_zero = container absence
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
