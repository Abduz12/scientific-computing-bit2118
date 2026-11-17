# Task 3: Mathematical Functions and Vectorization

**Program file:** [`code/Task_03_vectorization.py`](../code/Task_03_vectorization.py)

**Mathematical concept:** Vectorization applies a mathematical operation to a whole array at once instead of looping over each value.

## 1. Inputs and mathematical operation

**Inputs**

- `latency_ms`: 1,000,000 random latencies between 5 and 250 ms (seed 42)

**Mathematical operation**

- Convert milliseconds to seconds: seconds = latency / 1000
- Square each value: squared = seconds**2
- Time a Python loop against the vectorised version with `timeit`

## 2. Baseline output

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.1415 s
Vectorized time: 0.0033 s
Approximate speed-up: 43.2x
```

## 3. Change an input or parameter

**What I changed:** Changed `1_000_000` to `100_000` in `rng.uniform(5, 250, ...)`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Number of readings N | 1,000,000 | 100,000 | Loop time 0.14 s → 0.016 s; speed-up about 43x → about 21x |

New output (N 1,000,000 -> 100,000):

```text
First five squared latency values: [0.03787665 0.01266192 0.04637842 0.03092504 0.00078812]
Loop time: 0.0159 s
Vectorized time: 0.0008 s
Approximate speed-up: 20.6x
```

**How and why the result changes:** With ten times fewer readings both versions became faster, but the speed-up fell from about 43x to about 21x. Vectorised code has a small fixed start-up cost for each NumPy operation, which matters more when the array is small, while the loop's time grows in direct proportion to the number of values. So vectorisation helps most on large datasets. The first five squared values stayed the same because the seed (42) is the same. The exact timings depend on the computer.

## 4. Meaning of the output

The program simulates one million network latencies between 5 and 250 ms, converts each to seconds and squares it, which is the first step of an error calculation. The printed values (for example 0.0379) are squared latencies. The important output is the timing: the loop took about 0.14 s while the vectorised version took about 0.003 s, a speed-up of about 43 times for identical results. For a monitoring system that must process millions of readings continuously, this difference decides whether the analysis can keep up in real time.

## 5. Related real-world case

- **Scenario:** Brightness correction of a grey-scale image: a 1000 x 1000 image (1,000,000 pixels with brightness 0 to 255) is scaled to the range 0 to 1 and gamma-corrected with exponent 2.2.
- **Assumptions:**
  - The pixels are random 8-bit grey values (seed 42), standing in for a real image
  - Gamma correction means brightness raised to the power 2.2 after scaling to 0 to 1
  - The loop version and the vectorised version must give the same values
- **Input data:** `image`: a 1000 x 1000 array of random integers from 0 to 255.
- **Modified program:** [`code/Task_03_vectorization_case.py`](../code/Task_03_vectorization_case.py)

**Output:**

```text
Mean brightness before: 0.4999 (scaled to 0-1)
Mean brightness after gamma 2.2: 0.3133
Loop time: 1.2263 s
Vectorized time: 0.0059 s
Approximate speed-up: 207.1x
```

**Interpretation:** The mean brightness fell from 0.4999 to 0.3133 because raising numbers between 0 and 1 to the power 2.2 makes them smaller, which darkens the mid-tones. This is the effect of gamma correction on an image. In the run shown above, the vectorised code processed all 1,000,000 pixels about 207 times faster than the loop (0.006 s against 1.2 s). Image processing works on millions of pixels, so vectorised NumPy operations are the practical choice.
