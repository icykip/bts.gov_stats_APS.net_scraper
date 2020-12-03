import scrapy
import pandas as pd

class AirTravelTimeSpider(scrapy.Spider):
    name = 'btsSpider'
    start_urls = ['https://transtats.bts.gov/ONTIME/OriginDestination.aspx']
    download_delay = 1.5

    bussiest_routes = [["ATL", "DFW"],["HNL", "OGG"],["DEN", "ORD"],["ATL", "BWI"],["SAN", "SFO"],["LAS", "SFO"],["EWR", "SFO"],["EWR", "FLL"],["DEN", "LAS"],["ATL", "BOS"]]
    start_date = [['2', '1', '2020'], ['2', '15', '2020'], ['2', '1', '2019']]
    end_date = [['3', '15', '2020'], ['3', '15', '2020'], ['3', '15', '2019']]

    results_count = 0
    time = ['a', 'b', 'c']

    call_count = len(bussiest_routes) * len(start_date)

    key_values = ["Id", "Carriers","Total_Number","Average_Departure_Delay", "Average_Taxi_Out", "Average_Departure_to_Take-off(scheduled)", "Average_Arrival_Delay", "Average_Airborne_Time", "Average_Taxi_In", "Number_Cancelled", "Percent_Cancelled", "Number_Diverted", "Percent_Diverted"]

    items = pd.DataFrame(columns = key_values)

    def parse(self, response):
        for route in self.bussiest_routes:
            for date in range(3):
                data = {
                        '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').get(),
                        '__VIEWSTATEGENERATOR' : response.css('input#__VIEWSTATEGENERATOR::attr(value)').get(),
                        '__EVENTVALIDATION' : response.css('input#__EVENTVALIDATION::attr(value)').get(),
                        'cboAirport_Origin': route[0],
                        'cboAirport_Dest': route[1],
                        'stdatemon': self.start_date[date][0],
                        'stdateday': self.start_date[date][1],
                        'stdateyear': self.start_date[date][2],
                        'eddatemon': self.end_date[date][0],
                        'eddateday': self.end_date[date][1],
                        'eddateyear': self.end_date[date][2],
                        'btnSubmit': 'Submit'
                }
                yield scrapy.FormRequest(url='https://transtats.bts.gov/ONTIME/OriginDestination.aspx', formdata=data, callback=self.parse_results)

    def parse_results(self, response):
        counter = 0
        for row in response.xpath('/html/body/form/table[5]/tr[10]/td/div/table/tr'):
            if counter > 1:
                values = row.css('td::text').getall()
                values.insert(0, str(21 + (int)(self.results_count / 3)) + "-" + self.time[self.results_count % 3])
                item = pd.DataFrame([values], columns=self.key_values)
                self.items = self.items.append(item, ignore_index=True)
            counter += 1
        self.results_count += 1
        yield self.items.to_csv('Isaac_BTS.csv', index=False)
