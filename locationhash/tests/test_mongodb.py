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

LOCATIONS = [
    (37.58, 23.43),     # Athens, Greece
    (39.55, 116.25),    # Beijing, China
    (-33.55, 18.22),    # Cape Town, South Africa
    (53.20, -6.15),     # Dublin, Ireland
    (24.33, 81.48),     # Key West, Florida
    ]


class MongoDBTests(unittest.TestCase):
    def setUp(self):
        self.connection = Connection()
        self.db = self.connection.test_database

    def tearDown(self):
        self.connection.drop_database(self.db)

    def test_inserting_locations(self):
        locations = self.db.locations
        for l in LOCATIONS:
            locations.insert({'latitude': l[0], 'longitude': l[1]})

        self.assertEqual(len(LOCATIONS), locations.count())
