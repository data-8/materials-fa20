test = {
  'name': 'q3_1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure that blank1_1, blank2_1, and blank3_1 are set to one of the following options: "greater than", "less than" or "equal to";
          >>> check_options = [1 if i in ['greater than', 'less than', 'equal to'] else 0 for i in [blank1_1, blank2_1, blank3_1]];
          >>> sum(check_options) == 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure that blank1_2, blank2_2, and blank3_2 are set to one of the following options: "higher", "lower", "equal";
          >>> check_options = [1 if i in ["higher", "lower", "equal"] else 0 for i in [blank1_2, blank2_2, blank3_2]];
          >>> sum(check_options) == 3
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
