"""
Load trip datarmation.
"""
import asyncio


async def load():
    await asyncio.sleep(0.1)
    return {
        "trip": {
            "flights": [
                {
                    "travelerIds": [1, 2, 3],
                    "legs": [{"airlineCode": "AA", "flightNumber": "AA456"}],
                },
                {
                    "travelerIds": [1, 2],
                    "legs": [
                        {"airlineCode": "VA", "flightNumber": "VA789"},
                        {"airlineCode": "AK", "flightNumber": "AK789"},
                    ],
                },
            ]
        }
    }
