# encoding: utf-8
"""
Copyright 2011 Elliot Murphy

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import unittest2 as unittest
from pymongo import Connection
from locationhash import grid_id
from locationhash.tests.data import LOCATIONS


class MongoDBTests(unittest.TestCase):
    def setUp(self):
        self.connection = Connection()
        self.db = self.connection.test_database

    def tearDown(self):
        self.connection.drop_database(self.db)

    def test_inserting_locations(self):
        locations = self.db.locations
        for l in LOCATIONS:
            location_hash = grid_id(l[0], l[1], 400, 600)
            locations.insert({
                'latitude': l[0],
                'longitude': l[1],
                'hash': location_hash})

        self.assertEqual(len(LOCATIONS), locations.count())
        expected_latitude = 37.58
        spot = locations.find_one({"hash": (382, 203)})
        self.assertEqual(expected_latitude, spot["latitude"])
