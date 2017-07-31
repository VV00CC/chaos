# -*- coding:utf-8 -*-
import os
from utils import *
import csv
import codecs

class myReport():
    flag = True
    error = ""
    details = ""
    test_case = ""

    def set_test_case_name(self,case_name):
        self.test_case = case_name
    
    def reset_result(self):
        self.flag = True
        self.error = ""
        self.details = ""
        self.test_case = ""

    def my_assert(self,expression,comment):
        try:
            assert expression,comment
        except AssertionError,e:
            self.flag = False
            self.error = self.error+str(e)+"\n"
            
            
    def add_details(self,detail):
        self.details = self.details + detail
        
    def add_result(self,resultFilePath,startTime,endTime,duration):
        
        if not self.flag:
            result = str_2_tuple(self.test_case)+str_2_tuple("Failed")+str_2_tuple(self.error)+str_2_tuple(startTime)+str_2_tuple(endTime)+str_2_tuple(duration)+str_2_tuple(self.details)
        else:
            result = str_2_tuple(self.test_case)+str_2_tuple("Passed")+str_2_tuple(self.error)+str_2_tuple(startTime)+str_2_tuple(endTime)+str_2_tuple(duration)+str_2_tuple(self.details)

        self.generate_result(resultFilePath,result)

    def init_result_file(self):
        genTime = get_local_time()
        resultFileName = genTime+' test_result'
        resultFileName = resultFileName.replace(':','_')
        autyPath = os.path.dirname(os.path.dirname(__file__))
        resultFilePath = os.path.join(autyPath,'results',resultFileName)
        self.generate_result(resultFileName,('TestCase','TestResult','ErrorMessage','StartTime','EndTime','Duration','Details'))
        return resultFileName

    def generate_result(self,resultFileName,result):
        filePath = os.path.abspath(os.path.dirname(__file__))
        resultFilePath = os.path.join(os.path.dirname(filePath),'results',resultFileName+'.csv')
        print resultFilePath
        csvFile = file(resultFilePath,'a+')
        csvFile.write(codecs.BOM_UTF8)
        writer = csv.writer(csvFile)
        data = [result]
        writer.writerows(data)
        csvFile.close()
        html_result_path = os.path.join(os.path.dirname(filePath),'results',resultFileName+'.html')
        self.write_csv_to_html(resultFilePath,html_result_path)

    def write_csv_to_html(self,csv_path,save_path):
        #print os.getcwd()
        csvfile = file(csv_path, 'rb')
        reader = csv.reader(csvfile)
        html = open(save_path, 'w')
        html.write("""
        <html>
        <head>
        <meta charset=\"utf-8\">
        <title>Chaos test result</title>
        <h1>Chaos test result</h1>
        <h3>Result file path:"""+csv_path+"""</h3>
        <style>img{float:left;margin:5px;}</style>
        </head>
        <body">
        <table border="1">
        """)
        for line in reader:
            sig = True
            for each in line:
                if('Failed' in each):
                    sig = False
            if sig == False:
                html.write('<tr bgcolor="#8B2323">')
            else:
                html.write('<tr bgcolor="#00FF7F">')
            for each in line:
                if "\n" in each:
                    each = each.replace("\n","<br/>")
                html.write('<td>'+each+'</td>')
        html.write('</tr>')
        html.write("""
        </table>
        </body>
        </html>
        """)
        csvfile.close()
        html.close()

				




if __name__ == '__main__':
    myReport = myReport()
    startTime=get_specific_time()
    myReport.my_assert(1==1,"hahahha:")
    myReport.add_details("我们bingo")
    myReport.my_assert(1==2,"222222222路径22222:")
    myReport.my_assert(1==3,"11111111111111111:")
    time.sleep(5)
    endTime = get_specific_time()
    duration = endTime-startTime
    resultFilePath = myReport.init_result_file()
    myReport.add_result(resultFilePath,startTime,endTime,duration)
