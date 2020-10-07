test = {
  'name': 'q1_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure to define model_proportions;
          >>> import numpy as np;
          >>> isinstance(model_proportions, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like your simulation isn't random.;
          >>> np.std([simulate_visited_area_codes() for _ in range(1000)]) > 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The sum of the items in model proportions should be 1;
          >>> model_proportions.item(0) + model_proportions.item(1)
          1.0
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
