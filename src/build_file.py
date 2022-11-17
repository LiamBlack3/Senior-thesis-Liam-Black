import streamlit as st
import plotly.express as px

# st.title("The Evolution of Basketball!")

# st.write("This tool will allow you to...")
# st.write("Analyze how the game of basketball has changed in the past 25 years...")
# st.write("Find out each teams strength and weaknesses!")
# st.write('\n')
# st.write("Develop a strategy, and...")
# st.write("Attempt to predict game outcomes!")

# -- Create three columns
col1, col2, col3 = st.columns([5, 5, 20])
# -- Put the image in the middle column
# - Commented out here so that the file will run without having the image downloaded
# with col2:
# st.image("streamlit.png", width=200)
# -- Put the title in the last column
with col3:
    st.title("Streamlit NBA Demo")
# -- We use the first column here as a dummy to add a space to the left

# reading given tsv file
with open("nba_data.tsv", 'r') as myfile: 
  with open("nba_data.csv", 'w') as csv_file:
    for line in myfile:
       
      # Replace every tab with comma
      fileContent = re.sub("\t", ",", line)
       
      # Writing into csv file
      csv_file.write(fileContent)

def upload_file():
    uploaded_file = st.file_uploader("Please select your dataset")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
    return df