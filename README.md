# flask_antivirus
##调用卡巴斯基命exe工具检测文件


```notes
pip3 install virtualenv
virtualenv yourProjectName
cd yourProjectName
cd Scripts
activate

download python-packages:
pip download -d ./packages -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

install python-packages without internet:
pip install --no-index --find-links=/packs/ -r requirements.txt

install python-packages online:
pip install -r requirements.txt  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

# Flask Atvirus Demo

[![Generic badge](https://img.shields.io/badge/<flask>-<windows>-<COLOR>.svg)]()


## Background

> A Flask Demo, supply rest api. Run with waitress on Windows.


## Install

This project use Kaspersky software in Windows,
[Python3](https://www.python.org/downloads/), Flask

Download Python3 Windows installer , just run it.

Create your venv environment

## RUN
```commandline
waitress-serve --listen=127.0.0.1:9999 run:app
```

##Example
```
http://localhost:port/AtVirus/api/v1/engine/kaspersky/file?file_path=D:\AtVirusTest\Dump20210608\test1.sql

{
    "code": 20000,
    "data": {
        "endtime": "2021-07-07 14:36:44",
        "filemd5": "41a55371cbd28fae49715e4e9c23eb8a",
        "filename": "D:\\AtVirusTest\\Dump20210608\\test1.sql",
        "soft": "Kaspersky",
        "starttime": "2021-07-07 14:36:01",
        "status": "1",
        "virus": [
            {
                "virus_level": "",
                "virus_name": "Trojan.Win32.Generic"
            }
        ]
    },
    "msg": "success!"
}



http://localhost:7799/AtVirus/api/v1/engine/kaspersky/file?file_path=D:\AtVirusTest\test.txt
{
    "code": 20000,
    "data": {
        "endtime": "2021-07-22 14:33:03",
        "filemd5": "212cb962ac59075b964b07152d234b70",
        "filename": "D:\\AtVirusTest\\test.txt",
        "soft": "Kaspersky",
        "starttime": "2021-07-22 14:33:03",
        "status": "0",
        "virus": []
    },
    "msg": "success!"
}

```

## License

[MIT](LICENSE) © dotao