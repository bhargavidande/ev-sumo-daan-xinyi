# ev-sumo-daan-xinyi

---

##  Network and Infrastructure

### `network/daan_xinyi.net.xml`
- OSM-based accurate road network of the Daan–Xinyi district.
- Includes intersections, roundabouts, multi-lane roads, and urban grid structure.
- Generated using `netconvert` from OpenStreetMap data.

### `network/daan_xinyi_types.add.xml`
- Defines EV vehicle types and mobility parameters.
- Includes acceleration, deceleration, length, maximum speed, and color coding.
- Supports large-scale simulations with 2000+ EVs.

### `network/daan_xinyi_charging.add.xml`
- Defines EV charging stations (charging piles / charging guns).
- Each station specifies:
  - Charging power (kW)
  - Number of slots
  - Charging type (AC/DC)
- Charging stations are colocated with parking lots (PLs).

### `network/daan_xinyi_edge_computers.add.xml`
- Defines edge computing servers (ESs) attached to PLs.
- Each ES includes:
  - CPU capacity (Hz)
  - Maximum task handling capability
  - Logical association with parking lots

---

## Traffic and Route Modeling

### `routes/flow_definitions.xml`
- Defines probabilistic EV traffic flows.
- Includes:
  - Vehicle injection rates
  - Origin–destination pairs
  - Time-dependent traffic demand
- Supports realistic urban congestion patterns.

### `routes/ev_routes.rou.xml`
- Explicit EV routes generated from flow definitions.
- Contains routes for 2000+ EVs with randomized departure times.
- Generated automatically via `generate_routes.py`.

---

##  Simulation Configuration

### `config/daan_xinyi.sumocfg`
- Main SUMO configuration file.
- Specifies:
  - Network file
  - Route file
  - Simulation duration
  - Step length
  - Output settings
  - Random seed

### `config/additional.sumocfg`
- Includes all additional elements:
  - Vehicle types
  - Charging stations
  - Edge computing units
- Modular separation improves clarity and extensibility.

---

## Scripts

### `scripts/generate_routes.py`
- Generates `ev_routes.rou.xml` from `flow_definitions.xml`.
- Supports large-scale EV population and randomized departure times.

### `scripts/generate_pref_dist.py`
- Generates driver preference distributions:
  - Truncated normal distribution for parking duration
  - Gaussian distance-based location preference
  - Willingness 
- Save outputs files.

---

## How to Run the Simulation

### Requirements
- SUMO ≥ 1.17
- Python ≥ 3.8
- Python packages: `numpy`, `pandas`, `sumolib`, `traci`

### Step 1: Generate Routes

python3 scripts/generate_routes.py

### Step 2: Generate Driver Preferences

python3 scripts/generate_pref_dist.py

### Step 3: Run SUMO

sumo-gui -c config/daan_xinyi.sumocfg


### For headless execution:

sumo -c config/daan_xinyi.sumocfg

If you use this repository in academic work, please cite:
@misc{sumo_ev_pl_allocation_2026,
  author = {Bhargavi Dande, Po-Yen Chen and Hung-Yu Wei},
  title  = {SUMO-based EV Parking and Charging Allocation in Daan–Xinyi District},
  year   = {2026},
  note   = {NTU, Taiwan}
}
