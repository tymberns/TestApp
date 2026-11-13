#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:16:37 2026

@author: tyberns
"""

import time
import streamlit as st

st.title("Long-job test")
minutes = st.number_input("Minutes to wait", min_value=1, max_value=60, value=25)

if st.button("Run test"):
    with st.spinner(f"Waiting {int(minutes)} minutes... keep this tab open"):
        for i in range(int(minutes)):
            time.sleep(60)
            print(f"[heartbeat] minute {i + 1} of {int(minutes)}", flush=True)
    st.success(f"Survived {int(minutes)} minutes!")