# -*- coding: utf-8 -*-
"""
我的钢铁网(mysteel.com)价格爬虫
收集钢材、板材等建筑材料价格
"""

import requests
from datetime import datetime
from bs4 import BeautifulSoup


class MySteelScraper:
    """我的钢铁网价格数据爬虫"""

    def __init__(self):
        self.base_url = "https://www.mysteel.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get_steel_prices(self):
        """获取钢材价格数据"""
        prices = []
        try:
            url = "https://list1.mysteel.com/market/p-968-----010101-0-0101-------1.html"
            response = self.session.get(url, timeout=30)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='market-list-table')
            if table:
                rows = table.find_all('tr')[1:]
                for row in rows[:20]:
                    cells = row.find_all('td')
                    if len(cells) >= 5:
                        prices.append({
                            'category': '钢材',
                            'product': cells[0].get_text(strip=True),
                            'spec': cells[1].get_text(strip=True),
                            'region': cells[2].get_text(strip=True),
                            'price': cells[3].get_text(strip=True),
                            'change': cells[4].get_text(strip=True),
                            'source': '我的钢铁网',
                            'date': datetime.now().strftime('%Y-%m-%d')
                        })
        except Exception as e:
            print(f"获取钢材价格失败: {e}")
        return prices

    def get_plate_prices(self):
        """获取板材价格数据"""
        prices = []
        try:
            url = "https://list1.mysteel.com/market/p-968-----010102-0-0101-------1.html"
            response = self.session.get(url, timeout=30)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='market-list-table')
            if table:
                rows = table.find_all('tr')[1:]
                for row in rows[:15]:
                    cells = row.find_all('td')
                    if len(cells) >= 5:
                        prices.append({
                            'category': '板材',
                            'product': cells[0].get_text(strip=True),
                            'spec': cells[1].get_text(strip=True),
                            'region': cells[2].get_text(strip=True),
                            'price': cells[3].get_text(strip=True),
                            'change': cells[4].get_text(strip=True),
                            'source': '我的钢铁网',
                            'date': datetime.now().strftime('%Y-%m-%d')
                        })
        except Exception as e:
            print(f"获取板材价格失败: {e}")
        return prices

    def get_auxiliary_materials(self):
        """获取辅料价格数据"""
        prices = []
        auxiliary_items = [
            {'name': '电焊条J422', 'spec': 'Φ3.2mm', 'unit': '元/千克'},
            {'name': '电焊条J422', 'spec': 'Φ4.0mm', 'unit': '元/千克'},
            {'name': '二氧化碳焊丝', 'spec': 'ER50-6', 'unit': '元/千克'},
            {'name': '防锈漆', 'spec': '铁红', 'unit': '元/千克'},
            {'name': '防火涂料', 'spec': '超薄型', 'unit': '元/千克'},
            {'name': '膨胀螺栓', 'spec': 'M8×80', 'unit': '元/套'},
            {'name': '膨胀螺栓', 'spec': 'M10×100', 'unit': '元/套'},
            {'name': '钻尾螺丝', 'spec': 'M5.5×25', 'unit': '元/千个'},
            {'name': '密封胶', 'spec': '硅酮耐候', 'unit': '元/支'},
            {'name': '玻璃胶', 'spec': '中性', 'unit': '元/支'},
        ]
        for item in auxiliary_items:
            prices.append({
                'category': '辅料',
                'product': item['name'],
                'spec': item['spec'],
                'region': '全国均价',
                'price': '待获取',
                'change': '-',
                'unit': item['unit'],
                'source': '我的钢铁网/市场采集',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices

    def get_all_prices(self):
        """获取所有材料价格"""
        all_prices = []
        print("正在获取钢材价格...")
        all_prices.extend(self.get_steel_prices())
        print("正在获取板材价格...")
        all_prices.extend(self.get_plate_prices())
        print("正在获取辅料价格...")
        all_prices.extend(self.get_auxiliary_materials())
        return all_prices
