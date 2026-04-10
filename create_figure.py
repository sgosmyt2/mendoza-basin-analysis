import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

df = pd.read_csv("data/processed/mendoza_basin_with_indices.csv", parse_dates=["time"], index_col="time")

fig = plt.figure(figsize=(20, 12))
fig.patch.set_facecolor("white")

gs = gridspec.GridSpec(2, 3, hspace=0.35, wspace=0.3)

# SPI6 45 year plot

ax = fig.add_subplot(gs[0, :2])
spi6 = df["spi6"].dropna()
colors = ["red" if v < 0 else "blue" for v in spi6.values]
ax.bar(
    spi6.index,
    spi6.values,
    width=25,
    color=colors,
    alpha=0.8,
)
ax.axhline(
    y=-1.0,
    color="orange",
    linestyle="--",
    linewidth=1,
    alpha=0.6,
)
ax.axhline(
    y=-2.0,
    color="red",
    linestyle="--",
    linewidth=1,
    alpha=0.6,
)
ax.axhline(
    y=0,
    color="black",
    linewidth=0.5,
)
ax.set_ylabel("SPI6", fontsize=12)
ax.set_title("45 Years of Drought History", fontsize=14, fontweight="bold")
ax.set_ylim(-3.5, 3.5)

years_num = (spi6.index - spi6.index[0]).days / 365.25
z = np.polyfit(years_num, spi6.values, 1)
trend = np.polyval(z, years_num)
ax.plot(
    spi6.index, 
    trend,
    "r-", 
    linewidth=2.5, 
    alpha=0.8,
    label=f"Trend: {z[0]:+.4f}/year"
)
ax.legend(fontsize=10, loc="lower left")

# Water Balance by Month

ax = fig.add_subplot(gs[0, 2])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly = df.groupby(df.index.month).mean()
deficit = monthly["precip_mm"].values - monthly["pev_mm"].values 
colors = ["blue" if d >= 0 else "red" for d in deficit]
ax.bar(
    range(1, 13),
    deficit,
    color=colors,
    alpha=0.8,
    edgecolor="black",
    linewidth=0.5,
)
ax.axhline(
    y=0,
    color="black",
    linewidth=1,
)
ax.set_ylabel("Precip - PET (mm)", fontsize=12)
ax.set_title("Monthly Water Deficit", fontsize=14, fontweight="bold")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(months)

# Temperature Trend

ax = fig.add_subplot(gs[1, 0])
annual_temp = df.resample("YE")["temp_c"].mean()
years = annual_temp.index.year.values.astype(float)
years_rel = years - years[0]
z = np.polyfit(years_rel, annual_temp.values, 1)
trend = np.polyval(z, years_rel)

ax.bar(
    years,
    annual_temp.values,
    color="darkslategrey",
    alpha=0.8,
    edgecolor="black",
    linewidth=0.5,
)
ax.plot(
    years,
    trend,
    "r--",
    linewidth=2.5,
    label=f"+{z[0]*45:.1f}°C over 45 years",
)
ax.set_ylabel("Temperature (°C)", fontsize=12)
ax.set_title("Basin Warming", fontsize=14, fontweight="bold")
ax.legend(fontsize=10)

# Precipitation Trend

ax = fig.add_subplot(gs[1, 1])
annual_precip = df.resample("YE")["precip_mm"].sum()
years = annual_precip.index.year.values.astype(float)
years_rel = years - years[0]
z = np.polyfit(years_rel, annual_precip.values, 1)
trend = np.polyval(z, years_rel)

ax.bar(
    years,
    annual_precip.values,
    color="darkslategrey",
    alpha=0.8,
    edgecolor="black",
    linewidth=0.3,
)
ax.plot(
    years,
    trend,
    "r--",
    linewidth=2.5,
    label=f"{z[0]:+.1f} mm/year",
)
ax.set_ylabel("Annual Precipitation (mm)", fontsize=12)
ax.set_title("Precipitation Trend", fontsize=14, fontweight="bold")
ax.legend(fontsize=10)

# ML Results

ax = fig.add_subplot(gs[1, 2])
models = ["Climatology", "Persistence", "Ridge", "Random\nForest", "Gradient\nBoosting"]
skill_clim = [0, 0.321, 0.008, 0.337, 0.411]
skill_persist = [-0.474, 0, -0.462, 0.023, 0.132]
x = np.arange(len(models))
width = 0.35
bars1 = ax.bar(
    x - width/2, 
    skill_clim, 
    width, 
    label="vs Climatology", 
    color="tan", 
    alpha=0.8
)
bars2 = ax.bar(
    x + width/2, 
    skill_persist, 
    width, 
    label="vs Persistence", 
    color="dimgrey", 
    alpha=0.8
)
ax.axhline(
    y=0, 
    color="black", 
    linewidth=1
)
ax.set_ylabel("Skill Score", fontsize=12)
ax.set_title("SPI6 Forecast Skill", fontsize=14, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=9)
ax.legend(fontsize=9, loc="upper left")

# Title and Output

fig.suptitle("Is the Mendoza River Basin Becoming More Water Stressed?", fontsize=18, fontweight="bold", y=1.02)
plt.savefig("outputs/figures/dashboard.png", dpi=200, bbox_inches="tight", facecolor="white", edgecolor="none")
plt.show()