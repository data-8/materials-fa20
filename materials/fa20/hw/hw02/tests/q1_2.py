test = {
  'name': 'q1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np;
          >>> # It looks like you didn't make an array.;
          >>> type(book_title_words) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you included commas in the text.;
          >>> # The three pieces of text in the array should be:;
          >>> #   "Eats";
          >>> #   "Shoots";
          >>> #   "and Leaves";
          >>> not any([',' in text for text in book_title_words])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you didn't include both words in the;
          >>> # last piece of text.  It should be the actual string:;
          >>> #   "and Leaves";
          >>> 'and ' in book_title_words.item(2)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(book_title_words)
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> book_title_words.item(0) == 'Eats'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> book_title_words.item(1) == 'Shoots'
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> book_title_words.item(2) == 'and Leaves'
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
