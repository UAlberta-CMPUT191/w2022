test = {   'name': 'q32',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> # You either didn't add the 'Total Pay ($)' column, or you mislabeled it\n>>> 'Total Compensation 2019 ($)' in compensation.column_labels\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # You have the column in your table, \n'
                                               '>>> # but the values may be wrong\n'
                                               ">>> t = compensation.sort('Total Compensation 2019 ($)', descending = True)\n"
                                               ">>> t.column('Total Compensation 2019 ($)').item(0) == 27482409.0\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
