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
          >>> feedback.check_ans(answer_A, 1, "Double-check @2122 on Piazza to see what you can and cannot use during the exam. Collaborating with other students during the exam is NOT allowed.")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_A, 2, "Correct! You are allowed to use past worksheets, piazza posts, and the textbook, but you CANNOT share your solutions or work with other students on the test. If you share your work during the exam, your exam will not be graded and you will receive a 0 on the midterm.")
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
