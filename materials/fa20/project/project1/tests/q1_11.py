test = {
  'name': 'q1_11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Incorrect labels for columns;
          >>> t = stats_for_year(1990);
          >>> t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Incorrect number of rows;
          >>> t = stats_for_year(1990);
          >>> t.num_rows
          50
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(stats_for_year(1960).sort('geo').take(np.arange(5, 50, 5)))
          geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
          can  | 17847404         | 3.88                               | 32.6
          dza  | 11057864         | 7.52                               | 242.54
          gbr  | 52370595         | 2.69                               | 26.56
          irq  | 7289753          | 6.25                               | 191.93
          mar  | 12328532         | 7.04                               | 237.06
          nga  | 45138460         | 6.35                               | 339.85
          pol  | 29614201         | 3.11                               | 65.03
          tur  | 27472339         | 6.37                               | 258.29
          uzb  | 8526299          | 6.26                               | 169.4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> print(stats_for_year(2010).sort('geo').take(np.arange(3, 50, 5)))
          geo  | population_total | children_per_woman_total_fertility | child_mortality_under_5_per_1000_born
          bgd  | 147575433        | 2.28                               | 49.1
          col  | 45222699         | 2.01                               | 18.47
          eth  | 87639962         | 4.92                               | 82.94
          ind  | 1234281163       | 2.6                                | 58.23
          ken  | 42030684         | 4.37                               | 56.54
          moz  | 23531567         | 5.56                               | 104.53
          per  | 29027680         | 2.55                               | 20.13
          sdn  | 34545014         | 4.88                               | 75.92
          ukr  | 45792086         | 1.45                               | 11.72
          yem  | 23154854         | 4.67                               | 55.96
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
