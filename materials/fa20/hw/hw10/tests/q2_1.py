test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you assigned `binary_options` to an array;
          >>> type(binary_options) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Should be a two element array of a binary distribution;
          >>> sorted(set(binary_options)) == sorted(set([0, 1]))
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
