import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

def play_stp_lottery(): 
    nflips = 1
    while True: 
        if np.random.choice([True, False]): # landed tails
            nflips += 1
        else: 
            return 2**(nflips)

num_trials = st.number_input(label="number of trials ", value=1000) 

payouts = list()
for i in range(num_trials): 
    payouts.append(play_stp_lottery())

st.write(f"""After playing  the lottery {num_trials} times, the average payout is **{round(np.average([p for p in payouts if p > 0]), ndigits=3)}**. The bar graph gives the number of times the each prize was won.""")

prizes = sorted(list(set(payouts)))
fig = px.bar(x=["$"+str(p) for p in prizes], y=[len([1 for p in payouts if p == _p]) for _p in prizes], labels={
                     "x": "prize",
                     "y": "number of times",
                 })
st.plotly_chart(fig, use_container_width=True)

st.button("Rerun")

ntrials = 20
probs = [0.5**n  for n in range(1, ntrials+1)]
payouts = [2**n for n in range(1, ntrials+1)]
exp_payouts = [p*pay for p, pay in zip(probs, payouts)]
utils = [np.log(pay) for pay in payouts]
exp_utils = [p*util for p, util in zip(probs, utils)]

df = pd.DataFrame()
df['Number of Flips'] = list(range(1, ntrials+1))
df['Probability'] = probs
df['Payouts'] = payouts
df['Expected Payouts'] = exp_payouts
df['Utilities'] = utils
df['Expected Utilities'] = exp_utils


# Display an interactive table
st.dataframe(df, width=10000)

#df = pd.DataFrame()
#df['Number of Flips'] = list(range(1, ntrials+1))
#df['Probability'] = probs
#df['Payouts'] = payouts
#df['Expected Payouts'] = exp_payouts
#df['Utilities'] = utils
#df['Expected Utilities'] = exp_utils

#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

#st.line_chart(df)

#df = pd.DataFrame()
#df['Number of Flips'] = list(range(1, ntrials+1))
#df['Probability'] = probs
#df['Payouts'] = payouts
#df['Expected Payouts'] = exp_payouts
#df['Utilities'] = utils
#df['Expected Utilities'] = exp_utils

#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

#st.line_chart(df)
