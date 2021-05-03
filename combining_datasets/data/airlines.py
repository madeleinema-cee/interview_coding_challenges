"""
Load airline datarmation
"""
import asyncio


async def load():
    await asyncio.sleep(0.1)
    return {
        "airlines": [
            {"code": "AK", "name": "Alaskan"},
            {"code": "AA", "name": "American"},
            {"code": "BA", "name": "British"},
            {"code": "DT", "name": "Delta"},
            {"code": "UA", "name": "United"},
            {"code": "VA", "name": "Virgin"},
        ]
    }
