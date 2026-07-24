# Runtime Lowering Plan from Active_Schema v0

pass: PASS-75
title: Runtime Lowering Plan from Active_Schema v0
source_basis: Active_Schema v0 fixed source
active_schema_v0_commit: 6759504035cffc79e3189afec5b6797f3815611e

document_status: plan draft only
plan_status: DRAFT
proof_status: NOT_PROOF
runtime_status: NOT_EXECUTED
runtime_implementation_status: NOT_DONE

This document is not runtime implementation.
This document is not runtime execution.
This document is not renderer code.
This document is not proof.
This document is not final runtime.
No runtime code in this document.
No renderer implementation in this document.

## 1. Lowering boundary

coordinate_first_lowering_rule: coordinates, not angles
angle_restriction: only right angle / orthogonality is structural
number_policy: decimal scale + binary state/direction
notation_guard: no hexadecimal structural notation

## 2. Base-space lowering

base_space_rule: 2 directions × 3 axes = 6 directions
center_rule: center balance point / 정중심평형점
axis_lowering: X, Y, Z
direction_lowering: +X, -X, +Y, -Y, +Z, -Z

## 3. Matrix lowering

matrix_lowering: row × column
row_lowering: row moves along Y or Z depending on displayed plane
column_lowering: column moves along X

## 4. Occupancy lowering

occupancy_lowering: 100 = 10 × 10 full matrix
half_occupancy_lowering: 50 = 5 × 10 or 10 × 5
guard: 50 is not 5 × 5

## 5. Field relation lowering

field_relation_lowering: grid/content/numerator and matrix/container/denominator

grid/content/numerator:
- grid lowers as positioned receiving frame.
- content lowers as placed value or shape-state.
- numerator lowers as visible content-side expression.

matrix/container/denominator:
- matrix lowers as row-column relation field.
- container lowers as receiving field boundary.
- denominator lowers as base field for placement and relation.

## 6. Runtime object lowering order

Runtime object lowering order:

1. source boundary
2. schema field freeze
3. coordinate tuple lowering
4. axis/direction state lowering
5. matrix/grid lowering
6. occupancy layer lowering
7. field relation lowering
8. render_state lowering
9. validation fixtures
10. implementation boundary

## 7. Stage plan

| Stage | Name | Boundary |
| --- | --- | --- |
| Stage 0: source boundary | Fixed source basis | Use Active_Schema v0 as source, not runtime. |
| Stage 1: schema field freeze | Freeze field names | No renderer code and no execution. |
| Stage 2: coordinate tuple lowering | Lower (x, y, z) | Coordinate tuple first. |
| Stage 3: axis/direction state lowering | Lower direction state | +X, -X, +Y, -Y, +Z, -Z. |
| Stage 4: matrix/grid lowering | Lower row × column | Row/column relation only. |
| Stage 5: occupancy layer lowering | Lower occupancy relation | 100, 50, and guard. |
| Stage 6: field relation lowering | Lower numerator/denominator fields | grid/content and matrix/container relation. |
| Stage 7: render_state lowering | Lower visible/hidden render state | Renderer candidate only. |
| Stage 8: validation fixtures | Prepare validation before implementation | No Runtime execution. |
| Stage 9: implementation boundary | Define boundary for later implementation | Not implemented here. |

## 8. Runtime object lowering target fields

The following fields are the lowering targets:

~~~text
object_id
object_type
source_status
proof_status
runtime_status

coordinate.x
coordinate.y
coordinate.z

axis_state.x_direction
axis_state.y_direction
axis_state.z_direction

matrix_state.rows
matrix_state.columns
matrix_state.layer_axis
matrix_state.occupancy_value
matrix_state.occupancy_unit
matrix_state.occupancy_relation

field_relation.center_balance_point
field_relation.grid_content_numerator
field_relation.matrix_container_denominator
field_relation.boundary_state
field_relation.surface_state

render_state.visible_plane
render_state.hidden_plane_policy
render_state.renderer_candidate_shape
render_state.overlay_candidate
~~~

## 9. Renderer lowering order

renderer_lowering_order:
1. visible_plane selection
2. hidden_plane_policy selection
3. renderer_candidate_shape selection
4. overlay_candidate selection
5. validation before implementation

Renderer lowering is a plan only.
It is not renderer code.
It is not renderer implementation.

## 10. Validation boundary

validation before implementation

Validation must confirm:
- source boundary
- field names
- coordinate tuple
- axis/direction state
- matrix/grid relation
- occupancy relation
- field relation
- render_state relation

## 11. Next route

next_route: Runtime lowering plan validation before runtime implementation

The next step is plan validation.
It is not runtime implementation.
It is not runtime execution.
It is not proof.
