test = {
  'name': 'q1_1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(stemmed_message) == str
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(stemmed_message) < len('elements')
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
