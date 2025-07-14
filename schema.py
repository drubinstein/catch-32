from datetime import datetime

from pydantic import BaseModel, Field

# Define the innermost models first


class VehicleLocation(BaseModel):
    """
    Represents the geographical location of a vehicle.
    """

    Latitude: float
    Longitude: float


class Capacities(BaseModel):
    """
    Represents passenger capacity information.
    """

    EstimatedPassengerCapacity: int
    EstimatedPassengerCount: int
    EstimatedPassengerLoadFactor: str


class Distances(BaseModel):
    """
    Represents distance information related to a vehicle's call.
    """

    CallDistanceAlongRoute: float
    DistanceFromCall: float
    PresentableDistance: str
    StopsFromCall: int


class VehicleFeatures(BaseModel):
    """
    Represents features of the vehicle.
    """

    StrollerVehicle: bool


class Extensions(BaseModel):
    """
    Extensions containing additional vehicle information.
    """

    Capacities: Capacities
    Distances: Distances
    VehicleFeatures: VehicleFeatures


class MonitoredCall(BaseModel):
    """
    Represents details about a vehicle's current or next scheduled call.
    """

    AimedArrivalTime: datetime
    AimedDepartureTime: datetime
    ExpectedArrivalTime: datetime
    ExpectedDepartureTime: datetime
    Extensions: Extensions
    StopPointName: str
    StopPointRef: str
    VisitNumber: int


class FramedVehicleJourneyRef(BaseModel):
    """
    Reference to a framed vehicle journey.
    """

    DataFrameRef: str
    DatedVehicleJourneyRef: str


class MonitoredVehicleJourney(BaseModel):
    """
    Represents a monitored vehicle journey.
    """

    Bearing: float
    BlockRef: str
    DestinationName: str
    DirectionRef: str
    FramedVehicleJourneyRef: FramedVehicleJourneyRef
    JourneyPatternRef: str
    LineRef: str
    Monitored: bool
    MonitoredCall: MonitoredCall
    Occupancy: str
    OnwardCalls: dict  # This is an empty dictionary in the reference schema, so dict is appropriate
    OperatorRef: str
    OriginRef: str
    ProgressRate: str
    PublishedLineName: str
    VehicleLocation: VehicleLocation
    VehicleRef: str


class VehicleActivity(BaseModel):
    """
    Represents a single vehicle's activity.
    """

    MonitoredVehicleJourney: MonitoredVehicleJourney
    RecordedAtTime: datetime


class VehicleMonitoringDelivery(BaseModel):
    """
    Represents a delivery of vehicle monitoring information.
    """

    ResponseTimestamp: datetime
    ValidUntil: datetime
    VehicleActivity: list["VehicleActivity"] | None = None


class ServiceDelivery(BaseModel):
    """
    Represents the service delivery information.
    """

    ResponseTimestamp: datetime
    VehicleMonitoringDelivery: list["VehicleMonitoringDelivery"]


class Siri(BaseModel):
    """
    The root model for the Siri data structure.
    """

    ServiceDelivery: ServiceDelivery


class MtaBusResponse(BaseModel):
    """
    Represents the root of the Siri data structure.
    """

    Siri: Siri


