test = {
  'name': 'q3_1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(my_features) >= 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all([f in test_movies.labels for f in my_features])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like there are many movies in the training set that;
          >>> # don't have any of your chosen words.  That will make your;
          >>> # classifier perform very poorly in some cases.  Try choosing;
          >>> # at least 1 common word.;
          >>> train_f = train_movies.select(my_features);
          >>> np.count_nonzero(train_f.apply(lambda r: np.sum(np.abs(np.array(list(r)))) == 0)) < len(my_features)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like there are many movies in the test set that;
          >>> # don't have any of your chosen words.  That will make your;
          >>> # classifier perform very poorly in some cases.  Try choosing;
          >>> # at least 1 common word.;
          >>> test_f = test_movies.select(my_features);
          >>> np.count_nonzero(test_f.apply(lambda r: np.sum(np.abs(np.array(list(r)))) == 0)) < 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you may have duplicate words! Make sure not to!;
          >>> len(set(my_features)) >= 10
          True
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
