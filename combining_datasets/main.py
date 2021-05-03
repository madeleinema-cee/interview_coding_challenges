"""
Main module -- implement core logic here.
"""
import asyncio
import pprint

from data.airlines import load as airline_data
from data.profiles import load as profile_data
from data.trip import load as trip_data


class TravelerFlightInfo:
    """Contains all the functions to retrieve
     and merge data in a designated format

     Attributes:
         loop (asyncio.get_event_loop): asyncio event loop
         airlines (arr): an array of airlines info
         profiles (arr): an array of profiles info
         flights (arr): an array of flights info
         travelers_flight_data (dict): a dict of travelers and flights summary data
    """

    def __init__(self):
        self.loop = None
        self.airlines = None
        self.profiles = None
        self.flights = None
        self.travelers_flight_data = {
            'travelers': []
        }

    def main(self):
        """Platform for sequentially calling class methods

        Returns:
            self.travelers_flight_data (dict): a dict of travelers and flights summary data
        """
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.get_traveler_flight_info())
        self.parse_airlines()
        traveler_data = self.parse_profiles()
        self.travelers_flight_data['travelers'] = traveler_data

        return self.travelers_flight_data

    async def get_traveler_flight_info(self):
        """Retrieve airlines, profiles, and flights data to be preserved"""
        airline_task = self.loop.create_task(airline_data())
        profile_task = self.loop.create_task(profile_data())
        trip_task = self.loop.create_task(trip_data())
        await asyncio.wait([profile_task, airline_task, trip_task])

        self.airlines = airline_task.result()['airlines']
        self.profiles = profile_task.result()['profiles']
        self.flights = trip_task.result()['trip']['flights']

    def parse_airlines(self):
        """Parse airlines data and merge with flights data"""
        for airline in self.airlines:
            for flight in self.flights:
                for leg in flight['legs']:
                    if airline['code'] == leg['airlineCode']:
                        leg['airlineName'] = airline['name']

    def parse_profiles(self):
        """Parse profiles data and create an array of merged traveler flights summary data

        Returns:
            merged travelers data
        """
        travelers = []
        for profile in self.profiles:
            traveler_data = {
                'id': profile['personId'],
                'name': profile['name'],
                'frequentFlyerNumber': profile['rewardPrograms']['air']
            }

            traveler_data['flights'] = self.parse_flights(traveler_data)
            travelers.append(traveler_data)

            del traveler_data['frequentFlyerNumber']

        return travelers

    def parse_flights(self, traveler_data):
        """Parse flights data and merge with travelers data

        Arguments:
            traveler_data (dict): a dict of merged traveler summary data

        Returns:
            leg data for each flight
        """
        leg_data = []
        for flight in self.flights:
            if traveler_data['id'] in flight['travelerIds']:
                legs = {'legs': []}
                for leg in flight['legs']:
                    flight_leg = leg.copy()
                    airline_code = leg['airlineCode']
                    if airline_code in traveler_data['frequentFlyerNumber'].keys():
                        flight_leg['frequentFlyerNumber'] = traveler_data['frequentFlyerNumber'][airline_code]
                    else:
                        flight_leg['frequentFlyerNumber'] = ''
                    legs['legs'].append(flight_leg)

                leg_data.append(legs)
        return leg_data


if __name__ == "__main__":
    print("Traveler flight data: ")
    t = TravelerFlightInfo()
    result = t.main()
    pprint.pprint(result)
