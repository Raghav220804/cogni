import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Production & Deployment Dashboard")

# Create tabs
week1_tab, week2_tab, week3_tab, week4_tab = st.tabs(["Week 1", "Week 2", "Week 3", "Week 4"])

# -------------------- Week 1 --------------------
with week1_tab:
    st.header("Week 1 — Production, Demand, Surplus, SS & BTS")
    
    # Example tables for Week 1
    prod = {
    "NDC_Regular": 50000,
    "NDC_Diet":    30000,
    "SDC_Regular": 40000,
    "SDC_Diet":    30000,
}

# Demand week 1 (exact)
demand = {
    "NDC_Regular": 30000,
    "NDC_Diet":    20000,
    "SDC_Regular": 25000,
    "SDC_Diet":    15000,
}

# Safety stock floor per SKU per DC (exact)
ss = {
    "NDC_Regular": 5000,
    "NDC_Diet":    5000,
    "SDC_Regular": 5000,
    "SDC_Diet":    5000,
}

# BTS values computed for week 1 (exact from your worked example)
bts = {
    "NDC_Regular": 15000,
    "NDC_Diet":    5000,
    "SDC_Regular": 10000,
    "SDC_Diet":    10000,
}

# Build per-DC tables
ndc_df = pd.DataFrame([
    {
        "DC": "NDC",
        "SKU": "Regular",
        "Produced": prod["NDC_Regular"],
        "Demand": demand["NDC_Regular"],
        "Surplus": prod["NDC_Regular"] - demand["NDC_Regular"],
        "Safety_Stock": ss["NDC_Regular"],
        "BTS": bts["NDC_Regular"],
    },
    {
        "DC": "NDC",
        "SKU": "Diet",
        "Produced": prod["NDC_Diet"],
        "Demand": demand["NDC_Diet"],
        "Surplus": prod["NDC_Diet"] - demand["NDC_Diet"],
        "Safety_Stock": ss["NDC_Diet"],
        "BTS": bts["NDC_Diet"],
    }
])

sdc_df = pd.DataFrame([
    {
        "DC": "SDC",
        "SKU": "Regular",
        "Produced": prod["SDC_Regular"],
        "Demand": demand["SDC_Regular"],
        "Surplus": prod["SDC_Regular"] - demand["SDC_Regular"],
        "Safety_Stock": ss["SDC_Regular"],
        "BTS": bts["SDC_Regular"],
    },
    {
        "DC": "SDC",
        "SKU": "Diet",
        "Produced": prod["SDC_Diet"],
        "Demand": demand["SDC_Diet"],
        "Surplus": prod["SDC_Diet"] - demand["SDC_Diet"],
        "Safety_Stock": ss["SDC_Diet"],
        "BTS": bts["SDC_Diet"],
    }
])

# Totals across DCs for Week 1
totals_df = pd.DataFrame([
    {
        "Measure": "Total Produced (all DCs, per SKU)",
        "Regular": prod["NDC_Regular"] + prod["SDC_Regular"],
        "Diet":    prod["NDC_Diet"] + prod["SDC_Diet"],
    },
    {
        "Measure": "Total Demand (all DCs, per SKU)",
        "Regular": demand["NDC_Regular"] + demand["SDC_Regular"],
        "Diet":    demand["NDC_Diet"] + demand["SDC_Diet"],
    },
    {
        "Measure": "Total Surplus (all DCs, per SKU)",
        "Regular": (prod["NDC_Regular"] - demand["NDC_Regular"]) + (prod["SDC_Regular"] - demand["SDC_Regular"]),
        "Diet":    (prod["NDC_Diet"] - demand["NDC_Diet"]) + (prod["SDC_Diet"] - demand["SDC_Diet"]),
    },
    {
        "Measure": "Total Safety Stock (all DCs, per SKU)",
        "Regular": ss["NDC_Regular"] + ss["SDC_Regular"],
        "Diet":    ss["NDC_Diet"] + ss["SDC_Diet"],
    },
    {
        "Measure": "Total BTS (all DCs, per SKU)",
        "Regular": bts["NDC_Regular"] + bts["SDC_Regular"],
        "Diet":    bts["NDC_Diet"] + bts["SDC_Diet"],
    }
])

