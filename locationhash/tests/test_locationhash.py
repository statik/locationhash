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
from locationhash import grid_id
from locationhash.locationhash import World2dGrid


class locationhashTests(unittest.TestCase):
    def setUp(self):
        self.latitude = 64.2145
        self.longitude = 24.856
        self.grid_width = 400
        self.grid_height = 600
        self.grid = World2dGrid()

    def test_convenience_function(self):
        expected_result = (462, 204)
        location_id = grid_id(self.latitude, self.longitude,
            self.grid_width, self.grid_height)
        self.assertEqual(location_id, expected_result)

    def test_c_squares(self):
        with self.assertRaises(NotImplementedError):
            self.grid.calculate_bucket_csquares(self.latitude, self.longitude)

    def test_geohash(self):
        with self.assertRaises(NotImplementedError):
            self.grid.calculate_bucket_geohash(self.latitude, self.longitude)
