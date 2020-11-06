test = {
  'name': 'q1_15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(minimized_parameters) == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure to input `smooth=True` as the second argument to the `minimize` function;
          >>> # i.e. minimize(..., smooth=True);
          >>> (1 <= minimized_parameters.item(0) <= 2) and (-7 <= minimized_parameters.item(1) <= -6)
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
