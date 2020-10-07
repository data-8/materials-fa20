test = {
  'name': 'q1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> -1 <= observed_diff_proportion <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The observed difference in proportion should be about 0.219;
          >>> # Remember to use the sample table!;
          >>> np.round(observed_diff_proportion, 3) == 0.219
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
