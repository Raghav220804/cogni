import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

# ----------------------
st.title("📦 Cola Company Supply Planner")
st.write("""
Upload an Excel/CSV file with the following columns:
Week, SKU, Demand_North, Demand_South
""")

# ----------------------
# Parameters
MAX_PRODUCTION = 150_000
TRUCK_SIZE = 10_000
SAFETY_STOCK = 5_000
FORECAST_WEEKS = 4

# ----------------------
# File upload
uploaded_file = st.file_uploader("Upload Demand Data (Excel/CSV)", type=["xlsx","csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Input Demand Data")
    st.dataframe(df)

    # ----------------------
    # Forecast function
    def forecast_series(series, periods=FORECAST_WEEKS):
        try:
            model = ExponentialSmoothing(series, trend="add", seasonal=None)
            fit = model.fit()
            forecast = fit.forecast(periods)
            return forecast
        except:
            return pd.Series([series.mean()]*periods)

    # ----------------------
    # Forecast next 4 weeks per SKU
    forecast_list = []
    last_week = df["Week"].max()
    future_weeks = [last_week + i for i in range(1, FORECAST_WEEKS+1)]

    for sku in df["SKU"].unique():
        sku_df = df[df["SKU"]==sku].sort_values("Week")
        forecast_north = forecast_series(sku_df["Demand_North"])
        forecast_south = forecast_series(sku_df["Demand_South"])
        for i, week in enumerate(future_weeks):
            forecast_list.append({
        "Week": week,
        "SKU": sku,
        "Demand_North": int(forecast_north.iloc[i]),
        "Demand_South": int(forecast_south.iloc[i])
    })

    

    forecast_df = pd.DataFrame(forecast_list)
    st.subheader("🔮 Forecasted Demand (Next Weeks)")
    st.dataframe(forecast_df)

    # ----------------------
    # Combine historical + forecast
    combined_df = pd.concat([df[["Week","SKU","Demand_North","Demand_South"]], forecast_df], ignore_index=True)
    combined_df.sort_values(["Week","SKU"], inplace=True)
    combined_df.reset_index(drop=True, inplace=True)

    # ----------------------
    # Supply chain simulation
    results = []

    for week in combined_df["Week"].unique():
        week_df = combined_df[combined_df["Week"]==week]
        total_demand = week_df["Demand_North"].sum() + week_df["Demand_South"].sum()

        # Allocate production per SKU
        prod_dict = {}
        if total_demand <= MAX_PRODUCTION:
            for _, row in week_df.iterrows():
                prod_dict[row["SKU"]] = {
                    "Produced_North": row["Demand_North"],
                    "Produced_South": row["Demand_South"]
                }
        else:
            # Share production proportionally
            for _, row in week_df.iterrows():
                sku_total = row["Demand_North"] + row["Demand_South"]
                prod_n = int(MAX_PRODUCTION * (sku_total / total_demand) * (row["Demand_North"]/sku_total))
                prod_s = int(MAX_PRODUCTION * (sku_total / total_demand) * (row["Demand_South"]/sku_total))
                prod_dict[row["SKU"]] = {"Produced_North": prod_n, "Produced_South": prod_s}

        # Apply truck size & safety stock
        for sku, prod in prod_dict.items():
            prod_n = max((prod["Produced_North"]//TRUCK_SIZE)*TRUCK_SIZE, SAFETY_STOCK)
            prod_s = max((prod["Produced_South"]//TRUCK_SIZE)*TRUCK_SIZE, SAFETY_STOCK)
            demand_n = int(week_df[week_df["SKU"]==sku]["Demand_North"].values[0])
            demand_s = int(week_df[week_df["SKU"]==sku]["Demand_South"].values[0])
            fulfilled_n = min(prod_n, demand_n)
            fulfilled_s = min(prod_s, demand_s)
            fulfillment_pct = (fulfilled_n + fulfilled_s)/(demand_n+demand_s)*100 if (demand_n+demand_s)>0 else 100
            trucks_needed = (prod_n + prod_s)//TRUCK_SIZE

            results.append({
                "Week": week,
                "SKU": sku,
                "Produced_North": prod_n,
                "Produced_South": prod_s,
                "Demand_North": demand_n,
                "Demand_South": demand_s,
                "Demand_Fulfillment_%": round(fulfillment_pct,2),
                "Trucks_Required": trucks_needed
            })

    results_df = pd.DataFrame(results)
    st.subheader("🏭 Production & Deployment Plan")
    st.dataframe(results_df)

    # ----------------------
    # Plots
    st.subheader("🔎 Production Split per Week (North vs South per SKU)")
    fig, ax = plt.subplots(figsize=(10,5))
    for sku in results_df["SKU"].unique():
        df_sku = results_df[results_df["SKU"]==sku]
        ax.bar(df_sku["Week"], df_sku["Produced_North"], label=f"{sku} North")
        ax.bar(df_sku["Week"], df_sku["Produced_South"], bottom=df_sku["Produced_North"], label=f"{sku} South")
    ax.set_ylabel("Bottles Produced")
    ax.set_xlabel("Week")
    ax.legend()
    st.pyplot(fig)

    st.subheader("✅ Demand Fulfillment %")
    fig2, ax2 = plt.subplots(figsize=(10,4))
    for sku in results_df["SKU"].unique():
        df_sku = results_df[results_df["SKU"]==sku]
        ax2.plot(df_sku["Week"], df_sku["Demand_Fulfillment_%"], marker="o", label=sku)
    ax2.set_ylabel("Fulfillment %")
    ax2.set_xlabel("Week")
    ax2.set_ylim(0,105)
    ax2.legend()
    st.pyplot(fig2)

    st.subheader("🚚 Trucks Required per Week")
    fig3, ax3 = plt.subplots(figsize=(10,4))
    for sku in results_df["SKU"].unique():
        df_sku = results_df[results_df["SKU"]==sku]
        ax3.bar(df_sku["Week"], df_sku["Trucks_Required"], label=sku)
    ax3.set_ylabel("Trucks")
    ax3.set_xlabel("Week")
    ax3.legend()
    st.pyplot(fig3)
