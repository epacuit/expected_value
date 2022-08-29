import streamlit as st
import numpy as np
import plotly.express as px

def expected_value(L): 
    return sum([x*p for x,p in L])

def ev_str(L): 
    latex_str = '$EV(L) = '
    for x,p in L: 
        latex_str += f'{x} * {p} + '
    return latex_str[:-2] + f" = {expected_value(L)}$"

col1, col2 = st.columns(2)
with col1: 
    prize1 = st.number_input(label="prize 1 ", value=100)
with col2:
    p1 = round(st.number_input(label="proability 1 ", min_value=0.0, max_value=1.0, value=0.5), ndigits=2)

col1, col2 = st.columns(2)
with col1: 
    prize2 = st.number_input(label="prize 2 ", value=0) 
with col2:
    p2 = round(st.number_input(label="proability 2 ", min_value=0.0, max_value=1.0, value=0.5), ndigits=2)

if p1 + p2 != 1.0:
    st.error(f"The sum of the probabilities must be 1: {p1} + {p2} = {round(p1 + p2, ndigits=2)}")

else: 
    L = [(prize1, p1), (prize2, p2)]

    st.write(f"""$L=[{prize1}: {p1}, {prize2}: {p2}]$""")
    st.write(ev_str(L))

    num_trials = 1000

    payouts = list()
    for i in range(num_trials): 
        if np.random.choice([True, False], p=[p1, p2]): 
            payouts.append(prize1)
        else: 
            payouts.append(prize2)

    st.write(f"""After playing  the lottery {num_trials} times, the average payout is **{np.average(payouts)}**. The bar graph gives the number of times the each prize was won.""")
    fig = px.bar(x=["$"+str(prize1),  "$"+str(prize2)], y=[len([1 for p in payouts if p == prize1]), len([1 for p in payouts if p == prize2])], labels={
                     "x": "prize",
                     "y": "number of times",
                 })
    st.plotly_chart(fig, use_container_width=True)

