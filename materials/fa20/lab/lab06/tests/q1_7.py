test = {
  'name': 'q1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(model_proportions) % 2 == 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(np.unique(model_proportions)) == 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(model_proportions) == 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(simulation_proportion_correct) == float
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= one_statistic <= 25
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
