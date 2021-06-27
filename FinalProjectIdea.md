# Mô tả đồ án cuối kỳ
**Danh sách viên trong nhóm:**
+  Đặng Xuân Mai - 19521820
+  Nguyễn Thị Thảo Hiền - 19521488
+  Nguyễn Thị Cẩm Hướng - 19521594
+  Nguyễn Hoài Nam - 18521126

## Lý do chọn đề tài này
Trong thời buổi ngày càng hiện đại, những thông tin trang mạng được lan truyền với tốc độ rất nhanh. Tuy nhiên, không phải thông tin nào ở trên mạng cũng đều được đưa đúng theo sự thật diễn ra.

**Các định nghĩa do nhóm tìm hiểu được:**

**Tin giả** còn được gọi là tin rác hoặc tin tức giả mạo, là các thông tin giả được lan truyền qua phương tiện truyền thông truyền thống (như in và phát sóng, báo chí) hoặc phương tiện truyền thông xã hội trực tuyến...

*Link tham khảo khái niệm: [Tin giả](https://luathoangphi.vn/tin-gia-la-gi-dang-tin-gia-bi-xu-phat-nhu-the-nao/)*

Nguyên nhân mà người ta hay tạo ra các tin giả vì:
+ Trình độ nhận thức hạn chế, tung tin cho vui, không nghĩ đến hậu quả. 
+ Thích “câu like”, tạo sự chú ý để trở thành người quan trọng trong mắt người khác. 
+ Tung tin giả có chủ đích, nhằm gây mất trật tự, an ninh xã hội, kích động người dân.

**Tin thật, chính thống** thường dùng trong hoạt động truyền thông, báo chí - để chỉ một sự kiện, sự việc nào đó có tính mới và là nguồn tin được đưa trên sự thật đã xảy ra, chứ không bịa đặt,...

*Link tham khảo khái niệm: [Tin thật](https://sites.google.com/a/ecolaw.vn/viet-va-phat-hanh-mot-thong-cao-bao-chi/mot-so-khai-niem-co-ban-trong-truyen-thong-bao-chi/tin-tin-tuc-bao-chi-la-gi)*

> Tạo một mô hình phân biệt được tin thật hay giả dựa vào **tiêu đề**, từ đó tránh bị những nguồn thông tin không đáng tin dẫn dắt đi sai hướng. Những tin giả thường có những tiêu đề giật gân, có những từ ngữ không lành mạnh,... nhằm thu hút người đọc

## Mô tả bài toán
**Input:** Tiêu đề của 1 bài báo mạng nào đó

**Output:** Có phải là tin giả (1) hay tin thật (0).

## Mô tả về bộ dữ liệu
### Cách thức xây dựng bộ dữ liệu
Bộ dữ liệu **tự xây dựng**. 

Ngôn ngữ sử dụng: tiếng Anh.

Dùng những kiến thức đã có ở Python, kết hợp với thư viện **scrapy** để tạo ra chương trình gom những tiêu đề của những bài báo về.

Bộ dữ liệu lọc những thông tin trong khoảng **2-3 năm trở lại** đây để đảm bảo được tính mới. 

Chương trình gom dùng scrapy để tổng hợp những thông tin trên báo mạng:
+ Chương trình tổng hợp những trang tin giả [[Link]](https://github.com/dxmai/CS114.L21.KHCL/blob/main/FinalProject/Collect_Data.ipynb)
+ Ngoài ra còn có chương trình tổng hợp những trang tin châm biếm mà nhóm em đã làm để thầy có thể **nhận xét thêm** về quá trình và cách thức xây dựng bộ dữ liệu của chúng em [[Link]](https://github.com/dxmai/CS114.L21.KHCL/blob/main/Colab/SarcasmDetection/SarcasmDetection.ipynb)

Dữ liệu có định dạng giống dataset có sẵn trên [kaggel](https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection) nhưng nhóm sẽ chỉnh lại theo đúng bài toán mà mình đang hướng đến như sau:

headline: tiều đề bài báo

artilce_link: đường link dẫn đến bài báo

is_fake: là 1 nếu là tin giả, là 0 nếu là tin thật

### Số lượng, độ đa dạng của dữ liệu
Tham khảo tại: 
+ [Tổng hợp trang đáng tin](https://www.makeuseof.com/tag/trust-news-sites/)
+ [Tổng hợp những trang không đáng tin](https://www.dailydot.com/debug/fake-news-sites-list-facebook/)

Hiện tại nhóm em đã thu thập được trên 200 nghìn tiêu đề của bài báo mỗi loại (tổng cộng 400 nghìn tiêu đề). Những trang báo nhóm em chọn cũng không cùng 1 quốc gia (có trang báo của Anh, Mỹ, Úc,..) để đảm bảo được độ đa dạng của các loại tin.

### Các thao tác tiền xử lý dữ liệu như:
+ Chuyển về chữ thường (lowercase)
+ Chuyển các từ về dạng số bằng cách sử dụng tf-idf (hoặc những cách khác như Tokenizer, padding - em chỉ mới tìm hiểu được như vậy, nếu thầy duyệt đồ án thì em sẽ tìm hiểu kỹ hơn các kỹ thuật ạ)
+ Xử lý các từ mới nếu bộ test có từ nằm ngoài những từ đã được train (Out of vocabulary - OOV)


EDIT:

Đây là bài colab mà em đã thực hiện trên bộ dữ liệu Sarcasm Detection. Em biết là vẫn cần cải thiện thêm rất nhiều về bài toán này, nhưng em đã cố gắng để hoàn thiện được bài tập này tốt nhất theo cách của em. Nếu thầy xem xét duyệt đồ án "Nhận diện tin giả" này, em sẽ cố gắng tìm kiếm thêm nhiều phương pháp hơn nữa để cải tiến. Hy vọng thầy sớm duyệt đồ án cho em! Em cảm ơn!

Link đến bài Colab: [Sarcasm Detection](https://github.com/dxmai/CS114.L21.KHCL/blob/main/Colab/SarcasmDetection/SarcasmDetection_Model.ipynb) 

 Hết
 
*Em hy vọng là thầy sẽ sớm duyệt đồ án cho nhóm em ạ. Em xin cảm ơn và chúc thầy 1 ngày tốt lành!*







