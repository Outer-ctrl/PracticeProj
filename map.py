import plotly.express as px
import pandas as pd

# Sample data: each state is assigned a random value (can be customized)
state_data = {
    "state": [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
        "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"
    ],
    "value": [i for i in range(1, 51)]  # Simple numeric values for color scale
}

df = pd.DataFrame(state_data)

# Create choropleth map
fig = px.choropleth(
    df,
    locations="state",
    locationmode="USA-states",
    color="value",
    scope="usa",
    hover_name="state",
    color_continuous_scale="Viridis",
    title="Interactive US Map with State Data"
)

fig.update_layout(
    geo=dict(
        showlakes=True, lakecolor="rgb(255, 255, 255)"
    )
)

fig.show()