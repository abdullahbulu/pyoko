# -*-  coding: utf-8 -*-
"""
data models for tests
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
import datetime


data = {'auth_info': {'email': 'suuper@suup.com',
                      'password': '123',
                      'username': 'foo_user'},
        'lectures': [{'attendance': [{'attended': False,
                                      'date': datetime.date(2015, 5, 9),
                                      'hour': 2},
                                     {'attended': True,
                                      'date': datetime.date(2015, 5, 10),
                                      'hour': 4}],
                      'exams': [{'date': datetime.date(2015, 5, 11),
                                 'point': 65,
                                 'type': 'Q'}],
                      'node_in_list_node': {'foo': 'FOOOO'},
                      'code': 'math101',
                      'credit': 4,
                      'name': 'Introduction to Math'},
                     {'attendance': [{'attended': False,
                                      'date': datetime.date(2015, 5, 13),
                                      'hour': 2},
                                     {'attended': True,
                                      'date': datetime.date(2015, 5, 14),
                                      'hour': 4}],
                      'exams': [{'date': datetime.date(2015, 5, 15),
                                 'point': 65,
                                 'type': 'Q'}],
                      'node_in_list_node': {'foo': 'FOOOO'},
                      'code': 'rock101',
                      'credit': 10,
                      'name': 'Introduction to Rocking'}],
        'bio': "Lorem impsum dolar sit amet falan filan",
        'join_date': datetime.date(2015, 5, 16),
        'name': 'Jack',
        'archived': False,
        '_deleted': False,
        'number': '20300344',
        'timestamp': None,
        'pno': '2343243433',
        'surname': 'Black'}

clean_data = {'_deleted': False,
 'archived': False,
 'auth_info': {'email': 'suuper@suup.com',
  'password': '123',
  'username': 'foo_user'},
 'bio': 'Lorem impsum dolar sit amet falan filan',
 'join_date': '2015-05-16T00:00:00Z',
 'lectures': [{'attendance': [{'attended': False,
     'date': '2015-05-09T00:00:00Z',
     'hour': 2},
    {'attended': True, 'date': '2015-05-10T00:00:00Z', 'hour': 4}],
   'code': 'math101',
   'credit': 4,
   'exams': [{'date': '2015-05-11T00:00:00Z', 'point': 65, 'type': 'Q'}],
   'name': 'Introduction to Math',
   'node_in_list_node': {'foo': 'FOOOO'}},
  {'attendance': [{'attended': False,
     'date': '2015-05-13T00:00:00Z',
     'hour': 2},
    {'attended': True, 'date': '2015-05-14T00:00:00Z', 'hour': 4}],
   'code': 'rock101',
   'credit': 10,
   'exams': [{'date': '2015-05-15T00:00:00Z', 'point': 65, 'type': 'Q'}],
   'name': 'Introduction to Rocking',
   'node_in_list_node': {'foo': 'FOOOO'}}],
 'name': 'Jack',
 'number': '20300344',
 'pno': '2343243433',
 'surname': 'Black',
 'timestamp': None}
