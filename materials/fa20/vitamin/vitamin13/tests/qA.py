test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1,2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 2, "The array collects the result of each trial. We must initialize it in the beginning so that we can use it inside of the for loop and constantly append to it. If we were to create it inside of the for loop, an empty `simulated_sums` array would be created during every iteration. The end result of this will be an array with the result of just one trial. <br> Let's reframe this question. Collecting the results of 100 trials is like picking 100 apples. We need something to store our apples in, so we must first find some sort of container (this is the empty array outside of the for loop). Afterward, we will repeat the same process of picking an apple and putting it in the **same** container (this happens inside of the for loop).")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 1, "Right! If we were to create the array inside of the for loop, our final `simulated_sums` array would only contain the result of 1 trial. This is because we re-intialize it at the start of every iteration of the for loop.")
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
