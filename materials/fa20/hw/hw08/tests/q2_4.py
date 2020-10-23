test = {
  'name': 'q2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 1 <= restaurants_tied <= 3
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Remember, we are using a 95% confidence interval of [1.2, 11.2]. Our null hypothesis claims that Imm Thai's lead is 0.;
          >>> # This falls outside of our 95% confidence interval. What can we conclude if we use a 5% p-value cutoff? ;
          >>> restaurants_tied == 3
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # We are using a 95% confidence interval of [1.2, 11.2]. Our null hypothesis claims that Imm Thai's lead is 0. This falls outside of our 95% confidence interval. ;
          >>> # 100% - 95% = 5%, which is our p-value cutoff. At the 5% level of significance, 0 doesn't seem like a plausible value for Imm Thai's lead. We would reject the null.;
          >>> # Remember, there is a duality between confidence intervals and tests: if you are testing whether or not the true lead is a particular value x, and you use the 5% cutoff for the P-value, then you will reject the null hypothesis if x is not in your 95% confidence interval for the lead.;
          >>> restaurants_tied == 2
          False
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
