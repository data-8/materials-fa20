test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Assign answer_B to 1, 2, 3, or 4.;
          >>> answer_B in [1, 2, 3, 4]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1, "We know that the distribution is roughly normal and hence we know that 95% of the area under the normal curve (AKA 95% of the data) is contained within 2 SDs from the mean. How can we use this information to calculate a range of values? ")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 2, "We know that the distribution is roughly normal and hence we know that 95% of the area under the normal curve (AKA 95% of the data) is contained within 2 SDs from the mean. How can we use this information to calculate a range of values? ")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 4, "We know that the distribution is roughly normal and hence we know that 95% of the area under the normal curve (AKA 95% of the data) is contained within 2 SDs from the mean. How can we use this information to calculate a range of values? ")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 3, "We know that the distribution is roughly normal and hence we know that 95% of the area under the normal curve (AKA 95% of the data) is contained within 2 SDs from the mean. So our range will be (883 - 2 $*$ 270, 883 + 2 $*$ 270) = (343, 1423).")
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
