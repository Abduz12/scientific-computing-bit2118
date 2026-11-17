# Task 2: NumPy Arrays and Numerical Computation

**Program file:** [`code/Task_02_numpy_arrays.py`](../code/Task_02_numpy_arrays.py)

**Mathematical concept:** An array stores many numbers in one object, and NumPy applies one operation to every element without a loop.

## 1. Inputs and mathematical operation

**Inputs**

- `temperatures_c`: 24 hourly temperature readings in degrees Celsius

**Mathematical operation**

- Mean, minimum and maximum of the array with `np.mean`, `np.min`, `np.max`
- Vectorised conversion F = 1.8C + 32 applied to every element at once

## 2. Baseline output

```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

## 3. Change an input or parameter

**What I changed:** Changed `29.4` (the 13:00 reading) to `35.0` in the `temperatures_c` array.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| 13:00 reading | 29.4 C | 35.0 C | Mean 23.12 → 23.35 C; maximum 29.40 → 35.00 C; minimum unchanged at 17.50 C |

New output (13:00 reading 29.4 -> 35.0):

```text
Daily mean temperature: 23.35 C
Minimum temperature: 17.50 C
Maximum temperature: 35.00 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

**How and why the result changes:** Only one of the 24 readings changed, so only the statistics that depend on that reading changed. The mean rose by (35.0 − 29.4) / 24 = 0.23 C because the extra 5.6 C is shared between 24 hours. The maximum rose to 35.0 C because the changed reading is now the hottest of the day. The minimum stayed at 17.50 C because the changed reading was never the coldest. The Fahrenheit values printed are for the first six hours, so they did not change.

## 4. Meaning of the output

The array holds one temperature for each hour. `np.mean` gives the typical temperature of the day (23.12 C), `np.min` the coldest hour (17.50 C, early in the morning) and `np.max` the hottest (29.40 C, early afternoon). The weather station can use these three numbers to summarise the day. The conversion F = 1.8C + 32 is applied to the whole array in one line, so 17.5 C becomes 63.5 F and 29.4 C becomes about 84.9 F. NumPy does this without a loop because it performs the same operation on every element.

## 5. Related real-world case

- **Scenario:** A household smart meter records electricity use every hour. The family wants the daily total, the average, the peak hour, the cost and the hours of high use.
- **Assumptions:**
  - Readings are in kWh and cover one 24-hour day (hour 0 = midnight)
  - Flat tariff of KSh 25 per kWh (assumed for the exercise)
  - High use means more than 1.5 kWh in an hour
- **Input data:** 24 hourly values in `usage_kwh`, from 0.3 kWh at night to 2.8 kWh at 19:00.
- **Modified program:** [`code/Task_02_numpy_arrays_case.py`](../code/Task_02_numpy_arrays_case.py)

**Output:**

```text
Total daily use: 23.00 kWh
Average hourly use: 0.96 kWh
Peak hour: 19:00 with 2.8 kWh
Total daily cost: KSh 575.00
Hours above 1.5 kWh: [17, 18, 19, 20]
Share of use in those hours: 39.1%
```

**Interpretation:** The household used 23.00 kWh, which costs KSh 575 at the assumed rate. The average is 0.96 kWh per hour, but the use is far from even: the peak is 2.8 kWh at 19:00 and four evening hours (17:00 to 20:00) are above 1.5 kWh, so about 39% of the day's electricity is used in just four hours. If the family wants to reduce the bill, the evening is where to look, for example by moving ironing or washing to a lighter-use hour. Vectorisation made this easy: one multiplication gave the cost of all 24 hours and one comparison produced the mask of high-use hours.
