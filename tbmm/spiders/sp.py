import scrapy
import re
from tbmm.items import TbmmItem


class spSpider(scrapy.Spider):
	name = "sp"

	def start_requests(self):
		urls = [
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_sonuc?v_meclis=1&v_donem=20&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_bastarih=&v_bittarih=&v_kayit_sayisi=5000&v_kullanici_id=11312129&v_gelecek_sayfa=1',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		text1 = response.xpath('//table[last()]//tr[@onmouseover]')
		locations = []
		pages = []
		location1 = {}
		for tr in text1:
			
			item = TbmmItem()
			name = tr.xpath('td[3]/text()').extract()
			name = [x for x in name if not x=="\n"]
			name = name[0]
			name = name.split('\n: ')
			name = "".join(name)
			name = name.split('\n')
			name = "".join(name)
			item['name'] = name
			
			text2 = tr.xpath('td[last()]/table//tr')
			for x in text2:
			
				location1['cilt'] = x.xpath('td[1]/a/b/text()').extract_first()
				location1['birlesme'] = x.xpath('td[2]/a/b/text()').extract_first()
				pages = x.xpath('td[last()]/b/a/text()').extract()
				pages = [x.replace(" ","") for x in pages]
				location1['sayfa'] = pages
				locations.append(location1)
				location1 = {}
				
			item['locationList'] = locations
			
			yield item
			locations = []
		
		url = response.xpath('//table[last()]//tr[last()]//i[last()-1]/b/a/@href').extract_first()
		yield scrapy.Request(url, callback=self.parse)
		
			