import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

new_data = {
    'Company_name': ['Vos Logistics'] * 10,
    'Table_name': ['environmental impact'] * 10,
    'Super_item': ['CO2 emission ton/km per type'] * 10,
    'Item': ['fleet'] * 10,
    'Date': list(range(2013, 2023)),
    'Item_value_in_thousands_euros': [
        0.039, 0.038, 0.037, 0.036, 0.035, 0.035, 0.036, 0.035, 0.034, 0.032
    ]
}
new_df = pd.DataFrame(new_data)
fig = px.line(new_df, x='Date', y='Item_value_in_thousands_euros',
              title='CO2 Emission per Type Over Years',
              labels={'Date': 'Years', 'Item_value_in_thousands_euros': 'CO2 Emission ton/km per type'},
              template='plotly')
fig.update_layout(
    title='CO2 Emission (Fleet)',
    xaxis_title='Years',
    yaxis_title='CO2 Emission ton/km',
    title_x=0.5,
    plot_bgcolor='#FFFFFF',
    paper_bgcolor='#FFFFFF',
    font=dict(family='Montserrat', size=14, color='#1E1E1E'),
    xaxis=dict(tickfont=dict(size=14, color='#1E1E1E'), title_font=dict(family='Montserrat', size=14, color='#1E1E1E')),
    yaxis=dict(tickfont=dict(size=14, color='#1E1E1E'), title_font=dict(family='Montserrat', size=14, color='#1E1E1E')),
    yaxis_range=[0.03, 0.04],
    xaxis_showgrid=False,
    yaxis_showgrid=False,
    xaxis_zeroline=False,
    yaxis_zeroline=False,
)
fig.update_traces(
    line=dict(color='red', width=1),
    mode='lines+markers',
    marker=dict(color='#1E1E1E', size=8),
    hovertemplate='<b>Year</b>: %{x}<br><b>CO2 Emission ton/km </b>: %{y}<extra></extra>',
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#EBEBEE')
# title and x,y axis fonts
fig.update_layout(
    title_font=dict(family='Montserrat', size=20, color='#1E1E1E'),
    xaxis_title_font=dict(family='Montserrat', size=20, color='#1E1E1E'),
    yaxis_title_font=dict(family='Montserrat', size=20, color='#1E1E1E'),
    hoverlabel=dict(font=dict(family='Montserrat', size=14, color='#FFFFFF')), #popup
)
fig.add_trace(go.Scatter(
    x=new_df['Date'].tolist() + new_df['Date'].tolist()[::-1],
    y=(new_df['Item_value_in_thousands_euros']).tolist() + ([new_df['Item_value_in_thousands_euros'].min()] * len(new_df['Item_value_in_thousands_euros'])),
    fill='tozeroy',
    fillcolor='rgba(255, 0, 0, 0.4)',
    line=dict(color='rgba(255, 255, 255, 0)'),
    name='',
    showlegend=False
))
#html_content = fig.to_html(full_html=False)
#with open("env_Co2EmissionFleet.html", "w") as file:
 #  file.write(html_content)
fig.show() 
