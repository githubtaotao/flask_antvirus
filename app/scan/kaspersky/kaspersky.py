# -*- coding: utf-8 -*- 
# @Time : 2021/7/1 14:42 
# @Author : Dotao
# @File : kaspersky.py
import re
import subprocess
from ..scan_model.base import BaseScanModel


class Kaspersky(BaseScanModel):
    '''
    kaspersky:卡巴斯基
    '''

    def __init__(self, scan_software, target, mode='SCAN'):
        self.__name = 'Kaspersky'
        self.__target = target
        self.__mode = mode
        self.__json_rst = {
            'status': False,
            'virus': [],
            'starttime': False,
            'endtime': False,
            'filename': False,
            'filemd5': False,
            'soft': False,
        }
        self.__compile_rst = {
            'status': r"Total detected:\d{1,10}",
            'virus': r'(\/.*?\.[\w:]+:.*)',
            'starttime': r"Time Start:\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}",
            'endtime': r"Time Finish:\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}",
            'filename': r"\d",
            'filemd5': r"\d",
            'soft': r"\d",
        }
        super().__init__(scan_software, target)

    def scan(self):
        '''
        go~!
        :return:
        '''
        terminator = self.at_virus_process + "   " + self.__mode + "   " + self.__target
        output = self._call_sub_process(terminator)
        self._build_results(output)
        return self.__json_rst

    def _call_sub_process(self, terminator):
        '''
        call sub process to run atvirus program
        :param terminator:
        :return:
        '''
        pipe_process = subprocess.Popen(terminator, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_r, out_err = pipe_process.communicate(timeout=1 * 60 * 60)
        ret_code = pipe_process.poll()
        print('ret_code is %s' % ret_code)
        decode_r = out_r.decode('utf-8')
        decode_r = decode_r.replace('\t', '')
        results = decode_r.split('\r\n')
        print('output console is %s' % results)
        return results

    def _build_results(self, rst_lst):
        '''
        return json
        :param rst_lst:
        :return:
        '''

        for k, v in self.__json_rst.items():
            if not v:
                for item in rst_lst:
                    if k == 'virus':
                        res_lst = re.findall(self.__compile_rst[k], item)
                        if res_lst:
                            for full_path in res_lst:
                                if ':' not in full_path:
                                    continue
                                virus_name = full_path.split(':')[1]
                                self.__json_rst[k].append({
                                    'virus_name': virus_name,
                                    'virus_level': '',
                                })
                    else:
                        res_lst = re.findall(self.__compile_rst[k], item)
                        if res_lst:
                            res = res_lst[0]
                            if 'Start' in res:
                                res = res.replace('Time Start:', '')
                                self.__json_rst[k] = res
                            elif 'Finish' in res:
                                res = res.replace('Time Finish:', '')
                                self.__json_rst[k] = res
                            elif 'detected' in res:
                                res = res.replace('Total detected:', '')
                                self.__json_rst[k] = res
                            else:
                                pass
                            break

        self.__json_rst['filemd5'] = self.get_file_md5()
        self.__json_rst['filename'] = self.__target
        self.__json_rst['soft'] = self.__name