test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_B in [1, 2, 3]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1, "Try listing out all the possible outcomes first. For example, they could get Rock on the first draw, Hip Hop on the second, and Rock on the third (RHR).")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 2, "There are 8 possible outcomes, and each happens with equal probability of `1/8`. How many outcomes contain 2 Rock slips?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 3, "`R` represents Rock, while `H` represents Hip Hop. There are 8 possible outcomes, and each happens with an equal probability of `1/8`. `P(two Rock in three draws) = P(HRR) + P(RRH) + P(RHR) = (1/8) + (1/8) + (1/8) = 3/8`")
          <IPython.core.display.Markdown object>
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