# Display nicely
st.subheader("NDC — Week 1 (Exact values)")
st.table(ndc_df.set_index(["DC", "SKU"]))

st.subheader("SDC — Week 1 (Exact values)")
st.table(sdc_df.set_index(["DC", "SKU"]))

st.subheader("Totals across DCs — Week 1 (Exact)")
st.table(totals_df.set_index("Measure"))

# Small KPI tiles
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Production (Week 1)", f"{sum(prod.values()):,}")
with col2:
    st.metric("Total BTS (Week 1, all SKUs)", f"{sum(bts.values()):,}")
with col3:
    st.metric("Total Safety Stock (Week 1, all SKUs)", f"{sum(ss.values()):,}")

st.markdown("---")
st.info("These tables reproduce Week 1 exactly from your worked example. Say 'Proceed Step 2' to add Week 2 tables next.")


# -------------------- Week 2 --------------------
with week2_tab:
    st.header("Week 2 — Production, Demand, Surplus, SS & BTS")

    # ------------------ INPUT DATA ------------------
    prod_w2 = {
        "NDC_Regular": 50000,
        "NDC_Diet":    30000,
        "SDC_Regular": 40000,
        "SDC_Diet":    30000,
    }

    demand_w2 = {
        "NDC_Regular": 35000,
        "NDC_Diet":    25000,
        "SDC_Regular": 30000,
        "SDC_Diet":    20000,
    }

    ss_w2 = {
        "NDC_Regular": 5000,
        "NDC_Diet":    5000,
        "SDC_Regular": 5000,
        "SDC_Diet":    5000,
    }

    bts_w2 = {
        "NDC_Regular": 15000,
        "NDC_Diet":    5000,
        "SDC_Regular": 10000,
        "SDC_Diet":    10000,
    }

    # ------------------ BUILD TABLES ------------------
    ndc_df_w2 = pd.DataFrame([
        {
            "DC": "NDC",
            "SKU": "Regular",
            "Produced": prod_w2["NDC_Regular"],
            "Demand": demand_w2["NDC_Regular"],
            "Surplus": prod_w2["NDC_Regular"] - demand_w2["NDC_Regular"],
            "Safety_Stock": ss_w2["NDC_Regular"],
            "BTS": bts_w2["NDC_Regular"],
        },
        {
            "DC": "NDC",
            "SKU": "Diet",
            "Produced": prod_w2["NDC_Diet"],
            "Demand": demand_w2["NDC_Diet"],
            "Surplus": prod_w2["NDC_Diet"] - demand_w2["NDC_Diet"],
            "Safety_Stock": ss_w2["NDC_Diet"],
            "BTS": bts_w2["NDC_Diet"],
        }
    ])

    sdc_df_w2 = pd.DataFrame([
        {
            "DC": "SDC",
            "SKU": "Regular",
            "Produced": prod_w2["SDC_Regular"],
            "Demand": demand_w2["SDC_Regular"],
            "Surplus": prod_w2["SDC_Regular"] - demand_w2["SDC_Regular"],
            "Safety_Stock": ss_w2["SDC_Regular"],
            "BTS": bts_w2["SDC_Regular"],
        },
        {
            "DC": "SDC",
            "SKU": "Diet",
            "Produced": prod_w2["SDC_Diet"],
            "Demand": demand_w2["SDC_Diet"],
            "Surplus": prod_w2["SDC_Diet"] - demand_w2["SDC_Diet"],
            "Safety_Stock": ss_w2["SDC_Diet"],
            "BTS": bts_w2["SDC_Diet"],
        }
    ])

    totals_df_w2 = pd.DataFrame([
        {
            "Measure": "Total Produced (all DCs, per SKU)",
            "Regular": prod_w2["NDC_Regular"] + prod_w2["SDC_Regular"],
            "Diet":    prod_w2["NDC_Diet"] + prod_w2["SDC_Diet"],
        },
        {
            "Measure": "Total Demand (all DCs, per SKU)",
            "Regular": demand_w2["NDC_Regular"] + demand_w2["SDC_Regular"],
            "Diet":    demand_w2["NDC_Diet"] + demand_w2["SDC_Diet"],
        },
        {
            "Measure": "Total Surplus (all DCs, per SKU)",
            "Regular": (prod_w2["NDC_Regular"] - demand_w2["NDC_Regular"]) + (prod_w2["SDC_Regular"] - demand_w2["SDC_Regular"]),
            "Diet":    (prod_w2["NDC_Diet"] - demand_w2["NDC_Diet"]) + (prod_w2["SDC_Diet"] - demand_w2["SDC_Diet"]),
        },
        {
            "Measure": "Total Safety Stock (all DCs, per SKU)",
            "Regular": ss_w2["NDC_Regular"] + ss_w2["SDC_Regular"],
            "Diet":    ss_w2["NDC_Diet"] + ss_w2["SDC_Diet"],
        },
        {
            "Measure": "Total BTS (all DCs, per SKU)",
            "Regular": bts_w2["NDC_Regular"] + bts_w2["SDC_Regular"],
            "Diet":    bts_w2["NDC_Diet"] + bts_w2["SDC_Diet"],
        }
    ])

    # ------------------ DISPLAY TABLES ------------------
    st.subheader("NDC — Week 2")
    st.table(ndc_df_w2.set_index(["DC","SKU"]))

    st.subheader("SDC — Week 2")
    st.table(sdc_df_w2.set_index(["DC","SKU"]))

    st.subheader("Totals across DCs — Week 2")
    st.table(totals_df_w2.set_index("Measure"))

    # ------------------ KPI ------------------
    total_production_w2 = sum(prod_w2.values())
    total_demand_w2 = sum(demand_w2.values())
    total_bts_w2 = sum(bts_w2.values())
    total_ss_w2 = sum(ss_w2.values())
    fulfilled_demand_w2 = sum(min(prod_w2[k], demand_w2[k]) for k in demand_w2)
    fill_rate_w2 = round((fulfilled_demand_w2 / total_demand_w2) * 100, 1)
    service_level_w2 = round((len([1 for k in demand_w2 if prod_w2[k] >= demand_w2[k]]) / len(demand_w2)) * 100, 1)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production_w2:,}")
    col2.metric("Total Demand", f"{total_demand_w2:,}")
    col3.metric("Total BTS", f"{total_bts_w2:,}")
    col4.metric("Total Safety Stock", f"{total_ss_w2:,}")

    col5, col6 = st.columns(2)
    col5.metric("Fill Rate (%)", f"{fill_rate_w2}%")
    col6.metric("Service Level (%)", f"{service_level_w2}%")


