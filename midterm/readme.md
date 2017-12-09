# Midterm (Take-home)
## Due: 2017/12/14 6:00pm (上課前)

Midterm 總共有五題：

* Q1. 畫出 diamond shape
  - 類似 HW04 Q1 作業，只是本次需要輸出一個菱形，而不是三角形。
  - [Q1影片提示](https://youtu.be/f3BgTilP608)
* Q2. 刪除重複性的資料。
  - 讀入資料夾中的 symbols01.txt 及 symbols02.txt 裡面的所有 symbols。
  - 合併為一份沒有重複的 symbols，並輸出至 symbols03.txt。
  - 如果嘗試用 read()，可以想辦法把讀下來的整個字串 split 成 symbol 的 list。[split()](https://docs.python.org/3/library/stdtypes.html#str.split) 方法可以傳入特定字元，讓你作為切分字串的依據。
  - 寫入檔案時，請還是用 "\\n" 來分隔字串，讓檔案打開時，一行只有一個 symbol。
  - [Q2影片提示](https://youtu.be/PudB2pfXq_M)
* Q3. 下載台灣上市公司基本資料。
  - 使用 pythn 下載政府開放資料平台上的台灣上市公司基本資料。
  - 輸出成 pandas dataframe。
  - [Q3影片提示](https://youtu.be/RFX4Qr6HndY)
* Q4. 畫出技術曲線。
  - 選擇一種上課沒有提到過的技術曲線，使用 python 將它畫出來。
  - 股價可以使用預先下載的股價資料，或自己用 pandas datareader 自不同的資料源下載。
  - 這題不像是 HW05 Q2 只要各位畫價量曲線，我希望各位在價量圖上加上不同的曲線，或者是把 RSI 之類的曲線畫在價量圖下的 subplot。
  - 關於可用的技術指標，可以參考 [talib](https://github.com/mrjbq7/ta-lib)，或[參考這個連結](https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code)，但是有可能要自己解一些小 bug。
  - 讓我再把問題更簡化一點，不知道要畫什麼的，請直接畫 Bollinger Bands 就好了，Bollinger Bands 怎麼計算，可以參考 BBands_strategy() 裡面的算法，也可以自己用 pandas 去算。願意挑戰自己的，還請自由嘗試。
  - [Q4影片提示](https://youtu.be/r4-aCGiMDdI)
* Q5. 策略回測。
  - 寫出自己的交易策略，並回測看看結果怎樣。
  - [Q5影片提示](https://youtu.be/bjkxx3hldXU)
