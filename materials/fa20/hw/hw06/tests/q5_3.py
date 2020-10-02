test = {
  'name': 'q5_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The statistic should be between 0 and 13 face cards for;
          >>> # a sample size of 13;
          >>> num_face = deck_simulation_and_statistic(13, deck_model_probabilities);
          >>> 0 <= num_face <= 13
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
