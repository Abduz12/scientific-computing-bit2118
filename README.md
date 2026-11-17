# Scientific Computing (BIT 2118): Individual Repository

Abdirahman Mohamud | BSCCS/2024/54673 | Mount Kenya University

Individual submission for the BIT 2118 Scientific Computing group work (Tasks 2 to 20). The tasks were discussed in a group; this repository is my own submission and is not a group repository.

## Structure

```
code/          Python programs: Task_XX_name.py (the task) and Task_XX_name_case.py (my modified related real-world case)
docs/          One document per task: inputs and operation, baseline output, parameter change, interpretation, related case
docs/images/   Graphs produced by the programs
```

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python code/Task_02_numpy_arrays.py
python code/Task_02_numpy_arrays_case.py
```

## Tasks

| Task | Topic | Code | Documentation | Done |
|---|---|---|---|---|
| 2 | NumPy Arrays and Numerical Computation | [`Task_02_numpy_arrays.py`](code/Task_02_numpy_arrays.py), [`Task_02_numpy_arrays_case.py`](code/Task_02_numpy_arrays_case.py) | [docs](docs/Task_02_numpy_arrays.md) | ☑ |
| 3 | Mathematical Functions and Vectorization | [`Task_03_vectorization.py`](code/Task_03_vectorization.py), [`Task_03_vectorization_case.py`](code/Task_03_vectorization_case.py) | [docs](docs/Task_03_vectorization.md) | ☑ |
| 4 | Floating-Point Arithmetic and Numerical Errors | [`Task_04_numerical_errors.py`](code/Task_04_numerical_errors.py), [`Task_04_numerical_errors_case.py`](code/Task_04_numerical_errors_case.py) | [docs](docs/Task_04_numerical_errors.md) | ☑ |
| 5 | Matrix Algebra and Matrix Operations | [`Task_05_matrix_algebra.py`](code/Task_05_matrix_algebra.py), [`Task_05_matrix_algebra_case.py`](code/Task_05_matrix_algebra_case.py) | [docs](docs/Task_05_matrix_algebra.md) | ☑ |
| 6 | Solution of Systems of Linear Equations | [`Task_06_linear_systems.py`](code/Task_06_linear_systems.py), [`Task_06_linear_systems_case.py`](code/Task_06_linear_systems_case.py) | [docs](docs/Task_06_linear_systems.md) | ☑ |
| 7 | Gaussian Elimination and LU Decomposition | [`Task_07_gaussian_lu.py`](code/Task_07_gaussian_lu.py), [`Task_07_gaussian_lu_case.py`](code/Task_07_gaussian_lu_case.py) | [docs](docs/Task_07_gaussian_lu.md) | ☑ |
| 8 | Iterative Methods for Linear Systems | [`Task_08_iterative_linear.py`](code/Task_08_iterative_linear.py), [`Task_08_iterative_linear_case.py`](code/Task_08_iterative_linear_case.py) | [docs](docs/Task_08_iterative_linear.md) | ☑ |
| 9 | Eigenvalues and Eigenvectors | [`Task_09_eigenvalues.py`](code/Task_09_eigenvalues.py), [`Task_09_eigenvalues_case.py`](code/Task_09_eigenvalues_case.py) | [docs](docs/Task_09_eigenvalues.md) | ☑ |
| 10 | Root Finding: Bisection and Fixed-Point Methods | [`Task_10_bisection_fixed_point.py`](code/Task_10_bisection_fixed_point.py), [`Task_10_bisection_fixed_point_case.py`](code/Task_10_bisection_fixed_point_case.py) | [docs](docs/Task_10_bisection_fixed_point.md) | ☑ |
| 11 | Root Finding: Newton-Raphson and Secant Methods | [`Task_11_newton_secant.py`](code/Task_11_newton_secant.py), [`Task_11_newton_secant_case.py`](code/Task_11_newton_secant_case.py) | [docs](docs/Task_11_newton_secant.md) | ☑ |
| 12 | Polynomial and Nonlinear Equation Solving | [`Task_12_nonlinear_equations.py`](code/Task_12_nonlinear_equations.py), [`Task_12_nonlinear_equations_case.py`](code/Task_12_nonlinear_equations_case.py) | [docs](docs/Task_12_nonlinear_equations.md) | ☑ |
| 13 | Interpolation | [`Task_13_interpolation.py`](code/Task_13_interpolation.py), [`Task_13_interpolation_case.py`](code/Task_13_interpolation_case.py) | [docs](docs/Task_13_interpolation.md) | ☑ |
| 14 | Curve Fitting and Approximation | [`Task_14_curve_fitting.py`](code/Task_14_curve_fitting.py), [`Task_14_curve_fitting_case.py`](code/Task_14_curve_fitting_case.py) | [docs](docs/Task_14_curve_fitting.md) | ☑ |
| 15 | Numerical Differentiation | [`Task_15_numerical_differentiation.py`](code/Task_15_numerical_differentiation.py), [`Task_15_numerical_differentiation_case.py`](code/Task_15_numerical_differentiation_case.py) | [docs](docs/Task_15_numerical_differentiation.md) | ☑ |
| 16 | Numerical Integration | [`Task_16_numerical_integration.py`](code/Task_16_numerical_integration.py), [`Task_16_numerical_integration_case.py`](code/Task_16_numerical_integration_case.py) | [docs](docs/Task_16_numerical_integration.md) | ☑ |
| 17 | Ordinary Differential Equations: Euler Method | [`Task_17_euler_ode.py`](code/Task_17_euler_ode.py), [`Task_17_euler_ode_case.py`](code/Task_17_euler_ode_case.py) | [docs](docs/Task_17_euler_ode.md) | ☑ |
| 18 | Numerical Solution of ODEs Using SciPy | [`Task_18_scipy_ode.py`](code/Task_18_scipy_ode.py), [`Task_18_scipy_ode_case.py`](code/Task_18_scipy_ode_case.py) | [docs](docs/Task_18_scipy_ode.md) | ☑ |
| 19 | Numerical Optimization | [`Task_19_optimization.py`](code/Task_19_optimization.py), [`Task_19_optimization_case.py`](code/Task_19_optimization_case.py) | [docs](docs/Task_19_optimization.md) | ☑ |
| 20 | Random Numbers and Monte Carlo Methods | [`Task_20_monte_carlo.py`](code/Task_20_monte_carlo.py), [`Task_20_monte_carlo_case.py`](code/Task_20_monte_carlo_case.py) | [docs](docs/Task_20_monte_carlo.md) | ☑ |

## Notes on sources and AI use

The starter programs come from the BIT 2118 group work brief; I restored their indentation, and Task 16 uses `np.trapezoid` when available and `np.trapz` on older NumPy. Claude (Anthropic, 2026) was used to help prepare this repository: it ran the programs and drafted the parameter-change explanations, interpretations and related-case programs.

 I ran every program, checked the results, changed the parameters, and edited the explanations and cases in my own words.
