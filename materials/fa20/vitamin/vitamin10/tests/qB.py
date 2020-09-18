test = {
  'name': 'qB',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your answer is not one of the available choices!!;
          >>> answer_B in [1, 2]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.check_ans(answer_B, 1, "You would need to specify `np.average` in the second argument. By default, the new table produced by `group` will contain a column called `count`, which displays the number of times each grouped value appeared in the original table. `yelp.group('yelp_category')` would produce a table that looks like this: <img src='groups_yelp_data.png' width=200 height=200 />")
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> feedback.correct(answer_B, 2, "Right! By default, the new table produced by `group` will contain a column called `count`, which displays the number of times each grouped value appeared in the original table. `yelp.group('yelp_category')` would produce a table that looks like this: <img src='groups_yelp_data.png' width=200 height=200 />")
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
