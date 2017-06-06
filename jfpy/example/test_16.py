#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

if __name__ =='__main__':
    print (datetime.date.today().strftime('%d/%m/%Y'))

    birthdate = datetime.date(1978,2,2)

    print birthdate.strftime('%d/%m/%Y')

    bnd = birthdate+datetime.timedelta(days=1)
    print bnd.strftime('%d/%m/%Y')

    firstday = birthdate.replace(year= birthdate.year +1)

    print firstday.strftime('%d/%m/%Y')

