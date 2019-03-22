from datasources import tests

from Sentinel1 import Sentinel1

class Sentinel1TestCases(tests.BaseTestCases):

    def _setUp(self):
        self.spatial_mode = 'extent'
        self.datasource = Sentinel1
        self.spatial = {
                        "type": "Polygon",
                        "coordinates": [
                          [
                            [
                              -101.28433227539062,
                              46.813218976041945
                            ],
                            [
                              -100.89431762695312,
                              46.813218976041945
                            ],
                            [
                              -100.89431762695312,
                              47.06450941441436
                            ],
                            [
                              -101.28433227539062,
                              47.06450941441436
                            ],
                            [
                              -101.28433227539062,
                              46.813218976041945
                            ]
                          ]
                        ]
                      }
        self.temporal = ("2017-01-01", "2017-12-31")
        self.properties = {'sar:instrument_mode': {'eq': 'IW'}}
        self.limit = 10
