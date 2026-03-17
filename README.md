# Is the Mendoza River Basin Becoming More Water-Stressed?

Hydrological analysis of Argentina's Mendoza River Basin using ERA5 reanalysis data. 

The Mendoza River Basin supplies water to over 1 million people and irrigates one of Argentina's most productive agricultural regions. The basin depends on Andean snowmelt and summer rainfall, making it highly sensitive to climate variability. This project investigates whether water stress is increasing and whether drought conditions can be predicted in advance.

## Data

ERA5 Reanalysis Copernicus   
- Variables: Precipitation, Temperature, PET, Runoff, Soil Moisture 
- Resolution: 0.25° monthly 
- Range: 1980-2024  

## Key Findings

### Basin Climatology

- Mean Annual Precipitation: **806mm**  
- Mean Annual Potential Evapotranspiration: **1247mm**  
- Annual Water Deficit (P - PET): **-441mm**    
- Wettest Month: **June**   
- Driest Month:  **April**  

### Long Term Trends

- Precipitation Trend: **-8.07mm/year**  
- Temperature Trend: **0.03°C/year**, Total Change: **1.24°C**  
- Runoff Trend: **-6.84mm/year**    
- Annual Water Deficit: **-12.80mm/year**   

### Drought Analysis

- Drought Events: **27 drought events**  
- Longest Drought: **2019-07** to **2020-05** (11 months)        
- Most Severe Drought: **2019-07** to **2020-05** (Peak SPI6: -2.04)    
- Drought Frequency: **increased** from **7.3%** (1980-2001) to **27.9%** (2002-2024)   



## Setup
```bash
mamba env create -f environment.yml
conda activate basin-analysis

