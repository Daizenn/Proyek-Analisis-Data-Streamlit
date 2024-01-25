import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title("Bike Rental Dashboard")


if __name__ == "__main__":
    main()

# Inside the main function of app.py
    
jam = pd.read_csv("https://github.com/Daizenn/Proyek-Analisis-Data-Streamlit/blob/master/Dashboard/hour.csv")
jam.head()

jam['dteday'] = pd.to_datetime(jam['dteday'])
jam['season'] = jam.season.astype('category')
jam['mnth'] = jam.mnth.astype('category')
jam['holiday'] = jam.holiday.astype('category')
jam['weekday'] = jam.weekday.astype('category')
jam['workingday'] = jam.workingday.astype('category')
jam['weathersit'] = jam.weathersit.astype('category')

hari = pd.read_csv("https://github.com/Daizenn/Proyek-Analisis-Data-Streamlit/blob/master/Dashboard/day.csv")
hari.head()

hari['dteday'] = pd.to_datetime(hari['dteday'])
hari['season'] = hari.season.astype('category')
hari['mnth'] = hari.mnth.astype('category')
hari['holiday'] = hari.holiday.astype('category')
hari['weekday'] = hari.weekday.astype('category')
hari['workingday'] = hari.workingday.astype('category')
hari['weathersit'] = hari.weathersit.astype('category')
    
# Load cleaned data
all_df = jam.merge(hari, on='dteday', how='inner', suffixes=('_hour', '_day'))
all_df.head()

data_musim = all_df.groupby('season_day')['cnt_day'].mean()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']

data = {'Season': season_names, 'Average Rentals': data_musim}
df_season = pd.DataFrame(data)

# Display the bar chart
st.bar_chart(df_season.set_index('Season'))

avg_weather = all_df.groupby('weather_label')['cnt_day'].mean().reset_index().sort_values("cnt_day")

st.title('Rata - Rata Penyewaan Sepeda berdasarkan Kondisi Cuaca')
st.bar_chart(avg_weather.set_index('weather_label'), use_container_width=True)

st.title("Line Chart Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
st.line_chart(all_df.groupby('mnth_day')['cnt_day'].mean())

st.title("Perbedaan Antara Hari Kerja dan Hari Libur dalam Jumlah Sewa Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x="workingday_day", y="cnt_day", data=all_df, palette="magma")
st.pyplot(fig)
