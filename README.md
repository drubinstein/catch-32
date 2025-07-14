# Catch-32 - A B32 Bus Tracker

A Python application that determines if the B32 bus is currently at a stop using the MTA's SIRI Vehicle Monitoring API. 

Why? Because the B32 often disappears or doesn't show up at its schedule times. The best way to know if the B32 is on its way is to check if it's started moving.

Eventually, I will integrate this script with various notification systems. Those notification systems will probably not be merged, but if a developer wants to write the scaffolding for Twilio, WhatsApp, Google Meet, etc., I'll take your PRs.

## Features

- Check if a southbound B32 bus (heading to Williamsburg Bridge Plaza) is at any specified stop
- Pydantic-based data validation for reliable API response parsing
- Command-line interface for easy usage

## Prerequisites

- Python 3.13+
- MTA API key (get one from [MTA Developer Resources](https://api.mta.info/))
- (optional) [uv](https://docs.astral.sh/uv/) package manager

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd b32ed
```

2. Install dependencies using uv:
```bash
uv sync
```

## Usage

### Command Line Interface

Run the application with your MTA API key and the bus stop name:

```bash
uv run main.py --stop "STOP_NAME" --api_key "YOUR_MTA_API_KEY"
```

### Example

```bash
uv run main.py --stop "21 ST/45 RD" --api_key "your-api-key-here"
```

If a B32 bus heading to Williamsburg Bridge Plaza is currently at the specified stop, the program will output:
```
The B32 bus is in LIC and moving.
```


### Running with Development Dependencies

```bash
uv sync --group dev
```

### Code Formatting

```bash
uv run ruff format .
uv run ruff check .
```

## MTA API Information

This application uses the MTA's SIRI Vehicle Monitoring API:
- Endpoint: `http://bustime.mta.info/api/siri/vehicle-monitoring.json`
- Documentation: [MTA Developer Resources](https://api.mta.info/)
- Requires a free API key
