# tilted_nested_coordinate_frame_renderer.md

## purpose

Render a virtual tilted local coordinate frame nested inside a fixed global frame.

```text
global frame is fixed
child local frame is tilted
local six axes rotate together as one rigid frame
```

```text
parent_global_frame: X_G / Y_G / Z_G locked
child_tilted_local_frame: x_c / y_c / z_c attached to mass body
```

```text
z_c is tilted from Z_G by theta
rotation_axis_or_hinge required
x_axis_mode required
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
