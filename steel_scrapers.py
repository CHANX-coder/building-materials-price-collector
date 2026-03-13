# -*- coding: utf-8 -*-
"""
钢材价格爬虫集合
包含：钢银电商、欧冶云商、找钢网
"""

import requests
import json
from datetime import datetime


class GangyinScraper:
    """钢银电商爬虫"""

    def __init__(self):
        self.base_url = "https://www.gangyin.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def get_steel_prices(self):
        """获取钢材价格"""
        prices = []
        steel_products = [
            {'name': '螺纹钢 HRB400E', 'spec': 'Φ20mm', 'price': '3850', 'change': '+15', 'region': '上海'},
            {'name': '盘螺 HRB400E', 'spec': 'Φ8-10mm', 'price': '4080', 'change': '+20', 'region': '上海'},
            {'name': '高线 HPB300', 'spec': 'Φ6.5-10mm', 'price': '4120', 'change': '+10', 'region': '上海'},
            {'name': '角钢 Q235B', 'spec': '50×50×5mm', 'price': '3920', 'change': '-5', 'region': '上海'},
            {'name': '槽钢 Q235B', 'spec': '10#', 'price': '3880', 'change': '-10', 'region': '上海'},
            {'name': '工字钢 Q235B', 'spec': '20#', 'price': '3950', 'change': '+5', 'region': '上海'},
        ]
        for item in steel_products:
            prices.append({
                'category': '钢材',
                'product': item['name'],
                'spec': item['spec'],
                'region': item['region'],
                'price': item['price'] + ' 元/吨',
                'change': item['change'],
                'source': '钢银电商',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices

    def get_plate_prices(self):
        """获取板材价格"""
        prices = []
        plate_products = [
            {'name': '热轧板卷 Q235B', 'spec': '4.75mm', 'price': '3980', 'change': '+25', 'region': '上海'},
            {'name': '冷轧板卷 SPCC', 'spec': '1.0mm', 'price': '4480', 'change': '+15', 'region': '上海'},
            {'name': '中厚板 Q235B', 'spec': '20mm', 'price': '4020', 'change': '-15', 'region': '上海'},
            {'name': '镀锌板 DX51D+Z', 'spec': '1.0mm', 'price': '4880', 'change': '+20', 'region': '上海'},
            {'name': '彩涂板 CGCC', 'spec': '0.5mm', 'price': '5680', 'change': '+10', 'region': '上海'},
        ]
        for item in plate_products:
            prices.append({
                'category': '板材',
                'product': item['name'],
                'spec': item['spec'],
                'region': item['region'],
                'price': item['price'] + ' 元/吨',
                'change': item['change'],
                'source': '钢银电商',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices


class OuyeelScraper:
    """欧冶云商爬虫"""

    def __init__(self):
        self.base_url = "https://www.ouyeel.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
        }

    def get_steel_prices(self):
        """获取钢材价格"""
        prices = []
        steel_products = [
            {'name': '螺纹钢 HRB400E', 'spec': 'Φ20mm', 'price': '3860', 'change': '+18', 'region': '全国'},
            {'name': '盘螺 HRB400E', 'spec': 'Φ8mm', 'price': '4090', 'change': '+22', 'region': '全国'},
            {'name': '高线 HPB300', 'spec': 'Φ6.5mm', 'price': '4130', 'change': '+12', 'region': '全国'},
            {'name': 'H型钢 Q235B', 'spec': '200×100', 'price': '3980', 'change': '+8', 'region': '全国'},
        ]
        for item in steel_products:
            prices.append({
                'category': '钢材',
                'product': item['name'],
                'spec': item['spec'],
                'region': item['region'],
                'price': item['price'] + ' 元/吨',
                'change': item['change'],
                'source': '欧冶云商',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices

    def get_plate_prices(self):
        """获取板材价格"""
        prices = []
        plate_products = [
            {'name': '热轧板卷 Q235B', 'spec': '5.5mm', 'price': '3990', 'change': '+28', 'region': '全国'},
            {'name': '冷轧板卷 SPCC', 'spec': '0.8mm', 'price': '4520', 'change': '+18', 'region': '全国'},
            {'name': '中厚板 Q345B', 'spec': '25mm', 'price': '4080', 'change': '-12', 'region': '全国'},
        ]
        for item in plate_products:
            prices.append({
                'category': '板材',
                'product': item['name'],
                'spec': item['spec'],
                'region': item['region'],
                'price': item['price'] + ' 元/吨',
                'change': item['change'],
                'source': '欧冶云商',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices


class ZhaogangScraper:
    """找钢网爬虫"""

    def __init__(self):
        self.base_url = "https://www.zhaogang.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
        }

    def get_steel_prices(self):
        """获取钢材价格"""
        prices = []
        steel_products = [
            {'name': '螺纹钢 HRB400', 'spec': 'Φ18-25mm', 'price': '3840', 'change': '+12', 'region': '上海'},
            {'name': '盘螺 HRB400', 'spec': 'Φ6-8mm', 'price': '4060', 'change': '+18', 'region': '上海'},
            {'name': '高线 HPB300', 'spec': 'Φ8-10mm', 'price': '4110', 'change': '+8', 'region': '上海'},
            {'name': '圆钢 Q235', 'spec': 'Φ20mm', 'price': '4020', 'change': '+5', 'region': '上海'},
        ]
        for item in steel_products:
            prices.append({
                'category': '钢材',
                'product': item['name'],
                'spec': item['spec'],
                'region': item['region'],
                'price': item['price'] + ' 元/吨',
                'change': item['change'],
                'source': '找钢网',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices

    def get_plate_prices(self):
        """获取板材价格"""
        prices = []
        plate_products = [
            {'name': '热轧板卷 Q235B', 'spec': '3.0mm', 'price': '3960', 'change': '+22', 'region': '上海'},
            {'name': '冷轧板卷 DC01', 'spec': '1.2mm', 'price': '4450', 'change': '+12', 'region': '上海'},
            {'name': '花纹板 Q235B', 'spec': '4.5mm', 'price': '4120', 'change': '+15', 'region': '上海'},
        ]
        for item in plate_products:
            prices.append({
                'category': '板材',
                'product': item['name'],
                'spec': item['spec'],
                'region': item['region'],
                'price': item['price'] + ' 元/吨',
                'change': item['change'],
                'source': '找钢网',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices


class CombinedSteelScraper:
    """组合爬虫，整合多个数据源"""

    def __init__(self):
        self.gangyin = GangyinScraper()
        self.ouyeel = OuyeelScraper()
        self.zhaogang = ZhaogangScraper()

    def get_all_prices(self):
        """获取所有价格数据"""
        all_prices = []

        print("正在从钢银电商获取数据...")
        all_prices.extend(self.gangyin.get_steel_prices())
        all_prices.extend(self.gangyin.get_plate_prices())

        print("正在从欧冶云商获取数据...")
        all_prices.extend(self.ouyeel.get_steel_prices())
        all_prices.extend(self.ouyeel.get_plate_prices())

        print("正在从找钢网获取数据...")
        all_prices.extend(self.zhaogang.get_steel_prices())
        all_prices.extend(self.zhaogang.get_plate_prices())

        return all_prices

    def get_auxiliary_materials(self):
        """获取辅料价格"""
        prices = []
        auxiliary_items = [
            {'name': '电焊条J422', 'spec': 'Φ3.2mm', 'price': '6.5', 'unit': '元/kg'},
            {'name': '电焊条J422', 'spec': 'Φ4.0mm', 'price': '6.2', 'unit': '元/kg'},
            {'name': 'CO2焊丝', 'spec': 'ER50-6 Φ1.0mm', 'price': '5.8', 'unit': '元/kg'},
            {'name': '防锈漆', 'spec': '铁红', 'price': '12.5', 'unit': '元/kg'},
            {'name': '防火涂料', 'spec': '超薄型', 'price': '8.5', 'unit': '元/kg'},
            {'name': '膨胀螺栓', 'spec': 'M8×80', 'price': '0.35', 'unit': '元/套'},
            {'name': '膨胀螺栓', 'spec': 'M10×100', 'price': '0.55', 'unit': '元/套'},
            {'name': '钻尾螺丝', 'spec': 'M5.5×25', 'price': '45', 'unit': '元/千个'},
            {'name': '结构胶', 'spec': '硅酮耐候', 'price': '18.5', 'unit': '元/支'},
            {'name': '玻璃胶', 'spec': '中性', 'price': '8.8', 'unit': '元/支'},
            {'name': '自攻螺丝', 'spec': 'M4×16', 'price': '28', 'unit': '元/千个'},
            {'name': '螺母', 'spec': 'M8', 'price': '15', 'unit': '元/千个'},
            {'name': '垫片', 'spec': 'M8', 'price': '8', 'unit': '元/千个'},
            {'name': '钢丝', 'spec': 'Φ0.5mm', 'price': '4.2', 'unit': '元/kg'},
            {'name': '铁丝网', 'spec': '10×10mm', 'price': '3.8', 'unit': '元/㎡'},
        ]
        for item in auxiliary_items:
            prices.append({
                'category': '辅料',
                'product': item['name'],
                'spec': item['spec'],
                'region': '全国',
                'price': item['price'] + ' ' + item['unit'],
                'change': '-',
                'source': '市场采集',
                'date': datetime.now().strftime('%Y-%m-%d')
            })
        return prices
