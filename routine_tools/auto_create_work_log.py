from os.path import isfile
from datetime import datetime
from docx import Document
from docx.shared import Pt


def get_current_date():
    """
    取得當前的日期，並整理成文件命名與文件標題所需的格式
    """
    current_datetime = datetime.now()
    docs_suffix = f"{current_datetime.year}{current_datetime.month}{current_datetime.day}"
    docs_title_time = f"{current_datetime.month}/{current_datetime.day}"
    return docs_suffix, docs_title_time


def modify_work_log(org_docs_path, new_docs_path, docs_title_time):
    """
    修改工作日誌的標題，修改成今日日期
    :param org_docs_path: 工作日誌樣板路徑 
    :param new_docs_path: 新儲存工作日誌路徑
    :param docs_title_time: 修改成今日的時間
    :return: 
    """
    document = Document(org_docs_path)  # 讀取樣板word
    for paragraph in document.paragraphs:  # 循序讀取所有段落
        # print(paragraph.text)
        for run in paragraph.runs:  # run負責去修改裡面文字
            if "工作日誌" in run.text:  # 將對應的文字取代成新的文字
                run.text = run.text.replace('工作日誌', f'工作日誌 {docs_title_time}')
    document.save(new_docs_path)


if __name__ == "__main__":
    """自動建立每日例行的工作日誌，根據指定樣板，重新命名為今日的檔案名稱，修改內文標題時間"""
    _docs_suffix, _docs_title_time = get_current_date()  # 取得今天日期
    folder = r"C:\Users\jasper chiu\OneDrive - 百通科技股份有限公司"
    _org_docs_path = folder + rf"\Jasper_工作日誌_2022.docx"  # 樣板檔案路徑
    _new_docs_path = folder + rf"\Jasper_工作日誌_{_docs_suffix}.docx"  # 新生成檔案儲存路徑
    print(f"今天日期: {_docs_suffix}")
    if isfile(_new_docs_path):
        print("檔案已存在不生成新的工作日誌")
    else:
        print("檔案不存在，生成今日工作日誌")
        modify_work_log(_org_docs_path, _new_docs_path, _docs_title_time)
        print(f"新增今日工作日誌: {_new_docs_path}")