# Example Usage (optional, for testing the model)
if __name__ == "__main__":
    data = {
        "Siri": {
            "ServiceDelivery": {
                "ResponseTimestamp": "2025-07-12T11:34:33.366-04:00",
                "VehicleMonitoringDelivery": [
                    {
                        "ResponseTimestamp": "2025-07-12T11:34:33.366-04:00",
                        "ValidUntil": "2025-07-12T11:35:33.366-04:00",
                        "VehicleActivity": [
                            {
                                "MonitoredVehicleJourney": {
                                    "Bearing": 185.48943,
                                    "BlockRef": "MTA "
                                    "NYCT_GA_C5-Saturday_A_GA_24300_B32-102",
                                    "DestinationName": "WILLIAMSBURG BRIDGE PLAZA",
                                    "DirectionRef": "1",
                                    "FramedVehicleJourneyRef": {
                                        "DataFrameRef": "2025-07-12",
                                        "DatedVehicleJourneyRef": "MTA "
                                        "NYCT_GA_C5-Saturday-069000_B32_102",
                                    },
                                    "JourneyPatternRef": "MTA_B320048",
                                    "LineRef": "MTA NYCT_B32",
                                    "Monitored": True,
                                    "MonitoredCall": {
                                        "AimedArrivalTime": "2025-07-12T11:38:22.000-04:00",
                                        "AimedDepartureTime": "2025-07-12T11:38:22.000-04:00",
                                        "ExpectedArrivalTime": "2025-07-12T11:34:38.401-04:00",
                                        "ExpectedDepartureTime": "2025-07-12T11:34:38.401-04:00",
                                        "Extensions": {
                                            "Capacities": {
                                                "EstimatedPassengerCapacity": 80,
                                                "EstimatedPassengerCount": 10,
                                                "EstimatedPassengerLoadFactor": "manySeatsAvailable",
                                            },
                                            "Distances": {
                                                "CallDistanceAlongRoute": 2209.67,
                                                "DistanceFromCall": 91.37,
                                                "PresentableDistance": "approaching",
                                                "StopsFromCall": 0,
                                            },
                                            "VehicleFeatures": {
                                                "StrollerVehicle": False
                                            },
                                        },
                                        "StopPointName": "FRANKLIN ST/GREEN ST",
                                        "StopPointRef": "MTA_308730",
                                        "VisitNumber": 1,
                                    },
                                    "Occupancy": "seatsAvailable",
                                    "OnwardCalls": {},
                                    "OperatorRef": "MTA NYCT",
                                    "OriginRef": "MTA_505252",
                                    "ProgressRate": "normalProgress",
                                    "PublishedLineName": "B32",
                                    "VehicleLocation": {
                                        "Latitude": 40.73414,
                                        "Longitude": -73.958003,
                                    },
                                    "VehicleRef": "MTA NYCT_5007",
                                },
                                "RecordedAtTime": "2025-07-12T11:34:17.668-04:00",
                            },
                            {
                                "MonitoredVehicleJourney": {
                                    "Bearing": 43.472473,
                                    "BlockRef": "MTA "
                                    "NYCT_GA_C5-Saturday_A_GA_33300_B32-101",
                                    "DestinationName": "LONG ISLAND CITY 44DR - 21 ST",
                                    "DirectionRef": "0",
                                    "FramedVehicleJourneyRef": {
                                        "DataFrameRef": "2025-07-12",
                                        "DatedVehicleJourneyRef": "MTA "
                                        "NYCT_GA_C5-Saturday-069000_B32_101",
                                    },
                                    "JourneyPatternRef": "MTA_B320047",
                                    "LineRef": "MTA NYCT_B32",
                                    "Monitored": True,
                                    "MonitoredCall": {
                                        "AimedArrivalTime": "2025-07-12T11:37:00.000-04:00",
                                        "AimedDepartureTime": "2025-07-12T11:37:00.000-04:00",
                                        "ExpectedArrivalTime": "2025-07-12T11:35:00.008-04:00",
                                        "ExpectedDepartureTime": "2025-07-12T11:35:00.008-04:00",
                                        "Extensions": {
                                            "Capacities": {
                                                "EstimatedPassengerCapacity": 80,
                                                "EstimatedPassengerCount": 3,
                                                "EstimatedPassengerLoadFactor": "manySeatsAvailable",
                                            },
                                            "Distances": {
                                                "CallDistanceAlongRoute": 1552.74,
                                                "DistanceFromCall": 172.84,
                                                "PresentableDistance": "< 1 stop away",
                                                "StopsFromCall": 0,
                                            },
                                            "VehicleFeatures": {
                                                "StrollerVehicle": False
                                            },
                                        },
                                        "StopPointName": "KENT AV/METROPOLITAN AV",
                                        "StopPointRef": "MTA_308666",
                                        "VisitNumber": 1,
                                    },
                                    "Occupancy": "seatsAvailable",
                                    "OnwardCalls": {},
                                    "OperatorRef": "MTA NYCT",
                                    "OriginRef": "MTA_302294",
                                    "ProgressRate": "normalProgress",
                                    "PublishedLineName": "B32",
                                    "VehicleLocation": {
                                        "Latitude": 40.716529,
                                        "Longitude": -73.965758,
                                    },
                                    "VehicleRef": "MTA NYCT_9536",
                                },
                                "RecordedAtTime": "2025-07-12T11:34:10.659-04:00",
                            },
                        ],
                    }
                ],
            }
        }
    }

    try:
        siri_data = MtaBusResponse.model_validate(data)
        print("Pydantic model created successfully!")
        # You can access data like this:
        # print(siri_data.ServiceDelivery.VehicleMonitoringDelivery[0].VehicleActivity[0].MonitoredVehicleJourney.VehicleLocation.Latitude)
        # print(siri_data.ServiceDelivery.ResponseTimestamp)
    except Exception as e:
        print(f"Error creating Pydantic model: {e}")
