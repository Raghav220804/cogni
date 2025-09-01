import streamlit as st
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(layout="wide")
st.title("Production & Deployment Dashboard")

# Create tabs
week1_tab, week2_tab, week3_tab, week4_tab = st.tabs(["Week 1", "Week 2", "Week 3", "Week 4"])

# -------------------- Week 1 --------------------
# with week1_tab:
#     st.header("Week 1 — Production, Demand, Surplus, SS & BTS")

#     prod = {
#         "NDC_Regular": 50000,
#         "NDC_Diet":    30000,
#         "SDC_Regular": 40000,
#         "SDC_Diet":    30000,
#     }

#     demand = {
#         "NDC_Regular": 30000,
#         "NDC_Diet":    20000,
#         "SDC_Regular": 25000,
#         "SDC_Diet":    15000,
#     }

#     ss = {
#         "NDC_Regular": 5000,
#         "NDC_Diet":    5000,
#         "SDC_Regular": 5000,
#         "SDC_Diet":    5000,
#     }

#     bts = {
#         "NDC_Regular": 15000,
#         "NDC_Diet":    5000,
#         "SDC_Regular": 10000,
#         "SDC_Diet":    10000,
#     }

#     # Build tables
#     ndc_df = pd.DataFrame([
#         {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
#          "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
#         {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
#          "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
#     ])

#     sdc_df = pd.DataFrame([
#         {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
#          "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
#         {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
#          "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
#     ])

#     totals_df = pd.DataFrame([
#         {"Measure": "Total Produced (all DCs, per SKU)", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
#         {"Measure": "Total Demand (all DCs, per SKU)", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
#         {"Measure": "Total Surplus (all DCs, per SKU)", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
#          "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
#         {"Measure": "Total Safety Stock (all DCs, per SKU)", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
#         {"Measure": "Total BTS (all DCs, per SKU)", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
#     ])

#     # Display
#     st.subheader("NDC — Week 1")
#     st.table(ndc_df.set_index(["DC", "SKU"]))
#     st.subheader("SDC — Week 1")
#     st.table(sdc_df.set_index(["DC", "SKU"]))
#     st.subheader("Totals across DCs — Week 1")
#     st.table(totals_df.set_index("Measure"))

