test = {
  'name': 'q3_10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> test_stat = round(simulate_and_test_statistic(change_in_death_rates, "Death Penalty", "Murder Rate"), 3);
          >>> -5 < test_stat < 5
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