# -------------------- Week 3 --------------------
with week3_tab:
    st.header("Week 3 — Production, Demand, Surplus, SS & BTS")

    # ------------------ INPUT DATA ------------------
    prod_w3 = {
        "NDC_Regular": 50000,
        "NDC_Diet":    30000,
        "SDC_Regular": 40000,
        "SDC_Diet":    30000,
    }

    demand_w3 = {
        "NDC_Regular": 40000,
        "NDC_Diet":    30000,
        "SDC_Regular": 35000,
        "SDC_Diet":    25000,
    }

    ss_w3 = {
        "NDC_Regular": 5000,
        "NDC_Diet":    5000,
        "SDC_Regular": 5000,
        "SDC_Diet":    5000,
    }

    bts_w3 = {
        "NDC_Regular": 10000,
        "NDC_Diet":    0,
        "SDC_Regular": 5000,
        "SDC_Diet":    5000,
    }

    # ------------------ BUILD TABLES ------------------
    ndc_df_w3 = pd.DataFrame([
        {
            "DC": "NDC",
            "SKU": "Regular",
            "Produced": prod_w3["NDC_Regular"],
            "Demand": demand_w3["NDC_Regular"],
            "Surplus": prod_w3["NDC_Regular"] - demand_w3["NDC_Regular"],
            "Safety_Stock": ss_w3["NDC_Regular"],
            "BTS": bts_w3["NDC_Regular"],
        },
        {
            "DC": "NDC",
            "SKU": "Diet",
            "Produced": prod_w3["NDC_Diet"],
            "Demand": demand_w3["NDC_Diet"],
            "Surplus": prod_w3["NDC_Diet"] - demand_w3["NDC_Diet"],
            "Safety_Stock": ss_w3["NDC_Diet"],
            "BTS": bts_w3["NDC_Diet"],
        }
    ])

    sdc_df_w3 = pd.DataFrame([
        {
            "DC": "SDC",
            "SKU": "Regular",
            "Produced": prod_w3["SDC_Regular"],
            "Demand": demand_w3["SDC_Regular"],
            "Surplus": prod_w3["SDC_Regular"] - demand_w3["SDC_Regular"],
            "Safety_Stock": ss_w3["SDC_Regular"],
            "BTS": bts_w3["SDC_Regular"],
        },
        {
            "DC": "SDC",
            "SKU": "Diet",
            "Produced": prod_w3["SDC_Diet"],
            "Demand": demand_w3["SDC_Diet"],
            "Surplus": prod_w3["SDC_Diet"] - demand_w3["SDC_Diet"],
            "Safety_Stock": ss_w3["SDC_Diet"],
            "BTS": bts_w3["SDC_Diet"],
        }
    ])

    totals_df_w3 = pd.DataFrame([
        {
            "Measure": "Total Produced (all DCs, per SKU)",
            "Regular": prod_w3["NDC_Regular"] + prod_w3["SDC_Regular"],
            "Diet":    prod_w3["NDC_Diet"] + prod_w3["SDC_Diet"],
        },
        {
            "Measure": "Total Demand (all DCs, per SKU)",
            "Regular": demand_w3["NDC_Regular"] + demand_w3["SDC_Regular"],
            "Diet":    demand_w3["NDC_Diet"] + demand_w3["SDC_Diet"],
        },
        {
            "Measure": "Total Surplus (all DCs, per SKU)",
            "Regular": (prod_w3["NDC_Regular"] - demand_w3["NDC_Regular"]) + (prod_w3["SDC_Regular"] - demand_w3["SDC_Regular"]),
            "Diet":    (prod_w3["NDC_Diet"] - demand_w3["NDC_Diet"]) + (prod_w3["SDC_Diet"] - demand_w3["SDC_Diet"]),
        },
        {
            "Measure": "Total Safety Stock (all DCs, per SKU)",
            "Regular": ss_w3["NDC_Regular"] + ss_w3["SDC_Regular"],
            "Diet":    ss_w3["NDC_Diet"] + ss_w3["SDC_Diet"],
        },
        {
            "Measure": "Total BTS (all DCs, per SKU)",
            "Regular": bts_w3["NDC_Regular"] + bts_w3["SDC_Regular"],
            "Diet":    bts_w3["NDC_Diet"] + bts_w3["SDC_Diet"],
        }
    ])

    # ------------------ DISPLAY TABLES ------------------
    st.subheader("NDC — Week 3")
    st.table(ndc_df_w3.set_index(["DC","SKU"]))

    st.subheader("SDC — Week 3")
    st.table(sdc_df_w3.set_index(["DC","SKU"]))

    st.subheader("Totals across DCs — Week 3")
    st.table(totals_df_w3.set_index("Measure"))

    # ------------------ CUMULATIVE ------------------
    cumulative_df_w3 = pd.DataFrame([
        {
            "DC": "NDC",
            "Reg_BTS": 40000,   # W1+W2+W3
            "Diet_BTS": 10000,
            "SS_Reg": 5000,
            "SS_Diet": 5000,
        },
        {
            "DC": "SDC",
            "Reg_BTS": 40000,
            "Diet_BTS": 30000,
            "SS_Reg": 5000,
            "SS_Diet": 5000,
        }
    ])
    st.subheader("Cumulative BTS + SS after Week 3")
    st.table(cumulative_df_w3.set_index("DC"))

    # ------------------ KPI ------------------
    total_production_w3 = sum(prod_w3.values())
    total_demand_w3 = sum(demand_w3.values())
    total_bts_w3 = sum(bts_w3.values())
    total_ss_w3 = sum(ss_w3.values())
    fulfilled_demand_w3 = sum(min(prod_w3[k], demand_w3[k]) for k in demand_w3)
    fill_rate_w3 = round((fulfilled_demand_w3 / total_demand_w3) * 100, 1)
    service_level_w3 = round((len([1 for k in demand_w3 if prod_w3[k] >= demand_w3[k]]) / len(demand_w3)) * 100, 1)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production_w3:,}")
    col2.metric("Total Demand", f"{total_demand_w3:,}")
    col3.metric("Total BTS", f"{total_bts_w3:,}")
    col4.metric("Total Safety Stock", f"{total_ss_w3:,}")

    col5, col6 = st.columns(2)
    col5.metric("Fill Rate (%)", f"{fill_rate_w3}%")
    col6.metric("Service Level (%)", f"{service_level_w3}%")


