## $Id$

## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


from invenio.dbquery import run_sql
import datetime
#logfile = "/opt/cds-invenio/var/cache/oaiarxiv_oaiid.dat"

class HistoryEntry:
    date = None
    id = ""
    operation = "i"
    def __init__(self, date, id):
        self.date = date
        self.id = id

def get_history_entries(oai_src_id, monthdate):
    query = "SELECT harvesting_date, oai_record_id  from oaiHARVESTINGLOG WHERE oai_src_id=%s AND MONTH(harvesting_date) =" + str(monthdate.month) + " AND YEAR(harvesting_date) = " + str(monthdate.year) + " ORDER BY harvesting_date"
    res = run_sql(query,(str(oai_src_id)))
    result = []
    for entry in res:
        result.append(HistoryEntry(entry[0],str(entry[1])))
    return result