from flask import Flask, render_template
import plotly.express as px
import plotly
import json

app = Flask(__name__)

# Dummy threat data
def get_threat_data():
    # Replace with real scraping logic if allowed
    data = {
        "Threat": ["Malware", "Phishing", "Ransomware", "Zero-Day", "Botnet"],
        "Count": [50, 70, 40, 10, 25]
    }
    return data

@app.route("/")
def index():
    data = get_threat_data()
    
    # Create a bar chart directly using Plotly (no pandas needed)
    fig = px.bar(
        x=data["Threat"],
        y=data["Count"],
        color=data["Count"],
        title="Emerging Cyber Threats",
        labels={"x": "Threat Type", "y": "Count"}
    )
    
    # Convert figure to JSON for rendering
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("index.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)
