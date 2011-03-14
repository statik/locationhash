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

from memo import memoized


class World2dGrid:
    def __init__(self, width=400, height=600):
        self.width = width
        self.height = height
        self.latitude_offset = 90
        self.longitude_offset = 180
        self.width_scale_factor = width / 360
        self.height_scale_factor = height / 180

    def calculate_bucket(self, latitude, longitude):
        latitude = latitude + self.latitude_offset
        longitude = longitude + self.longitude_offset
        return (int(longitude * self.width_scale_factor),
            int(latitude * self.height_scale_factor))


@memoized
def _get_world_grid(horizontal_slices, vertical_slices):
    """Construct a World2dGrid Object of the correct size"""
    return World2dGrid(width=horizontal_slices, height=vertical_slices)


def grid_id(latitude, longitude, horizontal_slices, vertical_slices):
    """Given a location, calculate the grid ID."""
    grid = _get_world_grid(horizontal_slices, vertical_slices)
    return grid.calculate_bucket(latitude, longitude)
