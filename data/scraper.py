import urllib2

from BeautifulSoup import BeautifulSoup

# build link list

schedule_page = urllib2.urlopen("http://www.sports-reference.com/cfb/schools/northwestern/2012-schedule.html")
link_soup = BeautifulSoup(schedule_page)
schedule = link_soup.findAll(attrs={"id":"schedule"})
link_list = []
for s in schedule:
    trs = s.findAll('tr')
    for r in trs:
        tds = r.findAll('td')
        if len(tds) == 0:
            pass
        else:
            link = tds[1].a['href']
            string_link = str(link)
            link_list.append("http://www.sports-reference.com" + string_link)

#find score summary of each game

for l in link_list:
    page = urllib2.urlopen(l)
    soup = BeautifulSoup(page)
    scoring = soup.findAll(attrs={"id":"scoring"})

    # stupid designers used scoring id more than once
    first_table = scoring[0]

    trs = first_table.findAll('tr')
    for r in trs:
        tds = r.findAll('td')
        if len(tds) == 0:
            ths = r.findAll('th')
            quarter = ths[0].string
            print quarter
        else:
            team = tds[0].string
            score_type = tds[1].string
            time = tds[2].string
            away_score = tds[4].string
            home_score = tds[5].string
            print team, score_type, time, away_score, home_score