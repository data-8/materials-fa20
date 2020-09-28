test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "After they draw the first Hip Hop slip, they do not put that slip back. How many Hip Hop slips are left? How many total slips are left?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "After they draw the first Hip Hop slip, they do not put that slip back. How many total slips are left?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 4, "To start off, what is the probability of getting Hip Hop on the first draw?")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 3, "After they draw the first Hip Hop slip, there are only 9 Hip Hop slips and 20 total slips left. Thus, `P(Hip Hop on first, Hip Hop on second) = P(Hip Hop on first draw) * P(Hip Hop the second draw|Hip Hop on first draw) = 10/21 * 9/20`.")
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
