test = {
  'name': 'q2_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ak_mn.num_rows
          44
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ak_mn.column("Murder rate in Alaska").item(0) 
          10.19999981
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ak_mn.column("Murder rate in Minnesota").item(0)
          1.200000048
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
