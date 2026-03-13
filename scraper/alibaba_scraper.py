# -*- coding: utf-8 -*-
"""
阿里巴巴1688建筑材料价格爬虫
作为价格参考数据来源
"""

from datetime import datetime


class AlibabaScraper:
    """1688批发价格数据爬虫"""

    def __init__(self):
        self.base_url = "https://s.1688.com"

    def get_steel_reference_prices(self):
        """获取钢材参考价格"""
        steel_keywords = [
            ('螺纹钢 HRB400', '钢材'),
            ('盘螺 HRB400', '钢材'),
            ('高线 HPB300', '钢材'),
            ('角钢 50*50', '钢材'),
            ('槽钢 10#', '钢材'),
            ('工字钢 20#', '钢材'),
        ]
        prices = []
        for keyword, category in steel_keywords:
            prices.append({
                'category': category,
                'product': keyword,
                'spec': '市场主流规格',
                'region': '全国批发',
                'price': '参考1688平台',
                'change': '-',
                'source': '1688批发参考',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'note': '需登录1688查看实时价格'
            })
        return prices

    def get_plate_reference_prices(self):
        """获取板材参考价格"""
        plate_keywords = [
            ('热轧板卷 Q235B', '板材'),
            ('冷轧板卷 SPCC', '板材'),
            ('中厚板 Q235B', '板材'),
            ('镀锌板 DX51D', '板材'),
            ('彩涂板 CGCC', '板材'),
        ]
        prices = []
        for keyword, category in plate_keywords:
            prices.append({
                'category': category,
                'product': keyword,
                'spec': '市场主流规格',
                'region': '全国批发',
                'price': '参考1688平台',
                'change': '-',
                'source': '1688批发参考',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'note': '需登录1688查看实时价格'
            })
        return prices

    def get_auxiliary_reference_prices(self):
        """获取辅料参考价格"""
        auxiliary_items = [
            ('电焊条 J422', '辅料', '箱'),
            ('二氧化碳气体保护焊丝', '辅料', '盘'),
            ('防锈漆 铁红', '辅料', 'kg'),
            ('防火涂料 钢结构', '辅料', 'kg'),
            ('膨胀螺栓 M8', '辅料', '百套'),
            ('钻尾螺丝', '辅料', '千个'),
            ('结构胶 硅酮', '辅料', '支'),
            ('玻璃胶 中性', '辅料', '支'),
        ]
        prices = []
        for name, category, unit in auxiliary_items:
            prices.append({
                'category': category,
                'product': name,
                'spec': '常规规格',
                'region': '全国批发',
                'price': '参考1688平台',
                'change': '-',
                'unit': unit,
                'source': '1688批发参考',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'note': '需登录1688查看实时价格'
            })
        return prices

    def get_all_reference_prices(self):
        """获取所有参考价格"""
        all_prices = []
        all_prices.extend(self.get_steel_reference_prices())
        all_prices.extend(self.get_plate_reference_prices())
        all_prices.extend(self.get_auxiliary_reference_prices())
        return all_prices