#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Production", f"{sum(prod.values()):,}")
#     col2.metric("Total BTS", f"{sum(bts.values()):,}")
#     col3.metric("Total Safety Stock", f"{sum(ss.values()):,}")
# -------------------- Week 1 --------------------
with week1_tab:
    st.header("Week 1 — Production, Demand, Surplus, SS & BTS")

    prod = {
        "NDC_Regular": 50000,
        "NDC_Diet":    30000,
        "SDC_Regular": 40000,
        "SDC_Diet":    30000,
    }

    demand = {
        "NDC_Regular": 30000,
        "NDC_Diet":    20000,
        "SDC_Regular": 25000,
        "SDC_Diet":    15000,
    }

    ss = {
        "NDC_Regular": 5000,
        "NDC_Diet":    5000,
        "SDC_Regular": 5000,
        "SDC_Diet":    5000,
    }

    bts = {
        "NDC_Regular": 15000,
        "NDC_Diet":    5000,
        "SDC_Regular": 10000,
        "SDC_Diet":    10000,
    }

    # Build tables
    ndc_df = pd.DataFrame([
        {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
         "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
        {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
         "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
    ])

    sdc_df = pd.DataFrame([
        {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
         "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
        {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
         "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
    ])

    totals_df = pd.DataFrame([
        {"Measure": "Total Produced", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
        {"Measure": "Total Demand", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
        {"Measure": "Total Surplus", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
         "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
        {"Measure": "Total Safety Stock", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
        {"Measure": "Total BTS", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
    ])

    # Display tables
    st.subheader("NDC — Week 1")
    st.table(ndc_df.set_index(["DC", "SKU"]))
    st.subheader("SDC — Week 1")
    st.table(sdc_df.set_index(["DC", "SKU"]))
    st.subheader("Totals across DCs — Week 1")
    st.table(totals_df.set_index("Measure"))

    # -------------------- KPI --------------------
    total_production = sum(prod.values())
    total_demand = sum(demand.values())
    total_bts = sum(bts.values())
    total_ss = sum(ss.values())
    fulfilled_demand = sum(min(prod[k], demand[k]) for k in demand)
    fill_rate = round((fulfilled_demand / total_demand) * 100, 1)
    service_level = round((len([1 for k in demand if prod[k] >= demand[k]]) / len(demand)) * 100, 1)
    truck_size = 10000
    trucks_required = (total_production + truck_size - 1) // truck_size  # Round up

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production:,}")
    col2.metric("Total Demand", f"{total_demand:,}")
    col3.metric("Total BTS", f"{total_bts:,}")
    col4.metric("Total Safety Stock", f"{total_ss:,}")

    col5, col6, col7 = st.columns(3)
    col5.metric("Fill Rate (%)", f"{fill_rate}%")
    col6.metric("Service Level (%)", f"{service_level}%")
    col7.metric("Trucks Required", f"{trucks_required} trucks")


    
    

# -------------------- Week 2 --------------------
# with week2_tab:
#     st.header("Week 2 — Production, Demand, Surplus, SS & BTS")

#     prod = {
#         "NDC_Regular": 50000, "NDC_Diet": 30000, "SDC_Regular": 40000, "SDC_Diet": 30000,
#     }
#     demand = {"NDC_Regular": 35000, "NDC_Diet": 25000, "SDC_Regular": 30000, "SDC_Diet": 20000}
#     ss = {"NDC_Regular": 5000, "NDC_Diet": 5000, "SDC_Regular": 5000, "SDC_Diet": 5000}
#     bts = {"NDC_Regular": 15000, "NDC_Diet": 5000, "SDC_Regular": 10000, "SDC_Diet": 10000}

#     ndc_df = pd.DataFrame([
#         {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
#          "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
#         {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
#          "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
#     ])

#     sdc_df = pd.DataFrame([
#         {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
#          "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
#         {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
#          "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
#     ])

#     totals_df = pd.DataFrame([
#         {"Measure": "Total Produced", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
#         {"Measure": "Total Demand", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
#         {"Measure": "Total Surplus", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
#          "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
#         {"Measure": "Total Safety Stock", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
#         {"Measure": "Total BTS", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
#     ])

#     st.subheader("NDC — Week 2")
#     st.table(ndc_df.set_index(["DC", "SKU"]))
#     st.subheader("SDC — Week 2")
#     st.table(sdc_df.set_index(["DC", "SKU"]))
#     st.subheader("Totals across DCs — Week 2")
#     st.table(totals_df.set_index("Measure"))

#     # KPI
#     total_production = sum(prod.values())
#     total_demand = sum(demand.values())
#     total_bts = sum(bts.values())
#     total_ss = sum(ss.values())
#     fulfilled_demand = sum(min(prod[k], demand[k]) for k in demand)
#     fill_rate = round((fulfilled_demand / total_demand) * 100, 1)
#     service_level = round((len([1 for k in demand if prod[k] >= demand[k]]) / len(demand)) * 100, 1)

#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Total Production", f"{total_production:,}")
#     col2.metric("Total Demand", f"{total_demand:,}")
#     col3.metric("Total BTS", f"{total_bts:,}")
#     col4.metric("Total Safety Stock", f"{total_ss:,}")

#     col5, col6 = st.columns(2)
#     col5.metric("Fill Rate (%)", f"{fill_rate}%")
#     col6.metric("Service Level (%)", f"{service_level}%")

with week2_tab:
    st.header("Week 2 — Production, Demand, Surplus, SS & BTS")

    prod = {
        "NDC_Regular": 50000, "NDC_Diet": 30000,
        "SDC_Regular": 40000, "SDC_Diet": 30000,
    }
    demand = {
        "NDC_Regular": 35000, "NDC_Diet": 25000,
        "SDC_Regular": 30000, "SDC_Diet": 20000
    }
    ss = {
        "NDC_Regular": 5000, "NDC_Diet": 5000,
        "SDC_Regular": 5000, "SDC_Diet": 5000
    }
    bts = {
        "NDC_Regular": 15000, "NDC_Diet": 5000,
        "SDC_Regular": 10000, "SDC_Diet": 10000
    }

    # Build tables
    ndc_df = pd.DataFrame([
        {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
         "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
        {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
         "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
    ])

    sdc_df = pd.DataFrame([
        {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
         "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
        {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
         "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
    ])

    totals_df = pd.DataFrame([
        {"Measure": "Total Produced", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
        {"Measure": "Total Demand", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
        {"Measure": "Total Surplus", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
         "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
        {"Measure": "Total Safety Stock", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
        {"Measure": "Total BTS", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
    ])

    st.subheader("NDC — Week 2")
    st.table(ndc_df.set_index(["DC", "SKU"]))
    st.subheader("SDC — Week 2")
    st.table(sdc_df.set_index(["DC", "SKU"]))
    st.subheader("Totals across DCs — Week 2")
    st.table(totals_df.set_index("Measure"))

    # KPI calculations
    total_production = sum(prod.values())
    total_demand = sum(demand.values())
    total_bts = sum(bts.values())
    total_ss = sum(ss.values())
    fulfilled_demand = sum(min(prod[k], demand[k]) for k in demand)
    fill_rate = round((fulfilled_demand / total_demand) * 100, 1)
    service_level = round((len([1 for k in demand if prod[k] >= demand[k]]) / len(demand)) * 100, 1)

    # Example: Trucks required (assuming 10,000 units per truck)
    trucks_required = round(total_production / 10000)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production:,}")
    col2.metric("Total Demand", f"{total_demand:,}")
    col3.metric("Total BTS", f"{total_bts:,}")
    col4.metric("Total Safety Stock", f"{total_ss:,}")

    col5, col6, col7 = st.columns(3)
    col5.metric("Fill Rate (%)", f"{fill_rate}%")
    col6.metric("Service Level (%)", f"{service_level}%")
    col7.metric("Trucks Required", f"{trucks_required:,}")


# -------------------- Week 3 --------------------
with week3_tab:
    st.header("Week 3 — Production, Demand, Surplus, SS & BTS")

    prod = {"NDC_Regular": 50000, "NDC_Diet": 30000, "SDC_Regular": 40000, "SDC_Diet": 30000}
    demand = {"NDC_Regular": 40000, "NDC_Diet": 30000, "SDC_Regular": 35000, "SDC_Diet": 25000}
    ss = {"NDC_Regular": 5000, "NDC_Diet": 5000, "SDC_Regular": 5000, "SDC_Diet": 5000}
    bts = {"NDC_Regular": 10000, "NDC_Diet": 0, "SDC_Regular": 5000, "SDC_Diet": 5000}

    # Tables
    ndc_df = pd.DataFrame([
        {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
         "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
        {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
         "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
    ])
    sdc_df = pd.DataFrame([
        {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
         "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
        {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
         "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
    ])
    totals_df = pd.DataFrame([
        {"Measure": "Total Produced", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
        {"Measure": "Total Demand", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
        {"Measure": "Total Surplus", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
         "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
        {"Measure": "Total Safety Stock", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
        {"Measure": "Total BTS", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
    ])

    st.subheader("NDC — Week 3")
    st.table(ndc_df.set_index(["DC", "SKU"]))
    st.subheader("SDC — Week 3")
    st.table(sdc_df.set_index(["DC", "SKU"]))
    st.subheader("Totals across DCs — Week 3")
    st.table(totals_df.set_index("Measure"))

    # Cumulative BTS + SS after Week 3
    cumulative_df = pd.DataFrame([
        {"DC": "NDC", "Reg_BTS": 40000, "Diet_BTS": 10000, "SS_Reg": 5000, "SS_Diet": 5000},
        {"DC": "SDC", "Reg_BTS": 40000, "Diet_BTS": 30000, "SS_Reg": 5000, "SS_Diet": 5000},
    ])
    st.subheader("Cumulative BTS + SS after Week 3")
    st.table(cumulative_df.set_index("DC"))

    # KPI calculations
    total_production = sum(prod.values())
    total_demand = sum(demand.values())
    total_bts = sum(bts.values())
    total_ss = sum(ss.values())
    fulfilled_demand = sum(min(prod[k], demand[k]) for k in demand)
    fill_rate = round((fulfilled_demand / total_demand) * 100, 1)
    service_level = round((len([1 for k in demand if prod[k] >= demand[k]]) / len(demand)) * 100, 1)

    # Trucks required (assuming 10,000 units per truck)
    trucks_required = round(total_production / 10000)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production:,}")
    col2.metric("Total Demand", f"{total_demand:,}")
    col3.metric("Total BTS", f"{total_bts:,}")
    col4.metric("Total Safety Stock", f"{total_ss:,}")

    col5, col6, col7 = st.columns(3)
    col5.metric("Fill Rate (%)", f"{fill_rate}%")
    col6.metric("Service Level (%)", f"{service_level}%")
    col7.metric("Trucks Required", f"{trucks_required:,}")


# -------------------- Week 4 --------------------
# with week4_tab:
#     st.header("Week 4 — Production, Demand, Surplus, SS & BTS")
#     prod = {"NDC_Regular": 50000, "NDC_Diet": 30000, "SDC_Regular": 40000, "SDC_Diet": 30000}
#     demand = {"NDC_Regular": 45000, "NDC_Diet": 35000, "SDC_Regular": 40000, "SDC_Diet": 30000}
#     ss = {"NDC_Regular": 5000, "NDC_Diet": 5000, "SDC_Regular": 5000, "SDC_Diet": 5000}
#     bts = {"NDC_Regular": 0, "NDC_Diet": 0, "SDC_Regular": 0, "SDC_Diet": 0}

#     ndc_df = pd.DataFrame([
#         {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
#          "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
#         {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
#          "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
#     ])
#     sdc_df = pd.DataFrame([
#         {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
#          "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
#         {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
#          "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
#     ])
#     totals_df = pd.DataFrame([
#         {"Measure": "Total Produced", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
#         {"Measure": "Total Demand", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
#         {"Measure": "Total Surplus", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
#          "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
#         {"Measure": "Total Safety Stock", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
#         {"Measure": "Total BTS", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
#     ])
#     st.subheader("NDC — Week 4")
#     st.table(ndc_df.set_index(["DC", "SKU"]))
#     st.subheader("SDC — Week 4")
#     st.table(sdc_df.set_index(["DC", "SKU"]))
#     st.subheader("Totals across DCs — Week 4")
#     st.table(totals_df.set_index("Measure"))

#     total_production = sum(prod.values())
#     total_demand = sum(demand.values())
#     total_bts = sum(bts.values())
#     total_ss = sum(ss.values())
#     fulfilled_demand = sum(min(prod[k], demand[k]) for k in demand)
#     fill_rate = round((fulfilled_demand / total_demand) * 100, 1)
#     service_level = round((len([1 for k in demand if prod[k] >= demand[k]]) / len(demand)) * 100, 1)

#     col1, col2, col3, col4 = st.columns(4)
#     col1.metric("Total Production", f"{total_production:,}")
#     col2.metric("Total Demand", f"{total_demand:,}")
#     col3.metric("Total BTS", f"{total_bts:,}")
#     col4.metric("Total Safety Stock", f"{total_ss:,}")

#     col5, col6 = st.columns(2)
#     col5.metric("Fill Rate (%)", f"{fill_rate}%")
#     col6.metric("Service Level (%)", f"{service_level}%")

with week4_tab:
    st.header("Week 4 — Production, Demand, Surplus, SS & BTS")

    prod = {"NDC_Regular": 50000, "NDC_Diet": 30000, "SDC_Regular": 40000, "SDC_Diet": 30000}
    demand = {"NDC_Regular": 45000, "NDC_Diet": 35000, "SDC_Regular": 40000, "SDC_Diet": 30000}
    ss = {"NDC_Regular": 5000, "NDC_Diet": 5000, "SDC_Regular": 5000, "SDC_Diet": 5000}
    bts = {"NDC_Regular": 0, "NDC_Diet": 0, "SDC_Regular": 0, "SDC_Diet": 0}

    # Tables
    ndc_df = pd.DataFrame([
        {"DC": "NDC", "SKU": "Regular", "Produced": prod["NDC_Regular"], "Demand": demand["NDC_Regular"],
         "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"], "Safety_Stock": ss["NDC_Regular"], "BTS": bts["NDC_Regular"]},
        {"DC": "NDC", "SKU": "Diet", "Produced": prod["NDC_Diet"], "Demand": demand["NDC_Diet"],
         "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"], "Safety_Stock": ss["NDC_Diet"], "BTS": bts["NDC_Diet"]},
    ])
    sdc_df = pd.DataFrame([
        {"DC": "SDC", "SKU": "Regular", "Produced": prod["SDC_Regular"], "Demand": demand["SDC_Regular"],
         "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"], "Safety_Stock": ss["SDC_Regular"], "BTS": bts["SDC_Regular"]},
        {"DC": "SDC", "SKU": "Diet", "Produced": prod["SDC_Diet"], "Demand": demand["SDC_Diet"],
         "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"], "Safety_Stock": ss["SDC_Diet"], "BTS": bts["SDC_Diet"]},
    ])
    totals_df = pd.DataFrame([
        {"Measure": "Total Produced", "Regular": prod["NDC_Regular"] + prod["SDC_Regular"], "Diet": prod["NDC_Diet"] + prod["SDC_Diet"]},
        {"Measure": "Total Demand", "Regular": demand["NDC_Regular"] + demand["SDC_Regular"], "Diet": demand["NDC_Diet"] + demand["SDC_Diet"]},
        {"Measure": "Total Surplus", "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
         "Diet": (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"])},
        {"Measure": "Total Safety Stock", "Regular": ss["NDC_Regular"] + ss["SDC_Regular"], "Diet": ss["NDC_Diet"] + ss["SDC_Diet"]},
        {"Measure": "Total BTS", "Regular": bts["NDC_Regular"] + bts["SDC_Regular"], "Diet": bts["NDC_Diet"] + bts["SDC_Diet"]},
    ])

    st.subheader("NDC — Week 4")
    st.table(ndc_df.set_index(["DC", "SKU"]))
    st.subheader("SDC — Week 4")
    st.table(sdc_df.set_index(["DC", "SKU"]))
    st.subheader("Totals across DCs — Week 4")
    st.table(totals_df.set_index("Measure"))

    # KPI calculations
    total_production = sum(prod.values())
    total_demand = sum(demand.values())
    total_bts = sum(bts.values())
    total_ss = sum(ss.values())
    fulfilled_demand = sum(min(prod[k], demand[k]) for k in demand)
    fill_rate = round((fulfilled_demand / total_demand) * 100, 1)
    service_level = round((len([1 for k in demand if prod[k] >= demand[k]]) / len(demand)) * 100, 1)

    # Trucks required (assuming 10,000 units per truck)
    trucks_required = round(total_production / 10000)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production:,}")
    col2.metric("Total Demand", f"{total_demand:,}")
    col3.metric("Total BTS", f"{total_bts:,}")
    col4.metric("Total Safety Stock", f"{total_ss:,}")

    col5, col6, col7 = st.columns(3)
    col5.metric("Fill Rate (%)", f"{fill_rate}%")
    col6.metric("Service Level (%)", f"{service_level}%")
    col7.metric("Trucks Required", f"{trucks_required:,}")



# -------------------- Graphs Tab --------------------
graphs_tab = st.tabs(["Graphs"])[0]

with graphs_tab:
    st.header("📊 Production, Demand, BTS & Safety Stock — All Weeks")

    import plotly.express as px

    # Prepare data
    data = {
        "Week": ["Week 1"]*4 + ["Week 2"]*4 + ["Week 3"]*4 + ["Week 4"]*4,
        "SKU": ["NDC_Regular", "NDC_Diet", "SDC_Regular", "SDC_Diet"]*4,
        "Produced": [50000, 30000, 40000, 30000, 50000, 30000, 40000, 30000,
                     50000, 30000, 40000, 30000, 50000, 30000, 40000, 30000],
        "Demand":   [30000, 20000, 25000, 15000, 35000, 25000, 30000, 20000,
                     40000, 30000, 35000, 25000, 45000, 35000, 40000, 30000],
        "BTS":      [15000, 5000, 10000, 10000, 15000, 5000, 10000, 10000,
                     10000, 0, 5000, 5000, 0, 0, 0, 0],
        "Safety_Stock": [5000]*16
    }

    df = pd.DataFrame(data)

    # Sum per week across SKUs
    df_sum = df.groupby("Week")[["Produced", "Demand", "BTS", "Safety_Stock"]].sum().reset_index()

    # Plot simple grouped bar chart
    fig = px.bar(
        df_sum,
        x="Week",
        y=["Produced", "Demand", "BTS", "Safety_Stock"],
        barmode="group",
        text_auto=True,
        labels={"value": "Units", "Week": "Week"},
        color_discrete_map={
            "Produced": "#636EFA",
            "Demand": "#EF553B",
            "BTS": "#00CC96",
            "Safety_Stock": "#AB63FA"
        },
        title="Production, Demand, BTS & Safety Stock (Sum of all SKUs)"
    )

    fig.update_layout(
        xaxis_title="Week",
        yaxis_title="Units",
        title_font=dict(size=20),
        legend_title="Measure",
        margin=dict(t=80, b=50)
    )

    st.plotly_chart(fig, use_container_width=True)
