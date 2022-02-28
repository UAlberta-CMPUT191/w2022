test = {   'name': 'q5_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you have all the columns from both tables\n'
                                               '>>> set(["Name", "Menu_Item", "Yelp", \'Google\', "Overall", "Cost"]) == set(burritos.labels)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> burritos.num_rows == 212\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> len(np.unique(burritos.group('Name').column(1)))\n10", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
