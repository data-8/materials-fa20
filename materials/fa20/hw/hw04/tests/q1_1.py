test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you have all the columns from both tables;
          >>> set(["Name", "Menu_Item", "Yelp", "Google", "Overall", "Cost"]) == set(burritos.labels)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> burritos.num_rows == 212
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
