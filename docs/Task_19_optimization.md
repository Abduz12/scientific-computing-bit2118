# Task 19: Numerical Optimization

**Program file:** [`code/Task_19_optimization.py`](../code/Task_19_optimization.py)

**Mathematical concept:** Optimization finds inputs that minimise (or maximise) an objective function, subject to constraints and bounds.

## 1. Inputs and mathematical operation

**Inputs**

- Costs: Type A = 12, Type B = 18
- Capacities: Type A = 100, Type B = 170
- Required capacity: at least 1000; start point [5, 3]

**Mathematical operation**

- Objective: minimise 12x + 18y
- Constraint: 100x + 170y >= 1000, with x, y >= 0
- Solve with `minimize(method='SLSQP')`
- Search whole-server combinations

## 2. Baseline output

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 5.882
Total capacity: 1000.00
Minimum planning cost: 105.88
Best nearby integer solution: (108, 0, 6, 1020)
```

## 3. Change an input or parameter

**What I changed:** Changed the required capacity `1000` to `1500` in the constraint and in the whole-server search.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Required capacity | 1000 | 1500 | Type B units 5.882 → 8.824; minimum cost 105.88 → 158.82; whole-server cost 108 → 162 |

New output (required capacity 1000 -> 1500):

```text
Optimization success: True
Type A allocation: 0.000
Type B allocation: 8.824
Total capacity: 1500.00
Minimum planning cost: 158.82
Best nearby integer solution: (162, 0, 9, 1530)
```

**How and why the result changes:** A bigger capacity requirement needs more servers and therefore costs more. The optimiser still chooses only Type B, because Type B gives 170 / 18 = 9.44 capacity per unit of cost while Type A gives 100 / 12 = 8.33, so B is the cheaper way to get capacity. The cost rose in proportion to the requirement: 158.82 / 105.88 = 1.5, the same as 1500 / 1000. With whole servers, 9 Type B servers give 1530 capacity at a cost of 162, slightly above the continuous cost of 158.82 because 8.824 servers cannot be bought.

## 4. Meaning of the output

The optimiser minimises the cost 12x + 18y subject to a capacity of at least 1000 and non-negative allocations. The answer uses no Type A and 5.882 units of Type B, which gives exactly 1000 capacity at a cost of 105.88. Type B is chosen because it provides more capacity per shilling (170/18 compared with 100/12). The solution lies on the constraint boundary (capacity exactly 1000) because extra capacity would only cost more. When whole servers are needed, the search finds 6 Type B servers, giving 1020 capacity for 108, which is a little more than 105.88 because of rounding up.

## 5. Related real-world case

- **Scenario:** Cheapest daily mix of beans and rice that gives at least 45 g of protein and 1200 kcal. Beans cost KSh 15 per serving (9 g protein, 130 kcal) and rice costs KSh 10 per serving (3 g protein, 200 kcal).
- **Assumptions:**
  - Costs and nutrient values per serving are constant (assumed values)
  - Servings can be fractions in the first solution; a second search uses whole servings
  - Only protein and energy are considered
- **Input data:** Cost = 15x + 10y with constraints 9x + 3y ≥ 45 and 130x + 200y ≥ 1200, starting from [5, 5].
- **Modified program:** [`code/Task_19_optimization_case.py`](../code/Task_19_optimization_case.py)

**Output:**

```text
Optimization success: True
Beans servings: 3.830
Rice servings: 3.511
Protein: 45.0 g, energy: 1200.0 kcal
Minimum daily cost: KSh 92.55
Best whole-serving plan (cost, beans, rice): (100, 4, 4)
```

**Interpretation:** The cheapest plan is about 3.83 servings of beans and 3.51 servings of rice, costing KSh 92.55 per day. Both constraints are met exactly (45.0 g protein and 1200 kcal) because the cheapest plan only just meets both needs. With whole servings only, the best plan is 4 servings of beans and 4 of rice for KSh 100, which is KSh 7.45 more than the ideal because servings cannot be split. The optimiser therefore gives a lower bound for the cost and the whole-serving search gives a practical plan.