# -------------------- Week 4 --------------------
with week4_tab:
    st.header("Week 4 — Production, Demand, Surplus, SS & BTS")

    # ------------------ INPUT DATA ------------------
    prod_w4 = {
        "NDC_Regular": 50000,
        "NDC_Diet":    30000,
        "SDC_Regular": 40000,
        "SDC_Diet":    30000,
    }

    demand_w4 = {
        "NDC_Regular": 45000,
        "NDC_Diet":    35000,
        "SDC_Regular": 40000,
        "SDC_Diet":    30000,
    }

    ss_w4 = {
        "NDC_Regular": 5000,
        "NDC_Diet":    5000,
        "SDC_Regular": 5000,
        "SDC_Diet":    5000,
    }

    bts_w4 = {
        "NDC_Regular": 5000,
        "NDC_Diet":    0,
        "SDC_Regular": 0,
        "SDC_Diet":    0,
    }

    # ------------------ BUILD TABLES ------------------
    ndc_df_w4 = pd.DataFrame([
        {
            "DC": "NDC",
            "SKU": "Regular",
            "Produced": prod_w4["NDC_Regular"],
            "Demand": demand_w4["NDC_Regular"],
            "Surplus": prod_w4["NDC_Regular"] - demand_w4["NDC_Regular"],
            "Safety_Stock": ss_w4["NDC_Regular"],
            "BTS": bts_w4["NDC_Regular"],
        },
        {
            "DC": "NDC",
            "SKU": "Diet",
            "Produced": prod_w4["NDC_Diet"],
            "Demand": demand_w4["NDC_Diet"],
            "Surplus": prod_w4["NDC_Diet"] - demand_w4["NDC_Diet"],
            "Safety_Stock": ss_w4["NDC_Diet"],
            "BTS": bts_w4["NDC_Diet"],
        }
    ])

    sdc_df_w4 = pd.DataFrame([
        {
            "DC": "SDC",
            "SKU": "Regular",
            "Produced": prod_w4["SDC_Regular"],
            "Demand": demand_w4["SDC_Regular"],
            "Surplus": prod_w4["SDC_Regular"] - demand_w4["SDC_Regular"],
            "Safety_Stock": ss_w4["SDC_Regular"],
            "BTS": bts_w4["SDC_Regular"],
        },
        {
            "DC": "SDC",
            "SKU": "Diet",
            "Produced": prod_w4["SDC_Diet"],
            "Demand": demand_w4["SDC_Diet"],
            "Surplus": prod_w4["SDC_Diet"] - demand_w4["SDC_Diet"],
            "Safety_Stock": ss_w4["SDC_Diet"],
            "BTS": bts_w4["SDC_Diet"],
        }
    ])

    totals_df_w4 = pd.DataFrame([
        {
            "Measure": "Total Produced (all DCs, per SKU)",
            "Regular": prod_w4["NDC_Regular"] + prod_w4["SDC_Regular"],
            "Diet":    prod_w4["NDC_Diet"] + prod_w4["SDC_Diet"],
        },
        {
            "Measure": "Total Demand (all DCs, per SKU)",
            "Regular": demand_w4["NDC_Regular"] + demand_w4["SDC_Regular"],
            "Diet":    demand_w4["NDC_Diet"] + demand_w4["SDC_Diet"],
        },
        {
            "Measure": "Total Surplus (all DCs, per SKU)",
            "Regular": (prod_w4["NDC_Regular"] - demand_w4["NDC_Regular"]) + (prod_w4["SDC_Regular"] - demand_w4["SDC_Regular"]),
            "Diet":    (prod_w4["NDC_Diet"] - demand_w4["NDC_Diet"]) + (prod_w4["SDC_Diet"] - demand_w4["SDC_Diet"]),
        },
        {
            "Measure": "Total Safety Stock (all DCs, per SKU)",
            "Regular": ss_w4["NDC_Regular"] + ss_w4["SDC_Regular"],
            "Diet":    ss_w4["NDC_Diet"] + ss_w4["SDC_Diet"],
        },
        {
            "Measure": "Total BTS (all DCs, per SKU)",
            "Regular": bts_w4["NDC_Regular"] + bts_w4["SDC_Regular"],
            "Diet":    bts_w4["NDC_Diet"] + bts_w4["SDC_Diet"],
        }
    ])

    # ------------------ DISPLAY TABLES ------------------
    st.subheader("NDC — Week 4")
    st.table(ndc_df_w4.set_index(["DC","SKU"]))

    st.subheader("SDC — Week 4")
    st.table(sdc_df_w4.set_index(["DC","SKU"]))

    st.subheader("Totals across DCs — Week 4")
    st.table(totals_df_w4.set_index("Measure"))

    # ------------------ CUMULATIVE ------------------
    cumulative_w4_df = pd.DataFrame([
        {
            "DC": "NDC",
            "Reg_BTS": 45000,
            "Diet_BTS": 5000,
            "SS_Reg": 5000,
            "SS_Diet": 5000,
        },
        {
            "DC": "SDC",
            "Reg_BTS": 40000,
            "Diet_BTS": 30000,
            "SS_Reg": 5000,
            "SS_Diet": 5000,
        }
    ])
    st.subheader("Cumulative BTS + SS after Week 4")
    st.table(cumulative_w4_df.set_index("DC"))

    # ------------------ KPI ------------------
    total_production_w4 = sum(prod_w4.values())
    total_demand_w4 = sum(demand_w4.values())
    total_bts_w4 = sum(bts_w4.values())
    total_ss_w4 = sum(ss_w4.values())
    fulfilled_demand_w4 = sum(min(prod_w4[k], demand_w4[k]) for k in demand_w4)
    fill_rate_w4 = round((fulfilled_demand_w4 / total_demand_w4) * 100, 1)
    service_level_w4 = round((len([1 for k in demand_w4 if prod_w4[k] >= demand_w4[k]]) / len(demand_w4)) * 100, 1)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Production", f"{total_production_w4:,}")
    col2.metric("Total Demand", f"{total_demand_w4:,}")
    col3.metric("Total BTS", f"{total_bts_w4:,}")
    col4.metric("Total Safety Stock", f"{total_ss_w4:,}")

    col5, col6 = st.columns(2)
    col5.metric("Fill Rate (%)", f"{fill_rate_w4}%")
    col6.metric("Service Level (%)", f"{service_level_w4}%")

