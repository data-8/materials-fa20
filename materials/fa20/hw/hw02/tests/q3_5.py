test = {
  'name': 'q3_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(round(sum(celsius_temperature_ranges)), 768487)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(celsius_temperature_ranges)
          65000
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
