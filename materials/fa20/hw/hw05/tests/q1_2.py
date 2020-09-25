test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> final_scores.num_columns
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(['Opponent', 'Cal Score', 'Opponent Score']) == set(final_scores.labels)
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
