# Task 2 (related case): Household electricity use from hourly smart-meter readings
import numpy as np

# Hourly electricity use of one household over 24 hours (kWh)
usage_kwh = np.array([
    0.4, 0.3, 0.3, 0.3, 0.4, 0.8,
    1.5, 1.2, 0.7, 0.5, 0.5, 0.6,
    0.9, 0.8, 0.6, 0.6, 0.9, 1.6,
    2.4, 2.8, 2.2, 1.4, 0.8, 0.5
])
tariff = 25.0          # assumed flat rate in KSh per kWh

total_kwh = np.sum(usage_kwh)
mean_kwh = np.mean(usage_kwh)
peak_hour = np.argmax(usage_kwh)          # index = hour of the day (0-23)
hourly_cost = usage_kwh * tariff          # vectorised: cost of every hour at once
high_use = usage_kwh > 1.5                # boolean mask of high-use hours

print(f"Total daily use: {total_kwh:.2f} kWh")
print(f"Average hourly use: {mean_kwh:.2f} kWh")
print(f"Peak hour: {peak_hour}:00 with {usage_kwh[peak_hour]:.1f} kWh")
print(f"Total daily cost: KSh {hourly_cost.sum():.2f}")
print("Hours above 1.5 kWh:", np.where(high_use)[0].tolist())
print(f"Share of use in those hours: {usage_kwh[high_use].sum() / total_kwh:.1%}")
