# Active_Schema v0 Structure-Coordinate Minimum Runtime Schema

pass: PASS-68
title: Active_Schema v0 Structure-Coordinate Minimum Runtime Schema
source_basis: rendering branch current-standard closure
current_standard_commit: 3f76cb91f3390d481eea9aa180dec002b1e6fe02

document_status: schema draft only
proof_status: NOT_PROOF
runtime_status: NOT_EXECUTED

This document is not proof.
This document is not runtime execution.
This document is not final Active_Schema.
This document is not renderer implementation.
This document is not physics/math proof.

## 1. Coordinate-first boundary

coordinate_first_rule: coordinates, not angles
angle_restriction: only right angle / orthogonality is structural
representation_policy: coordinates, states, matrix expressions
number_policy: decimal scale + binary state/direction
notation_guard: no hexadecimal structural notation

## 2. Base formation

base_formation: 2 directions × 3 axes = 6 directions
origin: center balance point / 정중심평형점
axis_set: X, Y, Z
direction_set: +X, -X, +Y, -Y, +Z, -Z

## 3. Matrix relation

matrix_relation: row × column
row_rule: row moves along Y or Z depending on displayed plane
column_rule: column moves along X
coordinate_tuple_rule: spatial coordinate is (x, y, z)

## 4. Occupancy relation

occupancy_rule: 100 = 10 × 10 full matrix
half_occupancy_rule: 50 = 5 × 10 or 10 × 5
occupancy_guard: 50 is not 5 × 5

## 5. Field distinction

grid/content/numerator distinction:
- grid is the positioned visibility/receiving frame.
- content is the placed value or shape-state inside the frame.
- numerator is the visible content-side expression.

matrix/container/denominator distinction:
- matrix is the row-column relation field.
- container is the receiving field boundary.
- denominator is the base field that allows placement and relation.

## 6. State fields required for runtime lowering

State fields required for runtime lowering:
- coordinate state
- axis direction state
- matrix row-column state
- occupancy state
- field relation state
- boundary/surface state
- render visibility state

These fields are schema draft fields only.
They do not execute Runtime.

## 7. Minimal runtime object schema

minimal runtime object schema:

~~~yaml
object_id:
object_type:
source_status:
proof_status:
runtime_status:

coordinate:
  x:
  y:
  z:

axis_state:
  x_direction:
  y_direction:
  z_direction:

matrix_state:
  rows:
  columns:
  layer_axis:
  occupancy_value:
  occupancy_unit:
  occupancy_relation:

field_relation:
  center_balance_point:
  grid_content_numerator:
  matrix_container_denominator:
  boundary_state:
  surface_state:

render_state:
  visible_plane:
  hidden_plane_policy:
  renderer_candidate_shape:
  overlay_candidate:
~~~

## 8. Renderer boundary

renderer_output_target: monitor-visible structural object

renderer_candidate_shape:
- octahedral / double square-pyramid shell is renderer candidate, not proof

overlay_candidate:
- spherical overlay is renderer candidate, not proof

renderer candidate, not proof.

## 9. Next route

next_route: schema validation before runtime implementation

The next step is schema validation before runtime implementation.
It is not Runtime execution.
It is not proof.
