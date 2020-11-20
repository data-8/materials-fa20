test = {
  'name': 'q1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sorted_coordinates = coordinates.sort("school");
          >>> classify(sorted_coordinates.row(29), 3, train) == three_classify(sorted_coordinates.row(29))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You should expect to see really high accuracy;
          >>> 0.90 <= accuracy <= 1
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
