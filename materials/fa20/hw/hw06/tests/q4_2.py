test = {
  'name': 'q4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Remember, the sample should be a table. Make sure you are using the correct method to sample from a table.;
          >>> import numpy;
          >>> isinstance(representative_sample, numpy.ndarray)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The sample should be of size 200.;
          >>> representative_sample.num_rows == 200
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your sample should have the same columns as the original table, and ;
          >>> # all data in the sample should be present in the original table.;
          >>> all(np.in1d(representative_sample.column('mag'), earthquakes.column('mag')))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The mean can't be bigger than the biggest magnitude, or smaller than the smallest!;
          >>> representative_mean < max(representative_sample.column('mag')) and representative_mean > min(representative_sample.column('mag')) 
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
