test = {
  'name': 'q2_2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> _framingham_sim1 = simulate_framingham_null();
          >>> _framingham_sim2 = simulate_framingham_null();
          >>> _framingham_sim1 != _framingham_sim2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> _framingham_sim1 = simulate_framingham_null();
          >>> _framingham_sim2 = simulate_framingham_null();
          >>> _framingham_sim1 < framingham_observed_statistic and _framingham_sim2 < framingham_observed_statistic
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
