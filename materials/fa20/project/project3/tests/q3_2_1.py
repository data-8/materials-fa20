test = {
  'name': 'q3_2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # This test just checks to see if your classify function works correctly ;
          >>> # with k=5 nearest neighbors.;
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_my_features.row(r)
          ...     return classify(t, train_my_features, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])).most_common(1)[0][0];
          >>> check_5_nn = [check(i, 5) for i in np.arange(11)];
          >>> all(check_5_nn)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # This test just checks to see if your classify function works correctly ;
          >>> # with k=11 nearest neighbors.;
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> def check(r, k):
          ...     t = test_my_features.row(r)
          ...     return classify(t, train_my_features, g, k) == Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:k])).most_common(1)[0][0];
          >>> check_11_nn = [check(i, 11) for i in np.arange(11)];
          >>> all(check_11_nn)
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
