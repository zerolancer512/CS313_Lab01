Thông tin mô tả từng chức năng của chương trình:

1. Summary (log_file_path, input_file_path)

* log_file_path: đường dẫn chứa tập tin log 
- định dạng [../log.txt]
- Default: current path/log.txt

* input_file_path: đường dẫn chứa tập dữ liệu test
- định dạng [../test.txt]
- Requirement input

2. Replace (log_file_path, input_file_path, output_file_path)

* log_file_path: đường dẫn chứa tập tin log 
- định dạng [../log.txt]
- Default: current path/log.txt

* input_file_path: đường dẫn chứa tập dữ liệu test
- định dạng [../test.txt]
- Requirement input

* output_file_path: đường dẫn chứ tập dữ liệu đầu ra
- định dạng [../output.txt]
- Default: current path/replaced_data.txt

 
3. Discritize (n, equal_width, equal_depth, log_file_path, input_file_path, output_file_path)

* equal_with: chia giỏ theo độ rộng
- định dạng: bool
- Default: True

* equal_with: chia giỏ theo độ sâu
- định dạng: bool
- Default: False

*n: Số giỏ muốn chia, Nếu equal_depth = True n là số phần tử trong mỗi giỏ
- định dạng: interger number
- Requirement input

* log_file_path: đường dẫn chứa tập tin log 
- định dạng [../log.txt]
- Default: current path/log.txt

* input_file_path: đường dẫn chứa tập dữ liệu test
- định dạng [../test.txt]
- Requirement input

* output_file_path: đường dẫn chứ tập dữ liệu đầu ra
- định dạng [../output.txt]
- Default: current path/Discritized_data.txt

4. Normalize (method, log_file_path, input_file_path, output_file_path)

* method: phương pháp chuẩn hóa (1 - Min - max normalize, 2- Z-score normalize)
- định dạng: interger number
- Default: 1

* log_file_path: đường dẫn chứa tập tin log 
- định dạng [../log.txt]
- Default: current path/log.txt

* input_file_path: đường dẫn chứa tập dữ liệu test
- định dạng [../test.txt]
- Requirement input

* output_file_path: đường dẫn chứ tập dữ liệu đầu ra
- định dạng [../output.txt]
- Default: current path/Normalized_data.txt

