# Li-ion Cell Data Dashboard

## Overview

This project features:

- **Flask API**: Provides endpoints for accessing and managing cell data, including basic authentication, pagination, filtering, and OpenAPI documentation.
- **Dash Dashboard**: Visualizes cell data with interactive graphs for better insights.
- **Unit Testing**: Includes basic coverage for API endpoints and generates test results.

## Project Structure

- `app.py`: Flask application with REST API functionality, including authentication, pagination, filtering, and OpenAPI documentation.
- `dashboard.py`: Dash application for interactive data visualization.
- `test_app.py`: Unit tests for the Flask API.
- `coverage.txt`: Report on test coverage.

## Installation

1. **Clone the Repository**:

   git clone <repository_url>
   cd <repository_directory>

2. **Create and Activate a Virtual Environment**:
   
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Required Packages**:

   pip install Flask Flask-RESTPlus Flask-HTTPAuth mysql-connector-python requests dash plotly

## Configuration
1. **Database Connection**:

   Open app.py and update the database connection settings to match your MySQL configuration.
   Authentication:

   The default credentials for the API are:
   Username: admin
   Password: password123

## Running the Application
1. **Start the Flask API**:
   python cell_app.py
   - The API will be available at http://localhost:8080.
2. **Start the Dash Dashboard**:
   python dashboard.py
   - The dashboard will be available at http://localhost:8081.

## Dashboard
The Dash dashboard provides visualizations including:

- State of Health (SoH) Pie Chart: Displays the state of health of the selected cell.
- Current vs Time Graph: Line graph showing current over time.
- Voltage vs Time Graph: Line graph showing voltage over time.
- Capacity vs Time Graph: Line graph showing capacity over time.
- Temperature vs Time Graph: Line graph showing temperature over time.

## Running Unit Tests
1. **Run Tests**:

    python -m unittest test_app.py
2. **Generate Test Coverage Report**:

    coverage run -m unittest discover
    coverage report > coverage.txt

## API Documentation
The OpenAPI documentation for the API can be accessed at http://localhost:8080/swagger.json. Use tools like Swagger UI to interact with the documentation.
       

