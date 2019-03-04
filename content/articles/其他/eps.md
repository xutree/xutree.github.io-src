Title: eps 图像截切四周的空白
Category: 其他
Date: 2019-03-05 05:18:15
Modified: 2019-03-05 05:18:15
Tags: eps, 图像处理

```
$ epstopdf origin.eps temp.pdf
$ pdfcrop temp.pdf temp-crop.pdf
$ pdf2ps temp-crop.pdf final.eps
$ rm temp*
```
