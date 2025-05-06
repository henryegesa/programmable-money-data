#!/usr/bin/env python3
"""
generate_payment_sim_data.py
Creates input and output CSV files for the programmable‑money corridor simulation.
"""

import pandas as pd
from pathlib import Path

# ---------- 1. Define input parameters ----------
corridors = ["US‑EU", "US‑MX", "EU‑IN", "IN‑SG", "AU‑CN"]

input_df = pd.DataFrame({
    "corridor": corridors,
    "processing_cost_legacy_cents": [7.5]*5,
    "processing_cost_programmable_cents": [3.2]*5,
    "liquidity_buffer_legacy_pct": [1.8]*5,
    "liquidity_buffer_programmable_pct": [0.6]*5,
    "compliance_opex_legacy_bps": [7]*5,
    "compliance_opex_programmable_bps": [2]*5,
    "avg_ticket_wholesale_usd": [8400]*5,
    "avg_ticket_retail_usd": [420]*5,
    "daily_transactions": [1_000_000/5]*5,      # split 1 M tx/day evenly
    "buffer_recalc_seconds_legacy": [23*3600]*5,  # 23 h
    "buffer_recalc_seconds_programmable": [15]*5
})

# ---------- 2. Define headline output metrics ----------
output_df = pd.DataFrame({
    "corridor": corridors,
    "processing_cost_reduction_pct": [57]*5,
    "working_capital_release_bp": [120]*5,
    "false_positive_reduction_pct": [67]*5,
})

# ---------- 3. Write to CSV ----------
out_dir = Path(__file__).resolve().parent
input_path = out_dir / "payment_sim_inputs.csv"
output_path = out_dir / "payment_sim_outputs.csv"

input_df.to_csv(input_path, index=False)
output_df.to_csv(output_path, index=False)

print(f"✔ CSV files created:\n  {input_path}\n  {output_path}")
