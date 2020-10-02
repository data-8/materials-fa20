test = {
  'name': 'q2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to have your function return something.;
          >>> simulate_key_strike() is not None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import string;
          >>> all([simulate_key_strike() in list(string.ascii_lowercase + string.ascii_uppercase + string.digits + " ") for i in range(100)])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't use all the letters or numbers of the alphabet, or you;
          >>> # used too many.;
          >>> import numpy as np;
          >>> np.random.seed(22);
          >>> 63 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 45
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
