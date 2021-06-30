import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Data for our Dashboard
filename = "../data/prepped_superstore.csv"
df = pd.read_csv(filename, index_col="Row ID")


# Prep Data to display
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_profit_ratio = round(total_profit/total_sales, 2)


# Charts to display in the Dashboard 

# GO HERE


# 1 Initialize
app = dash.Dash("__name__")
# For publishing w/ Heroku
#server = app.server

# 2: Layout
app.layout = html.Div([
  # Row 1
    html.Div([  # Top Row start
 
        html.Div([
        html.H2("Superstore Regional Sales Dashboard"),
        html.H4("Sales from 2016-2019 ")
        ], className="eleven columns"), #Titles

        html.Div(html.Img(src="/assets/Superstore Logo.png", className="one columns"))

    ], className="twelve columns"), # Top Row end

    # Row 2
    html.Div([
        # KPI 
        html.Div([
            html.H3("Overall Profit Ratio:", className="twelve columns"),
            html.P(total_profit_ratio, style={"font-size": "60px","text-align": "center"})

        ], className="six columns")

    ]),  # End Row 2


    # Footer Row 
    html.Div([
        # Data Source
        html.H4("2016-2019 Sales Data for (fictional) Superstore, DATAcaded Dashboard course")
    ])

]) #full page div


# 3: Run on server
app.run_server(debug=True)

if __name__ == "__main__":
    app.run_server(debug=True)
