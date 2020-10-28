test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(answer_A) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.in_array(answer_A, make_array(1),"Statement 1 describes the Law of Averages, which only considers the distribution of 1 random sample. If a population distribution were right-skewed, we would expect the distribution of a large random sample to be right-skewed as well. On the other hand, CLT considers the distribution of sums/means derived from many random samples.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.in_array(answer_A, 2, "Statement 2 is close, but the CLT describes how the distribution of sample sums/means should be roughly normal, regardless of the population distribution. Let's imagine that our pouplation distribution were right-skewed. The CLT states that if we take many large random samples, the distribution of sample sums/means will be approximately normal even though the original population is right-skewed.")
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
