test = {
  'name': 'q3_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(differences)
          5000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # On average, your test statistic should be close to 0;
          >>> abs(np.average(differences)) < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure all test statistics are different;
          >>> all(differences == differences.item(0)) == False
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
