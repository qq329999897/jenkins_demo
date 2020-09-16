#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2020/9/14 10:56 上午

import os
import unittest
from common import HTMLTestReportCN
from common import zip_utils

case_path = os.path.join( os.path.dirname(__file__),'testcases')
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_*.py',
                                               top_level_dir=case_path
                                               )
all_case_suite = unittest.TestSuite()
all_case_suite.addTest( discover )

report_path = os.path.join(os.path.dirname(__file__),'reports/')
report_dir = HTMLTestReportCN.ReportDirectory(report_path)
report_dir.create_dir('jenkins示例自动化测试')
dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
html_file = open( report_html_path,'wb' )
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=html_file,
                                              title='jenkins示例自动化测试',
                                              description='学习实践用',
                                              tester='刘sir')
html_runner.run( all_case_suite )

# report_zip_path = dir_path + '/../JENKINS_自动化测试报告.zip'
# zip_utils.zip_dir(dir_path, report_zip_path)