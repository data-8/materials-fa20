test = {
  'name': 'q1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Did you add Career Length column?;
          >>> nfl.num_columns == 6
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Checking that the first 10 rows are correct;
          >>> nfl.take(np.arange(10))
          Player           | Salary   | Year Drafted | Pick Number | Position | Career Length
          Baker Mayfield   | 570000   | 2018         | 1           | QB       | 2
          Cam Newton       | 16200000 | 2011         | 1           | QB       | 9
          Eli Manning      | 11500000 | 2004         | 1           | QB       | 16
          Eric Fisher      | 10350000 | 2013         | 1           | OT       | 7
          Jadeveon Clowney | 15967200 | 2014         | 1           | DE       | 6
          Jameis Winston   | 20922000 | 2015         | 1           | QB       | 5
          Jared Goff       | 4259683  | 2016         | 1           | QB       | 4
          Kyler Murray     | 495000   | 2019         | 1           | QB       | 1
          Matthew Stafford | 13500000 | 2009         | 1           | QB       | 11
          Myles Garrett    | 3229750  | 2017         | 1           | DE       | 3
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
