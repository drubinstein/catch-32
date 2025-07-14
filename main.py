import argparse
import os
import requests

from schema import MtaBusResponse


def is_bus_at_stop(api_key: str, stop: str) -> bool:
    """
    Checks if a Williamsburg-bound B32 bus is at a specific stop.

    Args:
        api_key: Your MTA API key.
        stop: The name of the bus stop to check.

    Returns:
        True if the bus is at the specified stop, False otherwise.
    """

    # The URL for the MTA's SIRI VehicleMonitoring API for the B32 bus.
    url = f"http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={api_key}&LineRef=B32"

    # Fetch the data from the MTA API.
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    data = MtaBusResponse.model_validate(response.json())

    # Iterate through each active bus.
    for delivery in data.Siri.ServiceDelivery.VehicleMonitoringDelivery:
        if delivery.VehicleActivity is not None:
            for bus in delivery.VehicleActivity:
                # check if bus is south bound
                return (
                    bus.MonitoredVehicleJourney.DestinationName
                    == "WILLIAMSBURG BRIDGE PLAZA"
                    and bus.MonitoredVehicleJourney.MonitoredCall.StopPointName == stop
                )
    return False


if __name__ == "__main__":
    # Replace "YOUR_API_KEY" with your actual MTA API key.
    parser = argparse.ArgumentParser(
        description="Check if the B32 bus is at a specific stop."
    )
    parser.add_argument(
        "--stop",
        type=str,
        help="The name of the bus stop to check (default: Long Island City).",
        required=True,
    )
    parser.add_argument(
        "--api_key",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    if is_bus_at_stop(args.api_key, args.stop):
        print("The B32 bus is in LIC and moving.")
