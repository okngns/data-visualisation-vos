import pandas as pd
import plotly.graph_objects as go
data = {
    'Date': list(range(2013, 2023)),
    'Premises_Nett_CO2_emission': [
       5.6, 5.6, 4.8, 4.5, 4.5, 3.9, 4.0, 0.6, 2.8, 1.9
    ],
    'Premises_Based_on_electricity': [
        6.56, 6.75, 7.41, 6.65,  6.71, 5.7, 5.8, 5.6, 5.6, 4.8
    ]
}
df = pd.DataFrame(data)
fig = go.Figure()
fig.add_trace(go.Bar(x=df['Date'], y=df['Premises_Nett_CO2_emission'],
                     marker=dict(color='rgb(240, 132, 0)', line=dict(color='#FFFFFF', width=1)),  # Turuncu ton, beyaz kenar
                     name='Nett CO2 emission after compensation',
                     hovertemplate='<b>Year</b>: %{x}<br><b>Nett CO2 Emission after compensation </b>: %{y}<extra></extra>',
                     ))
fig.add_trace(go.Bar(x=df['Date'], y=df['Premises_Based_on_electricity'],
                     marker=dict(color='rgb(61, 134, 242)', line=dict(color='#FFFFFF', width=1)),  # Mavi ton, beyaz kenar
                     name='Based on electricity',
                     hovertemplate='<b>Year</b>: %{x}<br><b>Based on electricity usage</b>: %{y}<extra></extra>',
                     ))
fig.update_layout(
    xaxis_title='Years',
    yaxis_title='Emission per ton/m²',
    title='CO2 Emission (Premises)',
    title_x=0.5,
    plot_bgcolor='#FFFFFF',  # Grafik arka plan rengi
    paper_bgcolor='#FFFFFF',  # Sayfa arka plan rengi
    font=dict(family='Montserrat medium', size=20, color='#1E1E1E'),  # Font ayarları
    xaxis=dict(tickfont=dict(size=14, color='#1E1E1E'), title_font=dict(family='Montserrat medium', size=20, color='#1E1E1E')),  # X ekseni font ayarları
    yaxis=dict(tickfont=dict(size=14, color='#1E1E1E'), title_font=dict(family='Montserrat medium', size=20, color='#1E1E1E')),  # Y ekseni font ayarları
    yaxis_range=[0, 8],  # Y eksen aralığı
    xaxis_showgrid=True,  # X ekseni ızgaraları
    yaxis_showgrid=True,  # Y ekseni ızgaraları
    xaxis_zeroline=False,
    yaxis_zeroline=False,
    xaxis_gridwidth=1,  # X ekseni ızgara kalınlığı
    yaxis_gridwidth=1,  # Y ekseni ızgara kalınlığı
)
fig.update_traces(
    marker=dict(line=dict(width=1, color='#FFFFFF')),  # Sütun kenarları, oval şekil
    textposition='outside',  # Metinler sütunların dışında görünecek
)
fig.update_traces(
    hoverlabel=dict(bgcolor='black', bordercolor='white', font=dict(color='white')),  # Popup arka planı siyah, içerik beyaz
)
fig.show()
html_content = fig.to_html(full_html=False)
with open("env_Premises_CO2Emission2.html", "w") as file:
    file.write(html_content) 
#fig.write_html('okan.html')
