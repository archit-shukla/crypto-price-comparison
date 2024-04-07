# Cryptocurrency Price Comparison Tool

This project is a Python script that compares the prices of Bitcoin (BTC) and Ethereum (ETH) over a specified time period. It utilizes data sorted by date and generates line graphs using Plotly library to visualize the price trends.

## Features

- Fetches historical price data for Bitcoin and Ethereum from a data source.
- Allows users to enter start and end dates to compare prices within that period.
- Generates interactive line graphs using Plotly to compare price trends.
- Hosts a webpage on a local server for easy access and visualization.

## Requirements

- Python 3.x
- Plotly library (`pip install plotly`)
- Flask library (`pip install flask`)

## Getting Started

1. Clone the repository to your local machine.
2. Install the required Python libraries using pip: `pip install plotly flask`
3. Run the Python script to fetch and process cryptocurrency price data.
4. Start the local server to access the comparison tool webpage.
5. Enter the start and end dates to view the price comparison graphs.

## Project Structure

- `data`: Contains historical price data files for Bitcoin and Ethereum.
- `main`: Handles the backend calls.
- `index`: HTML templates for the webpage.
- `front_end`: Static files (CSS, JavaScript) for the webpage.
- `app.py`: Python script for fetching and processing price data.

## Usage

1. Run the `main.py` script to start the Flask server.
2. Open a web browser and navigate to `http://localhost:5000` to access the comparison tool.
3. Enter the start and end dates in the provided form to generate price comparison graphs.



