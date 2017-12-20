# -*- coding: utf-8 -*-
import scrapy
from tbmm.items import TbmmItem
import re


class spSpider(scrapy.Spider):
	name = "sp"
	custom_settings = {
		'ITEM_PIPELINES': {
			'tbmm.pipelines.TbmmPipeline': 300,
			'tbmm.pipelines.JsonWriterPipeline': 800,
		}
	}

	def start_requests(self):

		urls = [
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=20&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=21&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=22&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=23&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=24&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=25&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=26&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=01&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=02&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=03&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=04&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=05&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=06&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=07&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=08&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=09&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=10&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=11&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=12&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=13&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=14&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=15&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=16&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=17&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=18&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
			'https://www.tbmm.gov.tr/develop/owa/td_v2.tutanak_hazirla?v_meclis=1&v_donem=19&v_yasama_yili=&v_cilt=&v_birlesim=&v_sayfa=&v_anabaslik=&v_altbaslik=&v_mv=&v_sb=&v_ozet=&v_kelime=&v_bastarih=&v_bittarih=',
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		text1 = response.xpath('//table[last()]//tr[@onmouseover]')
		links = []
		pages = []
		location = {}
		for tr in text1:

			item = TbmmItem()
			name = tr.xpath('td[3]/text()').extract()
			name = [x for x in name if not x=="\n"]
			name = name[0]
			name = re.sub(r'\n:? ?',r'',name)
			item['name'] = name

			text2 = tr.xpath('td[last()]/table//tr')
			for x in text2:

				location['link'] = x.xpath('td[2]/a/@href').extract_first()
				pages = x.xpath('td[last()]/b/a/text()').extract()
				pages = [x.replace(" ","") for x in pages]
				location['sayfa'] = pages
				links.append(location)
				location = {}

			item['links'] = links

			yield item
			links = []

		url = response.xpath('//table[last()]//tr[last()]//i[last()-1]/b/a/@href').extract_first()
		yield scrapy.Request(url, callback=self.parse)
