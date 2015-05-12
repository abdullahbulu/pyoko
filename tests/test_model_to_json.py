# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from tests.data.test_data import data
from tests.data.test_model import Student


def test_model_to_json_compact():
    st = Student(**data)
    st.join_date = data['join_date']
    st.AuthInfo(**data['AuthInfo'])
    for lct_data in data['Lectures']:
        lecture = st.Lectures(**lct_data)
        lecture.ModelInListModel(**lct_data['ModelInListModel'])
        for atd in lct_data['Attendance']:
            lecture.Attendance.add(**atd)
        for exam in lct_data['Exams']:
            lecture.Exams.add(**exam)

    assert data == st.clean_value()


def test_model_to_json_expand():
    d = data
    s = Student()
    s.number = d['number']
    s.bio = d['bio']
    s.name = d['name']
    s.surname = d['surname']
    s.pno = d['pno']
    s.join_date = data['join_date']
    d = data['AuthInfo']
    ai = s.AuthInfo()
    ai.email = d['email']
    ai.password = d['password']
    ai.username = d['username']
    for ld in data['Lectures']:
        lecture = s.Lectures()
        lecture.code = ld['code']
        lecture.credit = ld['credit']
        lecture.name = ld['name']
        milm = lecture.ModelInListModel()
        milm.foo = ld['ModelInListModel']['foo']
        for atd in ld['Attendance']:
            lecture.Attendance.add(**atd)
        for exam in ld['Exams']:
            lecture.Exams.add(**exam)

    assert data == s.clean_value()
