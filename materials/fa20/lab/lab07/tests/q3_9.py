test = {
  'name': 'q3_9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(round(find_test_stat(change_in_death_rates, "Death Penalty", "Murder Rate"),3) - 0.607, 0)
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
