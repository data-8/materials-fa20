test = {
  'name': 'q1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you subtracted in the wrong order.;
          >>> round(pter.item(6), 4) != -1.1282
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(pter.item(6), 4)
          1.1282
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
