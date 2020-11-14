test = {
  'name': 'q3_2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from collections import Counter;
          >>> g = train_movies.column('Genre');
          >>> r = np.where(test_movies['Title'] == "godzilla")[0][0];
          >>> t = test_my_features.row(r);
          >>> godzilla_expected_genre = Counter(np.take(g, np.argsort(fast_distances(t, train_my_features))[:15])).most_common(1)[0][0];
          >>> godzilla_genre == godzilla_expected_genre
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
