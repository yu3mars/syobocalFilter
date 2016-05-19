# syobocalFilter
しょぼいカレンダーのフィルタリング用プログラム。  
しょぼいカレンダーが発行する.icsを読み込んでフィルタリングします。  
"【新】"、"【注】"、"【！】"が含まれるものだけを含んだ.icsを出力します。

# How to use
config.py.exampleをconfig.pyにコピーしたうえで、変数を適宜変更して使ってください。

cron設定例

    5   *    *   *     *     python  /path/to/syobocalFilter/syobocalFilter.py

# Require
python3

    pip install request