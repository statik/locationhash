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


class locationhashTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_grid_function(self):
        latitude = 64.2145
        longitude = 24.856
        grid_width = 400
        grid_height = 600
        expected_result = "FIXME"
        location_id = grid_id(latitude, longitude, grid_width, grid_height)
        self.assertEqual(location_id, expected_result)
