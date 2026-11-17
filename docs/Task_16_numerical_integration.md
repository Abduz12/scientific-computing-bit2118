# Task 16: Numerical Integration

**Program file:** [`code/Task_16_numerical_integration.py`](../code/Task_16_numerical_integration.py)

**Mathematical concept:** An integral is accumulated quantity (area under a curve); trapezoidal and Simpson's rules approximate it from samples.

## 1. Inputs and mathematical operation

**Inputs**

- `time_hours`: every two hours from 0 to 12
- `power_kw`: smart-meter readings

**Mathematical operation**

- Trapezoidal rule with `trapezoid(power, time)`
- Simpson's rule with `simpson(power, x=time)`
- Difference between the two estimates

## 2. Baseline output

```text
Energy using trapezoidal rule: 15.700 kWh
Energy using Simpson's rule: 15.800 kWh
Difference between estimates: 0.100 kWh
```

## 3. Change an input or parameter

**What I changed:** Changed the 6 h power reading from `1.8` to `3.0`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Power at 6 h | 1.8 kW | 3.0 kW | Trapezoid 15.700 → 18.100 kWh; Simpson 15.800 → 19.000 kWh; difference 0.100 → 0.900 kWh |

New output (6 h power 1.8 -> 3.0 kW):

```text
Energy using trapezoidal rule: 18.100 kWh
Energy using Simpson's rule: 19.000 kWh
Difference between estimates: 0.900 kWh
```

**How and why the result changes:** A larger reading at 6 h means more power used around the middle of the period, so both estimates of the energy rise. The trapezoidal estimate rose by 2.4 kWh (1.2 kW extra x 2 h) because that reading has a weight equal to the step size, 2 h. Simpson's estimate rose by 3.2 kWh because it gives interior odd points a bigger weight (4/3 x 2 h = 2.67 h). The two rules now differ by 0.9 kWh instead of 0.1 kWh because a sharp peak is not modelled the same way: Simpson fits parabolas through the points while the trapezoid joins them with straight lines. For smooth data the two agree closely; with a spike they differ more.

## 4. Meaning of the output

The smart-meter readings give power in kW every two hours, so the area under the power curve is the energy in kWh. The trapezoidal rule gives 15.700 kWh and Simpson's rule gives 15.800 kWh for the 12 hours. The two differ by only 0.100 kWh, so both give a good estimate. Simpson's rule fits parabolas through groups of three points and is usually more accurate when the data is smooth. The result shows how integration turns a rate (kW) into a total (kWh).

## 5. Related real-world case

- **Scenario:** A bus's speed (km/h) is recorded every 10 minutes during a one-hour trip. How far did it travel?
- **Assumptions:**
  - Speed is measured at the start and end of each 10-minute interval
  - Time is converted to hours so that km/h x h = km
  - The bus starts and ends the hour stopped
- **Input data:** Time 0 to 60 minutes and speed 0, 30, 45, 50, 40, 25 and 0 km/h.
- **Modified program:** [`code/Task_16_numerical_integration_case.py`](../code/Task_16_numerical_integration_case.py)

**Output:**

```text
Distance using trapezoidal rule: 31.667 km
Distance using Simpson's rule: 32.778 km
Difference between estimates: 1.111 km
Average speed over the hour: 32.78 km/h
```

**Interpretation:** The bus travelled about 31.7 km by the trapezoidal rule and about 32.8 km by Simpson's rule. The 1.1 km difference arises because the speed curve is smooth and peaked, so straight-line segments tend to underestimate the area under it, while Simpson's parabolas follow it more closely. The average speed is the distance divided by the time, about 32.8 km/h over the hour. A report could give the distance as roughly 32 to 33 km.
