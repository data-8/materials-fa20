test = {
  'name': 'q3_1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure your array only contains the integers that correspond;
          >>> # to the correct options, you don't need to calculate each value;
          >>> sum(nhs_true_statements % 1) == 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> min(nhs_true_statements) >= 1 and max(nhs_true_statements <= 6)
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
