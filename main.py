# -*- coding: utf-8 -*-
"""
建筑材料价格自动收集系统主程序
每天早上9点自动收集价格并发送邮件
"""

import os
import sys
from datetime import datetime
from pathlib import Path

from scraper.mysteel_scraper import MySteelScraper
from scraper.alibaba_scraper import AlibabaScraper
from data_processor import DataProcessor
from email_sender import EmailSender


def collect_prices():
    """收集所有价格数据"""
    print(f"\n{'='*60}")
    print(f"开始收集建筑材料价格 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    all_prices = []

    print("[1/3] 正在从我的钢铁网收集数据...")
    try:
        mysteel = MySteelScraper()
        mysteel_prices = mysteel.get_all_prices()
        all_prices.extend(mysteel_prices)
        print(f"✓ 从我的钢铁网获取到 {len(mysteel_prices)} 条数据\n")
    except Exception as e:
        print(f"✗ 我的钢铁网数据获取失败: {e}\n")

    print("[2/3] 正在从1688收集参考数据...")
    try:
        alibaba = AlibabaScraper()
        alibaba_prices = alibaba.get_all_reference_prices()
        all_prices.extend(alibaba_prices)
        print(f"✓ 从1688获取到 {len(alibaba_prices)} 条参考数据\n")
    except Exception as e:
        print(f"✗ 1688数据获取失败: {e}\n")

    print(f"{'='*60}")
    print(f"数据收集完成，共获取 {len(all_prices)} 条价格数据")
    print(f"{'='*60}\n")

    return all_prices


def process_and_save(prices):
    """处理并保存数据"""
    print("正在处理数据...")
    processor = DataProcessor(output_dir="data")

    json_path = processor.save_to_json(prices)
    print(f"✓ JSON数据已保存: {json_path}")

    try:
        excel_path = processor.save_to_excel(prices)
        print(f"✓ Excel数据已保存: {excel_path}")
    except Exception as e:
        print(f"✗ Excel保存失败: {e}")
        excel_path = None

    html_content = processor.create_html_report(prices)
    html_path = processor.save_html_report(html_content)
    print(f"✓ HTML报告已保存: {html_path}")

    return html_content, html_path, excel_path


def send_report(html_content, attachments):
    """发送邮件报告"""
    print("\n正在发送邮件报告...")
    to_email = os.getenv('RECIPIENT_EMAIL', '234497541@qq.com')

    try:
        sender = EmailSender()
        success = sender.send_price_report(
            to_email=to_email,
            html_content=html_content,
            attachments=attachments
        )
        if success:
            print(f"✓ 邮件已成功发送至 {to_email}")
        return success
    except Exception as e:
        print(f"✗ 邮件发送失败: {e}")
        return False


def main():
    """主程序入口"""
    Path("data").mkdir(exist_ok=True)

    prices = collect_prices()
    if not prices:
        print("错误：未能获取到任何价格数据")
        sys.exit(1)

    html_content, html_path, excel_path = process_and_save(prices)

    attachments = [str(html_path)]
    if excel_path:
        attachments.append(str(excel_path))

    send_report(html_content, attachments)

    print(f"\n{'='*60}")
    print(f"任务完成 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
