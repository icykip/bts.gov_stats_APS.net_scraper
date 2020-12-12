import scrapy
import pandas as pd
import math

class ArrivalsSpider(scrapy.Spider):
    name = 'ArrivalsData'
    start_urls = ['https://transtats.bts.gov/ONTIME/Arrivals.aspx']
    download_delay = 1.5

    key_values = ["City", "Carrier Code","Date (MM/DD/YYYY)", "Flight Number", "Tail Number", "Origin Airport",	"Scheduled Arrival Time"," Actual Arrival Time", "Scheduled Elapsed Time (Minutes)", "Actual Elapsed Time (Minutes)", "Arrival Delay (Minutes)", "Wheels-on Time", "Taxi-In time (Minutes)"]

    items = pd.DataFrame(columns = key_values)

    def parse(self, response):
        for city in response.css('select#cboAirport > option ::attr(value)').getall()[300:400]:
            for airline in response.css('select#cboAirline > option ::attr(value)').getall():
                data  = {
                        '__EVENTTARGET': 'GridView1',
                        '__EVENTARGUMENT': 'page$1',
                        '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').get(),
                        '__VIEWSTATEGENERATOR' : response.css('input#__VIEWSTATEGENERATOR::attr(value)').get(),
                        '__EVENTVALIDATION' : response.css('input#__EVENTVALIDATION::attr(value)').get(),
                        'chkStatistics$0': '0',
                        'chkStatistics$1': '1',
                        'chkStatistics$2': '2',
                        'chkStatistics$3': '3',
                        'chkStatistics$4': '4',
                        'chkStatistics$5': '5',
                        'chkStatistics$6': '6',
                        'cboAirport': city,
                        'cboAirline': airline,
                        'chkAllMonths': 'on',
                        'chkMonths$0': '1',
                        'chkMonths$1': '2',
                        'chkMonths$2': '3',
                        'chkMonths$3': '4',
                        'chkMonths$4': '5',
                        'chkMonths$5': '6',
                        'chkMonths$6': '7',
                        'chkMonths$7': '8',
                        'chkMonths$8': '9',
                        'chkMonths$9': '10',
                        'chkMonths$10': '11',
                        'chkMonths$11': '12',
                        'chkAllDays': 'on',
                        'chkDays$0': '1',
                        'chkDays$1': '2',
                        'chkDays$2': '3',
                        'chkDays$3': '4',
                        'chkDays$4': '5',
                        'chkDays$5': '6',
                        'chkDays$6': '7',
                        'chkDays$7': '8',
                        'chkDays$8': '9',
                        'chkDays$9': '10',
                        'chkDays$10': '11',
                        'chkDays$11': '12',
                        'chkDays$12': '13',
                        'chkDays$13': '14',
                        'chkDays$14': '15',
                        'chkDays$15': '16',
                        'chkDays$16': '17',
                        'chkDays$17': '18',
                        'chkDays$18': '19',
                        'chkDays$19': '20',
                        'chkDays$20': '21',
                        'chkDays$21': '22',
                        'chkDays$22': '23',
                        'chkDays$23': '24',
                        'chkDays$24': '25',
                        'chkDays$25': '26',
                        'chkDays$26': '27',
                        'chkDays$27': '28',
                        'chkDays$28': '29',
                        'chkDays$29': '30',
                        'chkDays$30': '31',
                        'chkYears$33': '2020',
                        'btnSubmit': 'Submit'
                }
                yield scrapy.FormRequest('https://transtats.bts.gov/ONTIME/Arrivals.aspx',formdata=data,callback=self.parse_pages)

    def parse_pages(self, response):
        count = response.css('span#lblRows ::text').get()
        if count != 'No data found for the above selection ..':
            for page in range(1, math.ceil(int(count.split()[-1])/100)):
                page_formated = 'Page${}'.format(page),
                data = {
                            '__EVENTTARGET': 'GridView1',
                            '__EVENTARGUMENT': page_formated,
                            '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').get(),
                            '__VIEWSTATEGENERATOR' : response.css('input#__VIEWSTATEGENERATOR::attr(value)').get(),
                            '__EVENTVALIDATION' : response.css('input#__EVENTVALIDATION::attr(value)').get(),
                            'chkStatistics$0': '0',
                            'chkStatistics$1': '1',
                            'chkStatistics$2': '2',
                            'chkStatistics$3': '3',
                            'chkStatistics$4': '4',
                            'chkStatistics$5': '5',
                            'chkStatistics$6': '6',
                            'cboAirport': response.css('select#cboAirport > option[selected] ::attr(value)').get(),
                            'cboAirline': response.css('select#cboAirline > option[selected] ::attr(value)').get(),
                            'chkAllMonths': 'on',
                            'chkMonths$0': '1',
                            'chkMonths$1': '2',
                            'chkMonths$2': '3',
                            'chkMonths$3': '4',
                            'chkMonths$4': '5',
                            'chkMonths$5': '6',
                            'chkMonths$6': '7',
                            'chkMonths$7': '8',
                            'chkMonths$8': '9',
                            'chkMonths$9': '10',
                            'chkMonths$10': '11',
                            'chkMonths$11': '12',
                            'chkAllDays': 'on',
                            'chkDays$0': '1',
                            'chkDays$1': '2',
                            'chkDays$2': '3',
                            'chkDays$3': '4',
                            'chkDays$4': '5',
                            'chkDays$5': '6',
                            'chkDays$6': '7',
                            'chkDays$7': '8',
                            'chkDays$8': '9',
                            'chkDays$9': '10',
                            'chkDays$10': '11',
                            'chkDays$11': '12',
                            'chkDays$12': '13',
                            'chkDays$13': '14',
                            'chkDays$14': '15',
                            'chkDays$15': '16',
                            'chkDays$16': '17',
                            'chkDays$17': '18',
                            'chkDays$18': '19',
                            'chkDays$19': '20',
                            'chkDays$20': '21',
                            'chkDays$21': '22',
                            'chkDays$22': '23',
                            'chkDays$23': '24',
                            'chkDays$24': '25',
                            'chkDays$25': '26',
                            'chkDays$26': '27',
                            'chkDays$27': '28',
                            'chkDays$28': '29',
                            'chkDays$29': '30',
                            'chkDays$30': '31',
                            'chkYears$33': '2020',
                            'btnSubmit': 'Submit'
                    }
                yield scrapy.FormRequest('https://transtats.bts.gov/ONTIME/Arrivals.aspx',formdata=data, callback=self.parse_results)

    def parse_results(self, response):
        counter = 0
        for row in response.xpath('/html/body/form/table[3]/tr[11]/td/div/table/tr')[:-1]:
            airport = response.css('span#lblAirport ::text').getall()[1].split(':')[0]
            if counter > 0:
                values = row.css('td ::text').getall()
                values.insert(0, airport)
                item = pd.DataFrame([values], columns=self.key_values)
                self.items = self.items.append(item, ignore_index=True)
            counter += 1
            yield self.items.to_csv('AZA-VEL.csv', index=False)