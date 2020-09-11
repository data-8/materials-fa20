test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> unemployment.select('Date', 'NEI', 'NEI-PTER').take(0)
          Date       | NEI     | NEI-PTER
          1994-01-01 | 10.0974 | 11.172
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
