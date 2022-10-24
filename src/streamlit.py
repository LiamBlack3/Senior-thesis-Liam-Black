import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import re
import altair as alt

st.title("The Evolution of Basketball!")

st.write("This tool will allow you to...")
st.write("Find out each teams strength and weaknesses!")
st.write('\n')
st.write("Develop a strategy, and...")
st.write("Attempt to predict game outcomes!")

# reading given tsv file
with open("nba_data.tsv", 'r') as myfile: 
  with open("nba_data.csv", 'w') as csv_file:
    for line in myfile:
       
      # Replace every tab with comma
      fileContent = re.sub("\t", ",", line)
       
      # Writing into csv file
      csv_file.write(fileContent)

uploaded_file = st.file_uploader("Please select your dataset")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    st.write("Which team has been the best at scoring in the past decade?")
    # Add some matplotlib code !
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3]

    column = ['3PPG', 'Wins']

    group_labels = ['Pelicans', 'Suns', 'Bucks']

    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.write("What percentage of games does this team win when they score x amount of three pointers?")
    df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.write(c)

    st.write("Based on past game data, how many three pointers do the Spurs need to make to have a good chance of beating the Miami Heat?")

    # fig, ax = plt.subplots()
    # df.hist(
    #     bins=8,
    #     column=["GP","Team"],
    #     grid=False,
    #     figsize=(8, 8),
    #     color="#86bf91",
    #     zorder=2,
    #     rwidth=0.9,
    #     ax=ax,
    #     )
    # st.write(fig)




# @st.cache
# def get_nba_data():
#     thesis_url = "https://docs.google.com/spreadsheets/d/1fN4djo2a-qJv2af2GW2SuR7KpC5-Gu99xVCRJM_M0AA/edit#gid=0"
#     df = pd.read_csv(thesis_url + "/thesis_data.tsv.gz")
#     return df.set_index("Team")

# try:
#     df = get_nba_data()
#     teams = st.multiselect(
#         "Choose teams", list(df.index), ["Suns", "Bulls"]
#     )
#     if not teams:
#         st.error("Please select at least one team.")
#     else:
#         data = df.loc[teams]
#         # data /= 1000000.0
#         st.write("MIN", data.sort_index())

#         data = data.T.reset_index()
#         data = pd.melt(data, id_vars=["index"]).rename(
#             columns={"index": "Team", "value": "MIN"}
#         )
#         chart = (
#             alt.Chart(data)
#             .mark_area(opacity=0.3)
#             .encode(
#                 x="Team",
#                 y=alt.Y("MIN", stack=None),
#                 color="Region:N",
#             )
#         )
#         st.altair_chart(chart, use_container_width=True)
# except urllib.URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )