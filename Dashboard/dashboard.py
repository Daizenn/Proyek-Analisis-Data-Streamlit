import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title("Bike Rental Dashboard")


if __name__ == "__main__":
    main()

# Inside the main function of app.py
 
# Load cleaned data
all_df = pd.read_csv("Dashboard/all_data.csv")

data_musim = all_df.groupby('season_day')['cnt_day'].mean()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']

data = {'Season': season_names, 'Average Rentals': data_musim}
df_season = pd.DataFrame(data)

# Display the bar chart
st.title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
st.bar_chart(df_season.set_index('Season'))

avg_weather = all_df.groupby('weather_label')['cnt_day'].mean().reset_index().sort_values("cnt_day")

# Display the horizontal bar chart with different colors for each category
st.title('Rata - Rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
st.bar_chart(avg_weather.set_index('weather_label'), color=st.color_picker('Choose a color'), use_container_width=True)

st.title("Line Chart Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
st.line_chart(all_df.groupby('mnth_day')['cnt_day'].mean(), color=st.color_picker('Choose a color'))

st.title("Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x="workingday_day", y="cnt_day", data=all_df, palette="magma")
st.pyplot(fig)
