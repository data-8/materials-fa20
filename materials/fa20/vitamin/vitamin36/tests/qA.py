test = {
  'name': 'qA',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> answer_A in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_A, 1, "Let's reframe the situation. Imagine you were studying for a midterm and trained yourself by taking a practice exam. If you took that exam a second time, you would probably end up with a high score. Is this a good measure how how well you will do on the actual midterm though? Does it make sense to test your knowledge on the same practice exam over and over again? Probably not. Similarly, we need to make sure we are not testing the accuracy of our classifier on the same dataset that we trained it on. This is why we split up the data into a training set and a test set. We do not touch the test set until the very end, when we are trying to figure out how good our classifier really is.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "If we were to evaluate the performance of a classifier using the data on which it was trained, we would end up with overly optimistic results. Instead, we should randomly split our data into a training and a testing set, train the algorithm on the training set, and then evaluate it on the testing set. This will provide us with a more reasonable measure of the classifier's performance.")
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
