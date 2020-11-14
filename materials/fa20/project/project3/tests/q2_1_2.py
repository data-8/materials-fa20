test = {
  'name': 'q2_1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you can use any two movies;
          >>> correct_dis = 0.000541242;
          >>> dis = distance_two_features("clerks.", "the avengers", "water", "feel");
          >>> np.isclose(np.round(dis, 9), correct_dis)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you can use any two features;
          >>> correct_dis = 0.006486728;
          >>> dis = distance_two_features("clerks.", "the avengers", "your", "that");
          >>> np.isclose(np.round(dis, 9), correct_dis)
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
