# -*- coding: utf-8 -*-
"""
数据整理和格式化模块
将收集到的价格数据整理成易读的格式
"""

import json
import pandas as pd
from datetime import datetime
from pathlib import Path


class DataProcessor:
    """价格数据处理器"""

    def __init__(self, output_dir="data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def create_html_report(self, prices_list):
        """生成HTML格式的价格报告"""
        today = datetime.now().strftime('%Y年%m月%d日')
        steel_prices = [p for p in prices_list if p['category'] == '钢材']
        plate_prices = [p for p in prices_list if p['category'] == '板材']
        aux_prices = [p for p in prices_list if p['category'] == '辅料']

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>建筑材料价格日报 - {today}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .content {{ padding: 30px; }}
        .summary {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }}
        .summary-item {{ text-align: center; }}
        .summary-item .number {{ font-size: 2.5em; font-weight: bold; }}
        .category-section {{ margin-bottom: 40px; }}
        .category-title {{
            font-size: 1.8em;
            color: #1e3c72;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
        }}
        td {{ padding: 12px 15px; border-bottom: 1px solid #e0e0e0; }}
        tr:nth-child(even) {{ background-color: #f8f9fa; }}
        .price {{ font-weight: 600; color: #e74c3c; font-size: 1.1em; }}
        .change-up {{ color: #e74c3c; font-weight: 600; }}
        .change-down {{ color: #27ae60; font-weight: 600; }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>建筑材料价格日报</h1>
            <div>{today}</div>
        </div>
        <div class="content">
            <div class="summary">
                <div class="summary-item">
                    <div class="number">{len(steel_prices)}</div>
                    <div>钢材品种</div>
                </div>
                <div class="summary-item">
                    <div class="number">{len(plate_prices)}</div>
                    <div>板材品种</div>
                </div>
                <div class="summary-item">
                    <div class="number">{len(aux_prices)}</div>
                    <div>辅料品种</div>
                </div>
                <div class="summary-item">
                    <div class="number">{len(prices_list)}</div>
                    <div>总计</div>
                </div>
            </div>
            {self._generate_table_html('钢材价格', steel_prices)}
            {self._generate_table_html('板材价格', plate_prices)}
            {self._generate_table_html('辅料价格', aux_prices)}
        </div>
        <div class="footer">
            <p>数据来源：我的钢铁网、1688批发平台</p>
            <p>生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>"""
        return html

    def _generate_table_html(self, title, prices):
        """生成单个类别的表格HTML"""
        if not prices:
            return ""
        html = f'<div class="category-section"><h2 class="category-title">{title}</h2><table><thead><tr><th>产品名称</th><th>规格</th><th>地区</th><th>价格</th><th>涨跌</th><th>数据来源</th></tr></thead><tbody>'
        for p in prices:
            change_class = 'change-up' if '↑' in str(p.get('change', '')) or '+' in str(p.get('change', '')) else 'change-down' if '↓' in str(p.get('change', '')) else ''
            html += f'<tr><td>{p.get("product", "-")}</td><td>{p.get("spec", "-")}</td><td>{p.get("region", "-")}</td><td class="price">{p.get("price", "-")}</td><td class="{change_class}">{p.get("change", "-")}</td><td>{p.get("source", "-")}</td></tr>'
        html += '</tbody></table></div>'
        return html

    def save_to_json(self, prices_list, filename=None):
        """保存数据为JSON文件"""
        if filename is None:
            filename = f"prices_{datetime.now().strftime('%Y%m%d')}.json"
        filepath = self.output_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(prices_list, f, ensure_ascii=False, indent=2)
        return filepath

    def save_to_excel(self, prices_list, filename=None):
        """保存数据为Excel文件"""
        if filename is None:
            filename = f"prices_{datetime.now().strftime('%Y%m%d')}.xlsx"
        filepath = self.output_dir / filename
        df = pd.DataFrame(prices_list)
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='全部数据', index=False)
            for category in df['category'].unique():
                category_df = df[df['category'] == category]
                category_df.to_excel(writer, sheet_name=category[:31], index=False)
        return filepath

    def save_html_report(self, html_content, filename=None):
        """保存HTML报告"""
        if filename is None:
            filename = f"report_{datetime.now().strftime('%Y%m%d')}.html"
        filepath = self.output_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return filepath
